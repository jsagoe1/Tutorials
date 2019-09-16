import random
import urllib.request
from math import *
import time
import re
import os


class Frac:
    """Fraction class with various function methods"""
    def __init__(self, x, y):               #initialize variables
        """instantiation variables with x as numerator
            and y as denominator"""
        self.x = x
        self.y = y

    def get_x(self):                        # getters
        """returns the numerator"""
        return self.x

    def get_y(self):
        """returns the denominator"""
        return self.y

    def set_x(self, new_x):                 # setters
        """sets and changes the numerator \
        for a fraction object"""
        self.x = new_x

    def set_y(self, new_y):
        """sets and changes the denominator \
        for a fraction object"""
        self.y = new_y

    def __str__(self):                      # string method
        """returns the string representation of self as <x, y>"""
        return "<"+str(self.x)+","+str(self.y)+">"

    def __add__(self, other):               # add two fractions
        """returns the sum of two functions """
        num = self.x*other.y + other.x*self.y
        denom = self.y*other.y
        return Frac(num, denom)

    def __sub__(self, other):               # subtract two fractions
        """returns (self - other)"""
        num = self.x*other.y - other.x*self.y
        denom = self.y*other.y
        return Frac(num, denom)

    def __float__(self):                    # float method
        """returns the floating point representation of self\
         to 5 decimal places"""
        ans = self.x/self.y
        return round(ans, 5)


def download_web_image(url):

    """downloads an image with address url and saves
        it to the cwd"""
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


def cleanup_words(words):
    """
    returns a clean word list with symbols
    and white spaces removed
    """
    clean_list = []
    for word in words:
        symbols = '~!@#$%^&*()_+`{}|[]\:";\'<>?,./'
        for i in range(0, len(symbols)):
            new_word = word.replace(symbols[i], " ")
            if new_word.isalpha() and len(new_word) > 2:
                clean_list.append(new_word)
    return clean_list


def rand_gen(n = 10):
    """returns an unsorted list of n elements"""
    import random
    return [random.randrange(0, (2*n)) for i in range(n)]


def toChars (s):
    """returns list of string characters"""
    return list(s)


def quad(a, b, c):
    """returns the solution of quadratic equation
       ax^2 + bx + c = 0"""

    import cmath
    top1 = -b + cmath.sqrt((b**2)-(4*a*c))
    top2 = -b - cmath.sqrt((b**2)-(4*a*c))
    ans1 = top1/(2*a)
    ans2 = top2/(2*a)
    ans1r = round(ans1.real, 3) + round(ans1.imag, 3)*1j
    ans2r = round(ans1.real, 3) + round(ans2.imag, 3)*1j
    if ans1.imag == 0 or ans2.imag == 0:
        return (ans1.real, ans2.real)
    else:
        return (ans1r, ans2r)



def right_justify(str_obj):
    """returns the string with enough spaces leading \
       so that the last letter of the string is in \
       column 70 of the display"""
    print(" "*(70-len(str_obj)) + str_obj)


def count_down(n):
    if n <= 0:
        time.sleep(1)
        print("t = 0: ---->>>BlastOff!!!!")
    else:
        time.sleep(1)
        print(n)
        count_down(n-1)


def is_password_strong1(password):
    # Password must:
    # be at least 8 character long
    # be at least one uppercase and lowercase letter.
    # contain at least one digit

    length_regex = re.compile(r'.{8,}')             # check lenght at least 8
    uppercase_regex = re.compile(r'[A-Z]')          # check for uppercase
    lowercase_regex = re.compile(r'[a-z]')          # check for lower case
    digit_regex = re.compile(r'[0-9]')              # check for number between 0 and 9

    test = (length_regex.search(password) is not None
            and uppercase_regex.search(password) is not None
            and lowercase_regex.search(password) is not None
            and digit_regex.search(password) is not None)

    return test

def is_password_strong2(password):
    length = len(password) >= 8
    case = password != password.upper() and password != password.lower()
    digit = any(c.isdigit() for c in password)
    test = length and case and digit == True
    return test


def search_dir_for_file(file_string, directory_to_search):
    files = []
    search_file_name = file_string.strip()
    find_count = 0
    os.chdir(directory_to_search)
    print("\n")
    for path, folder, file_names in os.walk(os.getcwd()):
        for string in file_names:
            new_string = string.lower()
            if search_file_name in new_string:
                find_count += 1
                print("File: "+string+"\nLocation:", path, "\n")
                continue
    if find_count > 1:
        end = "files"
    else:
        end = "file"
    print("     Found", find_count, end)
    if find_count == 0:
        print("File not Found")


# balanced parenthesis problem
def is_paren_balanced(paren_string):  #stack application
    from stack_data_structure import stack
    s = stack()
    is_balanced = True
    index = 0
    # define a match function

    def is_match(p1, p2):
        # check if p1,p2 match as opening and closing parens
        if p1 == "(" and p2 == ")":             # check for "()"
            return True
        elif p1 == "{" and p2 == "}":           # check for "{}"
            return True
        elif p1 == "[" and p2 == "]":           # check for "[]"
            return True
        else:
            return False
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]             # grab parens one by one
        if paren in "([{":                      # check for opening paren and add to list
            s.push(paren)
        else:                                   # if it is a closing one
            if s.is_empty():                    # check if stack is empty -> not balanced right away
                is_balanced = False
            else:
                top = s.pop()                   # take last paren in stack
                if not is_match(top, paren):    #compare with paren if equal
                    is_balanced = False
        index += 1
    if s.is_empty() and is_balanced:            #do above loop until stack is empty
        return True
    else:
        return False


