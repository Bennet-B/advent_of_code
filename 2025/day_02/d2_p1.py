# Note: In part 2 (see: d2_p2.py), I switched to a much faster approach for performance (by generating rather than scanning all IDs); that strategy could be applied here as well with minor adjustments.

INPUT_DATA: str = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

sum: int = 0

for range_str in INPUT_DATA.split(','):
    start, end = range_str.split('-')
    for id in range(int(start), int(end) + 1):
        s = str(id)
        if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
            #print(s)
            sum += id

print(f"\nSum of invalid ids: {sum}")

# personal solution: 19219508902