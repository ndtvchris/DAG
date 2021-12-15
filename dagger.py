from fileReader import fileReader
from node import node


class dagger:

    def __init__(self, infile):
        self.fr = fileReader(infile)  # this has start, end, list of names, dict of weights
        self.nodeDict = {}  # simply holds all the nodes
        self.nodeOrder = []  # for topo ordering
        for key in self.fr.weights:  # for all the keys in the weight dict, make nodes
            holdNode = node(key)  # key becomes the name
            self.nodeDict[key] = holdNode
        for n in self.nodeDict:  # for every key corresponding to a node
            holdNode = self.nodeDict[n]

            for nextNode in self.fr.weights[holdNode.name]:  # for every 'next' the node has
                holdNode.nextList.append(nextNode)

        self.nodeDict[self.fr.start].value = 0  # initializes value of start node to 0

    def makeTopo(self):
        pNode = self.fr.start  # holds key of first node
        goBack = ''  # holds value of previous node
        finished = False

        # self.nodeDict[pNode].visit = True  # visit to node complete
        while not finished:  # this should check if every node has been visited or not
            if len(self.nodeDict[pNode].nextList) == 0:  # if it has no next node, it doesn't go anywhere
                #self.nodeDict[pNode].visit = True  # so, it's been visited
                pNode = self.nodeDict[pNode].fromMax  # so, goes backwards to choose another pNode
            else:  # otherwise next nodes exist, so go through them
                pNode = self.nodeDict[pNode]  # now, pNode points to the node object sharing its name
                #pNode.visit = True  # we are in the node now, so it's visited
                aVal = pNode.value  # holds value of the parent node
                for nextNode in pNode.nextList:  # looks through each next node
                    if nextNode not in self.nodeDict:  # if the node doesn't exist, make it, set the value.
                        self.nodeDict[nextNode] = node(nextNode)  # can treat as visited, will never go anywhere
                        pNode.visit.append(nextNode) # adds the node to the 'visited' list as to not go there again
                        pathVal = self.fr.weights[pNode.name][nextNode]
                        self.nodeDict[nextNode].value = aVal + pathVal  # sets value
                        self.nodeDict[nextNode].fromMax = pNode.name  # stores from where the value was given
                    #elif self.nodeDict[nextNode].visit:  # if it's been visited already, go
                        #continue
                    elif nextNode in pNode.visit:  #  if the node has been visited, skip over it
                        continue
                    else:  # otherwise, it already exists and hasn't been visited
                        pNode.visit.append(nextNode)  # puts in visits list
                        pathVal = self.fr.weights[pNode.name][nextNode]  # value of path's weight
                        if aVal + pathVal > self.nodeDict[nextNode].value:  # if the new value is larger, set it
                            self.nodeDict[nextNode].value = aVal + pathVal
                            self.nodeDict[nextNode].fromMax = pNode.name  # also, make note of where it's from
                            #  also, if the value has been updated, blast the visit list to re-visit all the nodes
                            self.nodeDict[nextNode].visit.clear()
                        else:  # if not, move on
                            continue
                #  this for loop is to see if there are any branching nodes that have their own branches to visit
                for x in pNode.nextList:
                    # if the nextnode has branches and hasn't visited them, go to that node and visit
                    if len(self.nodeDict[x].nextList) != 0 and len(self.nodeDict[x].visit) < len(self.nodeDict[x].nextList):
                        goBack = x  # sets the new pNode
                        break
                    else: # otherwise, go backwards
                        goBack = pNode.fromMax
                pNode = goBack

            if goBack == '':
                finished = True
        print()



    def backTrace(self):
        done = False
        realOrder = ''
        pathsReversed = []
        beginning = self.fr.end
        finalWeight = self.nodeDict[beginning].value
        pointer = beginning  # start at the end and go back using fromMax
        while not done:
            if pointer == '':
                done = True
            else:
                pathsReversed.append(pointer)  # add the node to the list
                pointer = self.nodeDict[pointer].fromMax  # update pointer
        for x in pathsReversed[::-1]:
            realOrder += x + '->'
        for key in self.nodeDict:
            print(self.nodeDict[key].name)
            print(self.nodeDict[key].value)
            print(self.nodeDict[key].fromMax)
            print('\n')
        with open('DAGout.txt', 'w') as out:
            out.write(str(finalWeight) + '\n')
            out.write(realOrder[0:-2])



