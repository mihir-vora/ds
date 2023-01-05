def bubble(nums):
	for i in range(len(nums)):
		for j in range(len(nums)-i-1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
		print(i, nums)
	print(nums)
# [1,4, 5, 3, 8]
nums = [5, 1, 4, 8, 2]
def bubble_rec(n):
	count = 0
	# base condition
	if n == 1:
		return
	for i in range(n-1):
		if nums[i] > nums[i+1]:
			nums[i], nums[i+1] = nums[i+1], nums[i]
			count += 1

	# check any recu happend or not 
	# if not happend then return
	if count == 0:
		return

	# larget element are fixed
	# recur for the remaining array
	bubble_rec(len(nums) -1) 

bubble_rec(len(nums))
print(nums)