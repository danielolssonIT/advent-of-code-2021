
def increases(inp_list):
    sliding_windows = []
    for i in range(len(inp_list) - 2):
        depths = inp_list[i], inp_list[i+1], inp_list[i+2]
        sliding_windows.append(sum(depths))

    num_of_increases = 0
    for i in range(1, len(sliding_windows)):
        if sliding_windows[i] > sliding_windows[i-1]:
            num_of_increases += 1
    return num_of_increases


with open('../inputs/day1.txt', 'r') as f:
    inp = list(map(int, f.readlines()))

print(increases(inp))
#L = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
#print(increases(L))
