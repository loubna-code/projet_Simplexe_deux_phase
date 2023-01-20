import tkinter
from tkinter import ttk
import numpy as np
import sys
global root, root1,methode,var,ct,comb1,entrer1,entrer2,entrer4,entrer3,c,root2

Z=[]#fonction objective
b=[]#2 em mombre
type=[] #type
#c=np.zeros()
listCon=[]#list contantraint
listVariables=[]# list variables
listB=[] # list 2em mombre
listType=[]


    
    

def Accueill():
    global root,methode,var,ct,comb1,entrer1,entrer2
    root=tkinter.Tk()
    root.geometry('800x500+400+100')
    root.resizable(True,True)
    root.title('La methode simplex 1')
    root.config(background='gray')
    #fr1=tkinter.Frame(width=799,height=499,bg='gray')
    #fr1.place(x=1,y=1)
    label1= tkinter.Label(root,text="La methode simplex",fg='black',bg='gray',font=("Helvitica",20,'bold'))
    label1.place(x=240,y=10)
    label2= tkinter.Label(root,text="Méthode:",fg='black',bg='gray',font=("Courier",12,'italic'))
    label2.place(x=100,y=80)
    comb1=ttk.Combobox(root,value=('Simplexe/Deux phases','Graphique'),state='readonly')
    comb1.place(x=190,y=80)
   
    label3= tkinter.Label(root,text="Combien de variables de décision ?",fg='black',bg='gray',font=("Courier",12,'italic'))
    label3.place(x=80,y=120)
    entrer1=tkinter.Entry()
    entrer1.place(x=440,y=120)
    
    label4= tkinter.Label(root,text="Combien de contraintes?",fg='black',bg='gray',font=("Courier",12,'italic'))
    label4.place(x=80,y=160)
    entrer2=tkinter.Entry()
    entrer2.place(x=440,y=160)
    
    btn1=tkinter.Button(root,text='Continuer',fg='white',bg='GRAY',command=test)
    btn1.place(x=350,y=220)
    root.mainloop()


def Page1():
      
    global root1,var,methode,comb1,entrer1,ct,entrer2,entrer4,entrer3,c
    
    root1=tkinter.Tk()
    root1.geometry('800x500+400+100')
    root1.resizable(True,True)
    root1.title('La methode simplex2')
    root1.config(background='gray')
    label1= tkinter.Label(root1,text="La methode simplex",fg='black',bg='gray',font=("Helvitica",20,'bold'))
    label1.place(x=240,y=10)
    label2=tkinter.Label(root1,text="Le but de la fonction?",fg='black',bg='gray',font=("Courier",12,'italic'))
    label2.place(x=100,y=80)
    comb1=ttk.Combobox(root1,value=('Maximiser','Minimiser'),state='readonly')
    comb1.place(x=330,y=80)
    
    label3=tkinter.Label(root1,text='Fonction:',fg='black',bg='gray',font=("Courier",12,'italic'))
    label3.place(x=100,y=120)


    for x in range(int(var)-1):
        
        entrer3=tkinter.Entry(root1,justify='center',fg='black',font=10,width=5)
        entrer3.place(x=200+x*80,y=120)
        listVariables.append(entrer3)
        
        label5=tkinter.Label(root1,text='X'+str(x+1)+'+',fg='black',bg='gray',font=("Courier",12,'italic'))
        label5.place(x=240+x*80,y=120)
    entrer4=tkinter.Entry(root1,justify='center',fg='black',font=10,width=5)
    entrer4.place(x=200+(int(var)-1)*80,y=120)
    label5=tkinter.Label(root1,text='X'+str(var),fg='black',bg='gray',font=("Courier",12,'italic'))
    label5.place(x=240+(int(var)-1)*80,y=120)  



    label3=tkinter.Label(root1,text='Contraintes',fg='black',bg='gray',font=("Courier",12,'italic'))
    label3.place(x=300,y=160)

    for i in range(int(ct)):
        for x in range(int(var)-1):
            
           entrer5=tkinter.Entry(root1,justify='center',fg='black',font=10,width=5)
           entrer5.place(x=200+x*80,y=200+i*40)
           listCon.append(entrer5)
           label5=tkinter.Label(root1,text='X'+str(x+1)+'+',fg='black',bg='gray',font=("Courier",12,'italic'))
           label5.place(x=240+x*80,y=200+i*40)
           
           
        entrer6=tkinter.Entry(root1,justify='center',fg='black',font=10,width=5)
        entrer6.place(x=200+(int(var)-1)*80,y=200+i*40)
        listCon.append(entrer6)
        
        label5=tkinter.Label(root1,text='X'+str(var),fg='black',bg='gray',font=("Courier",12,'italic'))
        label5.place(x=240+(int(var)-1)*80,y=200+i*40) 
        
        comb2=ttk.Combobox(root1,value=('=','<=','>='),state='readonly',width=3)
        comb2.place(x=280+(int(var)-1)*80,y=200+i*40)
        listType.append(comb2)
        entrer7=tkinter.Entry(root1,justify='center',fg='black',font=10,width=5)
        entrer7.place(x=340+(int(var)-1)*80,y=200+i*40)
        listB.append(entrer7)


		
    label5=tkinter.Label(root1,text='Xi ≥ 0 avec i∈{1..'+str(var)+'}',fg='black',bg='gray',font=("Courier",12,'italic'))
    label5.place(x=240,y=200+int(ct)*40)
    btn1=tkinter.Button(root1,text='Continuer',fg='white',bg='GRAY',command=test1)
    btn1.place(x=350,y=200+int(ct)*40+40)
    root1.mainloop()
