numbers = [5,2,1,7,4]
# Menambahkan item ke belakang list
numbers.append(0)
print(numbers)
# Menambahkan item ke posisi yang dikehendaki
numbers.insert(0,10)
print(numbers)
# Menghilangkan item yang dikehendaki
numbers.remove(5)
print(numbers)
# Menghilangkan item dari list paling belakang
numbers.pop()
print(numbers)
# Menghilangkan item yang dikehendaki berdasarkan index
# pop(0) menghilangkan item yang terletak pada index ke 0
numbers.pop(0)
print(numbers)
# Mencari index dari item
print(numbers.index(7))
# Mencari item dalam list dalam boolean
# Apabila ada
print(7 in numbers)
# Apabila tidak ada
print(50 in numbers)
numbers.append(7)
print(numbers)
# Mencari jumlah item yang sama
print(numbers.count(7))
# Mengurutkan item dalam list secara ascending (default)
numbers.sort()
print(numbers)
# Mengurutkan item dalam list secara descending
# Cara 1
numbers.reverse()
# Cara 2
numbers.sort(reverse=True)
print(numbers)
# Mengcopy list
numbers2 = numbers.copy()
# Menghilangkan semua item dalam list
numbers.clear()
print("list numbers:",numbers)
print("list numbers2:",numbers2)