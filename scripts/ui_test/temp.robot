# All keywords, the build-in, external library or you definition, are all capital insensisive

***Settings***
| Documentation  | This is the description for the whole test suite, | 
| ...            | you can also split it into multiple lines, | 
| ...            | and it also support html style, *bold*, _italic_ | 
| metadata       | version | 2.0 | 
| metadata       | author  | me | 
| Library        | library1 | 
| Library        | library2 | arg1 | arg2 |         # You cannot import multiple libraries in one line.
| resource       | resource1 | 
| resource       | resource2 | resource3 |          # You could import multiple resource files in one line.
| variables      | var.py | 
| variables      | var1.py | var2.py |              # You could import multiple variable files in one line.
| Force tags     | tag1 | tag2 |        # Force added tags for all test cases in the suite.
| default tags   | tag3 | tag4 |        # Default added tags if no [tags] defined in test case.
| suite setup    | Run keyword | log | abc |                            # Suite setup/teardown is for the test suite, only run once in the suite.
| suite teardown | Run keywords | keyword1 | keyword2 | keyword3 |      # Run multiple keywords in setup/teardown with 'Run keywords'.
| test setup     | Run keyword | log | abc |                            # Test setup/teardown is default setup/teardown, will be overwriten by [setup]/[teardown] in test case.
| test teardown  | Run keywords | keyword1 | keyword2 | keyword3 |      # Test setup/teardown will run for each test case.
| test template  | keyword | 
| test timeout   | 2min 39s | 

***Variables***
| ${str}     | abc | 
| ${int}     | ${123} |
| @{list}    | a | b | c | 
| &{dict}    | a=a | b=b | c=c | 
| ${var1}    | ${var2} | 

***keywords***
keyword name
|  | [arguments] | ${arg1} | ${arg2} | 
|  | [documentation] | this is the description for the keyword | 
|  | [tags] | tag1 | tag2 | 
|  | [timeout] | 40s | 
|  | [teardown] | keyword | 
|  | log         | ${arg1} | 
|  | log         | ${arg2} | 
|  | [return]    | ${arg2} | 

keyword with different type arguments
|  | [Arguments] | ${mandatory arg} | ${arg with default value}=abc | @{varargs} | &{kw args} | 
|  | log         | ${mandatory arg} |
|  | log         | ${arg with default value} | 
|  | :for        | ${item} | in | @{varargs} |      # for loop 
|  |             | log     | ${item} | 
|  | log         | &{kw args} | 

embedded ${arg1} in keyword name
|  | log | ${arg1} | 
|  | [return] | ${arg1} | 

***test cases***
Test case name
|  | [Documentation] | This is the description for this test case, |  
|  | ...             | you can split it into multiple lines like this. | 
|  | ...             | *This is bold*, _this is italic_ | and here is a link: http://robotframework.org | 
|  | ...             | '...' is the key point. | 
|  | [tags]          | smoke | regression | 
|  | ...             | api | 
|  | [Setup]         | Keyword | arguments | arguments | 
|  | [teardown]      | Keyword | arguments | arguments | 
|  | [template]      | keyword | 
|  | [timeout]       | 1min 40s | 
|  | ${local var}=   | keyword which can return something | args | 

Test case with template
|  | [template] | keyword with two args | 
|  | arg1       | arg2    |  
|  | argg1      | argg2   | 
