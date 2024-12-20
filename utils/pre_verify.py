from env import Env


def pre_verify():
    if Env.MIN_HOLD < 1:
        raise ValueError("MIN_HOLD must be greater than 0")

    if Env.MAX_HOLD > 10 or Env.MAX_HOLD < Env.MIN_HOLD:
        raise ValueError("MAX_HOLD must be between 1 and 10")
