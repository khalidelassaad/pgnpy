class PgnConverter():
"""
The main converter class from *.pgn into other filetypes
The conversion is done thru a dynamic datastore per instance
This converter should handle *.pgn downloads from different
websites and into different outputs. Initial plan is pgn->csv
"""
    def __init__(self):
        self.infile = None
        self.outfile = None
        self.datacolumns = [] #The first row of the csv
        self.datareference = dict() #D[column] = position in datacolumns
        self.data = [] #This will be a nested list where each sublist is the data in that column
                       #NOTE: This

    def _load_lichess_pgn:
        #takes lichess *.pgn and loads the column names and data


    def load_input_pgn(self, path:str):
        #Open a *.pgn file from the filepath
        self.file = open(path,"r")
        return
