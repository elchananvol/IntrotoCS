import itertools
class Node:
    def __init__(self, data, positive_child=None, negative_child=None):
        self.data = data
        self.positive_child = positive_child
        self.negative_child = negative_child
        self.options = []

    def check_leaf(self):
        """
        check if the node is leaf
        :return: true if leaf ,else false
        """
        if self.positive_child:
            return False
        return True

    def get_sons(self):
        """
        :return: the two next node in the tree
        """
        return self.positive_child, self.negative_child


class Record:
    def __init__(self, illness, symptoms):
        self.illness = illness
        self.symptoms = symptoms


def parse_data(filepath):
    with open(filepath) as data_file:
        records = []
        for line in data_file:
            words = line.strip().split()
            records.append(Record(words[0], words[1:]))
        return records


class Diagnoser:
    def __init__(self, root):
        self.root = root

    def diagnose(self,symptoms):
        """
        :param symptoms is list of strings that contain all symptoms
        :return the data on leaf (disease) that have all symptoms
        """
        node = self.root
        while not node.check_leaf():

            if node.data in symptoms:
                node = node.positive_child
            else:
                node = node.negative_child
        return node.data

    def calculate_success_rate(self, records):
        """
        :param records: list of record objects
        :return: average of success the tree to find the right disease per records
        """
        counter = 0
        for record in records:
            if self.diagnose(record.symptoms) == record.illness:
                counter += 1
        if counter == 0:
            return counter
        return counter / len(records)

    def all_illnesses(self):
        """

        :return: all data on leaves
        """
        lst = self.get_all_leaves(self.root)
        lst = sorted(lst, key=lambda x: lst.count(x), reverse=True)
        lst = list(dict.fromkeys(lst))
        if None in lst:
            lst.remove(None)
        return lst

    def get_all_leaves(self, node, need_data=True):
        """

        :param node: object of Node
        :param need_data: bool value. if need data on leaves true , if need node self False. default true
        :return all data on leaves or the leaves themselves according the need_data
        """
        lst = []
        if node.check_leaf():
            if need_data:
                lst.append(node.data)
            else:
                lst.append(node)
        for son in node.get_sons():
            if son:
                lst += self.get_all_leaves(son, need_data)
        return lst

    def paths_to_illness(self, illness):
        """

        :param illness: name of illness
        :return: the paths to illness
        """
        paths_to_illness = []
        self.paths_to_illness_helper(illness, self.root, [], paths_to_illness)
        return paths_to_illness

    def paths_to_illness_helper(self, illness, node, lst, paths_to_illness):
        if node:
            right_son, left_son = node.get_sons()
            if not right_son:
                if node.data == illness:
                    paths_to_illness.append(lst[:])
            self.paths_to_illness_helper(illness, right_son, lst + [True], paths_to_illness)
            self.paths_to_illness_helper(illness, left_son, lst + [False], paths_to_illness)


def build_tree(records, symptoms):
    """

    :param records: list of record objects
    :param symptoms: list of symptoms
    :return: root of binary tree that ask for any symptom and return the right illness according the records
    """
    root = build_tree_helper(symptoms)
    diagnoser = Diagnoser(root)
    for record in records:
        diagnose(record.illness, record.symptoms, root)
    for node in diagnoser.get_all_leaves(root, False):
        node.options = sorted(node.options, key=lambda x: node.options.count(x), reverse=True)
        node.options = list(dict.fromkeys(node.options))
        if node.options:
            node.data = node.options[0]
    return root


def build_tree_helper(symptoms):
    """

    :param symptoms: list of symptoms
    :return: binary tree that ask for symptoms
    """
    if not symptoms:
        return Node(None)
    root = Node(symptoms[0], build_tree_helper(symptoms[1:]), build_tree_helper(symptoms[1:]))
    return root


def diagnose(illness, symptoms, root):
    """
    this faction check for the illness if it can writen on leaf.data and append to leaf options
    :param illness: name of illness
    :param symptoms: list of symptoms
    :param root: root
    """
    node = root
    while not node.check_leaf():
        if node.data in symptoms:
            node = node.positive_child
        else:
            node = node.negative_child
    node.options.append(illness)




def optimal_tree(records, symptoms, depth):
    """
    the faction build tree for any option of symptoms in and choose the best of the trees
    :param records: records: list of record objects
    :param symptoms: list of symptoms
    :param depth: depth of the tree
    :return: root of best tree
    """
    final_success, final_root = 0,0
    for i in itertools.combinations(symptoms, depth):
        root = build_tree(records, list(i))
        diagnoser = Diagnoser(root)
        success = diagnoser.calculate_success_rate(records)
        if success > final_success:
            final_success = success
            final_root = root
    return final_root
