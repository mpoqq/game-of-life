from state import State
import click


class UserInteraction:

    def __init__(self, state):
        self.state = state
        super(UserInteraction, self).__init__()

    def start(self):
        action = ''
        while action != 's':
            if self.state.value == State.RUNNING or self.state.value == State.PAUSE:
                action = click.prompt("Pause: p, Resume: r, Stepwise: b, Stop: s", type=click.STRING)
                if action == 'p':
                    self.state.value = State.PAUSE
                elif action == 'r':
                    self.state.value = State.RUNNING
                elif action == 'b':
                    self.state.value = State.STEPWISE
                elif action == 's':
                    self.state.value = State.STOP
            elif self.state.value == State.STEPWISE or self.state.value == State.WAIT:
                action = click.prompt("Next step: n, Normal mode: b", type=click.STRING)
                if action == 'n':
                    self.state.value = State.STEPWISE
                elif action == 'b':
                    self.state.value = State.RUNNING
