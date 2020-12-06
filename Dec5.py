import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# import data
AAPL = pd.read_csv('AAPL.csv', index_col=0)
NOK = pd.read_csv('NOK.csv', index_col=0)
AMD = pd.read_csv('AMD.csv', index_col=0)
GE = pd.read_csv('GE.csv', index_col=0)
MSFT = pd.read_csv('MSFT.csv', index_col=0)

# make 1 variable
stocks = pd.DataFrame()
stocks['AAPL'] = AAPL['Close']
stocks['NOK'] = NOK['Close']
stocks['AMD'] = AMD['Close']
stocks['GE'] = GE['Close']
stocks['MSFT'] = MSFT['Close']

root = tk.Tk()
# starting conditions

past = 1
present = 30
wallet = 1000


def buttonpress():
    # makes these things get through each iteration
    global past
    global present
    global wallet
    global L1, L2, L3, L4, L5, L6, label6, x
    global priceprint


    # number of each stock bought
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    x3 = float(entry3.get())
    x4 = float(entry4.get())
    x5 = float(entry5.get())

    #evaluate the pruchase
    price1 = float(stocks['AAPL'][present - 1:present]) * abs(x1)
    price2 = float(stocks['NOK'][present - 1:present]) * abs(x2)
    price3 = float(stocks['AMD'][present - 1:present]) * abs(x3)
    price4 = float(stocks['GE'][present - 1:present]) * abs(x4)
    price5 = float(stocks['MSFT'][present - 1:present]) * abs(x5)
    totalcost = price1 + price2 + price3 + price4 + price5
    if totalcost > wallet: #if the purchase was good
        canvas2 = tk.Toplevel(root)
        canvas2.geometry('300x40')
        labelExample = tk.Label(canvas2, text = "You bought too much. Try again")
        labelExample.pack()
    else: #if the purchase was bad
        # remove old elements
        if past == 1:
            pass
        else:
            canvas1.delete(L1, L2, L3, L4, L5, L6)
        try:
            canvas1.delete(priceprint)  # remove this label if it's not needed
        except:
            pass

        # updates the date
        past += 7
        present += 7
        # this changes the x-Axis so that it updates
        x = stocks.index[past:present]
        # money change after transaction
        stock1 = float(stocks['AAPL'][present - 1:present]) - float(stocks['AAPL'][present - 6:present - 5])
        stock2 = float(stocks['NOK'][present - 1:present]) - float(stocks['NOK'][present - 6:present - 5])
        stock3 = float(stocks['AMD'][present - 1:present]) - float(stocks['AMD'][present - 6:present - 5])
        stock4 = float(stocks['GE'][present - 1:present]) - float(stocks['GE'][present - 6:present - 5])
        stock5 = float(stocks['MSFT'][present - 1:present]) - float(stocks['MSFT'][present - 6:present - 5])

        # purchases
        purchase1 = stock1 * x1
        purchase2 = stock2 * x2
        purchase3 = stock3 * x3
        purchase4 = stock4 * x4
        purchase5 = stock5 * x5
        wallet = wallet + purchase1 + purchase2 + purchase3 + purchase4 + purchase5

        # output, the money gained and lost
        label1 = tk.Label(root, text=purchase1)
        label2 = tk.Label(root, text=purchase2)
        label3 = tk.Label(root, text=purchase3)
        label4 = tk.Label(root, text=purchase4)
        label5 = tk.Label(root, text=purchase5)
        label6 = tk.Label(root, text=wallet)

        # output placement
        L1 = canvas1.create_window(300, 100, window=label1)
        L2 = canvas1.create_window(300, 140, window=label2)
        L3 = canvas1.create_window(300, 180, window=label3)
        L4 = canvas1.create_window(300, 220, window=label4)
        L5 = canvas1.create_window(300, 260, window=label5)
        L6 = canvas1.create_window(250, 350, window=label6)

def buttonpress2():
    global priceprint
    try:
        canvas1.delete(priceprint) # remove this label if it's not needed
    except:
        pass
    #collect the amounts
    x1 = float(entry1.get())
    x2 = float(entry2.get())
    x3 = float(entry3.get())
    x4 = float(entry4.get())
    x5 = float(entry5.get())

    #price it out
    price1 = float(stocks['AAPL'][present - 1:present]) * abs(x1)
    price2 = float(stocks['NOK'][present - 1:present]) * abs(x2)
    price3 = float(stocks['AMD'][present - 1:present]) * abs(x3)
    price4 = float(stocks['GE'][present - 1:present]) * abs(x4)
    price5 = float(stocks['MSFT'][present - 1:present]) * abs(x5)
    totalcost = price1 + price2 + price3 + price4 + price5
    #print it
    pricelabel = tk.Label(root, text=totalcost)
    priceprint = canvas1.create_window(280, 50, window=pricelabel)


canvas1 = tk.Canvas(root, width=400, height=450)
canvas1.pack()

# labels
label6 = tk.Label(root, text=wallet)

canvas1.create_text(200, 100, text='Apple')
canvas1.create_text(200, 140, text='Nokia')
canvas1.create_text(200, 180, text='AMD')
canvas1.create_text(200, 220, text='GE')
canvas1.create_text(200, 260, text='MSFT')
canvas1.create_text(150, 350, text='Wallet')
canvas1.create_text(100, 300, text='Number of share')
canvas1.create_text(280, 300, text='profits and losses in $')
label6 = canvas1.create_window(250, 350, window=label6) # what's in the wallet right now


# text inputs for the user
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)
entry5 = tk.Entry(root)

canvas1.create_window(100, 100, window=entry1)
canvas1.create_window(100, 140, window=entry2)
canvas1.create_window(100, 180, window=entry3)
canvas1.create_window(100, 220, window=entry4)
canvas1.create_window(100, 260, window=entry5)

button1 = tk.Button(text='Buy stocks and move forward', command=buttonpress)
button2 = tk.Button(text='Price before you buy', command=buttonpress2)
canvas1.create_window(200, 400, window=button1)
canvas1.create_window(130, 50, window=button2)

figure = plt.Figure()
fig, ax = plt.subplots(figsize=(7, 5))
ax.set(xlim=(10, 29), ylim=(20, 100))  # gives boarder limits
x = stocks.index[past:present]
AAPL = list(stocks['AAPL'])
NOK = list(stocks['NOK'])
AMD = list(stocks['AMD'])
GE = list(stocks['GE'])
MSFT = list(stocks['MSFT'])


def animate(i):  # good info: https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

    plt.cla()  # removes old graph data, also clears out the axis
    plt.plot(x, AAPL[past:present], c='green', marker='', label='AAPL')
    plt.plot(x, NOK[past:present], c='grey', marker='o', label='NOK')
    plt.plot(x, AMD[past:present], c='brown', marker='+', label='AMD')
    plt.plot(x, GE[past:present], c='peru', marker='4', label='GE')
    plt.plot(x, MSFT[past:present], c='indigo', marker='|', label='MSFT')
    plt.legend(loc='upper left')
    plt.xticks(stocks.index[past:present:3], rotation=45)
    plt.xlabel('Date: year-month-day')
    plt.ylabel('Price per stock: $/share')
    plt.tight_layout()


anim = FuncAnimation(
    fig, animate, interval=300)

ax = figure.add_subplot(111)
plt.draw()
plt.show()

root.mainloop()