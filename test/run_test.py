import imp
import os
import sys
import unittest
base_dir = os.path.join(os.getcwd(), '..')
sys.path.append(base_dir)



if __name__ == '__main__':
    script = sys.argv[1]
    path = os.path.join(os.getcwd(), script)
    imp.load_source('test_module', path)
    unittest.main()