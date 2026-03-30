class dfa:
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
    def print_paths(self):
        print(self.paths)
    def apply_transition(self,state,letter):
        for transition in self.transitions[state]:
            if letter == transition[1]:
                self.state=transition[0]
                return True
        return False
    def process_word(self,word,output_file):
        self.paths[word]=[]
        self.state=self.initial_state
        for letter in word:
            if not(self.apply_transition(self.state,letter)):
                output_file.write("NU\n")
                self.paths[word]="Not a valid path"
                return
            self.paths[word].append(self.state)
        if self.state in self.final_states:
            output_file.write("DA\n")
        else:
            self.paths[word]="Not a valid path"
            output_file.write("NU\n")
    def process_words(self,output_file_path):
        fout=open(output_file_path,"w")
        self.state=self.initial_state
        self.paths={}
        for word in self.words:
            self.process_word(word,fout)


dfa=dfa()
dfa.read_data("./date_dfa.txt")
dfa.parse_transitions()
dfa.process_words("./output_dfa.txt")

#optional se poate apela print_alphabet pt. afisarea alfabetului
#optional se poate apela print_paths pt. afisarea drumurilor
dfa.print_paths()