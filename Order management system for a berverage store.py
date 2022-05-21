import sqlite3
import tkinter as tk
import tkinter.messagebox
import time

conn = sqlite3.connect('beverage_database_3.db')
cur = conn.cursor()
cur.execute('PRAGMA foreign_keys=ON')
cur.execute('''SELECT * FROM Item ''')
results = cur.fetchall()

def add_order():
    try:
        P01_Quantity = int(P01_Quantity_entry.get())
        P02_Quantity = int(P02_Quantity_entry.get())
        P03_Quantity = int(P03_Quantity_entry.get())
        P04_Quantity = int(P04_Quantity_entry.get())
        P05_Quantity = int(P05_Quantity_entry.get())

        if P01_Quantity>find_S01_P01_StoreNum() and "Cen" in  P01_clicked.get():
            raise Exception()

        elif P01_Quantity>find_S02_P01_StoreNum() and "Mong" in  P01_clicked.get():
            raise Exception()

        if P02_Quantity>find_S01_P02_StoreNum() and "Cen" in  P02_clicked.get():
            raise Exception()

        elif P02_Quantity>find_S02_P02_StoreNum() and "Mong" in  P02_clicked.get():
            raise Exception()

        if P03_Quantity>find_S01_P03_StoreNum() and "Cen" in  P03_clicked.get():
            raise Exception()

        elif P03_Quantity>find_S02_P03_StoreNum() and "Mong" in  P03_clicked.get():
            raise Exception()

        if P04_Quantity>find_S01_P04_StoreNum() and "Cen" in  P04_clicked.get():
            raise Exception()

        elif P04_Quantity>find_S02_P04_StoreNum() and "Mong" in  P04_clicked.get():
            raise Exception()

        if P05_Quantity>find_S01_P05_StoreNum() and "Cen" in  P05_clicked.get():
            raise Exception()

        elif P05_Quantity>find_S02_P05_StoreNum() and "Mong" in  P05_clicked.get():
            raise Exception()
        
# store order's detail in Orders table     
        cur.execute('''SELECT max(OrderNum) FROM Orders''')
        max_OrderNum = cur.fetchall()
        max_OrderNum_plus_1 = int(max_OrderNum[0][0])+1
        cur.execute('''INSERT INTO Orders VALUES (?, ?)''' , (max_OrderNum_plus_1, str(time.localtime()[0:3]) ))
        conn.commit()
        
# store order's detail in OrderLine table

        if "Central" in P01_clicked.get():
            Store_Num_P01 = "S01"
        elif "Mong" in P01_clicked.get():
            Store_Num_P01 = "S02"

        if "Central" in P02_clicked.get():
            Store_Num_P02 = "S01"
        elif "Mong" in P01_clicked.get():
            Store_Num_P02 = "S02"

        if "Central" in P03_clicked.get():
            Store_Num_P03 = "S01"
        elif "Mong" in P03_clicked.get():
            Store_Num_P03 = "S02"

        if "Central" in P04_clicked.get():
            Store_Num_P04 = "S01"
        elif "Mong" in P04_clicked.get():
            Store_Num_P04 = "S02"

        if "Central" in P05_clicked.get():
            Store_Num_P05 = "S01"
        elif "Mong" in P05_clicked.get():
            Store_Num_P05 = "S02"

        cur.execute('''INSERT INTO OrderLine VALUES (?, "P01", ?,  ?)''' , (max_OrderNum_plus_1, Store_Num_P01, P01_Quantity ) )
        conn.commit()
        cur.execute('''INSERT INTO OrderLine VALUES (?, "P02", ?, ?)''' , (max_OrderNum_plus_1, Store_Num_P02, P02_Quantity ) )
        conn.commit()
        cur.execute('''INSERT INTO OrderLine VALUES (?, "P03", ? , ?)''' , (max_OrderNum_plus_1, Store_Num_P03, P03_Quantity ) )
        conn.commit()
        cur.execute('''INSERT INTO OrderLine VALUES (?, "P04", ?, ?)''' , (max_OrderNum_plus_1, Store_Num_P04, P04_Quantity ) )
        conn.commit()
        cur.execute('''INSERT INTO OrderLine VALUES (?, "P05", ? , ?)''' , (max_OrderNum_plus_1, Store_Num_P05, P05_Quantity) )
        conn.commit()