l=np.zeros(())
bb=[]
cc=[]
V=[]
def page_nonborne():
    rooterreur=tkinter.Tk()
    rooterreur.geometry('800x500+400+100')
    rooterreur.config(background='gray')
    
    le1=tkinter.Label(rooterreur,text=" le probleme est non borne",borderwidth=1,width=40,height=5,relief="solid",font=("Arial, 12"))
    le1.place(x=230,y=180)
    rooterreur.mainloop()   
 

def page_pasdesolu():
    rooterreur1=tkinter.Tk()
    rooterreur1.geometry('800x500+400+100')
    rooterreur1.config(background='gray')
    
    le1=tkinter.Label(rooterreur1,text=" le probleme n'admet pas du solution",borderwidth=1,width=40,height=5,relief="solid",font=("Arial, 12"))
    le1.place(x=230,y=180)
    rooterreur1.mainloop()   
    
     
def page_resultat(Ligne,Colonne,l,bb,cc,zobj,V,ap):
     
    global root2,var,methode,comb1,entrer1,ct,entrer2,entrer4,entrer3,c
    #traitement()
    root2=tkinter.Tk()
    root2.geometry('800x500+400+100')
    root2.config(background='gray')
    
    for i in range (Colonne+1):
        l1=tkinter.Label(root2,text="  X%s  "%i,width=3,font=("Arial, 12"))
        l1.place(x=180+(i*50),y=100)
    
    for i in range (Ligne):
    
        
        l2=tkinter.Label(root2,text="  X%s  "%((V[i]+1)).astype(int),borderwidth=1,width=3,relief="solid",font=("Arial, 12"))
        l2.place(x=180,y=140+(i*40))
    
    for i in range (Ligne):
        for j in range (Colonne):
            l3=tkinter.Label(root2,text=f"{l[i][j]:.2f}",width=3)
            l3.place(x=230+(j*50),y=140+(i*40))
        
    l4=tkinter.Label(root2,text="B",borderwidth=1,width=3,relief="solid",font=("Arial, 12"))
    l4.place(x=230+((Colonne)*50),y=100) 
    
    for i in range (Ligne):
        
        l6=tkinter.Label(root2,text="  %s  "%bb[i],borderwidth=1,relief="solid",font=("Arial, 12")) 
        l6.place(x=230+((Colonne)*50),y=140+(i*40))
    
        
    for i in range (Colonne):
        l5=tkinter.Label(root2,text=f"{cc[i]:.2f}",borderwidth=1,relief="solid",font=("Arial, 12")) 
        l5.place(x=230+(i*50),y=140+(Ligne*40)) 
        
    l7=tkinter.Label(root2,text="Cj",borderwidth=1,width=3,relief="solid",font=("Arial, 12"))
    l7.place(x=180,y=140+(Ligne*40)) 
        
    l8=tkinter.Label(root2,text="Z= %s"%zobj,borderwidth=1,relief="solid",font=("Arial, 12"))
    l8.place(x=230+((Colonne)*50),y=140+(Ligne*40))
    l7=tkinter.Label(root2,text="Pivot=%s"%ap,borderwidth=1,width=10,relief="solid",font=("Arial, 12"))
    l7.place(x=450,y=140+(Ligne*60)) 
    btn1=tkinter.Button(root2,text='Next',fg='white',bg='GRAY',command=test2)
    btn1.place(x=350,y=140+(Ligne*60))
    root2.mainloop()

    
