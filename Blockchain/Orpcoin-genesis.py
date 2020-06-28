import datetime as date


def create_genesis_block():
        # First block to be added maually
        # with index 0 and arbitrary previous hash

        return Block(0, date.datetime.now(), "Genesis Block", "0")