# display information in window_add_order
        if "Central" in P01_clicked.get():
            P01_Store = "Central"
        elif "Mong" in P01_clicked.get():
            P01_Store = "Mongkok"

        if "Central" in P02_clicked.get():
            P02_Store = "Central"
        elif "Mong" in P02_clicked.get():
            P02_Store = "Mongkok" 

        if "Central" in P03_clicked.get():
            P03_Store = "Central"
        elif "Mong" in P03_clicked.get():
            P03_Store = "Mongkok"

        if "Central" in P04_clicked.get():
            P04_Store = "Central"
        elif "Mong" in P04_clicked.get():
            P04_Store = "Mongkok"

        if "Central" in P05_clicked.get():
            P05_Store = "Central"
        elif "Mong" in P05_clicked.get():
            P05_Store = "Mongkok"
            
        window_add_order = tk.Tk()
        window_add_order.title("Your order's details")
        #The following block of code aims to centre windiow_2.
        window_add_order_width = 300
        window_add_order_height = 550

        screen_width = window_add_order.winfo_screenwidth()   #Get the screen dimension
        screen_height = window_add_order.winfo_screenheight()

        center_x = int(screen_width/2 - window_add_order_width / 2)    #Find the center point
        center_y = int(screen_height/2 - window_add_order_height / 2)

        window_add_order.geometry(f'{window_add_order_width}x{window_add_order_height}+{center_x}+{center_y}')    #Set the position of the window to the center of the screen
        #The above block of code aims to centre windiow_2.

        information= tk.Label(window_add_order, text="You successfully placed an order. Thank you! \n Your order's details are as follows:", padx=10, pady=10)
        information.grid(row=0, column=0, columnspan=4)

        P01_ItemNum = tk.Label(window_add_order, text=f'{results[0][0]}', padx=10, pady=10)
        P01_ItemNum.grid(row=2, column=0)
        P01_Name = tk.Label(window_add_order, text=f'{results[0][1]}', padx=10, pady=10)
        P01_Name.grid(row=2, column=1)
        P01_Store = tk.Label(window_add_order , text=f'{P01_Store}', padx=10, pady=10)
        P01_Store.grid(row=2, column=2)
        P01_Quantity_display = tk.Label(window_add_order, text = f'{P01_Quantity}', padx=10, pady=10)
        P01_Quantity_display.grid(row=2, column=3)

        P02_ItemNum = tk.Label(window_add_order, text=f'{results[1][0]}', padx=10, pady=10)
        P02_ItemNum.grid(row=3, column=0)
        P02_Name = tk.Label(window_add_order, text=f'{results[1][1]}', padx=10, pady=10)
        P02_Name.grid(row=3, column=1)
        P02_Store = tk.Label(window_add_order , text=f'{P02_Store}', padx=10, pady=10)
        P02_Store.grid(row=3, column=2)
        P02_Quantity_display = tk.Label(window_add_order, text = f'{P02_Quantity}', padx=10, pady=10)
        P02_Quantity_display.grid(row=3, column=3)

        P03_ItemNum = tk.Label(window_add_order, text=f'{results[2][0]}', padx=10, pady=10)
        P03_ItemNum.grid(row=4, column=0)
        P03_Name = tk.Label(window_add_order, text=f'{results[2][1]}', padx=10, pady=10)
        P03_Name.grid(row=4, column=1)
        P03_Store = tk.Label(window_add_order , text=f'{P03_Store}', padx=10, pady=10)
        P03_Store.grid(row=4, column=2)
        P03_Quantity_display = tk.Label(window_add_order, text = f'{P03_Quantity}', padx=10, pady=10)
        P03_Quantity_display.grid(row=4, column=3)

        P04_ItemNum = tk.Label(window_add_order, text=f'{results[3][0]}', padx=10, pady=10)
        P04_ItemNum.grid(row=5, column=0)
        P04_Name = tk.Label(window_add_order, text=f'{results[3][1]}', padx=10, pady=10)
        P04_Name.grid(row=5, column=1)
        P04_Store = tk.Label(window_add_order , text=f'{P04_Store}', padx=10, pady=10)
        P04_Store.grid(row=5, column=2)
        P04_Quantity_display = tk.Label(window_add_order, text = f'{P04_Quantity}', padx=10, pady=10)
        P04_Quantity_display.grid(row=5, column=3)

        P05_ItemNum = tk.Label(window_add_order, text=f'{results[4][0]}', padx=10, pady=10)
        P05_ItemNum.grid(row=6, column=0)
        P05_Name = tk.Label(window_add_order, text=f'{results[4][1]}', padx=10, pady=10)
        P05_Name.grid(row=6, column=1)
        P05_Store = tk.Label(window_add_order , text=f'{P05_Store}', padx=10, pady=10)
        P05_Store.grid(row=6, column=2)
        P05_Quantity_display = tk.Label(window_add_order, text = f'{P05_Quantity}', padx=10, pady=10)
        P05_Quantity_display.grid(row=6, column=3)
        
        total_price = sum([P01_Quantity*results[0][2], P02_Quantity*results[1][2], P03_Quantity*results[2][2], P04_Quantity*results[3][2], P05_Quantity*results[4][2]])
        total_price_display = tk.Label(window_add_order, text=f"Total price=${total_price}", padx=10, pady=10)
        total_price_display.grid(row=7, column=0, columnspan=4)

        order_number_display = tk.Label(window_add_order, text=f"Your order number is {max_OrderNum_plus_1}.", padx=10, pady=10)
        order_number_display.grid(row=8, column=0, columnspan=4)

    except ValueError:
        tkinter.messagebox.showerror(title = 'Error',  message = "Please input integers!")

    except Exception:
        tkinter.messagebox.showerror(title = 'Error',  message = "There are insuffcient available stock.")
  
