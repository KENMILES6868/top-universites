import requests
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
url = "https://api.carbonintensity.org.uk/intensity/date"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()["data"]
    actual_intensities = []
    forecast_intensities = []
    datetimes = []
    for item in data:
        actual_intensity = item.get("intensity", {}).get("actual")
        forecast_intensity = item.get("intensity", {}).get("forecast")
        datetime_str = item["from"]

        actual_intensities.append(actual_intensity if actual_intensity is not None else 0)
        forecast_intensities.append(forecast_intensity if forecast_intensity is not None else 0)
        datetimes.append(datetime_str)
    datetimes = [mdates.datestr2num(dt) for dt in datetimes]

    fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=True)

    axs[0].plot(datetimes, forecast_intensities)
    axs[0].set_title("Forecast Intensity")
    axs[0].set_ylabel("Forecast Intensity")

    axs[1].plot(datetimes, actual_intensities)
    axs[1].set_title("Actual Intensity")
    axs[1].set_ylabel("Actual Intensity")

    axs[2].plot(datetimes, actual_intensities, color='blue', label='Actual Intensity')
    axs[2].plot(datetimes, forecast_intensities, color='red', label='Forecast Intensity')
    axs[2].set_title("Actual and Forecast Intensity")
    axs[2].set_ylabel("Intensity")
    axs[2].legend()
    plt.xticks(rotation=45)
    for ax in axs:
        ax.xaxis_date()
        date_formatter = mdates.DateFormatter('%Y-%m-%d %H:%M')
        ax.xaxis.set_major_formatter(date_formatter)
    plt.show()
else:
    print("Error.")