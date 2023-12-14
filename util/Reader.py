
class LineParser:
    def parseLines(filename):
        result = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                result.append(line.strip())

        return result