import numpy as np
import graph


class MarkovChainModel:

    def __init__(self, transition_matrix, states_names=None):
        """
        The constructor of the class MarkovChainModel needs a transition matrix and optional a name description of the
        states of the Markov chain. The constructor checks if the matrix is square and if the rows of the transition
        matrix add up to one. Additionally it checks, if the length of the states names is equal to the dimension of the
        transition matrix (every state has a name). If no state names are given, their are just enumerated.
        Attrs:
            transition_matrix: a 2d square matrix with rows add up to one
            states_names: name descriptions for every state (optional)
        """
        self.transition_matrix = np.array(transition_matrix)
        if self.transition_matrix.shape[0] != self.transition_matrix.shape[1]:
            raise ValueError("The transition matrix is not square.")
        self.size = self.transition_matrix.shape[0]

        if (np.sum(self.transition_matrix, axis=1) != 1).any():
            raise ValueError("The rows of a transition matrix have to add up to 1.")

        if states_names is not None and len(states_names) != self.size:
            raise ValueError("The states names array does not have the dimension of the transition matrix.")

        if states_names is None:
            self.states_names = list(range(self.size))
        else:
            self.states_names = list(states_names)

    def step_masses(self, masses):
        """
        Given a vector with masses we calculate how the masses are distributed after one step.
        Args:
            masses: a 1d vector with masses
        Returns:
            new_masses: a 1d vector with the masses distributed according to the transition matrix
        """
        return np.matmul(np.transpose(self.transition_matrix), masses)

    def simulate_masses(self, masses, N=1000):
        """
        The function simulate_masses is just a auxiliary function to call step_masses N times. The function saves
        the masses distribution after each step and returns the history.
        Args:
            masses: a 1d vector with the initial mass distribution
            N: number of iterations (default: 1000)
        Returns:
            masses_hist: a list with the mass distribution history
        """
        masses_hist = [masses]
        for i in range(N):
            masses_hist.append(self.step_masses(masses_hist[i]))

        return masses_hist

    def step_point(self, start_location=0):
        """
        The function step_point takes a start location and randomly choice the next destination of the particle
        (probabilites according to the corresponding row of the transition matrix)
        Args:
            start_location: an int (as index) or a string (as location name)
        Returns:
            new_location: an index of the destination location
        """
        # if a string is given we get the index of the start location
        if isinstance(start_location, str):
            start_location = self.states_names.index(start_location)

        return np.random.choice(self.size, 1, p=self.transition_matrix[start_location, :])[0]

    def simulate_point(self, start_location, N=10):
        """
        Similar to simulate_masses we start a location and iterate N times. Then we arrive at our end destination.
        We also save the history to look at the journey of the particle.
        Args:
            start_location: an int (as index) or a string (as location name)
            N: number of iterations (default: 10)
        Returns:
            locations: an array of all the states the point passed
        """
        # if a string is given we get the index of the start location
        if isinstance(start_location, str):
            start_location = self.states_names.index(start_location)

        locations = [start_location]
        for i in range(N):
            locations.append(self.step_point(locations[i]))

        return locations

    def is_irreducible(self):
        """
        A  matrix is irreducible if the directed graph corresponding to the matrix is irreducible. Thus,
        we just wrap the is_irreducible of the Graph class.
        """
        return graph.Graph.construct_from_matrix(self.transition_matrix, vertices=self.states_names).is_irreducible()


if __name__ == "__main__":
    model = MarkovChainModel([[0.3, 0.7], [0.9, 0.1]])
    print(model.simulate_masses([1, 1])[-1])
    print(model.simulate_point(1))
    print(model.is_irreducible())


