from queue import Queue
class nfa:
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
        if state in self.transitions:
            for transition in self.transitions[state]:
                if letter == transition[1]:
                    self.state_queue.put(transition[0])
    def process_word(self,word,output_file):
        self.previous_state[word]={}
        while not self.state_queue.empty():
            self.state_queue.get()
        self.state_queue.put(self.initial_state)
        for letter in word:
            states_count=self.state_queue.qsize()
            print(word,states_count,letter)
            if states_count == 0:
                output_file.write("NU\n")
                return
            for _ in range(states_count):
                state=self.state_queue.get()
                self.apply_transition(state,letter)
        while not self.state_queue.empty():
            if self.state_queue.get() in self.final_states:
                output_file.write("DA\n")
                return 
        output_file.write("NU\n")
    def process_words(self,output_file_path):
        self.paths={}        
        fout=open(output_file_path,"w")
        self.state_queue=Queue()
        for word in self.words:
            self.process_word(word,fout)

nfa=nfa()
nfa.read_data("./date_nfa.txt")
nfa.parse_transitions()
nfa.process_words("./output_nfa.txt")

#optional se poate apela print_alphabet pt. afisarea alfabetului
