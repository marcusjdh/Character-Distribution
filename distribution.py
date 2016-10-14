"""
distribution.py
Author: Marcus Helble
Credit: None

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
user=input("Please enter a string of text (the bigger the better): ")
print('The distribution of characters in "'+user+'" is: ')
lowell=user.lower()

acount= lowell.count('a')
bcount=lowell.count('b')
ccount= lowell.count('c')
dcount=lowell.count('d')
ecount=lowell.count('e')
fcount= lowell.count('f')
gcount=lowell.count('g')
hcount=lowell.count('h')
icount=lowell.count('i')
jcount=lowell.count('j')
kcount=lowell.count('k')
lcount=lowell.count('l')
mcount=lowell.count('m')
ncount=lowell.count('n')
ocount=lowell.count('o')
pcount=lowell.count('p')
qcount=lowell.count('q')
rcount=lowell.count('r')
scount=lowell.count('s')
tcount=lowell.count('t')
ucount=lowell.count('u')
vcount=lowell.count('v')
wcount=lowell.count('w')
xcount=lowell.count('x')
ycount=lowell.count('y')
zcount=lowell.count('z')
def compare(a, b):
    """
    compare - generic comparison function for testing two elements.
    """
    return b > a


def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it
tosort=[acount, bcount, ccount, dcount, ecount, fcount, gcount, hcount, icount, jcount, kcount, lcount, mcount, ncount, ocount, pcount, qcount, rcount, scount, tcount, ucount, vcount, wcount, xcount, ycount, zcount]
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
jamal=list(zip(tosort,alphabet))
bsort(jamal, compare)
finn=[x for x in range(1,27)]
rfinn = finn[::-1]
lol=(zip(tosort,rfinn,alphabet))
mac= [x for x in lol]
mac.sort(reverse=True)
c=0

while c < 26 and mac[c][0] != 0:
   print(str(mac[c][2])*int(mac[c][0]))
   c = c + 1

