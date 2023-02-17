#Sofia Pereira Coutinho
#November 20, 2022

#This program will use an API to obtain the current value of a crypto currency.
#It will then use this information to generate a report of how much in USD it would cost to buy the specified amount.
#The program will use a graphical user interface (GUI) to facilitate the exchange rate conversions.

import tkinter, tkinter.messagebox, requests, json, csv

#Create conversion function that will run when convert button is clicked
def convert():
    """Returns the crypto conversions in a csv file"""
    
    #If any entry box is empty, default back to 0
    if len(btc_box.get()) < 1:
        btc_qty = 0
    else:
        btc_qty = btc_box.get()
    
    if len(eth_box.get()) < 1:
        eth_qty = 0
    else:
        eth_qty = eth_box.get()
        
    if len(bnb_box.get()) < 1:
        bnb_qty = 0
    else:
        bnb_qty = bnb_box.get()
        
    if len(xrp_box.get()) < 1:
        xrp_qty = 0
    else:
        xrp_qty = xrp_box.get()
        
    #ensure user inserted valid values
    try:
        btc_qty = float(btc_qty)
        eth_qty = float(eth_qty)
        bnb_qty = float(bnb_qty)
        xrp_qty = float(xrp_qty)
        
        #ensure all values are positive
        assert btc_qty >= 0
        assert eth_qty >= 0
        assert bnb_qty >= 0
        assert xrp_qty >= 0
        
        valid = "yes"
    
    except ValueError:
        tkinter.messagebox.showwarning("Invalid Value", "An error occured. Please ensure that positive numeric values are entered.")
        valid = "no"
    
    except AssertionError:
        tkinter.messagebox.showwarning("Invalid Value", "An error occured. Please ensure that positive numeric values are entered.")
        valid = "no"
        
    except:
        tkinter.messagebox.showwarning("Error", "Something went wrong, please try again.")
        valid = "no"
        
        
    #ensure program only runs if all values inserted are valid
    if valid == "yes":
         
        btc = data["rates"]["BTC"]
        eth = data["rates"]["ETH"]
        bnb = data["rates"]["BNB"]
        xrp = data["rates"]["XRP"]
            
        btc_cost = btc * btc_qty
        eth_cost = eth * eth_qty
        bnb_cost = bnb * bnb_qty
        xrp_cost = xrp * xrp_qty
        total_cost = btc_cost + eth_cost + bnb_cost + xrp_cost

        #Create csv file and upload all relevant values 
        with open("crypto_conversions.csv","w") as file:
            writer = csv.writer(file, lineterminator="\n")
            writer.writerow(["Curreny","Price","Quantity","Cost (USD)", "Exchange Rate USD:COIN"])
            writer.writerow(["BTC", btc, btc_qty, btc_cost, 1/btc])
            writer.writerow(["ETH", eth, eth_qty, eth_cost, 1/eth])
            writer.writerow(["BNB", bnb, bnb_qty, bnb_cost, 1/bnb])
            writer.writerow(["XRP", xrp, xrp_qty, xrp_cost, 1/xrp])
            writer.writerow(["--", "--", "--", "--", "--"])
            writer.writerow(["Total", "--", "--", total_cost, "--"])
            
        tkinter.messagebox.showinfo("Success!", "The conversions were stored in crpyto_conversion.csv.")
        
        #Reset all values to 0 after successful upload into the CSV file
        btc_box.delete(0, "end")
        btc_box.insert(0, "0")
        
        eth_box.delete(0, "end")
        eth_box.insert(0, "0")
        
        bnb_box.delete(0, "end")
        bnb_box.insert(0, "0")
        
        xrp_box.delete(0, "end")
        xrp_box.insert(0, "0")
        

#Create the GUI for user interaction#
root = tkinter.Tk()
root.title("Crypto Exchange Rate Calculator")
root.configure(bg = "bisque")
root.geometry("345x75")

#Create all four crypto labels and respective entry boxes
btc_label = tkinter.Label(root, text="BTC:")
btc_label.grid(row=0, column=0, pady = 5, padx = 3)
btc_label.configure(bg = "bisque")

eth_label = tkinter.Label(root, text="ETH:")
eth_label.grid(row=0, column=2, pady = 5, padx = 3)
eth_label.configure(bg = "bisque")

bnb_label = tkinter.Label(root, text="BNB:")
bnb_label.grid(row=1, column=0, pady = 5, padx = 3)
bnb_label.configure(bg = "bisque")

xrp_label = tkinter.Label(root, text="XRP:")
xrp_label.grid(row=1, column=2, pady = 5, padx = 3)
xrp_label.configure(bg = "bisque")

btc_box = tkinter.Entry(root, width=10)
btc_box.grid(row=0, column=1)
btc_box.insert(0, "0")

eth_box = tkinter.Entry(root, width=10)
eth_box.grid(row=0, column=3, padx = 3)
eth_box.insert(0, "0")

bnb_box = tkinter.Entry(root, width=10)
bnb_box.grid(row=1, column=1)
bnb_box.insert(0, "0")

xrp_box = tkinter.Entry(root, width=10)
xrp_box.grid(row=1, column=3, padx = 3)
xrp_box.insert(0, "0")

#Create conversion button
convert_button = tkinter.Button(root, text="Convert Currency", command=convert)
convert_button.configure(bg="pale green", width = 15)
convert_button.grid(row=0, column=4, pady = 5, padx = 5)

#Create close button 
close_button = tkinter.Button(root, text="Close Converter", command=root.destroy)
close_button.configure(bg="dark orange", width = 15)
close_button.grid(row=1, column=4, pady = 5, padx = 5)


#Ensure program only runs if request is successful
try:
    response = requests.get("http://api.coinlayer.com/api/live?access_key=f732b5f05ca26ba8a082ee27aafe79e0")
    data = json.loads(response.text)
    
    #ensure it is the correct API link
    assert data["success"] == True

    root.mainloop()
    
except AssertionError:
    print("Error occured. Please double check API link.")

except:
    print("Error occured. Please double check link.")
