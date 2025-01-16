#---------------------------------------------------------------

def elso_karakter(string):
    """ 
    Visszatér a string első karakterével.
    """
    # YOUR CODE HERE
    ...

 #--------------------------------------------------------------- 

def utolso_karakter(string):
    """ 
    Visszatér az adott string utolso karakterével.
    """
    # YOUR CODE HERE
    ...

#assert utolso_karakter("Hello") == "o"

#---------------------------------------------------------------

def legkisebb(lista):
    """ 
    Visszatér egy számokat tartalmazó lista legkisebb számával.
    A feladat megoldása során nem használhatod a min() függvényt!
    """
    # YOUR CODE HERE
    ...
    

#assert legkisebb( [7, 4, 9, -4, -8, 3]) == -8

#---------------------------------------------------------------
  
def legnagyobb(lista):
    """ 
    Visszatér egy számokat tartalmazó lista legnagyobb számával.
    A feladat megoldása során nem használhatod a max függvényt!
    """
    # YOUR CODE HERE
    ...

#assert legnagyobb( [7, 4, 9, -4, -8, 3] ) == 9
  
#---------------------------------------------------------------

def osszeg(lista):
    """ 
    Visszatér egy számokat tartalmazó lista számainak összegével.
    A feladat megoldása során nem használhatod a sum() függvényt!
    """
    # YOUR CODE HERE
    ...

#assert osszeg( [1, 2, 3, 4, 5, 6] ) == 21

#---------------------------------------------------------------

def szorzat(lista):
    """ 
    Visszatér egy számokat tartalmazó lista számainak szorzatával.
    """
    # YOUR CODE HERE
    ...


#assert szorzat( [1, 2, 3, 4, 5] )  == 120

#---------------------------------------------------------------
    
def parosok_szama(lista):
    """ 
    Visszatér egy számokat tartalmazó lista páros számainak számával
    """
    # YOUR CODE HERE
    ...

#assert parosok_szama( [7, 4, 9, -4, -8, 3, 1] ) == 3

#---------------------------------------------------------------
   
def paratlanok_szama(lista):
    """ 
    Visszatér egy számokat tartalmazó lista páros számainak számával.
    """
    # YOUR CODE HERE
    ...

#assert paratlanok_szama( [7, 4, 9, -4, -8, 3, 1]) == 4

#---------------------------------------------------------------  

def pozitivok_szama(lista):
    """ 
    Visszatér egy számokat tartalmazó lista pozitív számainak számával.
    """
    # YOUR CODE HERE
    ...


#assert pozitivok_szama( [-7, -4, 9, -4, -8, 3, 1, 0]) == 3

#---------------------------------------------------------------  

def negativok_szama(lista):
    """ 
    Visszatér egy számokat tartalmazó lista negativ számainak számával.
    """
    # YOUR CODE HERE
    ...


#assert negativok_szama( [-7, -4, 9, -4, -8, 3, 1, 0]) == 4
    
#---------------------------------------------------------------  


def benne_van_a_listaban(lista, szam):
    """
    A visszatérési érték True, ha  a szám benne van a listában.
    A visszatérési érték False, ha  a szám nics benne a listában.
    """
    # YOUR CODE HERE
    ...


#assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 2) == False
#assert benne_van_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], 9) == True

#---------------------------------------------------------------
    
def benne_van_a_stringben(string, betu):
    """
    A visszatérési érték __True__, ha  a betü benne van a stringben.
    A visszatérési érték __False__, ha  a betü nics benne a stringben.
    """
    # YOUR CODE HERE
    ...


#assert benne_van_a_stringben("abrakadabra", "x") == False
#assert benne_van_a_stringben("abrakadabra", "d") == True

#---------------------------------------------------------------
    
def kereses_a_listaban(lista, szam):
    """
    A visszatérési érték a paraméterként megadott szám első előfordulási helye a listában.
    A visszatérési érték None, ha  a szám nics benne a listában.
    """
    # YOUR CODE HERE
    ...
    

#assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0], -7) == 0
#assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0],  9) == 2
#assert kereses_a_listaban([-7, -4, 9, -4, -8, 3, 1, 0],  2) == None
   
#---------------------------------------------------------------
  
def kereses_a_stringben(string, betu):
    """
    Visszatérési érték a paraméterként megadott betü első előfordulási helye a stringben. 
    A visszatérési érték None, ha  a betü nics benne a stringben.
    """
    # YOUR CODE HERE
    ...


#assert kereses_a_stringben("abrakadabra", "a") == 0
#assert kereses_a_stringben("abrakadabra", "k") == 4
#assert kereses_a_stringben("abrakadabra", "s") == None

#---------------------------------------------------------------
    
def parosok_kivalogatasa(lista):
    """
    Visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista páros számait tartalmazza.
    """
    # YOUR CODE HERE
    ...
    

#assert parosok_kivalogatasa( [7, 4, 9, 4, 8, 3, 1, 12, 0] ) == [4, 4, 8, 12, 0]

#---------------------------------------------------------------

def paratlanok_kivalogatasa(lista):
    """
    Visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista páratlan számait tartalmazza.
    """
    # YOUR CODE HERE
    ...


#assert paratlanok_kivalogatasa( [7, 4, 9, 4, 8, 3, 1, 12, 0] ) == [7, 9, 3, 1]

#---------------------------------------------------------------
 
def pozitivok_kivalogatasa(lista):
    """ 
    Visszatér egy listával, 
        amely a paraméterként átadott számokat tartalmazó lista pozitiv számait tartalmazza. 
    """
    # YOUR CODE HERE
    ...
    

#assert pozitivok_kivalogatasa( [7, 4, 9, -4, -8, 3, 1, 12, 0] ) == [7, 4, 9, 3, 1, 12]

#---------------------------------------------------------------
    
     
def negativok_kivalogatasa(lista):
    """
    Visszatér egy listával, 
      amely a paraméterként átadott számokat tartalmazó lista negatív számait tartalmazza.
    """
    # YOUR CODE HERE
    ...

#assert negativok_kivalogatasa( [7, 4, 9, -4, -8, 3, 1, 12, 0] ) == [-4, -8]

#---------------------------------------------------------------
    
def lista_atlag(lista):
    """ 
    Visszatér egy számokat tartalmazó lista számainak átlagával.
    """
    # YOUR CODE HERE    
    ...
    

#assert lista_atlag([1, 2, 3, 4, 5, 6]) == 21/6

#---------------------------------------------------------------

def faktorialis(n):
    """ visszatér a paraméterként megkapott szám faktoriálisával.
    """
    # YOUR CODE HERE
    ...
    

#assert  faktorialis(0) == 1
#assert  faktorialis(1) == 1
#assert  faktorialis(2) == 1 * 2
#assert  faktorialis(5) == 1 * 2 * 3 * 4 * 5
   
#---------------------------------------------------------------