from src.linked_list import LinkedList


def main():
    nums = LinkedList()

    nums.append(1)
    nums.append(2)
    nums.append(3)
    print(nums.size())

    for n in nums:
        print(n)


if __name__ == "__main__":
    main()