def int_to_bin(dec_num):     #stack application
    from stack_data_structure import stack
    s = stack()
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num

def longest_preceeding(ls):
    lens = list(word for word in ls)
    letters = []
    shortest_word = ls[lens.index(min(lens))]
    ls.remove(str(shortest_word))
    for i in range(len(shortest_word)):
        for each_word in ls:
            if each_word[i] == shortest_word[i] and (each_word[i] not in letters):
                letters.append(each_word[i])
            if each_word[i] != shortest_word[i] and (each_word[i] in letters):
                letters.remove(each_word[i])
    letters_str = ""
    for char in letters:
        letters_str = letters_str + char

    return letters_str


def select_sort(nums):

    for i in range(len(nums)):
        min_value = nums[i]
        min_index = i
        for j in range(i+1, len(nums)):
            new_value = nums[j]
            new_index = j
            if new_value < min_value:
                min_value = new_value
                min_index = new_index
        print(nums)
        print("Swapping {} for {}".format(min_value, nums[i]))
        temp_value = nums[i]
        nums[i] = min_value
        nums[min_index] = temp_value
    return nums


def merge_sort(nums):
    def merge(sorted_left, sorted_right):
        result = []
        left_pointer = right_pointer = 0

        while left_pointer < len(sorted_left) and right_pointer < len(sorted_right):
            if sorted_left[left_pointer] < sorted_right[right_pointer]:
                result.append(sorted_left[left_pointer])
                left_pointer += 1
            else:
                result.append(sorted_right[right_pointer])
                right_pointer += 1
        if left_pointer == len(sorted_left):
            result.extend(sorted_right[right_pointer:])
        if right_pointer == len(sorted_right):
            result.extend(sorted_left[left_pointer:])
        return result

    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)


def sort_nums(nums):
    for i in range(len(nums)):
        min_val = nums[i]
        min_index = i
        for j in range(i + 1, len(nums)):
            new_val = nums[j]
            new_index = j

            if new_val < min_val:
                min_val = new_val
                min_index = new_index

        temp_val = nums[i]
        nums[i] = min_val
        nums[min_index] = temp_val
    return nums


def create_arr(size=20, max=30):
    import random
    return list(random.randrange(0, max + 1) for i in range(size))


def shuffle_str(input_str):
    import random
    chars = list(c for c in input_str)
    random.shuffle(chars)
    out_str = ""
    for x in chars:
        out_str += x
    return out_str


def letter_count(word, letter):
    count = 0
    for char in word:
        if letter == char: count += 1
    print(count)


def is_smooth(s):
    s = s.strip()
    word_list = s.split()
    print(word_list)

    for i in range(len(word_list) - 1):
        if word_list[i][-1] != word_list[i + 1][0]:
            return False
    return True


class circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return self.radius * (3.142 ** 2)

    def get_circumference(self):
        return 2 * self.radius * 3.142

    def __add__(self, other):
        return self.get_area() + other.get_area()

    def __str__(self):
        printer = "Circle object with radius " + str(self.radius)
        return printer


def nextinline(ls, num):
    ls.remove(ls[0])
    ls.append(num)
    return ls


def letter_check(master_ls, other_ls):
    for char in other_ls:
        if char not in master_ls:
            return False
    return True


def remove_dups(s):
    ls = ""
    for char in s:
        if char not in ls:
            ls = ls + char
    return ls


def str_to_chars(s):
    chars = list(i for i in s)
    return chars


def flip(s, comm):
    s = s.split()

    if comm == "word":
        s_list = []
        for word in s:
            s_list.append(word[::-1])
        return " ".join(s_list)

    if comm == "sentence":
        s_list = []
        while len(s) > 0:
            print("s:      ", s)
            print("s_list: ", s_list)
            print("\n")
            s_list.append(s[-1])
            s.remove(s[-1])
        return " ".join(s_list)


def alternating_caps(s):
    s = s.split()
    new_s = []
    for i in range(len(s)):
        if is_even(i) == True:
            new_word = ""
            for j in range(len(s[i])):
                if is_even(j) == True:
                    new_word += s[i][j].upper()
                else:
                    new_word += s[i][j].lower()
            new_s.append(new_word)

        if is_even(i) == False:
            new_word = ""
            for j in range(len(s[i])):
                if is_even(j) == True:
                    new_word += s[i][j].lower()
                else:
                    new_word += s[i][j].upper()
            new_s.append(new_word)

    print(" ".join(new_s))


def is_even(i):
    return i % 2 == 0


