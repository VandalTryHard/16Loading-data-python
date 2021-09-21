import json

#изучение структуры данных
filename = 'c:/Users/Val/Desktop/Py/Project_2/16Loading data/JSON_file/eq_data_7_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

readable_file = 'c:/Users/Val/Desktop/Py/Project_2/16Loading data/JSON_file/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

#Построение списка всех землетрясений
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

#Извлечение магнитуд и Извлечение данных местоположения
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:10])
print(lats[:10])


