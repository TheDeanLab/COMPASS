import os
import unittest
import subprocess
import os


class TestDocs(unittest.TestCase):
    def test_sphinx_linkcheck(self):
        os.chdir(os.path.join(os.getcwd(), 'docs'))
        print("Current Directory:", os.getcwd())
        print("Files in Directory:", os.listdir("."))
        cmd = [
            "make",
            "linkcheck",
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        # Log the output to see which links are failing.
        print(result.stdout)
        print(result.stderr)
        assert result.returncode == 0, "Broken links found in Sphinx documentation!"


if __name__ == '__main__':
    unittest.main()
