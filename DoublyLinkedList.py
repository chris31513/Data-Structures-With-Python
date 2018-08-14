class DoublyLinkedList(object):

    class Node(object):
        element = None
        previous = None
        next = None

        def __init__(self, element):
            self.element = element

    head = None
    tail = None
    length = 0

    def add(self, element):
        new_node = self.Node(element)

        if (self.length == 0):
            self.head = self.tail = new_node

        else:
            temp = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.tail.previous = temp

        self.length += 1

    def delete(self, element):
        m = self.get_node(element)

        if (m is None):
            return

        if (self.length == 1):
            self.head = self.tail = None

        else:
            if (m == self.head):
                self.head = self.head.next

            elif (m == self.tail):
                t = self.tail.element
                self.tail = self.tail.previous

            else:
                m.previous.next = m.next
                m.next.previous = m.previous
        self.length -= 1


    def get_node(self, element):
        n = self.head

        while (n is not None):
            if (n.element == element):
                return n
            n = n.next

        return None

    def get_index(self, element):
        n = self.head
        i = 0

        while (i < self.length):
            if (n.element == element):
                return i
            n = n.next
            i += 1

        return -1

    def contains(self, element):
        return (self.get_index(element) > -1)

    def clean(self):
        self.head = self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def __nonzero__(self):
        return (self.length > 0)

    def __str__(self):
        if (self.length == 0):
            return '[]'
        n = self.head
        t = self.tail
        str = '['

        while (n is not None and n is not t):
            str += '{}, '.format(n.element)
            n = n.next

        str += '{}]'.format(t.element)

        return str

    def __eq__(self, l):
        if (l.length == self.length):
            m = l.head
            n = self.head
            while (n is not None):
                if (n.element != m.element) or ( (n is not None) and (m is None) ):
                    return False
                n = n.next
                m = m.next
            return True
