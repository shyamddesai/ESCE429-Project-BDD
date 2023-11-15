import random
import sys

from behave.__main__ import Configuration, Runner, run_behave


class ShuffleRunner(Runner):

    def feature_locations(self):
        locations = super().feature_locations()
        random.shuffle(locations)
        return locations


def main():
    config = Configuration()
    return run_behave(config, runner_class=ShuffleRunner)


if __name__ == '__main__':
    sys.exit(main())
