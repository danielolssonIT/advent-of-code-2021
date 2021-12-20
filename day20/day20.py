def parse_input(example=False):
    filename = "example.txt" if example else "day20.txt"
    with open(filename) as f:
        img_enhance_alg, input_image = f.read().split("\n\n")
    img_enhance_alg = img_enhance_alg.strip()
    grid = [line for line in input_image.split('\n')]

    return img_enhance_alg, grid


def in_bounds(row, col, grid_width, grid_height):
    return 0 <= row < grid_width and 0 <= col < grid_height


def adjacent_3x3_positions(row, col):
    return ((r, c) for r in range(row - 1, row + 2) for c in range(col - 1, col + 2))


def enhance_img(img_enhance_alg, input_img, out_of_bounds_value):
    output_img = []
    for i in range(-1, len(input_img[0]) + 1):
        row = []
        for j in range(-1, len(input_img) + 1):
            index = []
            for r, c in adjacent_3x3_positions(i, j):
                if in_bounds(r, c, len(input_img[0]), len(input_img)):
                    index.append(1 if input_img[r][c] == '#' else 0)
                else:
                    index.append(out_of_bounds_value)
            index = int(''.join(map(str, index)), 2)
            row.append(img_enhance_alg[index])
        output_img.append(row)
    return output_img


def solve(example=False, iterations=1):
    img_enhance_alg, input_img = parse_input(example)
    output_img = []
    alternating_border = img_enhance_alg[0] == '#'
    for i in range(iterations):
        output_img = enhance_img(img_enhance_alg, input_img, i % 2 if alternating_border else 0)
        input_img = output_img
    return sum(row.count("#") for row in output_img)


print(solve(iterations=2))
print(solve(iterations=50))
