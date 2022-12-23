from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from tkinter import messagebox
import pymysql
import random
import time
import webbrowser
from docxtpl import DocxTemplate




class DataEntryForm:
    
    def __init__(self,root) :
        self.root = root
        self.root.title ("BC Vehicle Sales Agreement Portal")
        self.root.geometry =("1350x850+0+0")
        self.root.configure(background = "gainsboro")
        self.root.resizable(width=False,height=False)
        
        vecid = StringVar()
        vecname = StringVar()
        vecmode = StringVar()
        regno = StringVar()
        chasis = StringVar()
        engno = StringVar()
        color = StringVar()
        vendorname = StringVar()
        vendoraddr = StringVar()
        buyername = StringVar()
        buyeraddr = StringVar()
        place = StringVar()
        price = StringVar()
        price_inwords = StringVar()
        regdate = StringVar()
        search = StringVar()
        
        
        
        
        
        MainFrame = Frame(self.root, bd=10, width=1350, height=850, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=5, width=1340, height=300, relief=RIDGE, bg='green')
        TopFrame1.grid(row=0,column=0)
        
        TopFrame2 = Frame(MainFrame, bd=5, width=1340, height=50, relief=RIDGE, bg='red')
        TopFrame2.grid(row=1, column=0)
        
        TopFrame3 = Frame(MainFrame, bd=5, width=1340, height=300, relief=RIDGE, bg='red')
        TopFrame3.grid(row=2, column=0)
        
        #------------=============inner frames=====
        InnerTopFrame1 = Frame(TopFrame1, bd=5, width=1330, height=190, relief=RIDGE, bg='light green')
        InnerTopFrame1.grid()
        
        InnerTopFrame2 = Frame(TopFrame2, bd=5, width=1330, height=48, relief=RIDGE)
        InnerTopFrame2.grid()
        
        InnerTopFrame3 = Frame(TopFrame3, bd=5, width=1330, height=280, relief=RIDGE)
        InnerTopFrame3.grid()
        
        regdate.set(time.strftime("%d/%m/%Y"))
        #DateToday.set(time.strftime("%d/%m/%Y"))
        
        def Reset():
        

            vecid.set("")
            vecname.set("")
            vecmode.set("")
            regno.set("")
            chasis.set("")
            engno.set("")
            color.set("")
            vendorname.set("")
            vendoraddr.set("")
            buyername.set("")
            buyeraddr.set("")
            place.set("")
            price.set("")
            price_inwords.set("")
            regdate.set("")
            search.set("")
            
            
            
            regdate.set(time.strftime("%d/%m/%Y"))
            #DateToday.set(time.strftime("%d/%m/%Y"))
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("Vehicle Agreement Portal","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        
        def addData():
            if vecid.get()=="" or vecname.get() =="" or vecmode.get()== "":
                tkinter.messagebox.showerror("Vehicle Agreement Portal","Enter Correct Details!")
            else:
                sqlCon = pymysql.connect(host="localhost", user="root", password="", database="vecdb")
                cur = sqlCon.cursor()
                cur.execute("insert into vectbl values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(          
                
                
                vecid.get().upper(),
                vecname.get().upper(),
                vecmode.get().upper(),
                regno.get().upper(),
                chasis.get().upper(),
                engno.get().upper(),
                color.get().upper(),
                vendorname.get().upper(),
                vendoraddr.get().upper(),
                buyername.get().upper(),
                buyeraddr.get().upper(),
                place.get().upper(),
                price.get().upper(),
                price_inwords.get().upper(),
                regdate.get(),
                
                ))
           
                sqlCon.commit()
                DisplayData()          
                sqlCon.close()
                
                tkinter.messagebox.showinfo("Vehicle Agreement Portal", "Record Entered Successfully!")
                
                
        def DisplayData():
                sqlCon = pymysql.connect(host="localhost", user="root", password="", database="vecdb")
                cur = sqlCon.cursor()
                cur.execute("select * from vectbl")  
                result = cur.fetchall()  
                if len(result)!=0:
                    tree_records.delete(*tree_records.get_children())
                    for row in result:
                        tree_records.insert('',END,values=row)
                sqlCon.commit()          
                sqlCon.close()
                
        def LearnersInfo(ev):
            viewInfo = tree_records.focus()        
            vecData = tree_records.item(viewInfo)
            row = vecData['values']

            vecid.set(row[0])
            vecname.set(row[1])
            vecmode.set(row[2])
            regno.set(row[3])
            chasis.set(row[4])
            engno.set(row[5])
            color.set(row[6])
            vendorname.set(row[7])
            vendoraddr.set(row[8])
            buyername.set(row[9])
            buyeraddr.set(row[10])
            place.set(row[11])
            price.set(row[12])
            price_inwords.set(row[13])
            regdate.set(row[14])
           
            
        
                
        def Update(): 
                sqlCon = pymysql.connect(host="localhost", user="root", password="", database="vecdb")
                cur = sqlCon.cursor()
                cur.execute("update vectbl set vecname=%s,vecmode=%s,regno=%s,chasis=%s,engno=%s,color=%s,vendorname=%s,vendoraddr=%s,buyername=%s,buyeraddr=%s,place=%s,price=%s,price_inwords=%s,regdate=%s where vecid=%s",(                                     
                
                
                vecname.get(),
                vecmode.get(),
                regno.get(),
                chasis.get(),
                engno.get(),
                color.get(),
                vendorname.get(),
                vendoraddr.get(),
                buyername.get(),
                buyeraddr.get(),
                place.get(),
                price.get(),
                price_inwords.get(),
                regdate.get(),
                vecid.get(),
                
                ))
                
                sqlCon.commit()
                DisplayData()          
                sqlCon.close()
                tkinter.messagebox.showinfo("Vehicle Agreement Portal", "Record  Successfully Updated!")        
                
                
                
        def deleteDB():
            sqlCon = pymysql.connect(host="localhost", user="root", password="", database="vecdb")
            cur = sqlCon.cursor()
            cur.execute("delete from vectbl where vecid=%s",vecid.get())
                
            sqlCon.commit()
            DisplayData()
            sqlCon.close()    
            tkinter.messagebox.showinfo("Vehicle Agreement Portal", "Record  successfully deleted")
     
     
        def searchDB():
            try:
                sqlCon = pymysql.connect(host="localhost", user="root", password="", database="vecdb")
                cur = sqlCon.cursor()
                cur.execute("select * from vectbl where vecid='%s'"%search.get())
            
                row = cur.fetchone()
                
                
                vecid.set(row[0])
                vecname.set(row[1])
                vecmode.set(row[2])
                regno.set(row[3])
                chasis.set(row[4])
                engno.set(row[5])
                color.set(row[6])
                vendorname.set(row[7])
                vendoraddr.set(row[8])
                buyername.set(row[9])
                buyeraddr.set(row[10])
                place.set(row[11])
                price.set(row[12])
                price_inwords.set(row[13])
                regdate.set(row[14])            
                
                
                
                   
                sqlCon.commit()
            except:       
                tkinter.messagebox.showinfo("Vehicle Agreement Portal", "No such record Found!")
                Reset()
            sqlCon.close() 
            search.set("")       
                    
        def print():
            doc = DocxTemplate("generate_vehicleagree_template.docx")
            
            vec_info=vecid.get()
            vecname_info= vecname.get()
            vecmode_info=vecmode.get()
            regno_info=regno.get()
            chasis_info=chasis.get()
            engno_info=engno.get()
            color_info=color.get()
            vendorname_info=vendorname.get()
            vendoraddr_info=vendoraddr.get()
            buyername_info=buyername.get()
            buyeraddr_info=buyeraddr.get()
            place_info=place.get()
            price_info=price.get()
            price_inwords_info=price_inwords.get()
            regdate_info=regdate.get()
            title=vecname.get()+vecmode.get()
            
            doc.render({"vecid":vec_info,
                "make": vecname_info,
                "mode":vecmode_info,
                "regno":regno_info,
                "chasisNo": chasis_info,
                "engineNo":engno_info,
                "color": color_info,
                "vendorName": vendorname_info,
                "vendorAddress": vendoraddr_info,
                "buyerName": buyername_info,
                "buyerAddress": buyeraddr_info,
                "place": place_info,
                "price": price_info,
                "priceInWords": price_inwords_info,
                "regDate": regdate_info, 
                "title":title})
            
            doc_name = "generated_new_agreement_" + vendorname_info+ title +".docx"
            doc.save(doc_name)
            
            #doc_name = "new_invoice" + name + datetime.now().strftime("%Y-%m-%d-%H%M%S")+".docx"
            #doc.save(doc_name)
            
            messagebox.showinfo("Agreement Complete", "Agreement Successfully Generation Complete")
            
            Reset()
            
        
        #========================================widgets===============
        lblReference = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Vech Ref. No",bd=10,bg='light green')
        lblReference.grid(row=0,column=0,sticky=W)
        txtReference = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=vecid)
        txtReference.grid(row=0,column=1)
        
        lblVecName = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Vehicle Name",bd=10,bg='light green')
        lblVecName.grid(row=1,column=0,sticky=W)
        txtVecName = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=vecname)
        txtVecName.grid(row=1,column=1)
        
        lblVecMode = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Vehicle Mode",bd=10,bg='light green')
        lblVecMode.grid(row=2,column=0,sticky=W)
        txtVecMode = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=vecmode)
        txtVecMode.grid(row=2,column=1)
        
        self.lblChasis = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Chasis No.",bd=10,bg='light green')
        self.lblChasis.grid(row=0,column=2,sticky=W)
        self.txtChasis = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=chasis)
        self.txtChasis.grid(row=0,column=3)
        
        self.lblEngine = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Engine No.",bd=10,bg='light green')
        self.lblEngine.grid(row=1,column=2,sticky=W)
        self.txtEngine = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=engno)
        self.txtEngine.grid(row=1,column=3)
        
        self.lblColor = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Color",bd=10,bg='light green')
        self.lblColor.grid(row=4,column=0,sticky=W)
        
        self.cboColor = ttk.Combobox(InnerTopFrame1, font =('arial',12,'bold'),width=31,textvariable=color)
        self.cboColor['value']=('', 'white', 'black', 'green','gold','red', 'blue', 'brown','silver','grey','yellow', 'cream', 'pink','custom')                                 
        self.cboColor.current(0)
        self.cboColor.grid(row=4,column=1)
        
        
        self.lblPlaceOfAgree = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Place of Agreement.",bd=10,bg='light green')
        self.lblPlaceOfAgree.grid(row=2,column=2,sticky=W)
        self.txtPlaceOfAgree = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=place)
        self.txtPlaceOfAgree.grid(row=2,column=3)
        
        self.lblVecPrice = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Price",bd=10,bg='light green')
        self.lblVecPrice.grid(row=3,column=2,sticky=W)
        self.txtVecPrice = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=price)
        self.txtVecPrice.grid(row=3,column=3)

        self.lblVecPrice_inwords = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Price in words",bd=10,bg='light green')
        self.lblVecPrice_inwords.grid(row=4,column=2,sticky=W)
        self.txtVecPrice_inwords = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=price_inwords)
        self.txtVecPrice_inwords.grid(row=4,column=3)
        
        self.lblRegistrationDate = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Registration Date",bd=10,bg='light green')
        self.lblRegistrationDate.grid(row=5,column=0,sticky=W)
        self.txtRegistrationDate = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=regdate)
        self.txtRegistrationDate.grid(row=5,column=1)
               
        
        self.lblPlateNo = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Plate No.",bd=10,bg='light green')
        self.lblPlateNo.grid(row=3,column=0,sticky=W)
        self.txtPlateNo = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=regno)
        self.txtPlateNo.grid(row=3,column=1)
        
        self.lblVendorName = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Vendor Name",bd=10,bg='light green')
        self.lblVendorName.grid(row=0,column=4,sticky=W)
        self.txtVendorName = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=vendorname)
        self.txtVendorName.grid(row=0,column=5)
        
        self.lblVendorAddr = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Vendor Address",bd=10,bg='light green')
        self.lblVendorAddr.grid(row=1,column=4,sticky=W)
        self.txtVendorAddr = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=vendoraddr)
        self.txtVendorAddr.grid(row=1,column=5)
        
        self.lblBuyerName = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Buyer Name",bd=10,bg='light green')
        self.lblBuyerName.grid(row=2,column=4,sticky=W)
        self.txtBuyerName = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=buyername)
        self.txtBuyerName.grid(row=2,column=5)
        
        self.lblBuyerAddr = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Buyer Address",bd=10,bg='light green')
        self.lblBuyerAddr.grid(row=3,column=4,sticky=W)
        self.txtBuyerAddr = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=32,justify=LEFT,textvariable=buyeraddr)
        self.txtBuyerAddr.grid(row=3,column=5)
        
        self.lblSearch = Label(InnerTopFrame1, font =('arial',12,'bold'), text="Search",bd=10,bg='light green')
        self.lblSearch.grid(row=4,column=4,sticky=W)
        self.txtSearch = Entry(InnerTopFrame1, font =('arial',12,'bold'),bd=5, width=33,justify=LEFT,textvariable=search)
        self.txtSearch.grid(row=4,column=5)
        
       
        
        #================================tables===============
        Scroll_x=Scrollbar(InnerTopFrame3, orient=HORIZONTAL)
        Scroll_y=Scrollbar(InnerTopFrame3, orient=VERTICAL)
        
        tree_records = ttk.Treeview(InnerTopFrame3, height=13,columns=("vecid", "vecname","vecmode","regno","chasis","engno","color","vendorname","vendoraddr","buyername","buyeraddr","place","price","price_inwords", "regdate"),xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM, fill=X)
        Scroll_y.pack(side=RIGHT, fill=Y)
        
        tree_records.heading("vecid",text="Vech Id")
        tree_records.heading("vecname",text="Vech Name")
        tree_records.heading("vecmode",text="Vech Mode")
        tree_records.heading("regno",text="Plate No")
        tree_records.heading("chasis",text="Chasis")
        tree_records.heading("engno",text="Engine no")
        tree_records.heading("color",text="Color")
        tree_records.heading("vendorname",text="Vendor's Name")
        tree_records.heading("vendoraddr",text="Vendor addr")
        tree_records.heading("buyername",text="Buyer's Name")
        tree_records.heading("buyeraddr",text="Buyer addr")
        tree_records.heading("place",text="Place")
        tree_records.heading("price",text="Price")
        tree_records.heading("price_inwords",text="PriceW")
        tree_records.heading("regdate",text="RegDate")        
  
        tree_records['show']='headings'
                
        tree_records.column("vecid",width=80)
        tree_records.column("vecname",width=80)
        tree_records.column("vecmode",width=80)
        tree_records.column("regno",width=70)
        tree_records.column("chasis",width=80)
        tree_records.column("engno",width=70)
        tree_records.column("color",width=70)
        tree_records.column("vendorname",width=100)
        tree_records.column("vendoraddr",width=150)
        tree_records.column("buyername",width=100)        
        tree_records.column("buyeraddr",width=150)
        tree_records.column("place",width=60)
        tree_records.column("price",width=60)
        tree_records.column("price_inwords",width=150)
        tree_records.column("regdate",width=70)
      
        tree_records.pack(fill=BOTH, expand=1)
        tree_records.bind("<ButtonRelease-1>",LearnersInfo)
        DisplayData()
        #=========================buttons=========================
        
        self.btnAddNew = Button(InnerTopFrame2, pady=1,bd=4,font =('arial',16,'bold'), width=11,text="Add New",command=addData)
        self.btnAddNew.grid(row=0,column=0,padx=3)
        
        self.btnDisplay = Button(InnerTopFrame2, pady=1,bd=4,font =('arial',16,'bold'), width=11,text="Display",command=DisplayData)
        self.btnDisplay.grid(row=0,column=1,padx=3)
        
        self.btnUpdate = Button(InnerTopFrame2, pady=1,bd=4,font =('arial',16,'bold'), width=11,text="Update",command=Update)
        self.btnUpdate.grid(row=0,column=2,padx=3)
        
        self.Delete = Button(InnerTopFrame2, pady=1,bd=4,font =('arial',16,'bold'), width=11,text="Delete", command=deleteDB)
        self.Delete.grid(row=0,column=3,padx=3)
        
        self.btnReset = Button(InnerTopFrame2, pady=1,bd=4,font =('arial',16,'bold'), width=11,text="Reset",command=Reset)
        self.btnReset.grid(row=0,column=4,padx=3)
        
        self.btnExit = Button(InnerTopFrame2, pady=1,bd=4,font =('arial',16,'bold'), width=12,text="Exit",command=iExit)
        self.btnExit.grid(row=0,column=5,padx=3)
        
        self.btnSearch = Button(InnerTopFrame2, pady=1,bd=4,font =('arial',16,'bold'), width=12,text="Search",command=searchDB)
        self.btnSearch.grid(row=0,column=6,padx=3)
        
        self.btnPrint = Button(InnerTopFrame2, pady=1,bd=4,font =('arial',16,'bold'), width=12,text="Print",command=print)
        self.btnPrint.grid(row=0,column=7,padx=3)
        
        
        
        
        
        
        
if __name__=='__main__':
    root = Tk()
    application = DataEntryForm(root)
    root.mainloop()