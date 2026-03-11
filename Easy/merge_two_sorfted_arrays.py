# nums1 = [1, 3, 5]
# nums2 = [2, 4, 6]
# # Output: [1, 2, 3, 4, 5, 6]


def merge(nums1: list, nums2: list):
    resList = []
    l = 0
    r = 0

    while l < len(nums1) and r < len(nums2):
        if nums1[l] <= nums2[r]:
            resList.append(nums1[l])
            l += 1
        else:
            resList.append(nums2[r])
            r += 1

    resList.extend(nums1[l:])
    resList.extend(nums2[r:])


    return resList
         


nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

result = merge(nums1, nums2)
print("result : ", result)

