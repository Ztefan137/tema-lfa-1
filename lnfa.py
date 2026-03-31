from queue import Queue
class l_nfa:
    def __init__(self):
        pass
    def read_data(self,path):
        fin=open(path,"r")
        self.N=int(fin.readline())
        self.states=[stare.strip() for stare in fin.readline().split()]
        self.M=int(fin.readline())
        self.read_transitions=[fin.readline().strip() for _ in range(self.M)]
        self.initial_state=fin.readline().strip()
        self.final_states_count=int(fin.readline())
        self.final_states=[stare.strip() for stare in fin.readline().split()]
        self.word_count=int(fin.readline())
        self.words=[fin.readline().strip() for _ in range(self.word_count)]
    def parse_transitions(self):
        self.transitions={}
        self.alphabet=set()
        for transition in self.read_transitions:
            if transition.split(" ")[0] not in self.transitions:
                self.transitions[transition.split(" ")[0]]=[]
            self.transitions[transition.split(" ")[0]].append((transition.split(" ")[1],transition.split(" ")[2]))
            self.alphabet.add(transition.split(" ")[2])
    def print_alphabet(self):
        print(self.alphabet)
    def apply_transition(self,state,letter):
        if letter == "lambda":
            self.visited[state]=1
        if state in self.transitions:
            for transition in self.transitions[state]:
                if letter == transition[1]:
                    self.state_queue.put(transition[0])
                    if letter == "lambda":
                        if self.visited[transition[0]] == 0:
                            self.apply_transition(transition[0],"lambda")
    def process_word(self,word,output_file):
        self.visited={}
        while not self.state_queue.empty():
            self.state_queue.get()
        self.state_queue.put(self.initial_state)
        for i in range(self.N):
            self.visited[self.states[i]]=0   
        self.apply_transition(self.initial_state,"lambda")
        for letter in word:
            states_count=self.state_queue.qsize()
            print(word,states_count,letter)
            if states_count == 0:
                output_file.write("NU\n")
                return
            for _ in range(states_count):
                state=self.state_queue.get()
                self.apply_transition(state,letter)
            states_count=self.state_queue.qsize()
            for _ in range(states_count):
                state=self.state_queue.get()
                self.state_queue.put(state)
                for i in range(self.N):
                    self.visited[self.states[i]]=0     
                self.apply_transition(state,"lambda")
        while not self.state_queue.empty():
            if self.state_queue.get() in self.final_states:
                output_file.write("DA\n")
                return
        output_file.write("NU\n")
    def process_words(self,output_file_path):
        fout=open(output_file_path,"w")
        self.state_queue=Queue()
        for word in self.words:
            self.process_word(word,fout)


l_nfa=l_nfa()
l_nfa.read_data("./date_lnfa.txt")
l_nfa.parse_transitions()
l_nfa.process_words("./output_lnfa.txt")

#optional se poate apela print_alphabet pt. afisarea alfabetului
