# Uses pgnpy to convert lichess pgn to .csv

import pgnpy

converter = pgnpy.PgnConverter()
converter.load_input_pgn("lichess_HushPuppies_2018-11-16.pgn")
converter.read_lichess_pgn()
converter.flush_to_csv("hushpuppiesOnLichess.csv")