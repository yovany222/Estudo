# Calcular a diferença entre: (soma dos quadrados entre 1 e 100) e (quadrado da soma entre 1 e 100)

def sum_of_the_squares(n):
     result = 0
     for i in range(1 , n+1):
          result += (i*i)
     return result

def squares_of_the_sum(n):
     result = 0
     for i in range(1 , n+1):
          result += (i)
     result = result * result
     return result

difference = (squares_of_the_sum(100) - sum_of_the_squares(100))

print(difference)

     
     
     
          