def check_order():
    try:
# retrieve the order from the Orders table
        order_number = int(Check_order_entry.get())
        
        cur_check_order_retrieve_Orders_table = conn.cursor()
        cur_check_order_retrieve_Orders_table.execute('''SELECT * FROM Orders WHERE OrderNum =?  ''', (order_number,))
        order_to_be_checked = cur_check_order_retrieve_Orders_table.fetchall()[0]
        order_to_be_checked_order_number = order_to_be_checked[0]
        order_to_be_checked_date = order_to_be_checked[1]
        order_to_be_checked_date = order_to_be_checked_date[1:-1]
        order_to_be_checked_date = order_to_be_checked_date.split(", ")

# retrieve the order from the OrderLine table
        order_details_items = []

        cur_check_order_retrieve_OrderLine_table = conn.cursor()
        cur_check_order_retrieve_OrderLine_table.execute('''SELECT StoreNum, NumOrdered FROM OrderLine WHERE OrderNum =? ''', (order_number,))
        order_details  = cur_check_order_retrieve_OrderLine_table.fetchall()

        # convert StoreNum into StoreName
        order_details  = list(map(list, order_details))
        for i, x in enumerate(order_details):
            for j, y in enumerate(x):
                if isinstance(y, int):
                    pass
                elif 'S01' in y:
                    order_details[i][j] = y.replace('S01', 'Central')
                elif 'S02' in y:
                    order_details[i][j] = y.replace('S02', 'Mongkok')
        
