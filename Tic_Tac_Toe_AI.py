def wincheck(rec):
	global winner,xo,cxo
	rboard=list(rec)
	winner=0
	for i in range(0,9,3):
		if(rboard[i] == 'X' or rboard[i] == 'O'):
			if(rboard[i] == rboard[i+1] and rboard[i+1] == rboard[i+2]):
				if rboard[i] == cxo:
					winner=1
				elif rboard[i] == xo:
					winner=2
					
				else:
					winner=0
	
	for i in range(0,3):
		if(rboard[i] == 'X' or rboard[i] == 'O'):
			if(rboard[i] == rboard[i+3] and rboard[i+3] == rboard[i+6]):	
				if rboard[i] == cxo:
					winner=1
				elif rboard[i] == xo:
					winner=2
					
				else:
					winner=0
				
	
	if(rboard[0] == rboard[4] and rboard[4] == rboard[8]):	
			if rboard[0] == cxo:
					winner=1
			elif rboard[0] == xo:
					winner=2
					
			else:
					winner=0
	
	if(rboard[6] == rboard[4] and rboard[4] == rboard[2]):	
			if rboard[4] == cxo:
					winner=1
			elif rboard[4] == xo:
					winner=2
					
			else:
	
					winner=0
				
	return winner
	
	
def poscheck(p):
	global vaclist
	if(p in vaclist):
		vaclist.remove(p)
		return True
	elif(p<10):
		print("ERROR : Already entered the position : ")
		userin()
	else:
		print("Number between 1 and 10 only accepted")
		userin()

def userin(symb):
	global vaclist,count,gboard,xo

	try:
		pos=int(input(("\nEnter the position : ")))
		if(poscheck(pos)):
				gboard[pos-1]=symb
				count=count-1
	except:
			print(" Enter a digit from 1 to 9")
			userin()

def show(shboard):
	print("\n")
	for i in range(9):
		print("\t\t",shboard[i],end=" ")
		if (i==2 or i ==5):
			print("\n")
	print("\n")
def cpu(predboard):
	global vaclist,gboard,count
	pbd=list(predboard)

	flag2=0
	for x in vaclist:
		
		pbd[x-1]=cxo
		wa=wincheck(pbd)
		
		if(wa==1):
			
			gboard[x-1]=cxo
			vaclist.remove(x)
			count=count-1
			flag2=1
			break
			
			
		pbd[x-1]="_"
	if(flag2!=1):
		for x in vaclist:
			
			pbd[x-1]=xo
			wa=wincheck(pbd)
			
			if(wa==2):
				
				gboard[x-1]=cxo
				vaclist.remove(x)
				count=count-1
				flag2=3
				break
				
			pbd[x-1]="_"
	if(flag2!=3 and flag2!=1):
		rnum = random.choice(vaclist)
		gboard[rnum-1]=cxo
		vaclist.remove(rnum)
		x=rnum
		count=count-1
	print("\nCPU Played at Position ",x)
	time.sleep(.15)
import random
import time
def beginhere():
	global gboard,vaclist,count,winner,turn,xo,cxo,mod,p1,p2
	gboard=["_","_","_","_","_","_","_","_","_"]
	vaclist=[1,2,3,4,5,6,7,8,9]                 
	print ("\nTik Tak Toe Mulitplayer Game")
	print("Choose Mode of Play")
	mod=int(input("1.Multiplayer\n2.vs CPU\n"))

	if mod == 2:
		p1="CPU"
		p2="You"
		xo=input("Choose your symbol : X or O ? ")
		xo=xo.upper()
		if(xo=="X"):
			cxo="O"
		else:
			cxo="X"
		print("Ok you selected : ",xo)
	if mod == 1:
		p1=input("Enter Player 1 Name : ")
		p2=input("Enter Player 2 Name : ")
		print(p1," : X")
		print(p2," : O")
		cxo="X"
		xo="O"
	sttr=input("Press any key to start the game")
	show(gboard)
	print("\nInitial Board")
	count=9
	winner=0
	turn=random.randint(0,1)
	if(turn == 0 and mod == 2):
		print("CPU Play First")
	if(turn == 1 and mod == 2):
		print("Your Turn First")
beginhere()
while(count>0):
	ch='a'
	if(turn==0 and mod==2):
		print("CPU Thinking .",end="")
		for i in range(4):
			time.sleep(1)
			print(".",end="")
		cpu(gboard)
		turn=1
	elif(turn==1 and mod==2):
		print("Your Turn")
		userin(xo)
		turn=0
	elif(turn==0 and mod==1):
		print("Turn for ",p1)
		userin(cxo)
		turn=1
	elif(turn==1 and mod ==1):
		print("Turn for ",p2)
		userin(xo)
		turn=0

	w=wincheck(gboard)

	show(gboard)
	if(w==1):
		print(p1," Won the Game")
		count=0
		ch =input(" Do you want to play again : Y/N")

	elif(w==2):
		print(p2," Won the Game")
		ch =input("Do you want to play again : Y/N")
		count=0

	elif(w==0 and count==0):
		print("Game is a Draw")
		count=0
		ch =input(" Do you want to play again : Y/N")
	if(ch=='Y' or ch=="y"):
		beginhere()
	if(ch=="N" or ch=='n'):
		print("\nThank You for playing Tic Tak Toe.... See You")
		print("\n\n")
		count=0