import requests
import json

# Store inventory API
url = 'https://www.intertoys.nl/AjaxGetInStoreInventory'

# All stores to check should be in the list
storeIds = [2981,2224,2145,2626,2040,2315,2078,2383,2434,2956,2425,2106,2118,2337,2364,2507,2526,2316,2010,2549,2499,2527,2570,2472,2538,2976,2021,2098,2411,2371,2447,2381,2585,2054,2424,2319,2439,2418,2487,2509,2357,2702,2241,2157,2422,2456,2093,2355,2347,2375,2628,2488,2217,2223,2137,2970,2409,2339,2501,2964,2302,2237,2086,2321,2419,2005,2326,2361,2396,2324,2340,2201,2004,2544,2147,2173,2210,2120,2103,2003,2161,2185,2160,2166,2310,2450,2546,2378,2454,2952,2030,2007,2967,2438,2107,2064,2165,2013,2036,2596,2328,2979,2011,2516,2101,2305,2551,2969,2049,2385,2220,2471,2392,2576,2146,2212,2303,2176,2960,2195,2032,2123,2430,2063,2033,2619,2043,2351,2597,2242,2200,2519,2368,2081,2437,2099,2053,2335,2448,2108,2428,2408,2082,2532,2329,2354,2391,2500,2301,2094,2227,2579,2433,2154,2446,2404,2306,2243,2402,2569,2038,2432,2384,2170,2523,2144,2218,2062,2463,2513,2379,2152,2333,2497,2460,2196,2367,2486,2953,2556,2467,2240,2334,2520,2578,2461,2236,2464,2018,2958,2496,2353,2387,2312,2426,2317,2332,2951,2047,2046,2412,2374,2091,2575,2095,2985,2058,2075,2343,2568,2442,2465,2373,2950,2427,2372,2540,2548,2451,2012,2415]

# Part to look for, also called Artikel Nummer
partNumber = 1980973

params = {'storeId': '11601',
          'storeNumber': ','.join([str(x) for x in storeIds]),
          'partNumber': partNumber,
          'hasLimit': False
          }

# To go around anti-scraping
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    try:
        json_data = response.json()
        print(len(json_data['inventory']))
        for item in json_data['inventory']:
            store_number = item['storeNumber']
            available = item['available']
            print(f"Store Number: {store_number} - Availability: {available}")
    except ValueError:
        print("Error: Not valid JSON format")
else:
    print("Error:", response.status_code)
