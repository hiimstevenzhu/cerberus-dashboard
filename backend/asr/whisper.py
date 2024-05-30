import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model", default="medium", help="Model to use", choices=["tiny", "base", "small", "medium", "large"])
    
    