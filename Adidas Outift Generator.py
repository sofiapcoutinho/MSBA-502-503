# Sammie Whitman & Sofia Coutinho
# Date of Submission = 12/11/22

# Final Project - Adidas Outfit Generator
    # the code below creates a Python program that allows the user to generate an outfit from Adidas brand clothes based on their color & price specifications
        # for tops, bottoms, shoes, outerwear, & accessories
    # the program executes the following:
        # Gender Selection
            # the user can pick from either Women or Men in terms of the designation for the clothes
        # Clothing Specifications
            # the user can set a color & a max price limit for each of the 5 clothing categories
        # Images
            # once the user is ready to generate an outfit, a window containing images of all clothing items will appear
            # the user will be able to input whether they like the outfit or not based on the images
        # Success/Failure
            # Success = if the user likes the outfit, then each clothing item's details will be written to a csv file called outfit.csv
            # Failure = if the user does not like the outfit, they will be prompted to try again to generate a new outfit


# import necessary packages
import pandas as pd
import tkinter, tkinter.messagebox, tkinter.ttk
from tkinter.messagebox import askyesno
import random
from tkinter import *
from tkinter.ttk import *
import tkinter.font as tkFont
from PIL import Image, ImageTk
import urllib.request
import io
import csv


# read in data
data = pd.read_csv('adidas CSV.csv')
data = pd.DataFrame(data)

# remove unnecessary columns
data.drop(['sku','original_price','currency','availability','source','source_website','brand','country','language','reviews_count','crawled_at'], axis=1, inplace=True)

# drop unnecessary categories
cat_drop = data[(data['category']=='Undergarments') | (data['category']=='Set') | (data['category']=='Sport') | (data['category']=='Swim')].index
data.drop(cat_drop , inplace=True)

# remove / from breadcrumbs to leave only the genders
bread_new = data['breadcrumbs'].str.split('/').str[0]
data['breadcrumbs'] = bread_new

# change breadcrumbs column name to gender
data.rename(columns={'breadcrumbs': 'gender'}, inplace=True)

# create gender dataframes for women & men
women = data[(data['gender']=='Women')]
men = data[(data['gender']=='Men')]

# group by color in each category to determine which colors are present in each category
color_grouped = data.groupby(['category','color','gender'])['category'].count()

# create colors option lists for each gender/category pair
women_accessory_colors = []
women_bottoms_colors = []
women_outerwear_colors = []
women_shoes_colors = []
women_top_colors = []
men_accessory_colors = []
men_bottoms_colors = []
men_outerwear_colors = []
men_shoes_colors = []
men_top_colors = []

# append color options to appropriate lists
for i in color_grouped.index.values:
    if i[0]=='Accessories' and i[2]=='Women':
        women_accessory_colors.append(i[1])
    elif i[0]=='Bottoms' and i[2]=='Women':
        women_bottoms_colors.append(i[1])
    elif i[0]=='Outerwear' and i[2]=='Women':
        women_outerwear_colors.append(i[1])
    elif i[0]=='Shoes' and i[2]=='Women':
        women_shoes_colors.append(i[1])
    elif i[0]=='Top' and i[2]=='Women':
        women_top_colors.append(i[1])
    elif i[0]=='Accessories' and i[2]=='Men':
        men_accessory_colors.append(i[1])
    elif i[0]=='Bottoms' and i[2]=='Men':
        men_bottoms_colors.append(i[1])
    elif i[0]=='Outerwear' and i[2]=='Men':
        men_outerwear_colors.append(i[1])
    elif i[0]=='Shoes' and i[2]=='Men':
        men_shoes_colors.append(i[1])
    elif i[0]=='Top' and i[2]=='Men':
        men_top_colors.append(i[1])



############ GUI ############
# create gender root 
gender_root = tkinter.Tk()
gender_root.title('Adidas Outfit Generator')
gender_root.geometry('560x80')

