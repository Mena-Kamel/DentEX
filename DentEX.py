from graphics import *
window= GraphWin ("DenTEX", 800, 600)
window.setCoords(0, 0, 800, 600)
window.setBackground("grey")

def textSet(self, font, size):
    self.setSize(size)
    self.setFace(font)
    
def isPressed(point, x1,y1, x2,y2):
    if point.getX()> x1 and  point.getX()< x2 and  point.getY()< y1 and  point.getY()> y2:
        return True
    else:
        return False

def getHistory():
    window3= GraphWin ("Patient History", 600, 600)
    window3.setCoords(0, 0, 600, 600)
    window3.setBackground("white")
    label= Text(Point(300, 500), "PATIENT HISTORY")
    label.draw(window3)
    

def newEntry(win, label, adjustment, y, w, t):
    if adjustment== "l":
        x= 50
    elif adjustment== "c":
        x=200
    else:
        x=400
    
    label= Text(Point(x, y), label)
    en= Entry(Point(x+120, y), w)
    en.setText(t)
    label.draw(win)
    label.setSize(10)
    label.setFace("helvetica")
    en.draw(win)
    return en
        
    

def getNewData():
    f= open("DenTEX", "a")
    window2= GraphWin ("NEW PATIENT FORM", 600, 600)
    window2.setCoords(0, 0, 600, 600)
    label4= Text(Point (300, 580), "NEW PATIENT FORM")
    textSet(label4,"helvetica", 30)
    label4.draw(window2)
    e1=newEntry(window2, "NAME", "c", 540, 30,'First, Middle, Last')
    e2=newEntry(window2, "OHIP NUMBER", "l", 510, 10,'')
    e3= newEntry(window2, "OHIP EXPIRY \n DATE", "4", 510, 10,'')
    e4=newEntry(window2, "GENDER", "r", 480, 10,'')
    e5=newEntry(window2, "D.O.B.", "l", 480, 10, 'dd/mm/yyyy')
    e6=newEntry(window2, "STREET NO.", "l", 450, 10, '')
    e8=newEntry(window2, "PROVINCE", "r", 450, 10, '')
    e7=newEntry(window2, "STREET \n NAME", "c", 420, 30, '')
    e9=newEntry(window2, "PHONE #", "c", 390, 20, '')
    e10=newEntry(window2, "EMERGENCY \n CONTACT", "l", 360, 20, '')
    e11=newEntry(window2, "RELATIONSHIP", "r", 360, 20, '')

    
    
    button3= Rectangle(Point (200, 240), Point(400, 210))
    button3.draw(window2)
    label2= Text(Point(300, 225), "SAVE & RETURN \n TO PREVIOUS MENU")
    label2.draw(window2)
    

    button4= Rectangle(Point (200, 300), Point(400, 270))
    button4.draw(window2)
    label3= Text(Point(300, 285), "PATIENT HISTORY")
    label3.draw(window2)

    location= window2.getMouse()

    f.write(e1.getText()+ ":" + e2.getText()+ ":" + e3.getText()+ ":" + e4.getText()+ ":"+ e5.getText()+ ":"+ e6.getText()+ ":"+ e7.getText()+ ":"+ e8.getText()+ ":"+ e9.getText()+ ":"+ e10.getText()+ ":"+ e11.getText()+":"+ "\n")
    
    if isPressed(location, 200, 240, 400, 210):
        window2.close()

    elif isPressed(location, 200, 300, 400, 270):
        getHistory()

    
    f.close()

