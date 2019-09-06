# exercise 1
marks = list((10,9,9.5,10,8,7.75,8.75,9,6,10))
print("Students marks: ",marks)

print("There is ",len(marks)," students in this course.")
print("There are ",marks.count(10)," students got full mark.")

marks.sort()
print("Marks in descending order: ",marks)

marks.reverse()
print("Marks in ascending order: ", marks)

print("The highest mark is at index ", marks.index(10), " and the lowest mark is at index ", marks.index(6))

# exercise 2
tuple = ("java", "python", "swift")
print("python is in the tuple.") if "python" in tuple else print("python is not in the tuple.")