# create gender options label
gender_label = tkinter.Label(gender_root, text = 'Select a gender for the outfit: ', font = ('Arial Bold',15))
gender_label.grid(row=0,column=0, pady=28)

# create function for women's generate outfit button 
def women_outfit():
    '''Generates an female outfit based on the filters the user inputted'''

    # global appropriate variables
    global gender_root
    
    # create root for user-input GUI
    root = tkinter.Tk()
    root.title('Adidas Outfit Generator')
    root.geometry('700x300')
    
    ######## LABELS ########
    top_label = tkinter.Label(root, text = 'Top', font = ('Arial Bold',15))
    top_label.grid(row=1,column=0)

    bottoms_label = tkinter.Label(root, text = 'Bottoms', font = ('Arial Bold',15))
    bottoms_label.grid(row=2,column=0)

    shoes_label = tkinter.Label(root, text = 'Shoes', font = ('Arial Bold',15))
    shoes_label.grid(row=3,column=0)

    outerwear_label = tkinter.Label(root, text = 'Outerwear', font = ('Arial Bold',15))
    outerwear_label.grid(row=4,column=0)

    accessory_label = tkinter.Label(root, text = 'Accesory', font = ('Arial Bold',15))
    accessory_label.grid(row=5,column=0)

    color_label = tkinter.Label(root, text = 'Color:', font = ('Arial Bold',15))
    color_label.grid(row=0,column=1, pady=12)

    price_label = tkinter.Label(root, text = 'Max Price (nearest $):', font = ('Arial Bold',15))
    price_label.grid(row=0,column=2, pady=12)
    
    
    ######## COMBOBOXES FOR COLOR OPTIONS ########
    top_color_options = tkinter.ttk.Combobox(root, values=women_top_colors, state='readonly', font = 15)
    top_color_options.configure(width=10)
    top_color_options.current(0)
    top_color_options.grid(row=1, column=1, padx=10)

    bottoms_color_options = tkinter.ttk.Combobox(root, values=women_bottoms_colors, state='readonly', font = 15)
    bottoms_color_options.configure(width=10)
    bottoms_color_options.current(0)
    bottoms_color_options.grid(row=2, column=1)

    shoes_color_options = tkinter.ttk.Combobox(root, values=women_shoes_colors, state='readonly', font = 15)
    shoes_color_options.configure(width=10)
    shoes_color_options.current(0)
    shoes_color_options.grid(row=3, column=1)

    outerwear_color_options = tkinter.ttk.Combobox(root, values=women_outerwear_colors, state='readonly', font = 15)
    outerwear_color_options.configure(width=10)
    outerwear_color_options.current(0)
    outerwear_color_options.grid(row=4, column=1)

    accessory_color_options = tkinter.ttk.Combobox(root, values=women_accessory_colors, state='readonly', font = 15)
    accessory_color_options.configure(width=10)
    accessory_color_options.current(0)
    accessory_color_options.grid(row=5, column=1)
    
    
    ######## ENTRYBOXES FOR PRICES ########
    top_price_box = tkinter.Entry(root, width=10, font = 15)
    top_price_box.insert(0, 0)
    top_price_box.grid(row=1, column=2, padx=10)

    bottoms_price_box = tkinter.Entry(root, width=10, font = 15)
    bottoms_price_box.insert(0, 0)
    bottoms_price_box.grid(row=2, column=2)

    shoes_price_box = tkinter.Entry(root, width=10, font = 15)
    shoes_price_box.insert(0, 0)
    shoes_price_box.grid(row=3, column=2)

    outerwear_price_box = tkinter.Entry(root, width=10, font = 15)
    outerwear_price_box.insert(0, 0)
    outerwear_price_box.grid(row=4, column=2)

    accessory_price_box = tkinter.Entry(root, width=10, font = 15)
    accessory_price_box.insert(0, 0)
    accessory_price_box.grid(row=5, column=2)
    
    # create generate outfit button function
    def generate_outfit():
        '''Generates outfit output'''
        
        # minimize extra windows
        gender_root.iconify()
        root.iconify()
               
        # get the user inputs from the GUI
        top_color = top_color_options.get()
        bottoms_color = bottoms_color_options.get()
        shoes_color = shoes_color_options.get()
        outerwear_color = outerwear_color_options.get()
        accessory_color = accessory_color_options.get()
        
        # only execute if prices are formatted correctly
        try:
            # change data types of prices to integers
            top_price = int(top_price_box.get())
            bottoms_price = int(bottoms_price_box.get())
            shoes_price = int(shoes_price_box.get())
            outerwear_price = int(outerwear_price_box.get())
            accessory_price = int(accessory_price_box.get())
                   
            # create dataframes for each category within the gender, using user specifications if they chose women
            df_top = women[(women['category'] == 'Top') & (women['color'] == top_color) & (women['selling_price'] <= top_price)]
            df_bottoms = women[(women['category'] == 'Bottoms') & (women['color'] == bottoms_color) & (women['selling_price'] <= bottoms_price)]
            df_shoes = women[(women['category'] == 'Shoes') & (women['color'] == shoes_color) & (women['selling_price'] <= shoes_price)]
            df_outerwear = women[(women['category'] == 'Outerwear') & (women['color'] == outerwear_color) & (women['selling_price'] <= outerwear_price)]
            df_accessory = women[(women['category'] == 'Accessories') & (women['color'] == accessory_color) & (women['selling_price'] <= accessory_price)]
            
            # if any of the outfit option category lists are empty, tell the user to try again with new color/price options 
            if df_top.empty | df_bottoms.empty | df_shoes.empty | df_outerwear.empty | df_accessory.empty:
                tkinter.messagebox.showwarning('No Outfits Available','Uh-oh! No outfits were found that fit your specifications. Please try again with new selections.')
                # maximize the user-inputs root
                root.deiconify()
                # set all options back to default
                top_color_options.current(0)
                bottoms_color_options.current(0)
                shoes_color_options.current(0)
                outerwear_color_options.current(0)
                accessory_color_options.current(0)
                top_price_box.delete(0, tkinter.END)
                bottoms_price_box.delete(0, tkinter.END)
                shoes_price_box.delete(0, tkinter.END)
                outerwear_price_box.delete(0, tkinter.END)
                accessory_price_box.delete(0, tkinter.END)
             
            # execute only if there are suitable clothing options for every category based on color/price specifications
            else:
                
                # create new window for outfit output
                new_window = Toplevel(gender_root)
                new_window.title('Generated Outfit')
                new_window.geometry('500x2000')
                
                # create random numbers for each category to generate the outfit
                top_rand = random.randrange(0,len(df_top))
                bottoms_rand = random.randrange(0,len(df_bottoms))
                shoes_rand = random.randrange(0,len(df_shoes))
                outerwear_rand = random.randrange(0,len(df_outerwear))
                accessory_rand = random.randrange(0,len(df_accessory))
                
                # find the data point from the random number for each category
                top_image_loc = df_top['images'].iloc[top_rand]
                bottoms_image_loc = df_bottoms['images'].iloc[bottoms_rand]
                shoes_image_loc = df_shoes['images'].iloc[shoes_rand]
                outerwear_image_loc = df_outerwear['images'].iloc[outerwear_rand]
                accessory_image_loc = df_accessory['images'].iloc[accessory_rand]
                      
                # insert images into new GUI
                top_link = urllib.request.urlopen(top_image_loc).read()
                im = Image.open(io.BytesIO(top_link))
                resize_image = im.reduce(3)
                top_image = ImageTk.PhotoImage(resize_image)
                label1 = tkinter.Label(new_window, image=top_image)
                label1.grid(row=0, column = 0)
                
                bottoms_link = urllib.request.urlopen(bottoms_image_loc).read()
                im = Image.open(io.BytesIO(bottoms_link))
                resize_image = im.reduce(3)
                bottoms_image = ImageTk.PhotoImage(resize_image)
                label2 = tkinter.Label(new_window, image=bottoms_image)
                label2.grid(row=1, column = 0)
                
                shoes_link = urllib.request.urlopen(shoes_image_loc).read()
                im = Image.open(io.BytesIO(shoes_link))
                resize_image = im.reduce(3)
                shoes_image = ImageTk.PhotoImage(resize_image)
                label3 = tkinter.Label(new_window, image=shoes_image)
                label3.grid(row=2, column = 0)
                
                outerwear_link = urllib.request.urlopen(outerwear_image_loc).read()
                im = Image.open(io.BytesIO(outerwear_link))
                resize_image = im.reduce(3)
                outerwear_image = ImageTk.PhotoImage(resize_image)
                label4 = tkinter.Label(new_window, image=outerwear_image)
                label4.grid(row=0, column = 1)
                
                accessory_link = urllib.request.urlopen(accessory_image_loc).read()
                im = Image.open(io.BytesIO(accessory_link))
                resize_image = im.reduce(3)
                accessory_image = ImageTk.PhotoImage(resize_image)
                label5 = tkinter.Label(new_window, image=accessory_image)
                label5.grid(row=1, column = 1)
                
                # ask the user if they like the outfit or not
                answer = askyesno(title="Outfit Generated",message="Yay! We found an outfit! Do you like it?")
                
                # if they like the outfit, write each item's info to a csv file called outfit.csv
                if answer == True:
                    tkinter.messagebox.showinfo('Yay!', 'A csv file called outfit.csv has been created with your outfit details!')
                    
                    # set each item to the row in the oringinal dataframe that matches
                    final_top = data[(data['images']==top_image_loc)]
                    final_bottoms = data[(data['images']==bottoms_image_loc)]
                    final_shoes = data[(data['images']==shoes_image_loc)]
                    final_outerwear = data[(data['images']==outerwear_image_loc)]
                    final_accessory = data[(data['images']==accessory_image_loc) & (data['gender']=='Women')] 
                    
                    # write each row to the csv
                    final_top.to_csv('outfit.csv',mode='w',index=False,header=True)
                    final_bottoms.to_csv('outfit.csv',mode='a',index=False,header=False)
                    final_shoes.to_csv('outfit.csv',mode='a',index=False,header=False)
                    final_outerwear.to_csv('outfit.csv',mode='a',index=False,header=False)
                    final_accessory.to_csv('outfit.csv',mode='a',index=False,header=False)
                    
                    # destroy the root once the process is done
                    gender_root.destroy()
                    root.destroy()
                
                # if they don't like the outfit, display a message telling them to try again
                else:
                    tkinter.messagebox.showinfo('Boo!','Oh no! Try the outfit generator again to create new outfit.')
                    
                    # maximize the root
                    root.deiconify()
                    # destroy the image window
                    new_window.destroy()
                    # set all options back to default
                    top_color_options.current(0)
                    bottoms_color_options.current(0)
                    shoes_color_options.current(0)
                    outerwear_color_options.current(0)
                    accessory_color_options.current(0)
                    top_price_box.delete(0, tkinter.END)
                    bottoms_price_box.delete(0, tkinter.END)
                    shoes_price_box.delete(0, tkinter.END)
                    outerwear_price_box.delete(0, tkinter.END)
                    accessory_price_box.delete(0, tkinter.END)
        
        # if the prices are formatted incorrectly, show a message stating to try again
        except:
            tkinter.messagebox.showwarning('Incorrect Formating','Uh-oh! Make sure you are formatting the Max Price to the nearest whole dollar. Please try again with new selections.')
            # maximize the root
            root.deiconify()
            # set all options back to default
            top_color_options.current(0)
            bottoms_color_options.current(0)
            shoes_color_options.current(0)
            outerwear_color_options.current(0)
            accessory_color_options.current(0)
            top_price_box.delete(0, tkinter.END)
            bottoms_price_box.delete(0, tkinter.END)
            shoes_price_box.delete(0, tkinter.END)
            outerwear_price_box.delete(0, tkinter.END)
            accessory_price_box.delete(0, tkinter.END)
    
    # create a function for the clear button        
    def clear_selections():
        '''Clears current selections'''
        top_color_options.current(0)
        bottoms_color_options.current(0)
        shoes_color_options.current(0)
        outerwear_color_options.current(0)
        accessory_color_options.current(0)
        top_price_box.delete(0, tkinter.END)
        bottoms_price_box.delete(0, tkinter.END)
        shoes_price_box.delete(0, tkinter.END)
        outerwear_price_box.delete(0, tkinter.END)
        accessory_price_box.delete(0, tkinter.END)
    
    # create a function for the exit button
    def destroy():
        '''Destroys the roots'''
        gender_root.destroy()
        root.destroy()

    ######## BUTTONS - GENERATE OUTFIT, CLEAR, EXIT ########
    # create generate outfit button
    outfit_button = tkinter.Button(root, text = 'Generate Outfit', command = generate_outfit, font = ('Arial Bold',14))
    outfit_button.configure(bg='light green', width=15)
    outfit_button.grid(row=2,column=3, padx=5)
    
    # create clear button
    clear_button = tkinter.Button(root, text = 'Clear', command = clear_selections, font = ('Arial Bold',14))
    clear_button.configure(bg='light yellow', width=15)
    clear_button.grid(row=3,column=3, padx=5)
    
    # create exit button
    exit_button = tkinter.Button(root, text = 'Exit', command = destroy, font = ('Arial Bold',14))
    exit_button.configure(bg='red', width=15)
    exit_button.grid(row=4,column=3, padx=5)
    

