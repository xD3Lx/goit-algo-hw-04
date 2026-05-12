import argparse
import math
from pathlib import Path


def parse_arguments():
    parser = argparse.ArgumentParser(description="Create a Koch snowflake SVG.")
    parser.add_argument(
        "level",
        type=int,
        nargs="?",
        help="Recursion level for the Koch snowflake.",
    )
    parser.add_argument(
        "-d",
        "--destination",
        type=Path,
        default=Path("koch_snowflake.svg"),
        help="Output SVG file.",
    )

    return parser.parse_args()


def ask_recursion_level():
    while True:
        try:
            level = int(input("Enter recursion level: "))
        except ValueError:
            print("Recursion level must be an integer.")
            continue

        if level < 0:
            print("Recursion level must be 0 or greater.")
            continue

        return level


def koch_curve(start, end, level):
    if level == 0:
        return [start, end]

    first = (
        start[0] + (end[0] - start[0]) / 3,
        start[1] + (end[1] - start[1]) / 3,
    )
    second = (
        start[0] + 2 * (end[0] - start[0]) / 3,
        start[1] + 2 * (end[1] - start[1]) / 3,
    )

    dx = second[0] - first[0]
    dy = second[1] - first[1]
    angle = -math.pi / 3
    peak = (
        first[0] + dx * math.cos(angle) - dy * math.sin(angle),
        first[1] + dx * math.sin(angle) + dy * math.cos(angle),
    )

    parts = (
        koch_curve(start, first, level - 1),
        koch_curve(first, peak, level - 1),
        koch_curve(peak, second, level - 1),
        koch_curve(second, end, level - 1),
    )

    points = []
    for part in parts:
        if points:
            points.extend(part[1:])
        else:
            points.extend(part)

    return points


def create_snowflake_points(level, size):
    height = size * math.sqrt(3) / 2
    vertices = [
        (0, height),
        (size / 2, 0),
        (size, height),
    ]

    points = []
    for index, start in enumerate(vertices):
        end = vertices[(index + 1) % len(vertices)]
        side_points = koch_curve(start, end, level)
        if points:
            points.extend(side_points[1:])
        else:
            points.extend(side_points)

    return normalize_points(points)


def normalize_points(points, margin=20):
    min_x = min(x for x, _ in points)
    max_x = max(x for x, _ in points)
    min_y = min(y for _, y in points)
    max_y = max(y for _, y in points)

    normalized_points = [
        (x - min_x + margin, y - min_y + margin) for x, y in points
    ]
    width = math.ceil(max_x - min_x + margin * 2)
    height = math.ceil(max_y - min_y + margin * 2)

    return normalized_points, width, height


def save_svg(points, width, height, output):
    path_data = " ".join(f"L {x:.2f} {y:.2f}" for x, y in points[1:])
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{height:.0f}" viewBox="0 0 {width:.0f} {height:.0f}">
  <path d="M {points[0][0]:.2f} {points[0][1]:.2f} {path_data} Z" fill="none" stroke="#1f6feb" stroke-width="2" stroke-linejoin="round"/>
</svg>
'''
    output.write_text(svg, encoding="utf-8")


def main():
    args = parse_arguments()
    level = args.level if args.level is not None else ask_recursion_level()
    destination = args.destination

    if level < 0:
        print("Recursion level must be 0 or greater.")
        return

    points, width, height = create_snowflake_points(level, 600)
    save_svg(points, width, height, destination)
    print(f"Koch snowflake saved to {destination}")


if __name__ == "__main__":
    main()
