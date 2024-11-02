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
for h in range(24):
    p_hour = data[data[:, 1] == h, 2]

    coverage_h_rolling_h = []  # Initialize coverage list for this hour
    for t in range(T, end_day - 1):
        # Filter data for the rolling calibration window
        p_hour_rolling = p_hour[(t - T):t]

        # 1st Naive Forecast for the rolling window
        pf_naive1_rolling = np.roll(p_hour_rolling, 1)
        # Calculate the forecast errors
        forecast_errors_rolling = p_hour_rolling[:(T - 1)] - pf_naive1_rolling[:(T - 1)]
        # Calculate the quantiles for the forecast errors
        q1_rolling = np.quantile(forecast_errors_rolling, (1 - nominal_coverage) / 2)
        q2_rolling = np.quantile(forecast_errors_rolling, (1 + nominal_coverage) / 2)

        # Compute lower and upper bounds for the prediction interval
        lower_bound_rolling = pf_naive1_rolling[T - 1] + q1_rolling  # indeksowanie od 0
        upper_bound_rolling = pf_naive1_rolling[T - 1] + q2_rolling

        real_rolling = p_hour_rolling[T - 1]

        # Check if the real value falls within the prediction interval
        if real_rolling < upper_bound_rolling and real_rolling > lower_bound_rolling:
            coverage_h_rolling_h.append(1)
        else:
            coverage_h_rolling_h.append(0)

    coverage_h_rolling.append(np.mean(coverage_h_rolling_h))

print(coverage_h_rolling)
plt.figure(2)
plt.plot(coverage_h_rolling, label='rolling')
plt.title('Coverage')
plt.legend()
plt.show()
