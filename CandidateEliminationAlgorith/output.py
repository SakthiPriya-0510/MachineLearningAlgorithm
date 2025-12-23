Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 20:34:20) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/cse/Desktop/ML-Algorith/CandidateEliminationAlgorithm/CEA.py 
After example 1
S = ['Technical', 'Senior', 'Excellent', 'Good', 'Urban']
G = [['?', '?', '?', '?', '?']]
----------------------------------------
After example 2
S = ['Technical', '?', 'Excellent', 'Good', 'Urban']
G = [['?', '?', '?', '?', '?']]
----------------------------------------
After example 3
S = ['Technical', '?', 'Excellent', 'Good', 'Urban']
G = [['Technical', '?', '?', '?', '?'], ['?', '?', 'Excellent', '?', '?'], ['?', '?', '?', 'Good', '?'], ['?', '?', '?', '?', 'Urban']]
----------------------------------------
After example 4
S = ['Technical', '?', 'Excellent', 'Good', 'Urban']
G = [['Technical', '?', 'Excellent', '?', '?'], ['Technical', '?', '?', '?', 'Urban'], ['?', '?', 'Excellent', '?', '?'], ['?', '?', 'Excellent', 'Good', '?'], ['?', '?', '?', 'Good', 'Urban'], ['?', '?', '?', '?', 'Urban']]
----------------------------------------
After example 5
S = ['Technical', '?', 'Excellent', 'Good', '?']
G = [['Technical', '?', 'Excellent', '?', '?'], ['?', '?', 'Excellent', '?', '?'], ['?', '?', 'Excellent', 'Good', '?']]
----------------------------------------
Final Specific Boundary: ['Technical', '?', 'Excellent', 'Good', '?']
Final General Boundary: [['Technical', '?', 'Excellent', '?', '?'], ['?', '?', 'Excellent', '?', '?'], ['?', '?', 'Excellent', 'Good', '?']]
>>> 
