'''
Created on Oct 26, 2016 10:51:59 PM

@author: Pati Ram Yadav

@Path: C:\JavaDev\Eclipse Mars.2 (4.5.2)\plugins\org.python.pydev_5.2.0.201608171824\pysrc\pydevd.py

@Module: context_managers.test_implementating_own_contextmanager

'''

import unittest
import shutil, tempfile
from os import path
from context_managers.implementating_own_contextmanager import File

class ContextManagerFileReadTEST(unittest.TestCase):
    """Test for open anonymous file"""
    
    def test_file_not_found(self):
        with File("a.txt", "w") as f:
            self.assertRaises(IOError, f.read())  # Here is error 

        # Create a file in the temporary directory
        f = File(path.join(self.test_dir, 'test.txt'), 'w')
        # Write something to it
        f.write('The owls are not what they seem')
        # Reopen the file and check if what we read back is the same
        f = File(path.join(self.test_dir, 'test.txt'))
        self.assertEqual(f.read(), 'The owls are not what they seem')
        
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)
        
    def test_file_found_and_readline(self):
        temp = path.join(self.test_dir, 'test.txt')
        f = File(temp, 'w')
        f.write('pati ram yadav')
        with File(temp) as f:
            self.assertEqual(f.read(), 'pati ram yadav')
                 


if __name__ == '__main__':
    unittest.main()
