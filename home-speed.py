from datetime import datetime

import dateutil.tz

from influxdb import InfluxDBClient
from speedtest import Speedtest


def main():
    print("Conducting speed test")
    st = Speedtest()
    upload, download = st.upload(), st.download()
    now = datetime.now(dateutil.tz.tzutc())

    print(f"upload={upload} download={download} now={now}")

    rows = [
        {
            "measurement": "network_speed",
            "tags": {"direction": "upload"},
            "time": now.isoformat(),
            "fields": {"value": upload},
        },
        {
            "measurement": "network_speed",
            "tags": {"direction": "download"},
            "time": now.isoformat(),
            "fields": {"value": download},
        },
    ]

    client = InfluxDBClient("pi", 8086, "influxdb", "influxdb", "db0")
    client.write_points(rows)
    print("Complete!")


if __name__ == "__main__":
    main()
