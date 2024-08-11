import threading

class Inits:
    def __init__(self):
        self._init_functions = []
        self._register_init_function(self.activateDestruct)

    def _register_init_function(self, func):
        """Register an initialization function."""
        self._init_functions.append(func)

    def activateDestruct(self, func):
        """Activate the self-destruct timer for the given function."""
        if hasattr(func, 'self_destruct'):
            func.timer = threading.Timer(func.timeout, func.self_destruct)
        else:
            raise ValueError(
                "Provided function does not have a self-destruct mechanism.")

    def runAll(self):
        """Run all registered initialization functions."""
        for func in self._init_functions:
            func()
