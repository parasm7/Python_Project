from tkinter import *
from sqlite3 import *
import random
import time
class window1:
    def __init__(self,parent):
        self.root=parent
        self.root.title("Login Frame")
        self.root.geometry("780x525")
        self.root.resizable(0, 0)
        self.log_in = PhotoImage(file="log_in.gif")
        self.labelbackimage = Label(mainroot, image=self.log_in)
        self.labelbackimage.pack()
        self.frame_title=Frame(self.root,height=80,width=1000,bg="black")
        self.frame_title.place(x=300,y=50)
        self.title_label=Label(self.frame_title,text="WELCOME",font=("Arial",35,'bold',),bg="black",fg="lightgreen")
        self.title_label.place(x=10,y=10)
        self.frame_log=Frame(self.root,width=100,height=100,bg="black")
        self.frame_log.place(x=300,y=200)
        self.log_user=Label(self.frame_log,text="Login ID :",font=("Arial",25,'bold'),bg="black",fg="lightgreen")
        self.log_user.grid(row=0,column=0,sticky=W)
        self.log_entryusr=Entry(self.frame_log,font=("Arial",20,'italic',),bg="lightgreen",fg="black")
        self.log_entryusr.grid(row=0,column=1)
        self.log_password= Label(self.frame_log, text="PASSWORD : ", font=("Arial", 25, 'bold',), bg="black",fg="lightgreen")
        self.log_password.grid(row=1,column=0)
        self.log_entrypas= Entry(self.frame_log, font=("Arial",20, 'bold',),show="*", bg="lightgreen", fg="black")
        self.log_entrypas.grid(row=1,column=1)
        self.frame_ack = Frame(self.root, height=80, width=600, bg="black")
        self.frame_ack.place(x=300, y=280)
        self.ack= Label(self.frame_ack, text="Detect", font=("Arial",12, 'bold',), bg="black",fg="lightgreen")
        self.ack.place(x=250, y=30)
        self.log_button=Button(self.root,text="LOG IN",height=2,width=12,font=("bold"),fg="black",bg="lightgreen",command=self.login)
        self.log_button.place(x=470,y=350)
    def login(self):
        usr = self.log_entryusr.get()
        pas = self.log_entrypas.get()
        con=connect('projectdb.sqlite')
        selectquery="SELECT* FROM logintab WHERE username='"+usr+"' AND password='"+pas+"';"
        cursor = con.execute(selectquery)
        res=False
        for row in cursor:
            res=True
        con.commit()
        con.close()
        if res==True:
            self.ack.configure(text='USER  Authenticated!')
            toplevel=Toplevel(self.root)
            win2=window2(toplevel)
        else:
            self.ack.configure(text='USER  Unauthenticated!')