def updateData(window2, inputData, oldlabel):
    fa= open("DenTEX", "r")
    refData= fa.readlines()
    fa.close()
    
    fb= open ("DenTEX", "r")
    flag=1
    
    for l in fb:
        patient= l.split(":")
        OHIP= patient[1]
        if OHIP==inputData:
            
            print patient
            e1=newEntry(window2, "NAME", "c", 540, 30,patient[0])
            e2=newEntry(window2, "OHIP NUMBER", "l", 510, 10,patient[1])
            e3= newEntry(window2, "OHIP EXPIRY \n DATE", "4", 510, 10,patient[2])
            e4=newEntry(window2, "GENDER", "r", 480, 10,patient[3])
            e5=newEntry(window2, "D.O.B.", "l", 480, 10, patient[4])
            e6=newEntry(window2, "STREET NO.", "l", 450, 10, patient[5])
            e8=newEntry(window2, "PROVINCE", "r", 450, 10, patient[7])
            e7=newEntry(window2, "STREET \n NAME", "c", 420, 30, patient[6])
            e9=newEntry(window2, "PHONE #", "c", 390, 20, patient[8])
            e10=newEntry(window2, "EMERGENCY \n CONTACT", "l", 360, 20, patient[9])
            e11=newEntry(window2, "RELATIONSHIP", "r", 360, 20, patient[10])
            flag=0
            fb.close
            oldlabel.setText("SAVE AND RETURN")
            location= window2.getMouse()
            if isPressed(location, 200, 300, 400, 260):
                window2.close()
            
            fc=open("DenTEX", "w")
            for i in refData:
                if i==l:
                    fc.write(e1.getText()+ ":" + e2.getText()+ ":" + e3.getText()+ ":" + e4.getText()+ ":"+ e5.getText()+ ":"+ e6.getText()+ ":"+ e7.getText()+ ":"+ e8.getText()+ ":"+ e9.getText()+ ":"+ e10.getText()+ ":"+ e11.getText()+ ":"+ "\n")
                else:
                    fc.write(i)
            fc.close()
            break
    
    return flag

            
                    
            

def accessData():
    window2= GraphWin ("CURRENT PATIENT INFORMATION", 600, 600)
    window2.setCoords(0, 0, 600, 600)
    label4= Text(Point (300, 580), "CURRENT PATIENT INFORMATION")
    textSet(label4,"helvetica", 30)
    label4.draw(window2)
    e1=Entry(Point(320,540), 15)
    t1= Text(Point(200, 540), "OHIP NUMBER")
    e1.draw(window2)
    t1.draw(window2)
    flag=1
    button3= Rectangle(Point (200, 300), Point(400, 260))
    button3.draw(window2)
    label2= Text(Point(300, 280), "SEARCH")
    label2.draw(window2)
    location= window2.getMouse()

    if isPressed(location, 200, 300, 400, 260):
        e1.undraw()
        t1.undraw()
        flag= updateData(window2, e1.getText(), label2)
        
        
    if flag==1:
        notification= Text(Point(300, 400), "Patient Data Not Found!")
        notification.draw(window2)
        label2.undraw()
        button3.undraw()
        button4= Rectangle(Point (200, 300), Point(400, 270))
        button4.draw(window2)
        label4= Text(Point (300, 285), "Add new Patient?")
        textSet(label4, "helvetica", 20)
        label4.draw(window2)

        button5= Rectangle(Point (200, 240), Point(400, 210))
        button5.draw(window2)
        label5= Text(Point (300, 225), "Back")
        textSet(label5, "helvetica", 20)
        label5.draw(window2)

        location= window2.getMouse()
        
        if isPressed(location, 200,300,400,270):
            window2.close()
            getNewData()
        elif isPressed(location, 200,240,400,210):
            window2.close()


    
#LOGO
label1= Text(Point (70, 580), "DenTEX")
textSet(label1,"helvetica", 35)
label1.setFill("white")
label1.draw(window)


#Navigation
button1= Rectangle(Point (200, 500), Point(600, 470))
button1.setFill("white")
button1.draw(window)
label2= Text(Point (400, 485), "Add new Patient")
textSet(label2, "helvetica", 20)
label2.draw(window)
 

button2= Rectangle(Point (200, 440), Point(600, 410))
button2.setFill("white")
button2.draw(window)
label3= Text(Point (400, 425), "Change Patient Information")
textSet(label3, "helvetica", 20)
label3.draw(window)

button3= Rectangle(Point (200, 380), Point(600, 350))
button3.setFill("white")
button3.draw(window)
label4= Text(Point (400, 365), "Manage Bookings")
textSet(label4, "helvetica", 20)
label4.draw(window)

button4= Rectangle(Point (300, 200), Point(500, 170))
button4.setFill("white")
button4.draw(window)
label5= Text(Point (400, 185), "QUIT")
textSet(label5, "helvetica", 20)
label5.draw(window)


#MENU 1

location= window.getMouse()
while not isPressed(location, 300,200, 500, 170):
    if  isPressed(location, 200,500, 600, 470):
        getNewData()
        location= window.getMouse()

    if isPressed (location, 200,440, 600, 410):
        accessData()
        location= window.getMouse()

window.close()

