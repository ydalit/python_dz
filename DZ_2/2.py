import random
import timeit

#вставки
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
      if arr[l] < arr[l+1]:
        arr[l], arr[l+1] = arr[l+1], arr[l]
  return arr

arr=[random.randint(1, 1000000) for _ in range(1000000)]

#время
time_insest=timeit.timeit(lambda:sort_insert, number=1000)  # number-количество запусков функции
time_bubble=timeit.timeit(lambda:bubble_sort_descending, number=1000) #больше запускаем - больше точность времени

print(f"Время выполнения методом вставками: {time_insest:.20f} секунд")
print(f"Время выполнения методом пузырьком: {time_bubble:.20f} секунд")

