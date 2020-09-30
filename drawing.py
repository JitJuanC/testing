def hangman_pic(draw: int):
    if draw == 1:
        print("""
                    
        
         
        
        _____
        """)
    elif draw == 2:
        print("""
                    
        
           
        |  
        _____
        """)
    elif draw == 3:
        print("""
                    
           
        |   
        |  
        _____
        """)
    elif draw == 4:
        print("""
                    
        |   
        |   
        |  
        _____
        """)
    elif draw == 5:
        print("""
        ----            
        |   
        |   
        |  
        _____
        """)
    elif draw == 6:
        print("""
        ----            
        |   O
        |   
        |  
        _____
        """)
    elif draw == 7:
        print("""
        ----            
        |   O
        |  / 
        |  
        _____
        """)
    elif draw == 8:
        print("""
        ----            
        |   O
        |  /| 
        |  
        _____
        """)
    elif draw == 9:
        print("""
        ----            
        |   O
        |  /|\\ 
        |  
        _____
        """)
    elif draw == 10:
        print("""
        ----            
        |   O
        |  /|\\ 
        |  / 
        _____
        """)
    elif draw == 11:
        print("""
        ----            
        |   O
        |  /|\\ 
        |  / \\
        _____
        """)
    elif draw == 12:
        print("""
        ----            
        |   O   \"I'm Dead\"
     ________________________
        |  /|\\ 
        |  / \\
        _____
        """)