# display the order's details in window_check_order 
        window_check_order = tk.Tk()
        window_check_order .title('Order details')
        #The following block of code aims to centre window_check_order.
        window_check_order_width = 450
        window_check_order_height = 550

        screen_width = window_check_order.winfo_screenwidth()   #Get the screen dimension
        screen_height = window_check_order.winfo_screenheight()

        center_x = int(screen_width/2 - window_check_order_width / 2)    #Find the center point
        center_y = int(screen_height/2 - window_check_order_height / 2)

        window_check_order.geometry(f'{window_check_order_width}x{window_check_order_height}+{center_x}+{center_y}')    #Set the position of the window to the center of the screen
        #The above block of code aims to centre window_check_order.
        
        description= tk.Label(window_check_order, text=f"Your order number is {order_number}. \n You placed this order on {order_to_be_checked_date[2]}/{order_to_be_checked_date[1]}/{order_to_be_checked_date[0]}. \n If you would like to change the quantities, please enter the new quantities in below entries.", padx=10, pady=10, wraplength = 300)
        description.grid(row=0, column=0, columnspan=5)

        ItemNum_title= tk.Label(window_check_order, text='Item Number', padx=10, pady=10)
        ItemNum_title.grid(row=1, column=0)
        Name_title= tk.Label(window_check_order, text='Name', padx=10, pady=10)
        Name_title.grid(row=1, column=1)
        Store_title= tk.Label(window_check_order, text='Store', padx=10, pady=10)
        Store_title.grid(row=1, column=2)
        Quantity_title= tk.Label(window_check_order, text='Quantity', padx=10, pady=10)
        Quantity_title.grid(row=1, column=3)
        
        P01_ItemNum = tk.Label(window_check_order, text=f'{results[0][0]}', padx=10, pady=10)
        P01_ItemNum.grid(row=2, column=0)
        P01_Name = tk.Label(window_check_order, text=f'{results[0][1]}', padx=10, pady=10)
        P01_Name.grid(row=2, column=1)
        P01_Store = tk.Label(window_check_order, text=f'{order_details[0][0]}', padx=10, pady=10)
        P01_Store.grid(row=2, column=2)
        P01_Quantity = tk.Label(window_check_order, text=f'{order_details[0][1]}', padx=10, pady=10)
        P01_Quantity.grid(row=2, column=3)
        P01_modify_Quantity = tk.Entry(window_check_order, width=15)
        P01_modify_Quantity.grid(row=2, column=4)
        
        P02_ItemNum = tk.Label(window_check_order, text=f'{results[1][0]}', padx=10, pady=10)
        P02_ItemNum.grid(row=3, column=0)
        P02_Name = tk.Label(window_check_order, text=f'{results[1][1]}', padx=10, pady=10)
        P02_Name.grid(row=3, column=1)
        P02_Store = tk.Label(window_check_order, text=f'{order_details[1][0]}', padx=10, pady=10)
        P02_Store.grid(row=3, column=2)
        P02_Quantity = tk.Label(window_check_order, text=f'{order_details[1][1]}', padx=10, pady=10)
        P02_Quantity.grid(row=3, column=3)
        P02_modify_Quantity = tk.Entry(window_check_order, width=15)
        P02_modify_Quantity.grid(row=3, column=4)

        P03_ItemNum = tk.Label(window_check_order, text=f'{results[2][0]}', padx=10, pady=10)
        P03_ItemNum.grid(row=4, column=0)
        P03_Name = tk.Label(window_check_order, text=f'{results[2][1]}', padx=10, pady=10)
        P03_Name.grid(row=4, column=1)
        P03_Store = tk.Label(window_check_order, text=f'{order_details[2][0]}', padx=10, pady=10)
        P03_Store.grid(row=4, column=2)
        P03_Quantity = tk.Label(window_check_order, text=f'{order_details[2][1]}', padx=10, pady=10)
        P03_Quantity.grid(row=4, column=3)
        P03_modify_Quantity = tk.Entry(window_check_order, width=15)
        P03_modify_Quantity.grid(row=4, column=4)

        P04_ItemNum = tk.Label(window_check_order, text=f'{results[3][0]}', padx=10, pady=10)
        P04_ItemNum.grid(row=5, column=0)
        P04_Name = tk.Label(window_check_order, text=f'{results[3][1]}', padx=10, pady=10)
        P04_Name.grid(row=5, column=1)
        P04_Store = tk.Label(window_check_order, text=f'{order_details[3][0]}', padx=10, pady=10)
        P04_Store.grid(row=5, column=2)
        P04_Quantity = tk.Label(window_check_order, text=f'{order_details[3][1]}', padx=10, pady=10)
        P04_Quantity.grid(row=5, column=3)
        P04_modify_Quantity = tk.Entry(window_check_order, width=15)
        P04_modify_Quantity.grid(row=5, column=4)

        P05_ItemNum = tk.Label(window_check_order, text=f'{results[4][0]}', padx=10, pady=10)
        P05_ItemNum.grid(row=6, column=0)
        P05_Name = tk.Label(window_check_order, text=f'{results[4][1]}', padx=10, pady=10)
        P05_Name.grid(row=6, column=1)
        P05_Store = tk.Label(window_check_order, text=f'{order_details[4][0]}', padx=10, pady=10)
        P05_Store.grid(row=6, column=2)
        P05_Quantity = tk.Label(window_check_order, text=f'{order_details[4][1]}', padx=10, pady=10)
        P05_Quantity.grid(row=6, column=3)
        P05_modify_Quantity = tk.Entry(window_check_order, width=15)
        P05_modify_Quantity.grid(row=6, column=4)

        total_price = order_details[0][1]*results[0][2] + order_details[1][1]*results[1][2] + order_details[2][1]*results[2][2] + order_details[3][1]*results[3][2] + order_details[4][1]*results[4][2]
        total_price_display = tk.Label(window_check_order, text=f"Total price=${total_price}", padx=10, pady=10)
        total_price_display.grid(row=7, column=0, columnspan=4)

        submit_button_modify_order=tk.Button(window_check_order, text='Modify',  command=lambda: update(order_details, order_number, P01_modify_Quantity, P02_modify_Quantity, P03_modify_Quantity, P04_modify_Quantity, P05_modify_Quantity))
        submit_button_modify_order.grid(row=7, column=4)
    
    except ValueError:
        tkinter.messagebox.showerror(title = 'Error',  message = "Please input integers!")

    except IndexError:
        tkinter.messagebox.showerror(title = 'Error',  message = "The order could not be found!")
        
