def sum67(nums):
 sum=0
 dupsum=0
 dup=[]
 j=0
 i=0
 for j in range(0,len(nums)+1):
  if(i==6):
   dup=nums[j:]
 for i in range(0,len(nums)+1):
  if(i==7):
   dup=nums[j:i+1]
 for k in nums:
  sum=sum+k
 for k in dup:
  dupsum=dupsum+k
 sum=sum-dupsum
 return sum
  
print sum67([6,7])
