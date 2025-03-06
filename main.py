from first_task import *
from second_task import * 
from tree_task import *
import threading

def menu_main():
    caption_start = "МЕНЮ\n0. Выход\n1.	Задача 1\n2. Задача 2\n3. Задача 3"
    while True:
        print(caption_start)
        
        choice = input("Выберите пункт меню: ")  

        if choice == '1':
            thread = threading.Thread(target=menu_first)
            thread.start()  
            thread.join()  

        elif choice == '2':
            thread = threading.Thread(target=menu_second)
            thread.start() 
            thread.join() 

        elif choice == '3':
            thread = threading.Thread(target=menu_tree)
            thread.start() 
            thread.join() 

        elif choice == '0':
            print("Завершение работы программы.") 
            break  

        else:
            print("Неверный выбор.")  

        
if __name__ == "__main__":
    menu_main()
    
    
    
    
