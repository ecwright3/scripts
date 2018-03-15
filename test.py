

import argparse
import sys

class Core(object):

       
    def commit(self, args=None):
        parser = argparse.ArgumentParser(
            description ='Record changes to the repository')
        parser.add_argument('-a','--amend',action='store_true') 
        parser.add_argument('-n','--name',nargs='+') 
        args = parser.parse_args(args[1:])
        if args.name == None:
            print('Running git commit, amend=%s, name=None' %(args.amend))
            return
        
        elif len(args.name) > 1:
            fullname = ""
            for n in args.name:
                fullname += n + "-"
            fullname = fullname[:-1]
            
            #fullname = reduce((lambda x: x * y), [1, 2, 3, 4]) 
        else:
            fullname = args.name[0]    
        print('Running git commit, amend=%s, name=%s' %(args.amend, fullname))

if __name__ == '__main__':
    Core()
