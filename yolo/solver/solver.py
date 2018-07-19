class Solver(object):
    """
    Solver Abstract class
    """

    def __init__(self, dataset, net, common_params, solver_params):
        """
        TODO: Remove this Java abomination
        :param dataset:
        :param net:
        :param common_params:
        :param solver_params:
        """
        raise NotImplementedError

    def solve(self):
        raise NotImplementedError
