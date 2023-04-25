import pygame
import random
import time
import tkinter
import customtkinter as ct
import os
import sys
array = [0,]




def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                drawArray(arr)
def selection_sort(array):
    size = len(array)
    for s in range(size):
        min_idx = s
         
        for i in range(s + 1, size):
             
            if array[i] < array[min_idx]:
                min_idx = i
        (array[s], array[min_idx]) = (array[min_idx], array[s])
        drawArray(array)

def insertion_sort(arr): 
   
        for i in range(1, len(arr)): 
            a = arr[i] 
            j = i - 1 
           
            while j >= 0 and a < arr[j]: 
                arr[j + 1] = arr[j] 
                j -= 1 
                 
            arr[j + 1] = a 
            drawArray(array)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

            drawArray(arr)

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

            drawArray(arr)

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

            drawArray(arr)
    
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        count = [0] * 10
        for i in range(len(arr)):
            count[(arr[i] // exp) % 10] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        output = [0] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
        for i in range(len(arr)):
            arr[i] = output[i]
            drawArray(arr)
        exp *= 10
        
cellsize = 0
with open('config.txt', 'r') as file:
    line = file.readline()
    cellsize = float(line.split(';:')[1].strip())

def drawArray(arr):
    Surface.fill((33,35,37))
    for tp in range(len(arr)):
        color = (31, 106, 165)
        
        pygame.draw.rect(Surface, color, pygame.Rect((tp*cellsize, arr[tp]*cellsize, cellsize, cellsize * 5000)))
    pygame.display.update()

pygame.init()
for i in range(800 // int(cellsize)):
    array.append(random.randint(0, 800 // int(cellsize)))
Surface = pygame.display.set_mode((800, 800))

t = ct.CTk()
t.geometry("200x400")
ct.set_appearance_mode("Dark")
ct.set_default_color_theme("blue")
drawArray(array)
def tkbubblesort(): 
    bubble_sort(array)
def tkinsertionsort(): 
    insertion_sort(array)
def tkselectionsort(): 
    selection_sort(array)
def tkmergesort(): 
    merge_sort(array)
def tkmergesort(): 
    merge_sort(array)
def tkradixsort(): 
    radix_sort(array)
def tkreset():
    array = [0,]
    for i in range(800 // int(cellsize)):
        array.append(random.randint(0, 800 // int(cellsize)))
    drawArray(array)
def update_cellsize(val):
    global cellsize
    cellsize = float(val)
    tkreset()

def quit_programs():
    global quit_flag
    quit_flag = True
    t.quit()
    pygame.quit()

def update():
    lines = f";:{cellsize}\n"
    with open('config.txt', 'w') as file:
        file.writelines(lines)
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 

slider_var = tkinter.DoubleVar(value=cellsize)
slider = ct.CTkSlider(t, from_=1, to=60, orient=tkinter.HORIZONTAL, command=update_cellsize, variable=slider_var)
slider.pack()

quit_flag = False
while not quit_flag:
    b = ct.CTkButton(t, text="Apply changes", command=update)
    b.pack(pady=25)

    b = ct.CTkButton(command=tkbubblesort,text = "Bubble")
    b.pack(pady=5)
    b = ct.CTkButton(command=tkinsertionsort,text = "Insertion")
    b.pack(pady=5)
    b = ct.CTkButton(command=tkselectionsort,text = "Selection")
    b.pack(pady=5)
    b = ct.CTkButton(command=tkmergesort,text = "Merge")
    b.pack(pady=5)
    b = ct.CTkButton(command=tkradixsort,text = "Radix")
    b.pack(pady=5)
    
    b = ct.CTkButton(command=tkreset,text = "Reset Array")
    b.pack(pady=25)
    b = ct.CTkButton(t, text="Quit", command=quit_programs)
    b.pack(pady=5)

    t.mainloop()

lines = f";:{cellsize}\n"
with open('config.txt', 'w') as file:
    file.writelines(lines)