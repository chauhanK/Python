
courses = ['Economics', 'Math', 'Physics', 'CompSci']
courses_2 = ['Psychology','Art']

print(courses)

#Length of the list
print(len(courses))

#Print last element of the list
print(courses[-1])

print(courses[:2])

print(courses[2:])

#Appent element at last
courses.append('History')

#Insert element in between
courses.insert(2,'History')

# Extend a list
courses.extend(courses_2)

courses.pop()


#Sorting --------This will sort a list in place
courses.sort()

#Reverse Sort
courses.sort(reverse=True)

#This will not sort a list in place,so we need to store it in other variable
sortedCourses = sorted(courses)

























