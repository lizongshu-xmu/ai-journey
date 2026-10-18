import argparse


def average_of(chinese, math, english):
    """给三科分数，返回平均分（保留一位小数）。"""
    total = chinese + math + english
    return round(total / 3, 1)


def main():
    parser = argparse.ArgumentParser(description="统计 CSV 里每个学生的平均分")
    parser.add_argument("--file", default="data.csv", help="要统计的 CSV 文件路径")
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")

            if parts[0] == "学号":
                continue

            name    = parts[1]
            chinese = int(parts[2])
            math    = int(parts[3])
            english = int(parts[4])

            avg = average_of(chinese, math, english)
            print(f"{name}\t{avg}")


if __name__ == "__main__":
    main()