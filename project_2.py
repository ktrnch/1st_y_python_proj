from tkinter import *
def add_fg(f,d,s,w):
    file_e=open(f,"a", encoding="utf-8")
    l="" 
    for i in s:
        v=d[i]
        w+=int(v)
        it=i+":"+v+"\n"
        l+=it
    total_weight=2+round(w/1000,2)
    file_e.write(l)
    file_e.close()

    flw= Tk()
    flw.title("Your backpack")
    flw.geometry("800x900")
    
    file=open(f, encoding="utf-8")
    fl=file.read()
    readfl= Label(flw, text=fl)
    readfl.pack(padx=10, pady=10)
    note= "NB!, Weight of your backpack together with all items is:"+str(total_weight)+" kg"+"\nMake sure it is less than 20% of your body mass:)\n(weight of backpack itself used for computing - 2 kg)"
    weightl= Label(flw, text=note)
    weightl.pack(padx=10, pady=10)
    
def add(n,i,w):
    file=open(n, "a", encoding="utf-8")
    it=i.get()
    wg=w.get()
    file.write(it+":"+wg+"\n")
    i.set(" ")
    w.set(" ")
    file.close()
    return i, w, file

def check(t,b):
    tot_weight=0
    rw= Tk()
    rw.title("Forgotten items")
    rw.geometry("800x200")
    thing=open(b, encoding="utf-8")
    ness=open(t, encoding="utf-8")
    ness_d={}
    things_d={}
    for line in thing:
        u_item,u_weight = line.strip().split(":")
        things_d[u_item]=u_weight
        try:
            n_wg=int(u_weight)
            tot_weight+=n_wg
        except:
            continue
    for line in ness:
        item,weight = line.strip().split(":")
        ness_d[item]=weight
        def fg_it(d):
            for item, _ in d:
                print(item)
                return item
    ness_s=set(ness_d.keys())
    tings_s=set(things_d.keys())
    forgotten_items=ness_s-tings_s
    print(tot_weight)
    things=open(b,"a", encoding="utf-8")
    
    def set_pr(s):
        line="\n"
        for e in s:
            line+=e+", "
        return line
    
    fg="Are you sure you want go hiking without: "+set_pr(forgotten_items)+"?"
    add_l=Label(rw, text=fg)
    add_l.pack()
    add_b=Button(rw,text = 'Oh no! Add to backpack', command=lambda:add_fg(b,ness_d,forgotten_items,tot_weight))
    add_b.pack()
    
    rw.mainloop()
    things.close()
    return things, tot_weight


def submit():
    f_name=name.get()
    print("The name is : " + f_name)
    window.destroy()
    fw = Tk()
    fw.title("Packing backpack")
    fw.geometry("800x100")
    framelst = Frame(fw)
    framelst.pack()
    
    item=StringVar()
    weight=StringVar()
    
    item_l=Label(framelst, text = 'Item')
    item_l.pack(side=LEFT)
    item_e = Entry(framelst, textvariable=item)
    item_e.pack(side=LEFT)
    weight_l=Label(framelst, text = 'Weigtht of the item(in grams)')
    weight_l.pack(side=LEFT)
    weight_e = Entry(framelst, textvariable=weight)
    weight_e.pack(side=LEFT)
    add_b=Button(framelst,text = 'Add to backpack', command= lambda: add(f_name,item,weight))
    add_b.pack(side=BOTTOM)
    fin_b=Button(framelst,text = 'Finish packing', command= lambda: check("necessities.txt",f_name))
    fin_b.pack(side=BOTTOM)
    fw.mainloop()
    
window = Tk()
window.title("Backpack list")
window.geometry("400x150")
fr = Frame(window)
fr.pack()
greetings = Label(fr, text='Hi! Happy to see yo here.\nHere you can create a list for your hiking trip\nEnter name for file(in form file.txt)to finde or create it')
greetings.pack(side=TOP)
name=StringVar()
name_e = Entry(fr,textvariable=name)
name_e.pack(side=BOTTOM)
sub_b=Button(window,text = 'Submit', command = submit)
sub_b.pack(side=BOTTOM)

window.mainloop()
