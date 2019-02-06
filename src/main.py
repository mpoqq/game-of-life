from ctypes import c_uint
from multiprocessing import Process, Value

import click

from initializer import initialize_from_file, initialize_random
from visualization import visualize_grid
from user_interaction import UserInteraction
from state import State


@click.command()
@click.option(
    '--random_config',
    '-r',
    type=click.FloatRange(0, 1),
    help='Number between 0 and 1. Probability of setting a cell to dead.',
    required=False,
)
@click.option(
    '--number_of_columns',
    '-columns',
    type=click.INT,
    help='Number of grid columns.',
    default=40,
)
@click.option(
    '--number_of_rows',
    '-rows',
    type=click.INT,
    help='Number of grid rows.',
    default=40,
)
@click.option(
    '--config_file',
    type=click.File('r'),
    help='',
    required=False,
)
@click.option(
    '--speed',
    '-s',
    type=click.INT,
    help='Delay between frames in milliseconds.',
    default=200,
)
@click.option(
    '--save',
    default=[None, 50],
    type=click.Tuple([click.STRING, click.INT]),
    help='Argument 1: Filename, Argument 2: frames. '
         'If set, the animation is saved to the file with the amount of frames.',
    required=False,
)
def create_new_board(random_config, number_of_columns, number_of_rows, config_file, speed, save):
    if config_file:
        grid = initialize_from_file(config_file)
    elif random_config:
        prob = random_config
        click.echo("Probability is %f." % prob)
        grid = initialize_random(prob, number_of_columns, number_of_rows)
    else:
        prob = click.prompt("Enter at least random probability:", type=click.FloatRange(0, 1))
        grid = initialize_random(prob, number_of_columns, number_of_rows)
        click.echo("Probability is %f." % float(prob))
    click.echo("Number of grid columns %d " % grid.shape[0])
    click.echo("Number of grid rows %d " % grid.shape[1])
    if save[0] is not None:
        click.echo("Animation will be saved in %s with %d frames." % save)
    # thread shared values
    state = Value(c_uint, State.RUNNING)
    speed = Value(c_uint, speed)
    # start multi process to run the visualization not in the main thread
    visualize_process = Process(target=visualize_grid, args=[grid, speed, state, save])
    visualize_process.start()
    # user interaction has to run in main thread to read user inputs
    user_interaction = UserInteraction(state)
    user_interaction.start()
    visualize_process.join()


if __name__ == '__main__':
    create_new_board()
