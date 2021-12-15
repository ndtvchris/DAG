class fileReader:

    def __init__(self, infile):
        with open(infile) as file:
            self.start = file.readline().rstrip()
            self.end = file.readline().rstrip()
            self.weights = {}


            for line in file:
                first = line.split('->')
                second = first[1].split(':')
                name = first[0]
                after = second[0]
                weight = int(second[1])

                if name not in self.weights:
                    self.weights[name] = {after : weight}
                else:
                    self.weights[name][after] = weight