def find_max_recursive(ls):
    def maximum(l, r):
        if l >= r:
            return l
        else:
            return r

    if len(ls) == 0:
        return

    if len(ls) == 1:
        return ls[0]

    mid = len(ls) // 2

    left = find_max_recursive(ls[:mid])
    right = find_max_recursive(ls[mid:])

    return maximum(right, left)


def find_max_iterative(ls):
    maximum = ls[0]
    idx = 0
    for j in range(1, len(ls)):
        if ls[j] > maximum:
            idx = j
            maximum = ls[idx]

    return "{} --> {}".format(maximum, [idx])


"""unordered set of numbers
the nth element in the list if it was sorted
nth order statistics = nth smallest"""


def nth_smallest(l, n):
    sorted_l = sorted(l)
    sorted_set = []
    for i in sorted_l:
        if i not in sorted_set:
            sorted_set.append(i)

    return sorted_set[n - 1]


import ctypes


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError("invalid index")
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        return (c*ctypes.py_object)()

    def __str__(self):
        arr = [self._A[i] for i in range(self._n)]
        return str(arr)

    def capacity(self):
        return self._capacity
        
        
        
class Stack:
    
    # initialize
    def __init__(self, size:int = 10):
        self._size = size
        self._data = []
    
    # push
    def push(self, data):
        if len(self._data) < self._size:
            self._data.append(data)
            
        else:
            print("Stack is Full-> Cannot add {}".format(data))
        
    # pop
    def pop(self):
        first = self._data[0]
        self._data.remove(first)
        return first
        
    # lenght
    def getCurSize(self):
        return len(self._data)
        
    def getSize(self):
        return self._size
        
    # is_empty
    def is_empty(self):
        return len(self._data) == 0
    
    # is_full
    def is_full(self):
        return len(self._data) == self._size
        
    def show_stack(self):
        print(self._data[::-1])

    def top(self):
        return self._data[-1]
        
        
class Queue:
    # initialize
    def __init__(self):
        self._data = []
        
    # add
    def add(self, data):
        self._data.append[data]
        
    # reduce
    def reduce(self):
        if not self.is_empty():
            first = self._data[0]
            self._data.remove(first)
            return first
        else:
            print("Queue is empty")
            
    # lenght
    def getSize(self):
        return len(self._data)
            
    # is_empty
    def is_empty(self):
        return len(self._data) == 0
            
    def show_stack(self):
        print(self._data)
    
    def first(self):
        return self._data[0]        
        
        

        
class SinglyLinkedList:
    
    class Node:
        def __init__(self, data = None):
            self.data = data
            self.next = None
            
    def __init__(self):
        self.head = Node()
        self.tail = None
        self.size = 0
    
    #insert new head
    def add_first(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node        
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
            
    # def add_last (set data at tail)
    def add_last(self, data):
        new_node =  Node(data)
        if self.tail == None:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.next = None
        self.size += 1
        
    def is_empty(self):
        return  self.size == 0
        
    def __len__(self):
        return self.size
        
        
class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None
    
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            new_node.prev = cur_node
            cur_node.next = new_node
            
    def prepend(self, data):
        new_node = self.Node(data)
        if self.head == None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            
    def print_list(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.data)
            cur_node = cur_node.next
            
    def add_after_node(self, key, data):
        new_node = self.Node(data)
        cur_node = self.head
        while cur_node:
            if cur_node.next == None and cur_node.data == key:
                self.append(data)
                return
            elif cur_node.data == key:
                temp_node = cur_node.next    
                new_node.prev = cur_node
                new_node.next = temp_node
                temp_node.prev = new_node
            cur_node = cur_node.next
        if cur_node == None: 
            raise EOFError("Key: \"{}\" not in list".format(key))
        
    def add_before_node(self, key, data):
        pass
        
    
class HashMap:
    """
    Hashmap class
    """    
    
    def __init__(self):
            self.size = 6
            self.map = [None] * self.size
	
    def _get_hash(self, key):
            hash = 0
            for char in str(key):
                    hash += ord(char)
            return hash % self.size
	
    def add(self, key, value):
            key_hash = self._get_hash(key)
            key_value = [key, value]
	
            if self.map[key_hash] is None:
                    self.map[key_hash] = list([key_value])
                    return True
            else:
                    for pair in self.map[key_hash]:
                            if pair[0] == key:
                                    pair[1] = value
                                    return True
                    self.map[key_hash].append(key_value)
                    return True
		
    def get(self, key):
            key_hash = self._get_hash(key)
            if self.map[key_hash] is not None:
                    for pair in self.map[key_hash]:
                            if pair[0] == key:
                                    return pair[1]
            return None
		
    def delete(self, key):
            key_hash = self._get_hash(key)
	
            if self.map[key_hash] is None:
                    return False
            for i in range (0, len(self.map[key_hash])):
                    if self.map[key_hash][i][0] == key:
                            self.map[key_hash].pop(i)
                            return True
            return False

    def keys(self):
            arr = []
            for i in range(0, len(self.map)):
                    if self.map[i]:
                            arr.append(self.map[i][0])
            return arr
		
    def print(self):
            print('---PHONEBOOK----')
            for item in self.map:
                    if item is not None:
                            print(str(item))
                            
                            