def update(order_details, order_number, P01_modify_Quantity, P02_modify_Quantity, P03_modify_Quantity, P04_modify_Quantity, P05_modify_Quantity):
    try:
# update the order
        P01_new_Quantity = int(P01_modify_Quantity.get())
        P02_new_Quantity = int(P02_modify_Quantity.get())
        P03_new_Quantity = int(P03_modify_Quantity.get())
        P04_new_Quantity = int(P04_modify_Quantity.get())
        P05_new_Quantity = int(P05_modify_Quantity.get())

        
        if order_details[0][0] == "Central" and order_details[0][1] + find_S01_P01_StoreNum() - P01_new_Quantity < 0:
            raise Exception()

        elif order_details[0][0] == "Mongkok" and order_details[0][1] + find_S02_P01_StoreNum() - P01_new_Quantity < 0:
            raise Exception()

        if order_details[1][0] == "Central" and order_details[1][1] + find_S01_P02_StoreNum() - P02_new_Quantity < 0:
            raise Exception()

        elif order_details[1][0] == "Mongkok" and order_details[0][1] + find_S02_P02_StoreNum() - P02_new_Quantity < 0:
            raise Exception()

        if order_details[2][0] == "Central" and order_details[2][1] + find_S01_P03_StoreNum() - P03_new_Quantity < 0:
            raise Exception()

        elif order_details[2][0] == "Mongkok" and order_details[2][1] + find_S02_P03_StoreNum() - P03_new_Quantity < 0:
            raise Exception()

        if order_details[3][0] == "Central" and order_details[3][1] + find_S01_P04_StoreNum() - P04_new_Quantity < 0:
            raise Exception()

        elif order_details[3][0] == "Mongkok" and order_details[3][1] + find_S02_P04_StoreNum() - P04_new_Quantity < 0:
            raise Exception()

        if order_details[4][0] == "Central" and order_details[4][1] + find_S01_P05_StoreNum() - P05_new_Quantity < 0:
            raise Exception()

        elif order_details[4][0] == "Mongkok" and order_details[4][1] + find_S02_P05_StoreNum() - P05_new_Quantity < 0:
            raise Exception()
            
        cur_modify_order_update_OrderLine_table = conn.cursor()
        cur_modify_order_update_OrderLine_table.execute('''UPDATE OrderLine SET  NumOrdered=? WHERE OrderNum=? and ItemNum = "P01" ''', (P01_new_Quantity, order_number))
        conn.commit()

        cur_modify_order_update_OrderLine_table = conn.cursor()
        cur_modify_order_update_OrderLine_table.execute('''UPDATE OrderLine SET  NumOrdered=? WHERE OrderNum=? and ItemNum = "P02" ''', (P02_new_Quantity, order_number))
        conn.commit()

        cur_modify_order_update_OrderLine_table = conn.cursor()
        cur_modify_order_update_OrderLine_table.execute('''UPDATE OrderLine SET  NumOrdered=? WHERE OrderNum=? and ItemNum = "P03" ''', (P03_new_Quantity, order_number))
        conn.commit()
        
        cur_modify_order_update_OrderLine_table = conn.cursor()
        cur_modify_order_update_OrderLine_table.execute('''UPDATE OrderLine SET  NumOrdered=? WHERE OrderNum=? and ItemNum = "P04" ''', (P04_new_Quantity, order_number))
        conn.commit()

        cur_modify_order_update_OrderLine_table = conn.cursor()
        cur_modify_order_update_OrderLine_table.execute('''UPDATE OrderLine SET  NumOrdered=? WHERE OrderNum=? and ItemNum = "P05" ''', (P05_new_Quantity, order_number))
        conn.commit()

