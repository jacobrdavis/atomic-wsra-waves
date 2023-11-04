import matplotlib.pyplot as plt
from IPython import get_ipython


def read_stored_variable(variable_name: str):
    """ Read a variable stored by another ipynb instance.

    Read a variable from the current iPython InteractiveShell instance
    using the iPython `store -r`magic command.  The variable is evaluated
    upon return so that the variable is recognized in the development
    environment (e.g., by Pylance in VS code).
    """
    get_ipython().run_line_magic('store', '-r ' + variable_name)
    return eval(variable_name)


def configure_figures():
    plt.rcParams.update({'font.size': 12})
    plt.rcParams["font.family"] = "sans-serif"
    plt.rcParams["font.sans-serif"] = 'Helvetica'