def traitement():
    global c
    #traitement phase
    Zoptimal=0#Z final pour afficher

        
    for n in range(len(b)):
        if b[n]<0 :
           # c[n]=c[n]*(-1)x * K for x in test_list
            c[n]=[x*(-1) for x in c[n]]
            b[n]=-b[n]
            if type[n]=="<=":
                type[n]=">="
            else:
                if type[n]==">=":
                    type[n]="<="
    print(c,b,type)
    
    e_count=0
    a_count=0
    for n in range(len(type)):
        if (type[n]=="<=" or type[n]==">="):
                e_count+=1
        if (type[n]==">=" or type[n]=="="):
                a_count+=1
    
    print(e_count,a_count)
    
    e=np.zeros((len(c),e_count))
    a=np.zeros((len(c),a_count))
    ei=0
    ai=0
    for n in range(len(c)):
        if type[n]=="<=":
            e[n][ei]=1
            ei+=1
            continue
        else:
            if type[n]==">=":
                e[n][ei]=-1
                a[n][ai]=1
                ei+=1
                ai+=1
                continue
            else:
                if type[n]=="=":
                    a[n][ai]=1
                    ai+=1
                    continue
        
            
    print(e,end=("\n"))
    print(a,end=("\n"))
             
    c=np.concatenate((c,e),axis=1)
    
    c=np.concatenate((c,a),axis=1)
    print("\n\n concatenation\n\n",c,b)
    
    cj=np.zeros(len(c.T))
    v_base=np.zeros(len(c))
    Zoptimal=0
    
    
    def Indexe1occu(liste):
        for i in range(len(liste)):
            if liste[i]==min(liste):
                return i
        
        
        
        
    def trouver_pivot(c,b,cj):
        IndiceMin=Indexe1occu(cj)
        ratio=np.zeros(len(c))
        for i in range(len(ratio)):
            if c[i][IndiceMin]>0:
                ratio[i]=b[i]/c[i][IndiceMin]
            else:ratio[i]=sys.maxsize
        if min(ratio)==sys.maxsize:
            return[-1,-1]
        else:
            return [Indexe1occu(ratio),IndiceMin]
            
    def check(list):
        for i in range(len(list)):
            if(list[i]<0):
                return True
        return False
            
    def iteration(v_base,c,b,cj,e_count,a_count,Zoptimal):
        
        #info pibvot
        ipivot=trouver_pivot(c, b, cj)[0]
        jpivot=trouver_pivot(c, b, cj)[1]
        pivot=c[ipivot][jpivot]
        
        cjpivot=cj[jpivot]
        
        newbipivot=b[ipivot]/pivot
        #change base
        v_base[ipivot]=jpivot
        # souv col pivot
        col=np.zeros(len(c))
        for i in range(len(c)):
            col[i]=c[i][jpivot]
        
        
        
        
        for j in range(len(c.T)):
            c[ipivot][j]=c[ipivot][j]/pivot
        
        for i in range(len(c)):
            if(i!=ipivot):
                for j in range(len(c.T)):
                    c[i][j]=c[i][j]-(col[i]*c[ipivot][j])
        
        for j in range(len(cj)):
            cj[j]=cj[j]-(cjpivot*c[ipivot][j])
        #changer b   
       
        print("newbipivot",newbipivot)
    
        for i in range(len(b)):
            if(i!=ipivot):
                    b[i]=b[i]-(col[i]*newbipivot)
            else: b[i]=newbipivot
        
        print("cjpivot",cjpivot)
        Zoptimal-=(cjpivot*newbipivot)
        #print("z--->",Zoptimal)
        return Zoptimal
           
        
        
        
        
    def phase1(v_base,c,b,cj,e_count,a_count):
        zz=0
        for i in range(len(c.T)):
           if i>=(len(c.T)-a_count):
               cj[i]=1
               
        for i in range(len(c)):
            indice=-1
            for j in range(len(c.T)-a_count-e_count,len(c.T)):
                if c[i][j]!=0:
                    indice=j
            v_base[i]=indice
        
        for i in range(len(v_base)):
            if v_base[i]>=(len(c.T)-a_count):
                zz=zz-b[i]
                for j in range(len(c.T)):
                    cj[j]=cj[j]-c[i][j]
                    
          
        
     
        while (trouver_pivot(c, b, cj)!=[-1,-1]) and (check(cj)):
           page_resultat(len(c),len(c.T),c,b,cj,zz,v_base,c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]]) 
           print("---------------------------------------------------------")
           print("cj:" ,cj)
           print("z--->",zz)
           print("trouver_pivot",c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]])
           print("c",c,end="\n")
           print("b",b)
           zz=iteration(v_base,c,b,cj, e_count, a_count,zz)
           
           #print("Z",zz)
           print("---------------------------------------------------------") 
           
           
        if(trouver_pivot(c, b, cj)==[-1,-1]):
           page_nonborne()
           
        else:
            page_resultat(len(c),len(c.T),c,b,cj,zz,v_base,c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]])
            
        if(check(cj)) and zz!=0:
            page_pasdesolu()
            
            
        #page_resultat(len(c),len(c.T),c,b,cj,zz,v_base,c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]])   
        print("---------------------------------------------------------")
        print("cj:" ,cj)
        print("z--->",zz)
        print("trouver_pivot",c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]])
        print("c",c,end="\n")
        print("b",b)
        """
        if(trouver_pivot(c, b, cj)==[-1,-1]):
            print("le prob non borne")
        if(check(cj)) and zz!=0:
            print("le prob n'admit pas de solution")
         """   
        
     
        
     
        
     
        
     
     
    def phase2(v_base,c,b,cj,e_count,a_count):
        zz=0
        #suppression des variables artificiel
        c=c[:, :-a_count]
        cj=cj[:-a_count]
        print("\n\nc:phase2\n\n",c,"\n\n",cj)
        # revien a les coef de z initial
        for i in range(len(Z)):
            cj[i]=Z[i]
            
        print("Z",Z)
        print("\n cj",cj) 
        #correstion de ligne cj et zz
        
        for i in range(len(v_base)):
            if (cj[v_base[i].astype(int)]):
                Vfaute=cj[v_base[i].astype(int)]
                for j in range(len(c.T)):
                    cj[j]=cj[j]-(Vfaute*c[i][j])
                zz=zz-(Vfaute*b[i])
        print("\n cj corriger",cj)
        print("\n zz corriger",zz)
        #a_count=0 
        
    
        while (trouver_pivot(c, b, cj)!=[-1,-1]) and (check(cj)):
           page_resultat(len(c),len(c.T),c,b,cj,zz,v_base,c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]]) 
           print("---------------------------------------------------------")
           print("cj:" ,cj)
           print("z--->",zz)
           print("trouver_pivot",c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]])
           print("c",c,end="\n")
           print("b",b)
           zz=iteration(v_base,c,b,cj, e_count, 0,zz)
           
           
           #print("Z",zz)
           print("---------------------------------------------------------") 
        page_resultat(len(c),len(c.T),c,b,cj,zz,v_base,c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]])   
        print("---------------------------------------------------------")
        print("cj:" ,cj)
        print("z--->",zz)
        print("trouver_pivot",c[trouver_pivot(c, b, cj)[0]][trouver_pivot(c, b, cj)[1]])
        print("c",c,end="\n")
        print("b",b)    
        if(trouver_pivot(c, b, cj)==[-1,-1]):
            page_nonborne()
        for j in range(len(cj)):
            if(cj[j]==0):
                if j in v_base:
                    continue
                else:
                    print("il'y a un segument de solution")
        return zz    
    
    phase1(v_base,c,b,cj,e_count,a_count) 
    Zoptimal=phase2(v_base,c,b,cj,e_count,a_count)     

def test():
    global root,root1,comb1,methode,entrer1,ct,entrer2,var
    methode=comb1.get()
    var=entrer1.get()
    ct=entrer2.get()
   
    root.destroy()
    Page1()
    
def test2():
    global root2
    root2.destroy()
    
def test1():    
    global root,root1,comb1,methode,entrer1,ct,entrer2,var,variable,entrer4,entrer3,c
    
    objectif=comb1.get()
    print(objectif)
    for i in listVariables:
        Z.append(int(i.get()))
        
    Z.append(int(entrer4.get()))
    print(Z)
    
    for i in listB:
        b.append(int(i.get())) # b les valeurs de variables de base
    print(b)
    
    for i in listType:
        type.append(i.get())
    print(type)
    c=np.zeros((len(b),len(Z)))# matrice (le corps de tableau)
    
    for i in range(len(b)):
        for j in  range(len(Z)):
            c[i][j]=(listCon.pop(0)).get()
    print(c)
    if objectif=="Maximiser":
        for i in range(len(Z)):
            Z[i]=-Z[i]
        
            
            
    
    root1.destroy()
    traitement()

if __name__=='__main__':
    Accueill()