# display a messagebox  
        tkinter.messagebox.showinfo(title = 'Modified successfully',  message = f"You modified order {order_number} successfully. \nYou can enter the order number again to check the order's details.")
        
    except ValueError:
        tkinter.messagebox.showerror(title = 'Error',  message = "Please input integers!")

    except Exception:
        tkinter.messagebox.showerror(title = 'Error',  message = "There are insuffcient stocks.")
        
def delete():
    try:
        order_to_be_deleted = int(delete_order_entry.get())

        cur_delete_order_check = conn.cursor()
        cur_delete_order_check.execute('''SELECT * FROM Orders WHERE OrderNum=? ''', (order_to_be_deleted,))
        cur_delete_order_check = cur_delete_order_check.fetchall()
        cur_delete_order_check = cur_delete_order_check[0][0]
        
        cur = conn.cursor()
        cur.execute('''DELETE FROM Orders WHERE OrderNum=?  ''', (order_to_be_deleted,))
        conn.commit()

        tkinter.messagebox.showinfo(title = 'Deleted successfully',  message = f"Order {cur_delete_order_check } has been deleted successfully.")
        
    except ValueError:
        tkinter.messagebox.showerror(title = 'Error',  message = "Please input integers!")

    except IndexError:
        tkinter.messagebox.showerror(title = 'Error',  message = "The order could not be found!")
        
window = tk.Tk()
window.title('Welcome to KEMA Beverage Store')
#The following block of code aims to centre windiow.
window_width = 480
window_height = 610

screen_width = window.winfo_screenwidth()   #Get the screen dimension
screen_height = window.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)    #Find the center point
center_y = int(screen_height/2 - window_height / 2)

window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')    #Set the position of the window to the center of the screen
#The above block of code aims to centre windiow.

# find the current avaliable stock of each product in each store
def find_S01_P01_StoreNum():
        cur_find_S01_P01_StoreNum = conn.cursor()
        cur_find_S01_P01_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S01" AND ItemNum = "P01"  ''')
        return cur_find_S01_P01_StoreNum.fetchall()[0][0]

def find_S02_P01_StoreNum():
        cur_find_S02_P01_StoreNum = conn.cursor()
        cur_find_S02_P01_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S02" AND ItemNum = "P01"  ''')
        return cur_find_S02_P01_StoreNum.fetchall()[0][0]

def find_S01_P02_StoreNum():
        cur_find_S01_P02_StoreNum = conn.cursor()
        cur_find_S01_P02_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S01" AND ItemNum = "P02"  ''')
        return cur_find_S01_P02_StoreNum.fetchall()[0][0]

def find_S02_P02_StoreNum():
        cur_find_S02_P02_StoreNum = conn.cursor()
        cur_find_S02_P02_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S02" AND ItemNum = "P02"  ''')
        return cur_find_S02_P02_StoreNum.fetchall()[0][0]

def find_S01_P03_StoreNum():
        cur_find_S01_P03_StoreNum = conn.cursor()
        cur_find_S01_P03_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S01" AND ItemNum = "P03"  ''')
        return cur_find_S01_P03_StoreNum.fetchall()[0][0]

def find_S02_P03_StoreNum():
        cur_find_S02_P03_StoreNum = conn.cursor()
        cur_find_S02_P03_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S02" AND ItemNum = "P03"  ''')
        return cur_find_S02_P03_StoreNum.fetchall()[0][0]
    
def find_S01_P04_StoreNum():
        cur_find_S01_P04_StoreNum = conn.cursor()
        cur_find_S01_P04_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S01" AND ItemNum = "P04"  ''')
        return cur_find_S01_P04_StoreNum.fetchall()[0][0]

