import matplotlib.pyplot as plt

class MultiplicationByScalar:
    def __init__(self) -> None:
        pass
    
    def multiplication(self, vector : list, scalar : int) -> list:
        multiplied_vector = []
        
        for i in range(len(vector)):
            multiplied_vector.append(vector[i] * scalar)
            
        return multiplied_vector
    
class DrawVectorSC:
    def __init__(self) -> None:
        pass
    
    def draw(self, vector : list, scalar : int) -> list:
        vector_calculation = MultiplicationByScalar()
        result = vector_calculation.multiplication(vector, scalar)
        
        plt.plot(result, 'o', linestyle='-')
        plt.grid()
        plt.show()
        
        return result
        