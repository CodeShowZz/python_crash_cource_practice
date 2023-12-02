cities = {
    "fujian": {"country": "中国", "population": "6000W", "fact": "在台湾对面"},
    "shenzhen": {"country": "中国", "population": "8000W", "fact": "在香港对面"},
    "shanghai": {"country": "中国", "population": "8000W", "fact": "中国金融中心"},
}

for city,info in cities.items():
    print(f"this city name is {city}")
    print(f"- the country is {info['country']},population is {info['population']},fact is {info['fact']}")