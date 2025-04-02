import src.lib.Sim as Sim

def t_data_test(t_Sim):
    pass

def main():
    t_Sim = Sim()
    assert t_data_test(t_Sim) == True, "SimTests.py: Data extraction failed"
    

if __name__ == "__main__":
    main()