def find_S02_P04_StoreNum():
        cur_find_S02_P04_StoreNum = conn.cursor()
        cur_find_S02_P04_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S02" AND ItemNum = "P04"  ''')
        return cur_find_S02_P04_StoreNum.fetchall()[0][0]

def find_S01_P05_StoreNum():
        cur_find_S01_P05_StoreNum = conn.cursor()
        cur_find_S01_P05_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S01" AND ItemNum = "P05"  ''')
        return cur_find_S01_P05_StoreNum.fetchall()[0][0]

def find_S02_P05_StoreNum():
        cur_find_S02_P05_StoreNum = conn.cursor()
        cur_find_S02_P05_StoreNum.execute('''SELECT AvailableStockNum FROM AvailableStock WHERE StoreNum ="S02" AND ItemNum = "P05"  ''')
        return cur_find_S02_P05_StoreNum.fetchall()[0][0]

# Dropdown menu options
P01_options = [
    f"Central ({find_S01_P01_StoreNum()})",
    f"Mongkok ({find_S02_P01_StoreNum()})"
]

P02_options = [
    f"Central ({find_S01_P02_StoreNum()})",
    f"Mongkok ({find_S02_P02_StoreNum()})"
]

P03_options = [
    f"Central ({find_S01_P03_StoreNum()})",
    f"Mongkok ({find_S02_P03_StoreNum()})"
]

P04_options = [
    f"Central ({find_S01_P04_StoreNum()})",
    f"Mongkok ({find_S02_P04_StoreNum()})"
]

P05_options = [
    f"Central ({find_S01_P05_StoreNum()})",
    f"Mongkok ({find_S02_P05_StoreNum()})"
]

# datatype of menu text
P01_clicked = tk.StringVar()
P02_clicked = tk.StringVar()
P03_clicked = tk.StringVar()
P04_clicked = tk.StringVar()
P05_clicked = tk.StringVar()

# initial menu text
P01_clicked.set( "Please select" )
P02_clicked.set( "Please select" )
P03_clicked.set( "Please select" )
P04_clicked.set( "Please select" )
P05_clicked.set( "Please select" )

instruction= tk.Label(window, text='If you would like to place an order, please indicate the quantities below.', padx=10, pady=10)
instruction.grid(row=0, column=0, columnspan=5)

ItemNum_title= tk.Label(window, text='Item Number', padx=10, pady=10)
ItemNum_title.grid(row=1, column=0)
Name_title= tk.Label(window, text='Name', padx=10, pady=10)
Name_title.grid(row=1, column=1)
Price_title= tk.Label(window, text='Price', padx=10, pady=10)
Price_title.grid(row=1, column=2)
Store_title= tk.Label(window, text='Store', padx=10, pady=10)
Store_title.grid(row=1, column=3)
Quantity_title= tk.Label(window, text='Quantity', padx=10, pady=10)
Quantity_title.grid(row=1, column=4)

P01_ItemNum = tk.Label(window, text=f'{results[0][0]}', padx=10, pady=10)
P01_ItemNum.grid(row=2, column=0)
P01_Name = tk.Label(window, text=f'{results[0][1]}', padx=10, pady=10)
P01_Name.grid(row=2, column=1)
P01_Price = tk.Label(window, text=f'${results[0][2]}', padx=10, pady=10)
P01_Price.grid(row=2, column=2)
P01_Store = tk.OptionMenu(window , P01_clicked , *P01_options )    # Create Dropdown menu
P01_Store.grid(row=2, column=3)
P01_Quantity_entry = tk.Entry(window, width=15)
P01_Quantity_entry.grid(row=2, column=4)

P02_ItemNum = tk.Label(window, text=f'{results[1][0]}', padx=10, pady=10)
P02_ItemNum.grid(row=3, column=0)
P02_Name = tk.Label(window, text=f'{results[1][1]}', padx=10, pady=10)
P02_Name.grid(row=3, column=1)
P02_Price = tk.Label(window, text=f'${results[1][2]}', padx=10, pady=10)
P02_Price.grid(row=3, column=2)
P02_Store = tk.OptionMenu( window , P02_clicked , *P02_options )    # Create Dropdown menu
P02_Store.grid(row=3, column=3)
P02_Quantity_entry = tk.Entry(window, width=15)
P02_Quantity_entry.grid(row=3, column=4)

