import random
import time

#вставкой
def sort_insert(arr):
    for i in range(1, len(arr)):
        element=arr[i]
        j=i-1
        while j>=0 and arr[j]>element:
            arr[j+1]=arr[j]
            j-=1
            arr[j+1]=element
    return arr

#пузырёчек
def bubble_sort_descending(arr):
  n = len(arr)
  for k in range(n):
    for l in range(0, n-k-1):
      if arr[l] > arr[l+1]:
        arr[l], arr[l+1] = arr[l+1], arr[l]
  return arr

arr=[random.randint(1, 100000) for _ in range(1000000)]

#время вставкой
insert_start_time=time.time()
sort_insert(arr)
inset_end_time=time.time()

insert_time=inset_end_time-insert_start_time

#время пузырьком
bubble_start_time=time.time()
bubble_sort_descending(arr)
bubble_end_time=time.time()

bubble_time=bubble_end_time-bubble_start_time

print(f"Время выполнения методом вставками: {insert_time:.20f} секунд")
print(f"Время выполнения методом пузырьком: {bubble_time:.20f} секунд")

