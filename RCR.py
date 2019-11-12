

class Rcorrelation:  #Classes used to calculate linear regression
    
    global X,Y,X_power2,line_xy 
    X = list()
    Y = list()
    X_power2 = list()

    def open_data(filename):
        #The function that opens the file and reads how many of x and y.
        with open(filename)as lines:
            for line in lines:
                x,y = line.split(",") #Split each line into X and Y values, respectively.
                X.append(int(x))#Take X value on each line, put in X list empty.
                Y.append(int(y)) #Take Y value on each line, put in Y list empty.
            print('Data X is =',X,"\n",'It have',len(X),'numbers.')
            print('Data Y is =',Y,"\n",'It have',len(Y),'numbers.')

    def xy_data():
        #The function calculates sum and mean of X and y.
        try:
            print('X =', X)
            print('Sum of X =',sum(X))
            print('Average of X =',sum(X)/len(X))
            print('Y =', Y)
            print('Sum of Y =',sum(Y))
            print('Average of X =',sum(Y)/len(Y))
        except ZeroDivisionError:
            print('ZeroDivisionError: some of data divided by zero(0)')


    def X_pow2(X):
        #The function calculates the value of x raised to the power of two and show the sum of X ^ 2.
        for i in X:
            print('X power 2 in position',i,'=',i**2)
            X_power2.append(i**2)
        print('Sum of X power 2=',sum(X_power2))

    def XY(X,Y):
        #Functions that find the values of X and Y multiplied together with positive sums.
        global XY
        XY = list()
        for i in X,Y:
            count = 0
            while count < len(X):
                print('Sum of X multiple Y in position',X[count],'and',Y[count],'=',X[count]*Y[count])
                XY.append(X[count]*Y[count])
                count += 1
            break
        print('Sum of X multiple Y =',(sum(XY)))

    def beta1():
       #The function calculates beta1 of the linear regression equation.
        global B1
        try:
            B1 = (sum(XY)-(sum(X)*sum(Y))/len(X))/(sum(X_power2)-(len(X)*((sum(X)/len(X))**2)))
            print('Beta1 =',round(B1,2))
        except ZeroDivisionError:
            print('ZeroDivisionError: some of data divided by zero(0)')
        except NameError:
            print('NameError: Program cannot find data to calculate')
        
    def beta0():
         #The function calculates the beta0 of the linear regression equation.
        global B0
        try:
            B0 = (sum(Y)/len(Y))-B1*(sum(X)/len(X))
            print('Beta0 =',round(B0,2))
        except ZeroDivisionError:
            print('ZeroDivisionError: some of data divided by zero(0)')

    def regression():
        #Functions that express the linear regression equation.
        try:
            print('Y =',round(B0,2),'+',round(B1,2),'(X)')
        except NameError:
            print('NameError: Program cannot find data to calculate')


    def r_square(): #The function that to find r-squared
        try:
            import scipy
            from scipy import stats
            slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(X,Y)
            print ("r-squared:", r_value**2)
        except ValueError:
            print('Program Do not have enough data.')
     

def menu():
    #The function that displays the program window.
    return input("=== 1)open file, 2)Data of X and Y, 3)summary of X power2, 4)summary of X multiple Y, 5)Beta0 and Beta1, 6)regression, 7)R-correlation, Q)uite ===:")

def main():
   #Menu function that links to the top menu.
    done = False
    while not done:
        choice = menu()  #If the function is not done, the menu will pop up.
        if choice == "1":
            try:
                Rcorrelation.open_data(input('filename:'))
            except OSError:
                print('Cannot find the location of data X and Y, please try again.')  #Displays when the user entered an invalid data address. And could not find the address of the file.
            except ValueError:
                print('Data in file cannot link to our program.') #Give a message when the data in the file can not be calculated in this program.
        elif choice == "2":
            Rcorrelation.xy_data()
        elif choice == "3":
            Rcorrelation.X_pow2(X)
        elif choice == "4":
            Rcorrelation.XY(X,Y)
        elif choice == "5":
            Rcorrelation.beta1()
            Rcorrelation.beta0()
        elif choice == "6":
            Rcorrelation.regression()
        elif choice == "7":
            Rcorrelation.r_square()
        elif choice == "Q" or choice == "q":
            done = True
        else:
            print('Please key the number of program or press "Q" to close program.')
            #If the user inserts a number or text other than this, display the new input or press Q to quit the program.
main()
