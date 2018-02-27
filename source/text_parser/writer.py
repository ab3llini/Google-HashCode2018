import os


class TextWriter:
    def __init__(self, outfile):
        self.__fileout = outfile
        self.__out = None

    def __enter__(self):
        """
        Called when entering a with context. Opens the output file.
        """
        self.start()
        return self

    def __exit__(self, tp, value, traceback):
        """
        Called when terminating a with context. Closes the output file.
        """
        self.close()

    def close(self):
        self.__out.close()

    def start(self):
        self.__out = open(self.__fileout, 'w')

    def write_line(self, token_list, separator=' ', endline='\n'):
        """
        Write each token in sequence with this format:
        t[0] sep t[1] sep t[2] sep ...  t[N-1] sep t[N] endline
        :param token_list: a list of tokens to write, the written output is the str() of each token
        :param separator: the separator printed between each token. Ignored if None
        :param endline: the end sequence delimiter to use. Ignored if None
        :return:
        """
        for i in range(len(token_list)-1):
            self.__out.write(str(token_list[i]))
            if separator is not None:
                self.__out.write(separator)
        self.__out.write(str(token_list[-1]))
        if endline is not None:
            self.__out.write(endline)

    def write_matrix(self, token_matrix, column_separator=' ', endrow='\n', endmat='\n'):
        """
        Write a matrix in output with this format:
        t[0, 0] csep t[0, 1] csep ... t[0, N] endr
        t[1, 0] csep t[1, 1] csep ... t[1, N] endr
        ...
        t[M, 0] csep t[M, 1] csep ... t[M, N] endmat

        :param token_matrix: the matrix of tokens to write down. The output is the str() of each token
        :param column_separator: the separator char between columns. Ignored if None.
        :param endrow: the separator char at the end of a row. Ignored if None.
        :param endmat: the char at the end of the matrix. Ignored if None.
        :return:
        """
        for i in range(len(token_matrix)-1):
            self.write_line(token_matrix[i], separator=column_separator, endline=endrow)
        self.write_line(token_matrix[-1], separator=column_separator, endline=endmat)

