# SWEN331-Fuzzer
A Fuzzer for swen 331

Modules to install:
-Python 2.7.11 (or any 2.7 version)
-pip (to install dependencies)
-mechanize
```shell
pip install mechanize
```
-beautifulsoup4
```shell
pip install beautifulsoup4
```

Preconditions...
  1. In the terminal cd into the projects directory
  2. Enter "python fuzz.py discover -h" to see all available options

Discover:
To run the fuzzer on DVWA:
  1. In step 2 replace [path/file_name] with the path and file name that you wish to use for guessing URLs
  2. Enter "python fuzz.py discover 'http://127.0.0.1/dvwa/' --common-words [path/file_name] --custom-auth 'dvwa'"

To run the fuzzer on bWapp:
  1. In step 2 replace [path/file_name] with the path and file name that you wish to use for guessing URLs
  2. Enter "python fuzz.py discover 'http://127.0.0.1/bWapp/' --common-words [path/file_name] --custom-auth 'bwapp'"

Test:
To run the fuzzer on DVWA:
  1. In step 2 replace the first [path/file_name] with the path and file name containing guesses, replace the
  second[path/file_name] with the path and file name for the technical words list should be newline-delimited.
  2. Enter "python fuzz.py test 'http://127.0.0.1/dvwa/' --custom-auth 'dvwa' --common-words [path/file_name]
            --vectors test/vectors.txt --sensitive [path/file_name] --random True/False --slow Int(milliseconds)"
  3. The following arguments are not required: custom-auth, common-words, random, slow

To run the fuzzer on bWapp:
  1. In step 2 replace the first [path/file_name] with the path and file name containing guesses, replace the
  second[path/file_name] with the path and file name for the technical words list should be newline-delimited.
  2. Enter "python fuzz.py test 'http://127.0.0.1/bWapp/' --custom-auth 'bwapp' --common-words [path/file_name]
            --vectors test/vectors.txt --sensitive [path/file_name] --random True/False --slow Int(milliseconds)"
  3. The following arguments are not required: custom-auth, common-words, random, slow

