class PgnConverter():
    """
    WARNING: THIS DOES LOAD THE ENTIRE FILE INTO MEMORY
The main converter class from *.pgn into other filetypes
The conversion is done thru a dynamic datastore per instance
This converter should handle *.pgn downloads from different
websites and into different outputs. Initial plan is pgn->csv
"""
#KEYWORDS
#li - lichess.org
    def __init__(self):
        self.infile = None
        self.outfile = None
        self.datacolumns = [] #The first row of the csv
        self.datareference = dict() #D[column] = position in datacolumns
        self.data = [] #This will be a nested list where each sublist is the data in that column

    def __del__(self):
        if self.infile:
            self.infile.close()
        if self.outfile:
            self.outfile.close()

    def _li_add_column(self,columnname:str):
        #if a name isn't in the reference, add it there and to the datacolumns list
        if not columnname in self.datareference:
            self.datacolumns.append(columnname)
            self.datareference[columnname] = len(self.datacolumns)-1
            self.data.append([])
        return

    def _li_add_datum(self,columnname:str,datum:str):
        if not columnname in self.datareference:
            raise ValueError("columnname '{}' not loaded properly.")
        index = self.datareference[columnname]
        self.data[index].append(datum)
        #print([len(datum) for datum in self.data]) #Used for debugging
        return

    def _li_preload_columns(self):
        #loads all the columns into the self object
        self.infile.seek(0)
        for line in self.infile:
            if line[0] == "[":
                columnname = line.split(" ")[0][1:]
                self._li_add_column(columnname)
            elif "-" in line:
                self._li_add_column("PGN")
        return

    def _li_load_data(self):
        #loads all the data into the self object
        self.infile.seek(0)
        columns = list(self.datacolumns)
        for line in self.infile:
            #check to see which columns are not filled and fill 'em
            if line[0] == "[":
                columnname = line.split(" ")[0][1:]
                datum = line.split("\"")[1]
                self._li_add_datum(columnname, datum)
                if columnname in columns:
                    columns.remove(columnname)
            elif "-" in line:
                self._li_add_datum("PGN", line.strip())
                columns.remove("PGN")
                for leftout in columns:
                    self._li_add_datum(leftout, "")
                columns = list(self.datacolumns)
        return

    def load_input_pgn(self, path:str):
        #Open a *.pgn file from the filepath
        self.infile = open(path,"r")
        return

    def read_lichess_pgn(self):
        #takes lichess *.pgn and loads the column names and data
        #SOURCE: lichess.org
        self._li_preload_columns()
        self._li_load_data()
        return

    def flush_to_csv(self, path:str):
        #Path is a string with the filename and extension of the output CSV
        if not self.data:
            raise ValueError("No data to flush, try loading a file first")
        self.outfile = open(path,"w+")
        self.outfile.write(",".join(self.datacolumns)+"\n")
        for i in range(len(self.data[0])):
            linedata = []
            for j in range(len(self.datacolumns)):
                linedata.append(self.data[j][i])
            self.outfile.write(",".join(linedata)+"\n")
        self.outfile.close()
        return
