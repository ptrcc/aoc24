def list_is_increasing_or_decreasing(nums: list[int]) -> bool:
    increasing = True
    decreasing = True
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            decreasing = False
        if nums[i] > nums[i + 1]:
            increasing = False
        if nums[i] == nums[i + 1]:
            increasing = False
            decreasing = False

        # diff at most 3
        if abs(nums[i] - nums[i + 1]) > 3:
            increasing = False
            decreasing = False

    return increasing or decreasing

try:
    with open("input.txt", "r") as f:
        data = f.read().splitlines()

    count_valid = 0
    unsafe = []
    for entry in data:
        if not entry.strip():  # Skip empty lines
            continue
        try:
            nums = [int(i) for i in entry.split(" ")]
            if list_is_increasing_or_decreasing(nums):
                count_valid += 1
            else:
                unsafe.append(nums)
        except ValueError:
            print(f"Skipping invalid line: {entry}")
    print("Number of valid entries:", count_valid)

    ######## PART 2 ########
    unsafe_safed_count = 0
    for entry in unsafe:
        print("======")
        print(entry)
        print("-------")
        for i in range(len(entry)):
            # list without element i
            new_list = entry[:i] + entry[i + 1:]
            print(new_list)
            if list_is_increasing_or_decreasing(new_list):
                unsafe_safed_count += 1
                break


    print("Number of valid entries after fixing:", unsafe_safed_count+count_valid)


except FileNotFoundError:
    print("Error: 'input.txt' not found.")
finally:
    print("Done.")

