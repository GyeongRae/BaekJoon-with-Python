t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    room_number = n // h + 1

    if(floor == 0):
            floor = h
            room_number = n//h
            print(floor*100+ room_number)
    else:
        print(floor*100+ room_number)
