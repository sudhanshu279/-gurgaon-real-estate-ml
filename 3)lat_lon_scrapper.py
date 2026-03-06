from geopy.geocoders import Nominatim
import pandas as pd
import time

geolocator = Nominatim(
    user_agent="capstone_gurgaon_sector_project",  # MUST be unique
    timeout=10
)

data = []

for sector in range(1, 116):
    try:
        location = geolocator.geocode(
            f"Sector {sector}, Gurgaon, Haryana, India"
        )

        if location:
            lat = location.latitude
            lon = location.longitude
        else:
            lat, lon = None, None

        data.append({
            "Sector": f"Sector {sector}",
            "Latitude": lat,
            "Longitude": lon
        })

        print(f"Sector {sector} done")

        time.sleep(1.2)   # 🔥 VERY IMPORTANT (rate limit)

    except Exception as e:
        print("Error:", e)
        data.append({
            "Sector": f"Sector {sector}",
            "Latitude": None,
            "Longitude": None
        })

df = pd.DataFrame(data)
df.to_csv("gurgaon_sectors_coordinates.csv", index=False)



# in latlong.csv we updated some sectors which we got from gurgaon_sectors_coordinates.csv . we will latlong.csv for analytics page