# create function for men's generate outfit button 
def men_outfit():
    '''Generates an male outfit based on the filters the user inputted'''
    
    # global appropriate variables
    global gender_root

    # create root for user-input GUI
    root = tkinter.Tk()
    root.title('Adidas Outfit Generator')
    root.geometry('700x300')
    
    ######## LABELS ########
    top_label = tkinter.Label(root, text = 'Top', font = ('Arial Bold',15))
    top_label.grid(row=1,column=0)

    bottoms_label = tkinter.Label(root, text = 'Bottoms', font = ('Arial Bold',15))
    bottoms_label.grid(row=2,column=0)

    shoes_label = tkinter.Label(root, text = 'Shoes', font = ('Arial Bold',15))
    shoes_label.grid(row=3,column=0)

    outerwear_label = tkinter.Label(root, text = 'Outerwear', font = ('Arial Bold',15))
    outerwear_label.grid(row=4,column=0)

    accessory_label = tkinter.Label(root, text = 'Accesory', font = ('Arial Bold',15))
    accessory_label.grid(row=5,column=0)

    color_label = tkinter.Label(root, text = 'Color:', font = ('Arial Bold',15))
    color_label.grid(row=0,column=1, pady=12)    

    price_label = tkinter.Label(root, text = 'Max Price (nearest $):', font = ('Arial Bold',15))
    price_label.grid(row=0,column=2, pady=12)
    
    ######## COMBOBOXES FOR COLOR OPTIONS ########
    top_color_options = tkinter.ttk.Combobox(root, values=men_top_colors, state='readonly', font = 15)
    top_color_options.configure(width=10)
    top_color_options.current(0)
    top_color_options.grid(row=1, column=1, padx=10)

    bottoms_color_options = tkinter.ttk.Combobox(root, values=men_bottoms_colors, state='readonly', font = 15)
    bottoms_color_options.configure(width=10)
    bottoms_color_options.current(0)
    bottoms_color_options.grid(row=2, column=1)

    shoes_color_options = tkinter.ttk.Combobox(root, values=men_shoes_colors, state='readonly', font = 15)
    shoes_color_options.configure(width=10)
    shoes_color_options.current(0)
    shoes_color_options.grid(row=3, column=1)

    outerwear_color_options = tkinter.ttk.Combobox(root, values=men_outerwear_colors, state='readonly', font = 15)
    outerwear_color_options.configure(width=10)
    outerwear_color_options.current(0)
    outerwear_color_options.grid(row=4, column=1)

    accessory_color_options = tkinter.ttk.Combobox(root, values=men_accessory_colors, state='readonly', font = 15)
    accessory_color_options.configure(width=10)
    accessory_color_options.current(0)
    accessory_color_options.grid(row=5, column=1)
    
    ######## ENTRYBOXES FOR PRICES ########
    top_price_box = tkinter.Entry(root, width=10, font = 15)
    top_price_box.insert(0, 0)
    top_price_box.grid(row=1, column=2, padx=10)

    bottoms_price_box = tkinter.Entry(root, width=10, font = 15)
    bottoms_price_box.insert(0, 0)
    bottoms_price_box.grid(row=2, column=2)

    shoes_price_box = tkinter.Entry(root, width=10, font = 15)
    shoes_price_box.insert(0, 0)
    shoes_price_box.grid(row=3, column=2)

    outerwear_price_box = tkinter.Entry(root, width=10, font = 15)
    outerwear_price_box.insert(0, 0)
    outerwear_price_box.grid(row=4, column=2)

    accessory_price_box = tkinter.Entry(root, width=10, font = 15)
    accessory_price_box.insert(0, 0)
    accessory_price_box.grid(row=5, column=2)
    
    # create generate outfit function
    def generate_outfit():
        '''Generates outfit output'''
        
        # minimize the gender root & root
        gender_root.iconify()
        root.iconify()
               
        # get the user inputs from the GUI
        top_color = top_color_options.get()
        bottoms_color = bottoms_color_options.get()
        shoes_color = shoes_color_options.get()
        outerwear_color = outerwear_color_options.get()
        accessory_color = accessory_color_options.get()
        
        # only execute if prices are formatted correctly
        try:
            # change the data type of the prices to integers
            top_price = int(top_price_box.get())
            bottoms_price = int(bottoms_price_box.get())
            shoes_price = int(shoes_price_box.get())
            outerwear_price = int(outerwear_price_box.get())
            accessory_price = int(accessory_price_box.get())
             
            # create dataframes for each category within the gender, using user specifications if they chose men
            df_top = men[(men['category'] == 'Top') & (men['color'] == top_color) & (men['selling_price'] <= top_price)]
            df_bottoms = men[(men['category'] == 'Bottoms') & (men['color'] == bottoms_color) & (men['selling_price'] <= bottoms_price)]
            df_shoes = men[(men['category'] == 'Shoes') & (men['color'] == shoes_color) & (men['selling_price'] <= shoes_price)]
            df_outerwear = men[(men['category'] == 'Outerwear') & (men['color'] == outerwear_color) & (men['selling_price'] <= outerwear_price)]
            df_accessory = men[(men['category'] == 'Accessories') & (men['color'] == accessory_color) & (men['selling_price'] <= accessory_price)]
            
            # if any of the outfit option category lists are empty, tell the user to try again with new color/price options 
            if df_top.empty | df_bottoms.empty | df_shoes.empty | df_outerwear.empty | df_accessory.empty:
                tkinter.messagebox.showwarning('No Outfits Available','Uh-oh! No outfits were found that fit your specifications. Please try again with new selections.')
                # maximize the root
                root.deiconify()
                # set the options back to defaults
                top_color_options.current(0)
                bottoms_color_options.current(0)
                shoes_color_options.current(0)
                outerwear_color_options.current(0)
                accessory_color_options.current(0)
                top_price_box.delete(0, tkinter.END)
                bottoms_price_box.delete(0, tkinter.END)
                shoes_price_box.delete(0, tkinter.END)
                outerwear_price_box.delete(0, tkinter.END)
                accessory_price_box.delete(0, tkinter.END)
            
            # execute only if there are suitable clothing options for every category based on color/price specifications
            else:
                # create new window for outfit
                new_window = Toplevel(gender_root)
                new_window.title('Generated Outfit')
                new_window.geometry('500x2000')
                
                # create random numbers for each category to generate the outfit
                top_rand = random.randrange(0,len(df_top))
                bottoms_rand = random.randrange(0,len(df_bottoms))
                shoes_rand = random.randrange(0,len(df_shoes))
                outerwear_rand = random.randrange(0,len(df_outerwear))
                accessory_rand = random.randrange(0,len(df_accessory))
                
                # find the data point from the random number for each category
                top_image_loc = df_top['images'].iloc[top_rand]
                bottoms_image_loc = df_bottoms['images'].iloc[bottoms_rand]
                shoes_image_loc = df_shoes['images'].iloc[shoes_rand]
                outerwear_image_loc = df_outerwear['images'].iloc[outerwear_rand]
                accessory_image_loc = df_accessory['images'].iloc[accessory_rand]
                      
                # insert images into new GUI
                top_link = urllib.request.urlopen(top_image_loc).read()
                im = Image.open(io.BytesIO(top_link))
                resize_image = im.reduce(3)
                top_image = ImageTk.PhotoImage(resize_image)
                label1 = tkinter.Label(new_window, image=top_image)
                label1.grid(row=0, column = 0)
                
                bottoms_link = urllib.request.urlopen(bottoms_image_loc).read()
                im = Image.open(io.BytesIO(bottoms_link))
                resize_image = im.reduce(3)
                bottoms_image = ImageTk.PhotoImage(resize_image)
                label2 = tkinter.Label(new_window, image=bottoms_image)
                label2.grid(row=1, column = 0)
                
                shoes_link = urllib.request.urlopen(shoes_image_loc).read()
                im = Image.open(io.BytesIO(shoes_link))
                resize_image = im.reduce(3)
                shoes_image = ImageTk.PhotoImage(resize_image)
                label3 = tkinter.Label(new_window, image=shoes_image)
                label3.grid(row=2, column = 0)
                
                outerwear_link = urllib.request.urlopen(outerwear_image_loc).read()
                im = Image.open(io.BytesIO(outerwear_link))
                resize_image = im.reduce(3)
                outerwear_image = ImageTk.PhotoImage(resize_image)
                label4 = tkinter.Label(new_window, image=outerwear_image)
                label4.grid(row=0, column = 1)
                
                accessory_link = urllib.request.urlopen(accessory_image_loc).read()
                im = Image.open(io.BytesIO(accessory_link))
                resize_image = im.reduce(3)
                accessory_image = ImageTk.PhotoImage(resize_image)
                label5 = tkinter.Label(new_window, image=accessory_image)
                label5.grid(row=1, column = 1)
                
                # ask the user if they like the outfit or not
                answer = askyesno(title="Outfit Generated",message="Yay! We found an outfit! Do you like it?")           
                
                # if they like the outfit, write each item's info to a csv file called outfit.csv
                if answer == True:
                    tkinter.messagebox.showinfo('Yay!', 'A csv file called outfit.csv has been created with your outfit details!')

                    # set each item to the row in the oringinal dataframe that matches
                    final_top = data[(data['images']==top_image_loc)]
                    final_bottoms = data[(data['images']==bottoms_image_loc)]
                    final_shoes = data[(data['images']==shoes_image_loc)]
                    final_outerwear = data[(data['images']==outerwear_image_loc)]
                    final_accessory = data[(data['images']==accessory_image_loc) & (data['gender']=='Men')] 

                    # write each row to the csv
                    final_top.to_csv('outfit.csv',mode='w',index=False,header=True)
                    final_bottoms.to_csv('outfit.csv',mode='a',index=False,header=False)
                    final_shoes.to_csv('outfit.csv',mode='a',index=False,header=False)
                    final_outerwear.to_csv('outfit.csv',mode='a',index=False,header=False)
                    final_accessory.to_csv('outfit.csv',mode='a',index=False,header=False)
                    
                    # destroy the root once the process is done
                    gender_root.destroy()
                    root.destroy()

                # if they don't like the outfit, display a message telling them to try again
                else:
                    tkinter.messagebox.showinfo('Boo!','Oh no! Try the outfit generator again to create a new outfit.')
                    # maximize the root
                    root.deiconify()
                    # destroy the new window
                    new_window.destroy()
                    # set all options back to default
                    top_color_options.current(0)
                    bottoms_color_options.current(0)
                    shoes_color_options.current(0)
                    outerwear_color_options.current(0)
                    accessory_color_options.current(0)
                    top_price_box.delete(0, tkinter.END)
                    bottoms_price_box.delete(0, tkinter.END)
                    shoes_price_box.delete(0, tkinter.END)
                    outerwear_price_box.delete(0, tkinter.END)
                    accessory_price_box.delete(0, tkinter.END)
        
        # if the prices are formatted incorrectly, show a message stating to try again
        except:
            tkinter.messagebox.showwarning('Incorrect Formating','Uh-oh! Make sure you are formatting the Max Price to the nearest whole dollar. Please try again with new selections.')
            # maximize the root
            root.deiconify()
            # set all options back to default
            top_color_options.current(0)
            bottoms_color_options.current(0)
            shoes_color_options.current(0)
            outerwear_color_options.current(0)
            accessory_color_options.current(0)
            top_price_box.delete(0, tkinter.END)
            bottoms_price_box.delete(0, tkinter.END)
            shoes_price_box.delete(0, tkinter.END)
            outerwear_price_box.delete(0, tkinter.END)
            accessory_price_box.delete(0, tkinter.END)

    # create a function for the clear button 
    def clear_selections():
        '''Clears current selections'''
        top_color_options.current(0)
        bottoms_color_options.current(0)
        shoes_color_options.current(0)
        outerwear_color_options.current(0)
        accessory_color_options.current(0)
        top_price_box.delete(0, tkinter.END)
        bottoms_price_box.delete(0, tkinter.END)
        shoes_price_box.delete(0, tkinter.END)
        outerwear_price_box.delete(0, tkinter.END)
        accessory_price_box.delete(0, tkinter.END)
 
    # create a function for the exit button 
    def destroy():
        '''Destroys the roots'''
        gender_root.destroy()
        root.destroy()

    ######## BUTTONS - GENERATE OUTFIT, CLEAR, EXIT ########
    # create outfit button
    outfit_button = tkinter.Button(root, text = 'Generate Outfit', command = generate_outfit, font = ('Arial Bold',14))
    outfit_button.configure(bg='light green', width=15)
    outfit_button.grid(row=2,column=3, padx=5)
    
    # create clear button
    clear_button = tkinter.Button(root, text = 'Clear', command = clear_selections, font = ('Arial Bold',14))
    clear_button.configure(bg='light yellow', width=15)
    clear_button.grid(row=3,column=3, padx=5)
        
    # create exit button
    exit_button = tkinter.Button(root, text = 'Exit', command = destroy, font = ('Arial Bold',14))
    exit_button.configure(bg='red', width=15)
    exit_button.grid(row=4,column=3, padx=5)
    
    
# create women button
women_button = tkinter.Button(gender_root, text = 'Women', command = women_outfit, font = ('Arial Bold',15))
women_button.configure(bg='pink', width=8)
women_button.grid(row=0,column=1, padx=20)

# create men button
men_button = tkinter.Button(gender_root, text = 'Men', command = men_outfit, font = ('Arial Bold',15))
men_button.configure(bg='light blue', width=8)
men_button.grid(row=0,column=2)


# mainloop the gender root
gender_root.mainloop()



################################################# END OF CODE ###########################################################


    
    
