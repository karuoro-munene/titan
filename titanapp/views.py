import json

from django.contrib.auth.decorators import user_passes_test, login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Booking, Package


def home(request):
    return render(request, "index.html")


def air(request):
    return render(request, "air.html")


def sea(request):
    return render(request, "sea.html")


def youbuyweship(request):
    return render(request, "buy-ship.html")


def pricing(request):
    return render(request, "pricing.html")


def whatpeopleship(request):
    return render(request, "what-people-ship.html")


def trackpackage(request):
    if request.method == 'GET' and 'q' in request.GET and request.GET['q']:
        query = request.GET.get('q')
        try:
            package = Package.objects.get(invoice_number=int(query))
        except ObjectDoesNotExist:
            q = int(query)
            if (q==2688)or(q==2690)or(q==2687)or(q==2686)or(q==2671)or(q==2670)or(q==2663)or(q==2661)or(q==2660)or(q==2655):
                package = Package.objects.create(invoice_number=int(query))
                package.status = "Item dispatched August 5th. ETA Kenya in August 13th."
                package.generated = True
                package.save()
            else:
                error = {"error": "Object does not exist"}
    return render(request, "track-package.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def bookings(request):
    bookings = Booking.objects.all()
    return render(request, "bookings.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.read = True;
    booking.save()
    return render(request, "booking.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def package(request, id):
    package = Package.objects.get(id=id)
    return render(request, "package.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def managepackages(request):
    packages = Package.objects.all()
    return render(request, "manage-packages.html", locals())


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def administration(request):
    return render(request, "administration.html", locals())


def processbook(request):
    dict = request.POST.dict()
    if request.method == 'POST':
        try:
            booking = Booking.objects.create(name=dict['name'],
                                             address=f"{dict['address']}, {dict['city']},{dict['state']}, {dict['zip']}",
                                             city=dict['city'],
                                             state=dict['state'],
                                             zip=dict['zip'],
                                             phonenumber=dict['phonenumber'], message=dict['message'])
            booking.save()
            message = {"message": "Booking successfully created"}
        except Exception as e:
            message = {"message": str(e)}

    return HttpResponse(json.dumps(message), content_type='application/json')


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def addpackage(request):
    dict = request.POST.dict()
    if request.method == 'POST':
        try:
            package = Package.objects.get(invoice_number=dict['invoice'])
            package.status = dict['status']
            package.save()
            message = {"message": "Package successfully saved"}
        except ObjectDoesNotExist:
            package = Package.objects.create(invoice_number=dict['invoice'],
                                             status=dict['status'])
            package.save()
            message = {"message": "Package successfully saved"}
    # TWILIO: 5JWQ9NEYZNB7W9MX7G7DLP37

    return HttpResponse(json.dumps(message), content_type='application/json')


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def editpackage(request):
    dict = request.POST.dict()
    if request.method == 'POST':
        try:
            package = Package.objects.get(id=int(dict['id']))
            package.invoice_number = dict['invoice']
            package.status = dict['status']
            package.save()
            message = {"message": "Package successfully edited"}
        except Exception as e:
            message = {"message": str(e)}
    # TWILIO: 5JWQ9NEYZNB7W9MX7G7DLP37

    return HttpResponse(json.dumps(message), content_type='application/json')


@user_passes_test(lambda u: u.is_superuser)
@login_required(login_url="accounts/login/")
def updatetracking(request):
    picked = []
    us_warehouse = [2523, 2524, 2528, 2529, 2530, 2534, 2536, 2537, 2538, 2539, 2540, 2541, 2542, 2545, 2546, 2547,
                    2548,
                    2549, 2550]
    in_transit = [2306, 2313, 2336, 2337, 2338, 2339, 2340, 2344, 2345, 2347, 2352, 2353, 2354, 2355, 2358, 2359, 2361,
                  2362, 2363, 2366, 2367, 2368, 2369, 2371, 2372, 2373, 2374, 2375, 2376, 2377, 2378, 2379, 2380, 2381,
                  2384, 2385, 2386, 2389, 2390, 2393, 2395, 2397, 2398, 2399, 2400, 2401, 2403, 2408, 2409, 2413, 2415,
                  2416, 2417, 2418, 2422, 2424, 2426, 2427, 2428, 2429, 2430, 2431, 2432, 2433, 2434, 2435, 2436, 2439,
                  2440, 2443, 2444, 2445, 2446, 2447, 2448, 2449, 2450, 2451, 2452, 2453, 2454, 2455, 2458, 2459, 2461,
                  2462, 2463, 2464, 2465, 2468, 2470, 2471, 2472, 2473, 2474, 2475, 2478, 2479, 2480, 2481, 2482, 2483,
                  2484, 2485, 2486, 2487, 2488, 2490, 2492, 2493, 2494, 2495, 2496, 2498, 2501, 2502, 2503, 2504, 2505,
                  2506, 2509, 2510, 2511, 2512, 2513, 2515, 2516, 2517, 2518, 2521, 2522, 2535, 2540, 2543, 2544]
    kenyan_warehouse = [2525, 2526, 2527, 2531, 2532, 2533]
    dispatched = [2004, 2005, 2006, 2007, 2008, 2009, 2010, 2013, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2023, 2024,
                  2026, 2027, 2028, 2029, 2030, 2031, 2032, 2034, 2035, 2036, 2037, 2038, 2039, 2040, 2041, 2042, 2043,
                  2045, 2046, 2047, 2049, 2050, 2051, 2052, 2053, 2054, 2055, 2056, 2057, 2058, 2059, 2060, 2061, 2062,
                  2063, 2064, 2065, 2066, 2067, 2068, 2069, 2070, 2071, 2072, 2073, 2075, 2076, 2077, 2078, 2131, 2132,
                  2133, 2134, 2135, 2136, 2142, 2143, 2144, 2146, 2147, 2149, 2150, 2151, 2152, 2153, 2158, 2161, 2163,
                  2164, 2167, 2168, 2177, 2178, 2180, 2181, 2182, 2183, 2184, 2186, 2188, 2189, 2190, 2191, 2192, 2193,
                  2195, 2198, 2200, 2202, 2203, 2206, 2208, 2209, 2212, 2214, 2217, 2219, 2220, 2221, 2222, 2225, 2226,
                  2228, 2230, 2231, 2232, 2233, 2234, 2235, 2237, 2238, 2241, 2243, 2244, 2245, 2248, 2249, 2252, 2254,
                  2258, 2260, 2261, 2263, 2264, 2265, 2266, 2269, 2270, 2272, 2273, 2274, 2277, 2279, 2280, 2282, 2285,
                  2286, 2287, 2288, 2289, 2290, 2291, 2292, 2294, 2296, 2297, 2299, 2300, 2301, 2302, 2303, 2307, 2308,
                  2310, 2312, 2313, 2315, 2318, 2321, 2322, 2323, 2324, 2325, 2327, 2328, 2329, 2334, 2350, 2352, 2354,
                  2356, 2357, 2360, 2383, 2388, 2391, 2392, 2393, 2404, 2405, 2406, 2410, 2411, 2419, 2420, 2421, 2423,
                  2441, 2442, 2506, 2507, 2508, 2514, 2519, 2520]
    for x in picked:
        try:
            package = Package.objects.get(invoice_number=x)
            package.status = "Item Picked"
            package.save()
        except ObjectDoesNotExist:
            package = Package.objects.create(status="Item Picked", invoice_number=x)
            package.save()

    for x in us_warehouse:
        try:
            package = Package.objects.get(invoice_number=x)
            package.status = "Item in US Warehouse"
            package.save()
        except ObjectDoesNotExist:
            package = Package.objects.create(status="Item in US Warehouse", invoice_number=x)
            package.save()

    for x in in_transit:
        try:
            package = Package.objects.get(invoice_number=x)
            package.status = "Item in Transit to Kenya"
            package.save()
        except ObjectDoesNotExist:
            package = Package.objects.create(status="Item in Transit to Kenya", invoice_number=x)
            package.save()

    for x in kenyan_warehouse:
        try:
            package = Package.objects.get(invoice_number=x)
            package.status = "Item in Kenyan Warehouse"
            package.save()
        except ObjectDoesNotExist:
            package = Package.objects.create(status="Item in Kenyan Warehouse", invoice_number=x)
            package.save()

    for x in dispatched:
        try:
            package = Package.objects.get(invoice_number=x)
            package.status = "Item Dispatched for Delivery (Kenya)"
            package.save()
        except ObjectDoesNotExist:
            package = Package.objects.create(status="Item Dispatched for Delivery (Kenya)", invoice_number=x)
            package.save()

    return render(request, "updatetracking.html", locals())


def maureen(request):
    return render(request, "maureen.html")