class window2:
    def __init__(self,parent):
        self.root=parent
        self.root.title("Main Frame")
        self.root.geometry("1280x720")
        self.root.resizable(0,0)
        self.image_main=PhotoImage(file="main_frame.gif")
        self.labelbackimage=Label(self.root, image=self.image_main)
        self.labelbackimage.pack()
        #####################Frame Left###########################
        self.frame_left = Frame(self.root, width=900, height=590, bg='light sky blue')
        self.frame_left.place(x=10, y=120)
        self.frameFood = Frame(self.frame_left, width=448, height=580, bd=7, relief=RIDGE, bg='lightblue')
        self.frameFood.place(x=5, y=5)
        self.framedrink = Frame(self.frame_left, width=437, height=287, bd=7, relief=RIDGE, bg='lightblue')
        self.framedrink.place(x=459, y=5)
        ##################################Food Menu################################
        self.Foodmenu = Frame(self.frameFood, bg='lightblue')
        self.Foodmenu.place(x=1, y=10)
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.var3 = IntVar()
        self.var4 = IntVar()
        self.var5 = IntVar()
        self.var6 = IntVar()
        self.var7 = IntVar()
        self.var8 = IntVar()
        self.var9 = IntVar()
        self.var10 = IntVar()
        self.var11 = IntVar()
        self.var12 = IntVar()
        self.var13 = IntVar()

        self.e_dateoforder = StringVar()
        self.e_Costofdrinks = StringVar()
        self.e_Costoffood = StringVar()
        self.e_totalcost = StringVar()
        self.e_Servicecharge = StringVar()
        self.e_GST = StringVar()
        self.e_subtotal = StringVar()

        self.text_input = StringVar()
        self.operator = ""
        self.e_hamburger = StringVar()
        self.e_doubleburger = StringVar()
        self.e_chickenburger = StringVar()
        self.e_cheeseburger = StringVar()
        self.e_cheesesandwich = StringVar()
        self.e_Chickensandwitch = StringVar()
        self.e_paneerpizza = StringVar()
        self.e_chickenpizza = StringVar()
        self.e_frenchfries = StringVar()
        self.e_onionrings = StringVar()
        self.e_applepie = StringVar()
        self.e_icecream = StringVar()
        self.e_salad = StringVar()

        self.e_hamburger.set('0')
        self.e_doubleburger.set('0')
        self.e_chickenburger.set('0')
        self.e_cheeseburger.set('0')
        self.e_cheesesandwich.set('0')
        self.e_Chickensandwitch.set('0')
        self.e_paneerpizza.set('0')
        self.e_chickenpizza.set('0')
        self.e_frenchfries.set('0')
        self.e_onionrings.set('0')
        self.e_applepie.set('0')
        self.e_icecream.set('0')
        self.e_salad.set('0')

        self.Receipt_Ref = StringVar()
        self.e_dateoforder = StringVar()
        self.e_dateoforder.set(time.strftime("%d/%m/%Y"))

        ##########################################
        self.hamburger = Checkbutton(self.Foodmenu, text='Ham Burger', variable=self.var1, onvalue=1, offvalue=0,
                                     font=('arial', 18, "bold"), bg='lightblue', command=self.chkhamburger)
        self.hamburger.grid(row=0, sticky=W)
        self.doubleburger = Checkbutton(self.Foodmenu, text='Double Burger', variable=self.var2, onvalue=1, offvalue=0,
                                        font=('arial', 18, "bold"), bg='lightblue', command=self.chkdoubleburger)
        self.doubleburger.grid(row=1, sticky=W)
        self.chickenburger = Checkbutton(self.Foodmenu, text='Chicken Burger', variable=self.var3, onvalue=1,
                                         offvalue=0, font=('arial', 18, "bold"), bg='lightblue',
                                         command=self.chkchickenburger)
        self.chickenburger.grid(row=2, sticky=W)
        self.cheeseburger = Checkbutton(self.Foodmenu, text='Cheese Burger', variable=self.var4, onvalue=1, offvalue=0,
                                        font=('arial', 18, "bold"), bg='lightblue', command=self.chkcheeseburger)
        self.cheeseburger.grid(row=3, sticky=W)
        self.cheesesandwich = Checkbutton(self.Foodmenu, text='Cheese Sandwitch', variable=self.var5, onvalue=1,
                                          offvalue=0, font=('arial', 18, "bold"), bg='lightblue',
                                          command=self.chkcheesesandwitch)
        self.cheesesandwich.grid(row=4, sticky=W)
        self.Chickensandwitch = Checkbutton(self.Foodmenu, text='Chicken Sandwitch', variable=self.var6, onvalue=1,
                                            offvalue=0, font=('arial', 18, "bold"), bg='lightblue',
                                            command=self.chkchickensandwitch)
        self.Chickensandwitch.grid(row=5, sticky=W)
        self.paneerpizza = Checkbutton(self.Foodmenu, text='Peppy Paneer pizza', variable=self.var7, onvalue=1,
                                       offvalue=0, font=('arial', 18, "bold"), bg='lightblue',
                                       command=self.chkpaneerpizza)
        self.paneerpizza.grid(row=6, sticky=W)
        self.chickenpizza = Checkbutton(self.Foodmenu, text='Barbecue Chicken pizza\t', variable=self.var8, onvalue=1,
                                        offvalue=0, font=('arial', 18, "bold"), bg='lightblue',
                                        command=self.chkchickenpizza)
        self.chickenpizza.grid(row=7, sticky=W)
        self.frenchfries = Checkbutton(self.Foodmenu, text='French Fries', variable=self.var9, onvalue=1, offvalue=0,
                                       font=('arial', 18, "bold"), bg='lightblue', command=self.chkfrenchfries)
        self.frenchfries.grid(row=8, sticky=W)
        self.onionrings = Checkbutton(self.Foodmenu, text='Onion Rings', variable=self.var10, onvalue=1, offvalue=0,
                                      font=('arial', 18, "bold"), bg='lightblue', command=self.chkonionrings)
        self.onionrings.grid(row=9, sticky=W)
        self.applepie = Checkbutton(self.Foodmenu, text='Apple Pie', variable=self.var11, onvalue=1, offvalue=0,
                                    font=('arial', 18, "bold"), bg='lightblue', command=self.chkapplepie)
        self.applepie.grid(row=10, sticky=W)
        ##############ice cream options###########
        self.listicecream = ['Chocolate', 'Vanilla', 'Butterscotch', 'Fruits & Nut']
        self.optionicecreamvar = StringVar()
        self.optionicecreamvar.set('Flavours')
        self.optionicecream = OptionMenu(self.Foodmenu, self.optionicecreamvar, *self.listicecream)
        self.optionicecream.config(bg='lightblue', fg='black', font=('arial', 11, 'bold'))
        self.optionicecream.place(x=150, y=468)
        self.icecream = Checkbutton(self.Foodmenu, text='Ice-cream', variable=self.var12, onvalue=1, offvalue=0,
                                    font=('arial', 18, "bold"), bg='lightblue', command=self.chkicecream)
        self.icecream.grid(row=11, sticky=W)
        ###########
        self.salad = Checkbutton(self.Foodmenu, text='Salad', variable=self.var13, onvalue=1, offvalue=0,
                                 font=('arial', 18, "bold"), bg='lightblue', command=self.chksalad)
        self.salad.grid(row=12, sticky=W)
        #################################Entry for food###############
        self.txthamburger = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                  state=DISABLED, textvariable=self.e_hamburger)
        self.txthamburger.grid(row=0, column=1)
        self.txtdoubleburger = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                     state=DISABLED, textvariable=self.e_doubleburger)
        self.txtdoubleburger.grid(row=1, column=1)
        self.txtchickenburger = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                      state=DISABLED, textvariable=self.e_chickenburger)
        self.txtchickenburger.grid(row=2, column=1)

        self.txtcheeseburger = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                     state=DISABLED, textvariable=self.e_cheeseburger)
        self.txtcheeseburger.grid(row=3, column=1)
        self.txtcheesesandwich = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                       state=DISABLED, textvariable=self.e_cheesesandwich)
        self.txtcheesesandwich.grid(row=4, column=1)
        self.txtChickensandwitch = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                         state=DISABLED, textvariable=self.e_Chickensandwitch)
        self.txtChickensandwitch.grid(row=5, column=1)
        self.txtpaneerpizza = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                    state=DISABLED, textvariable=self.e_paneerpizza)
        self.txtpaneerpizza.grid(row=6, column=1)
        self.txtchickenpizza = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                     state=DISABLED, textvariable=self.e_chickenpizza)
        self.txtchickenpizza.grid(row=7, column=1)
        self.txtfrenchfries = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                    state=DISABLED, textvariable=self.e_frenchfries)
        self.txtfrenchfries.grid(row=8, column=1)
        self.txtonionrings = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                   state=DISABLED, textvariable=self.e_onionrings)
        self.txtonionrings.grid(row=9, column=1)
        self.txtapplepie = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                 state=DISABLED, textvariable=self.e_applepie)
        self.txtapplepie.grid(row=10, column=1)
        self.txticecream = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                 state=DISABLED, textvariable=self.e_icecream)
        self.txticecream.grid(row=11, column=1)
        self.txtsalad = Entry(self.Foodmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                              state=DISABLED, textvariable=self.e_salad)
        self.txtsalad.grid(row=12, column=1)
        ################################DRINKS MENU####################
        self.drinkmenu = Frame(self.framedrink, bg='lightblue')
        self.drinkmenu.place(x=1, y=10)
        self.empty = Label(self.drinkmenu, text=('emptyspacevalu'), bg="lightblue", fg="lightblue")
        self.empty.grid(row=0, column=1)
        self.var14 = IntVar()
        self.var15 = IntVar()
        self.var16 = IntVar()
        self.var17 = IntVar()
        self.var18 = IntVar()
        self.var19 = IntVar()

        self.text_input = StringVar()
        self.operator = ""
        self.e_milkshakes = StringVar()
        self.e_coffee = StringVar()
        self.e_hotchocolate = StringVar()
        self.e_tea = StringVar()
        self.e_coke = StringVar()
        self.e_orangejuice = StringVar()

        self.e_milkshakes.set('0')
        self.e_coffee.set('0')
        self.e_hotchocolate.set('0')
        self.e_tea.set('0')
        self.e_coke.set('0')
        self.e_orangejuice.set('0')

        #########Milk shake options#############
        self.listshakes = ['Orio', 'Mango', 'Strawberry', 'Banana']
        self.optionshakesvar = StringVar()
        self.optionshakesvar.set('Flavours')
        self.optionshakes = OptionMenu(self.drinkmenu, self.optionshakesvar, *self.listshakes)
        self.optionshakes.config(bg='lightblue', fg='black', font=('arial', 11, 'bold'))
        self.optionshakes.place(x=166, y=4)
        self.milkshakes = Checkbutton(self.drinkmenu, text='Milk Shake', variable=self.var14, onvalue=1, offvalue=0,
                                      font=('arial', 18, "bold"), bg='lightblue', command=self.chkmilkshakes)
        self.milkshakes.grid(row=0, sticky=W)
        #############
        self.coffee = Checkbutton(self.drinkmenu, text='Coffee\t', variable=self.var15, onvalue=1, offvalue=0,
                                  font=('arial', 18, "bold"), bg='lightblue', command=self.chkcoffee)
        self.coffee.grid(row=1, sticky=W)
        self.hotchocolate = Checkbutton(self.drinkmenu, text='Hot Chocolate\t', variable=self.var16, onvalue=1,
                                        offvalue=0,
                                        font=('arial', 18, "bold"), bg='lightblue', command=self.chkhotchocolate)
        self.hotchocolate.grid(row=2, sticky=W)
        self.tea = Checkbutton(self.drinkmenu, text='Tea', variable=self.var17, onvalue=1, offvalue=0,
                               font=('arial', 18, "bold"), bg='lightblue', command=self.chktea)
        self.tea.grid(row=3, sticky=W)
        self.coke = Checkbutton(self.drinkmenu, text='Coke\t', variable=self.var18, onvalue=1, offvalue=0,
                                font=('arial', 18, "bold"), bg='lightblue', command=self.chkcoke)
        self.coke.grid(row=4, sticky=W)
        self.orangejuice = Checkbutton(self.drinkmenu, text='Orange Juice \t', variable=self.var19, onvalue=1,
                                       offvalue=0,
                                       font=('arial', 18, "bold"), bg='lightblue', command=self.chkorangejuice)
        self.orangejuice.grid(row=5, sticky=W)
        ######################DRINKS ENTRY############################
        self.txtmilkshakes = Entry(self.drinkmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                   state=DISABLED, textvariable=self.e_milkshakes)
        self.txtmilkshakes.grid(row=0, column=2)
        self.txtcoffee = Entry(self.drinkmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                               state=DISABLED, textvariable=self.e_coffee)
        self.txtcoffee.grid(row=1, column=2)
        self.txthotchocolate = Entry(self.drinkmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                     state=DISABLED, textvariable=self.e_hotchocolate)
        self.txthotchocolate.grid(row=2, column=2)
        self.txttea = Entry(self.drinkmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                            state=DISABLED, textvariable=self.e_tea)
        self.txttea.grid(row=3, column=2)
        self.txtcoke = Entry(self.drinkmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                             state=DISABLED, textvariable=self.e_coke)
        self.txtcoke.grid(row=4, column=2)
        self.txtorangejuice = Entry(self.drinkmenu, font=('arial', 14, 'bold'), bd=6, width=6, justify=LEFT,
                                    state=DISABLED, textvariable=self.e_orangejuice)
        self.txtorangejuice.grid(row=5, column=2)

        #################################TOTAL COST#######################
        self.frametotal = Frame(self.frame_left, width=437, height=182, bd=3, relief=RIDGE, bg='azure')
        self.frametotal.place(x=459, y=295)
        self.total = Frame(self.frametotal, bg='azure')
        self.total.place(x=10, y=6)
        self.Costofdrinks = Label(self.total, font=('areal', 14), text="Cost of Drinks. \t", bg='azure', fg="black")
        self.Costofdrinks.grid(row=0, column=0, sticky=W)
        self.Costofdrinks_e = Entry(self.total, font=('arial', 12), bd=2, bg="white", insertwidth=2, justify=RIGHT,
                                    textvariable=self.e_Costofdrinks)
        self.Costofdrinks_e.grid(row=0, column=1)
        self.Costoffood = Label(self.total, font=('areal', 14), text="Cost of Food. \t", bg='azure', fg="black")
        self.Costoffood.grid(row=1, column=0, sticky=W)
        self.Costoffood_e = Entry(self.total, font=('arial', 12), bd=2, bg="white", insertwidth=2, justify=RIGHT,
                                  textvariable=self.e_Costoffood)
        self.Costoffood_e.grid(row=1, column=1)
        self.Servicecharge = Label(self.total, font=('areal', 13), text="Service charge@10%.\t", bg='azure', fg="black")
        self.Servicecharge.grid(row=2, column=0, sticky=W)
        self.Servicecharge_e = Entry(self.total, font=('arial', 12), bd=2, bg="white", insertwidth=2, justify=RIGHT,
                                     textvariable=self.e_Servicecharge)
        self.Servicecharge_e.grid(row=2, column=1)
        self.totalcost = Label(self.total, font=('areal', 15), text="TOTAL Cost. \t", bg='azure', fg="black")
        self.totalcost.grid(row=3, column=0, sticky=W)
        self.totalcost_e = Entry(self.total, font=('arial', 12), bd=2, bg="white", insertwidth=2, justify=RIGHT,
                                 textvariable=self.e_totalcost)
        self.totalcost_e.grid(row=3, column=1)
        self.GST = Label(self.total, font=('areal', 13), text="GST tax. \t", bg='azure', fg="black")
        self.GST.grid(row=4, column=0, sticky=W)
        self.GST_e = Entry(self.total, font=('arial', 12), bd=2, bg="white", insertwidth=2, justify=RIGHT,
                           textvariable=self.e_GST)
        self.GST_e.grid(row=4, column=1)
        self.subtotal = Label(self.total, font=('areal', 15), text="SUB_TOTAL.\t", bg='azure', fg="black")
        self.subtotal.grid(row=5, column=0, sticky=W)
        self.subtotal_e = Entry(self.total, font=('arial', 12), bd=2, bg="white", insertwidth=2, justify=RIGHT,
                                textvariable=self.e_subtotal)
        self.subtotal_e.grid(row=5, column=1)
        ######################Buttons#############################
        self.frame_Buttons = Frame(self.frame_left, width=437, height=105, bd=5, relief=RIDGE, bg='alice blue')
        self.frame_Buttons.place(x=459, y=480)
        self.Total_Button = Button(self.frame_Buttons, text="TOTAL", height=3, width=11, bd=4, font=("bold"),
                                   fg="black", bg="lightgreen", command=self.CostofItem)
        self.Total_Button.place(x=2, y=3)
        self.Receipt_Button = Button(self.frame_Buttons, text="RECEIPT", height=3, width=12, bd=4, font=("bold"),
                                     fg="black", bg="indianred1", command=self.Receipt)
        self.Receipt_Button.place(x=141, y=2)
        self.Reset_Button = Button(self.frame_Buttons, text="RESET", height=3, width=11, bd=4, font=("bold"),
                                   fg="black", bg="lightgreen", command=self.Reset)
        self.Reset_Button.place(x=291, y=3)

        ############################Frame Right###########################
        self.frame_right = Frame(self.root, width=350, height=590, bg='light sky blue')
        self.frame_right.place(x=920, y=120)
        ##########################receipt###################
        self.framereceipt = Frame(self.frame_right)
        self.framereceipt.place(x=4, y=284)
        self.textreceipt = Text(self.framereceipt, width=37, height=16, bg="white", bd=3, font=('arial', 12))
        self.textreceipt.grid(row=0, column=0)
        ##########################calculator##############
        self.frame_cal = Frame(self.frame_right, width=310, height=560, bg='white')
        self.frame_cal.place(x=5, y=6)
        self.operator = ""
        self.text_Input = StringVar()
        self.entry = Entry(self.frame_cal, textvar=self.text_Input,font=(35),bd=10, insertwidth=88, width=29,
                           justify='right')
        self.entry.grid(columnspan=4)
        ##############################################################################
        self.btn7 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="7", font=(14),
                           command=lambda: self.btn_click(7)).grid(row=1, column=0)
        self.btn8 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="8", font=(14),
                           command=lambda: self.btn_click(8)).grid(row=1, column=1)
        self.btn9 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="9", font=(14),
                           command=lambda: self.btn_click(9)).grid(row=1, column=2)
        self.btn_Add = Button(self.frame_cal, padx=20, pady=5, bd=6, text="+", font=(14),
                              command=lambda: self.btn_click("+")).grid(row=1, column=3)
        ################################################################################
        self.btn4 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="4", font=(14),
                           command=lambda: self.btn_click(4)).grid(row=2, column=0)
        self.btn5 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="5", font=(14),
                           command=lambda: self.btn_click(5)).grid(row=2, column=1)
        self.btn6 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="6", font=(14),
                           command=lambda: self.btn_click(6)).grid(row=2, column=2)
        self.btn_Sub = Button(self.frame_cal, padx=22, pady=5, bd=6, text="-", font=(14),
                              command=lambda: self.btn_click("-")).grid(row=2, column=3)
        ################################################################################
        self.btn1 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="1", font=(14),
                           command=lambda: self.btn_click(1)).grid(row=3, column=0)
        self.btn2 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="2", font=(14),
                           command=lambda: self.btn_click(2)).grid(row=3, column=1)
        self.btn3 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="3", font=(14),
                           command=lambda: self.btn_click(3)).grid(row=3, column=2)
        self.btn_Multi = Button(self.frame_cal, padx=22, pady=5, bd=6, text="*", font=(14),
                                command=lambda: self.btn_click("*")).grid(row=3, column=3)
        ################################################################################
        self.btn_clear = Button(self.frame_cal, padx=20, pady=5, bd=6, text="C", font=(14),
                                command=self.btn_clear).grid(row=4, column=0)
        self.btn0 = Button(self.frame_cal, padx=20, pady=5, bd=6, text="0", font=(14),
                           command=lambda: self.btn_click(0)).grid(row=4, column=1)
        self.btn_equal = Button(self.frame_cal, padx=20, pady=5, bd=6, text="=", font=(14),
                                command=self.btn_equal).grid(row=4, column=2)
        self.btn_Div = Button(self.frame_cal, padx=22, pady=5, bd=6, text="/", font=(14),
                              command=lambda: self.btn_click("/")).grid(row=4, column=3)
        #####################################################

    def btn_click(self, numbers):
        global operator
        self.operator = self.operator + str(numbers)
        self.text_Input.set(self.operator)

    def btn_clear(self):
        global operator
        self.operator = ""
        self.text_Input.set("")

    def btn_equal(self):
        global operator
        self.sumup = str(eval(self.operator))
        self.text_Input.set(self.sumup)
        self.operator = ""

    def Reset(self):
        self.e_Costofdrinks.set("")
        self.e_Costoffood.set("")
        self.e_totalcost.set("")
        self.e_Servicecharge.set("")
        self.e_GST.set("")
        self.e_subtotal.set("")
        self.optionicecreamvar.set('Flavours')
        self.optionshakesvar.set('Flavours')
        self.textreceipt.delete("1.0", END)

        self.e_hamburger.set('0')
        self.e_doubleburger.set('0')
        self.e_chickenburger.set('0')
        self.e_cheeseburger.set('0')
        self.e_cheesesandwich.set('0')
        self.e_Chickensandwitch.set('0')
        self.e_paneerpizza.set('0')
        self.e_chickenpizza.set('0')
        self.e_frenchfries.set('0')
        self.e_onionrings.set('0')
        self.e_applepie.set('0')
        self.e_icecream.set('0')
        self.e_salad.set('0')

        self.e_milkshakes.set('0')
        self.e_coffee.set('0')
        self.e_hotchocolate.set('0')
        self.e_tea.set('0')
        self.e_coke.set('0')
        self.e_orangejuice.set('0')

        self.var1.set('0')
        self.var2.set('0')
        self.var3.set('0')
        self.var4.set('0')
        self.var5.set('0')
        self.var6.set('0')
        self.var7.set('0')
        self.var8.set('0')
        self.var9.set('0')
        self.var10.set('0')
        self.var11.set('0')
        self.var12.set('0')
        self.var13.set('0')
        self.var14.set('0')
        self.var15.set('0')
        self.var16.set('0')
        self.var17.set('0')
        self.var18.set('0')
        self.var19.set('0')

        self.txthamburger.configure(state=DISABLED)
        self.txtdoubleburger.configure(state=DISABLED)
        self.txtchickenburger.configure(state=DISABLED)
        self.txtcheeseburger.configure(state=DISABLED)
        self.txtcheesesandwich.configure(state=DISABLED)
        self.txtChickensandwitch.configure(state=DISABLED)
        self.txtpaneerpizza.configure(state=DISABLED)
        self.txtchickenpizza.configure(state=DISABLED)
        self.txtfrenchfries.configure(state=DISABLED)
        self.txtonionrings.configure(state=DISABLED)
        self.txtapplepie.configure(state=DISABLED)
        self.txticecream.configure(state=DISABLED)
        self.txtsalad.configure(state=DISABLED)

        self.txtmilkshakes.configure(state=DISABLED)
        self.txtcoffee.configure(state=DISABLED)
        self.txthotchocolate.configure(state=DISABLED)
        self.txttea.configure(state=DISABLED)
        self.txtcoke.configure(state=DISABLED)
        self.txtorangejuice.configure(state=DISABLED)
        #################################cost total###

    def CostofItem(self):
        self.Item1 = float(self.e_hamburger.get())
        self.Item2 = float(self.e_doubleburger.get())
        self.Item3 = float(self.e_chickenburger.get())
        self.Item4 = float(self.e_cheeseburger.get())
        self.Item5 = float(self.e_cheesesandwich.get())
        self.Item6 = float(self.e_Chickensandwitch.get())
        self.Item7 = float(self.e_paneerpizza.get())
        self.Item8 = float(self.e_chickenpizza.get())
        self.Item9 = float(self.e_frenchfries.get())
        self.Item10 = float(self.e_onionrings.get())
        self.Item11 = float(self.e_applepie.get())
        self.Item12 = float(self.e_icecream.get())
        self.Item13 = float(self.e_salad.get())

        self.Item14 = float(self.e_milkshakes.get())
        self.Item15 = float(self.e_coffee.get())
        self.Item16 = float(self.e_hotchocolate.get())
        self.Item17 = float(self.e_tea.get())
        self.Item18 = float(self.e_coke.get())
        self.Item19 = float(self.e_orangejuice.get())

        self.PriceofFood = (self.Item1 * 80.0) + (self.Item2 * 105.0) + (self.Item3 * 121.0) + (self.Item4 * 121.0) + (
                    self.Item5 * 70.0) \
                           + (self.Item6 * 80.0) + (self.Item7 * 195.0) + (self.Item8 * 280.0) + (self.Item9 * 75.0) + (
                                       self.Item10 * 85.0) \
                           + (self.Item11 * 350.0) + (self.Item12 * 40.0) + (self.Item13 * 45.0)
        self.PriceofDrinks = (self.Item14 * 40.0) + (self.Item15 * 35.0) + (self.Item16 * 42.0) + (self.Item17 * 25.0) \
                             + (self.Item18 * 35.0) + (self.Item19 * 29.0)

        self.drinksprice = "₹", str('%.2f' % (self.PriceofDrinks))
        self.foodprice = "₹", str('%.2f' % (self.PriceofFood))
        self.e_Costofdrinks.set(self.drinksprice)
        self.e_Costoffood.set(self.foodprice)
        self.SC = '₹', str('%.2f' % (2.5))
        self.e_Servicecharge.set(self.SC)
        self.TC = "₹", str('%.2f' % (self.PriceofDrinks + self.PriceofFood + 2.5))
        self.e_totalcost.set(self.TC)
        self.tax = "₹", str('%.2f' % (+1.5))
        self.e_GST.set(self.tax)
        self.TT = ((self.PriceofDrinks + self.PriceofFood + 2.5) + 1.5)
        self.ST = "₹", str('%.2f' % (self.TT))
        self.e_subtotal.set(self.ST)
        ############################

    def Receipt(self):
        self.textreceipt.delete("1.0", END)
        self.x = random.randint(10999, 807810)
        self.randomRef = str(self.x)
        self.Receipt_Ref.set("BILL" + self.randomRef)
        self.textreceipt.insert(END,
                                'Receipt Ref:\t\t' + self.Receipt_Ref.get() + '\t' + self.e_dateoforder.get() + "\n")
        self.textreceipt.insert(END, 'Items:\t\t\t' + "Cost of Items\n\n")
        self.textreceipt.insert(END, 'Ham Burger:\t\t\t\t' + self.e_hamburger.get() + "\n")
        self.textreceipt.insert(END, 'Double Burger:\t\t\t\t' + self.e_doubleburger.get() + "\n")
        self.textreceipt.insert(END, 'Chicken Burger:\t\t\t\t' + self.e_chickenburger.get() + "\n")
        self.textreceipt.insert(END, 'Cheese Burger:\t\t\t\t' + self.e_cheeseburger.get() + "\n")
        self.textreceipt.insert(END, 'Cheese Sandwitch:\t\t\t\t' + self.e_cheesesandwich.get() + "\n")
        self.textreceipt.insert(END, 'Chicken Sandwitch:\t\t\t\t' + self.e_Chickensandwitch.get() + "\n")
        self.textreceipt.insert(END, 'Peppy Paneer pizza:\t\t\t\t' + self.e_paneerpizza.get() + "\n")
        self.textreceipt.insert(END, 'Barbecue Chicken pizza:\t\t\t\t' + self.e_chickenpizza.get() + "\n")
        self.textreceipt.insert(END, 'French Fries:\t\t\t\t' + self.e_frenchfries.get() + "\n")
        self.textreceipt.insert(END, 'Onion Rings:\t\t\t\t' + self.e_onionrings.get() + "\n")
        self.textreceipt.insert(END, 'Apple Pie:\t\t\t\t' + self.e_applepie.get() + "\n")
        self.textreceipt.insert(END,
                                'Ice-cream:\t\t' + self.optionicecreamvar.get() + '\t\t' + self.e_icecream.get() + "\n")
        self.textreceipt.insert(END,
                                'Milk Shake:\t\t' + self.optionshakesvar.get() + '\t\t' + self.e_milkshakes.get() + "\n")
        self.textreceipt.insert(END, 'Coffee:\t\t\t\t' + self.e_coffee.get() + "\n")
        self.textreceipt.insert(END, 'Hot Chocolate:\t\t\t\t' + self.e_hotchocolate.get() + "\n")
        self.textreceipt.insert(END, 'Tea:\t\t\t\t' + self.e_tea.get() + "\n")
        self.textreceipt.insert(END, 'Coke:\t\t\t\t' + self.e_coke.get() + "\n")
        self.textreceipt.insert(END, 'Orange Juice:\t\t\t\t' + self.e_orangejuice.get() + "\n\n")

        self.textreceipt.insert(END,
                                'Cost of Drinks:\t\t\t' + self.e_Costofdrinks.get() + '\nCost of Food:\t\t\t' + self.e_Costoffood.get() + "\n")
        self.textreceipt.insert(END,
                                'Service Charge:\t\t\t' + self.e_Servicecharge.get() + '\nTotal Cost:\t\t\t' + self.e_totalcost.get() + "\n")
        self.textreceipt.insert(END,
                                'GST tax Paid:\t\t\t' + self.e_GST.get() + '\nSUB_Total:\t\t\t' + self.e_subtotal.get())

        ###############################

    def chkhamburger(self):
        if (self.var1.get() == 1):
            self.txthamburger.configure(state=NORMAL)
            self.txthamburger.focus()
            self.txthamburger.delete('0', END)
            self.e_hamburger.set("")
        elif (self.var1.get() == 0):
            self.txthamburger.configure(state=DISABLED)
            self.e_hamburger.set("0")

    def chkdoubleburger(self):
        if (self.var2.get() == 1):
            self.txtdoubleburger.configure(state=NORMAL)
            self.txtdoubleburger.focus()
            self.txtdoubleburger.delete('0', END)
            self.e_doubleburger.set("")
        elif (self.var2.get() == 0):
            self.txtdoubleburger.configure(state=DISABLED)
            self.e_doubleburger.set("0")

    def chkchickenburger(self):
        if (self.var3.get() == 1):
            self.txtchickenburger.configure(state=NORMAL)
            self.txtchickenburger.focus()
            self.txtchickenburger.delete('0', END)
            self.e_chickenburger.set("")
        elif (self.var3.get() == 0):
            self.txtchickenburger.configure(state=DISABLED)
            self.e_chickenburger.set("0")

    def chkcheeseburger(self):
        if (self.var4.get() == 1):
            self.txtcheeseburger.configure(state=NORMAL)
            self.txtcheeseburger.focus()
            self.txtcheeseburger.delete('0', END)
            self.e_cheeseburger.set("")
        elif (self.var4.get() == 0):
            self.txtcheeseburger.configure(state=DISABLED)
            self.e_cheeseburger.set("0")

    def chkcheesesandwitch(self):
        if (self.var5.get() == 1):
            self.txtcheesesandwich.configure(state=NORMAL)
            self.txtcheesesandwich.focus()
            self.txtcheesesandwich.delete('0', END)
            self.e_cheesesandwich.set("")
        elif (self.var5.get() == 0):
            self.txtcheesesandwich.configure(state=DISABLED)
            self.e_cheesesandwich.set("0")

    def chkchickensandwitch(self):
        if (self.var6.get() == 1):
            self.txtChickensandwitch.configure(state=NORMAL)
            self.txtChickensandwitch.focus()
            self.txtChickensandwitch.delete('0', END)
            self.e_Chickensandwitch.set("")
        elif (self.var6.get() == 0):
            self.txtChickensandwitch.configure(state=DISABLED)
            self.e_Chickensandwitch.set("0")

    def chkpaneerpizza(self):
        if (self.var7.get() == 1):
            self.txtpaneerpizza.configure(state=NORMAL)
            self.txtpaneerpizza.focus()
            self.txtpaneerpizza.delete('0', END)
            self.e_paneerpizza.set("")
        elif (self.var7.get() == 0):
            self.txtpaneerpizza.configure(state=DISABLED)
            self.e_paneerpizza.set("0")

    def chkchickenpizza(self):
        if (self.var8.get() == 1):
            self.txtchickenpizza.configure(state=NORMAL)
            self.txtchickenpizza.focus()
            self.txtchickenpizza.delete('0', END)
            self.e_chickenpizza.set("")
        elif (self.var8.get() == 0):
            self.txtchickenpizza.configure(state=DISABLED)
            self.e_chickenpizza.set("0")

    def chkfrenchfries(self):
        if (self.var9.get() == 1):
            self.txtfrenchfries.configure(state=NORMAL)
            self.txtfrenchfries.focus()
            self.txtfrenchfries.delete('0', END)
            self.e_frenchfries.set("")
        elif (self.var9.get() == 0):
            self.txtfrenchfries.configure(state=DISABLED)
            self.e_frenchfries.set("0")

    def chkonionrings(self):
        if (self.var10.get() == 1):
            self.txtonionrings.configure(state=NORMAL)
            self.txtonionrings.focus()
            self.txtonionrings.delete('0', END)
            self.e_onionrings.set("")
        elif (self.var10.get() == 0):
            self.txtonionrings.configure(state=DISABLED)
            self.e_onionrings.set("0")

    def chkapplepie(self):
        if (self.var11.get() == 1):
            self.txtapplepie.configure(state=NORMAL)
            self.txtapplepie.focus()
            self.txtapplepie.delete('0', END)
            self.e_applepie.set("")
        elif (self.var11.get() == 0):
            self.txtapplepie.configure(state=DISABLED)
            self.e_applepie.set("0")

    def chkicecream(self):
        if (self.var12.get() == 1):
            self.txticecream.configure(state=NORMAL)
            self.optionshakes.configure(state=NORMAL)
            self.txticecream.focus()
            self.txticecream.delete('0', END)
            self.e_icecream.set("")
        elif (self.var12.get() == 0):
            self.txticecream.configure(state=DISABLED)
            self.optionshakes.configure(state=DISABLED)
            self.e_icecream.set("0")

    def chksalad(self):
        if (self.var13.get() == 1):
            self.txtsalad.configure(state=NORMAL)
            self.txtsalad.focus()
            self.txtsalad.delete('0', END)
            self.e_salad.set("")
        elif (self.var13.get() == 0):
            self.txtsalad.configure(state=DISABLED)
            self.e_salad.set("0")

    def chkmilkshakes(self):
        if (self.var14.get() == 1):
            self.txtmilkshakes.configure(state=NORMAL)
            self.optionshakes.configure(state=NORMAL)
            self.txtmilkshakes.focus()
            self.txtmilkshakes.delete('0', END)
            self.e_milkshakes.set("")
        elif (self.var14.get() == 0):
            self.txtmilkshakes.configure(state=DISABLED)
            self.optionshakes.configure(state=DISABLED)
            self.e_milkshakes.set("0")

    def chkcoffee(self):
        if (self.var15.get() == 1):
            self.txtcoffee.configure(state=NORMAL)
            self.txtcoffee.focus()
            self.txtcoffee.delete('0', END)
            self.e_coffee.set("")
        elif (self.var15.get() == 0):
            self.txtcoffee.configure(state=DISABLED)
            self.e_coffee.set("0")

    def chkhotchocolate(self):
        if (self.var16.get() == 1):
            self.txthotchocolate.configure(state=NORMAL)
            self.txthotchocolate.focus()
            self.txthotchocolate.delete('0', END)
            self.e_hotchocolate.set("")
        elif (self.var16.get() == 0):
            self.txthotchocolate.configure(state=DISABLED)
            self.e_hotchocolate.set("0")

    def chktea(self):
        if (self.var17.get() == 1):
            self.txttea.configure(state=NORMAL)
            self.txttea.focus()
            self.txttea.delete('0', END)
            self.e_tea.set("")
        elif (self.var17.get() == 0):
            self.txttea.configure(state=DISABLED)
            self.e_tea.set("0")

    def chkcoke(self):
        if (self.var18.get() == 1):
            self.txtcoke.configure(state=NORMAL)
            self.txtcoke.focus()
            self.txtcoke.delete('0', END)
            self.e_tea.set("")
        elif (self.var18.get() == 0):
            self.txtcoke.configure(state=DISABLED)
            self.e_coke.set("0")

    def chkorangejuice(self):
        if (self.var19.get() == 1):
            self.txtorangejuice.configure(state=NORMAL)
            self.txtorangejuice.focus()
            self.txtorangejuice.delete('0', END)
            self.e_orangejuice.set("")
        elif (self.var19.get() == 0):
            self.txtorangejuice.configure(state=DISABLED)
            self.e_orangejuice.set("0")


mainroot=Tk()
win=window1(mainroot)
mainroot.mainloop()