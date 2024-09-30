import matplotlib.pyplot as plt

class VectorSubtraction:
    def __init__(self) -> None:
        pass
    
    def Sub(self, initial_vector : list[int], travel_vector : list[int]):
        result_vector = []
        
        for i in range(len(initial_vector)):
            result_vector.append(initial_vector[i] - travel_vector[i])
        
        return result_vector
    
class DrawVectorSub:
    def __init__(self) -> None:
        pass
    
    def draw(self, initial_vector: list[int], travel_vector: list[int]):
        initial_vector = initial_vector
        travel_vector = travel_vector

        call = VectorSubtraction()
        result = call.Sub(initial_vector, travel_vector)

        plt.figure(figsize=(8, 6))

        plt.plot([0, initial_vector[0]], [0, initial_vector[1]], label='Initial Vector', color='blue')
        plt.plot([initial_vector[0], result[0]], [initial_vector[1], result[1]], label='Travel Vector', color='green')
        plt.plot([0, result[0]], [0, result[1]], label='Result Vector', color='red')

        plt.grid()
        plt.legend()
        plt.show()

        return result