P03_ItemNum = tk.Label(window, text=f'{results[2][0]}', padx=10, pady=10)
P03_ItemNum.grid(row=4, column=0)
P03_Name = tk.Label(window, text=f'{results[2][1]}', padx=10, pady=10)
P03_Name.grid(row=4, column=1)
P03_Price = tk.Label(window, text=f'${results[2][2]}', padx=10, pady=10)
P03_Price.grid(row=4, column=2)
P03_Store = tk.OptionMenu( window , P03_clicked , *P03_options )    # Create Dropdown menu
P03_Store.grid(row=4, column=3)
P03_Quantity_entry = tk.Entry(window, width=15)
P03_Quantity_entry.grid(row=4, column=4)

P04_ItemNum = tk.Label(window, text=f'{results[3][0]}', padx=10, pady=10)
P04_ItemNum.grid(row=5, column=0)
P04_Name = tk.Label(window, text=f'{results[3][1]}', padx=10, pady=10)
P04_Name.grid(row=5, column=1)
P04_Price = tk.Label(window, text=f'${results[3][2]}', padx=10, pady=10)
P04_Price.grid(row=5, column=2)
P04_Store = tk.OptionMenu( window , P04_clicked , *P04_options )    # Create Dropdown menu
P04_Store.grid(row=5, column=3)
P04_Quantity_entry = tk.Entry(window, width=15)
P04_Quantity_entry.grid(row=5, column=4)

P05_ItemNum = tk.Label(window, text=f'{results[4][0]}', padx=10, pady=10)
P05_ItemNum.grid(row=6, column=0)
P05_Name = tk.Label(window, text=f'{results[4][1]}', padx=10, pady=10)
P05_Name.grid(row=6, column=1)
P05_Price = tk.Label(window, text=f'${results[4][2]}', padx=10, pady=10)
P05_Price.grid(row=6, column=2)
P05_Store = tk.OptionMenu( window , P05_clicked , *P05_options )    # Create Dropdown menu
P05_Store.grid(row=6, column=3)
P05_Quantity_entry = tk.Entry(window, width=15)
P05_Quantity_entry.grid(row=6, column=4)

submit_button_add_order = tk.Button(window, text='Submit' , command=add_order)
submit_button_add_order.grid(row=7, column=0, columnspan=5)

Check_order = tk.Label(window, text="If you would like to view or modify an order's details, please enter the order number to check the order's details.", padx=10, pady=10, wraplength = 400)
Check_order.grid(row=8, column=0, columnspan=5)
Check_order_entry = tk.Entry(window, width=15)
Check_order_entry.grid(row=9, column=0, columnspan=5)

a_new = tk.Label(window, text="")
a_new.grid(row=10)
submit_button_check_order = tk.Button(window, text='Check' , command=check_order)   
submit_button_check_order.grid(row=11, column=0, columnspan=5)

delete_order = tk.Label(window, text="If you would like to delete an order, please enter the order number below.", padx=10, pady=10, wraplength = 400)
delete_order.grid(row=12, column=0, columnspan=5)
delete_order_entry = tk.Entry(window, width=15)
delete_order_entry.grid(row=13, column=0, columnspan=5)
a_new_2 = tk.Label(window, text="")
a_new_2.grid(row=14)
submit_button_delete_order = tk.Button(window, text='Delete',  command= delete) 
submit_button_delete_order.grid(row=15, column=0, columnspan=5)

cur_addrss_information = conn.cursor()
cur_addrss_information.execute('SELECT * FROM Store')
cur_addrss_information = cur_addrss_information.fetchall()
S01_name = cur_addrss_information[0][1]
S02_name = cur_addrss_information[1][1]
S01_address = cur_addrss_information[0][2]
S02_address  = cur_addrss_information[1][2]

addrss_information = tk.Label(window, text=f"Our stores' addresses: \n {S01_name}:{S01_address} \n {S02_name}:{S02_address}", padx=10, pady=10, wraplength = 400)
addrss_information.grid(row=16, column=0, columnspan=5)
window.mainloop()

conn.close()


















































































