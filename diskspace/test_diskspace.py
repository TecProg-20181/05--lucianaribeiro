import unittest
import os
import subprocess
from diskspace import *

class TestDiskspace(unittest.TestCase):

    def setUp(self):
        pass
    
    def test_subprocess_check_output(self):
        abs_directory = os.path.abspath('')
        cmd = 'du -d 1 .'

        subprocess_return = subprocess.check_output(cmd.strip().split(' '))
        diskspace_check_output_return = diskspace.subprocess_check_output(cmd)

        self.assertEqual(subprocess_return, diskspace_check_output_return)
    
    def test_bytes_to_readable(self):
        cmd = bytes_to_readable(512)
        self.assertEqual(cmd, '256.00Kb')
        self.assertNotEqual(cmd, '512.00Kb')
    
    def test_bytes_to_readable_wrong(self):
        blocks = 100
        self.assertNotEqual(bytes_to_readable(blocks), "512.00Kb")

