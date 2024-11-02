import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('GEFCOM.txt')

T = 365
start_day = 366
end_day = 1082

forecast_errors = []
prediction_intervals = []

# nominal_coverage = 0.9
nominal_coverage = 0.5

coverage_h_rolling = []
coverage_h = []

for h in range(24):
    # Filter data for the current hour
    p_hour = data[data[:, 1] == h, 2]
    # 1st Naive Forecast
    pf_naive1 = np.roll(p_hour,1)
    print(pf_naive1)
    print(p_hour)
    # Calculate the forecast errors for the specified range of days
    forecast_errors= p_hour[1:T] - pf_naive1[1:T]
    # We want to have 90% of values in our forecast, so we don't want 5% worst scenarios and 5% best scenarios
    q1 = np.quantile(forecast_errors, (1-nominal_coverage)/2)
    q2 = np.quantile(forecast_errors, (1+nominal_coverage)/2)
    #print(q1, q2)
    lower_bound = pf_naive1[T:(end_day - 1)] + q1
    upper_bound = pf_naive1[T:(end_day - 1)] + q2

    #TASK 2
    prediction_intervals.append((lower_bound, upper_bound))
    real = p_hour[T:]
    hits = []
    for day in range(len(lower_bound)):
        if real[day] < upper_bound[day] and real[day] > lower_bound[day]:
            hits.append(1)
        else:
            hits.append(0)

    coverage_h.append(np.mean(hits))

    #ROLLING
    rolling_hits = []  # Initialize coverage list for this hour
    for t in range(T, end_day - 1):
        # Filter data for the rolling calibration window
        p_hour_rolling = p_hour[(t - T):t]

        # 1st Naive Forecast for the rolling window
        pf_naive1_rolling = np.roll(p_hour_rolling, 1)
        # Calculate the forecast errors
        forecast_errors_rolling = p_hour_rolling[:(T-1)] - pf_naive1_rolling[:(T-1)]
        # Calculate the quantiles for the forecast errors
        q1_rolling = np.quantile(forecast_errors_rolling, (1 - nominal_coverage) / 2)
        q2_rolling = np.quantile(forecast_errors_rolling, (1 + nominal_coverage) / 2)

        # Compute lower and upper bounds for the prediction interval
        lower_bound_rolling = pf_naive1_rolling[T - 1] + q1_rolling #indeksowanie od 0
        upper_bound_rolling = pf_naive1_rolling[T - 1] + q2_rolling

        real_rolling = p_hour_rolling[T-1]

        # Check if the real value falls within the prediction interval
        if real_rolling < upper_bound_rolling and real_rolling > lower_bound_rolling:
            rolling_hits.append(1)
        else:
            rolling_hits.append(0)

    coverage_h_rolling.append(np.mean(rolling_hits))

# print(coverage_h)
# plt.figure(1)
# plt.plot(lower_bound, label='lower')
# plt.plot(upper_bound, label='upper')
# plt.title('Bounds')
# plt.legend()
# plt.show()

#print(coverage_h_rolling)
plt.figure(2)
plt.plot(coverage_h, label='fixed')
plt.plot(coverage_h_rolling, label='rolling')
plt.axhline(y=0.5)
plt.title('Coverage')
plt.legend()
plt.show()

print(np.mean(coverage_h))
print(np.mean((coverage_h_rolling)))