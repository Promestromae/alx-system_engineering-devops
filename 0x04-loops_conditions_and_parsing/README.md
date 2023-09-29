0. Create a SSH RSA key pair
inside your directory you can generate your private and public key using ssh-keygen -t rsa

1. For Best School loop,
2. While Best School loop
Initialize variable 'a' with the value 1
The while loop checks the condition [ $a -le 10 ], which means "while 'a' is less than or equal to 10."
As long as the condition is true, the loop body will execute.
In the loop body, the string "Best School" is printed using the echo command.
After printing, the value of a is incremented by 1 using the ((a++)) expression.
The loop goes back to the beginning, checks the condition again, and repeats the process until the condition becomes false (when 'a' exceeds 10).
3. Until Best School loop
4. If 9, say Hi!
when you run this bash script, it will print "Best School" ten times, and on the ninth iteration, it will print "Hi" as well. Each output will be on separate lines.

5. 4 bad luck, 8 is your chance
Each output will be on separate lines, and "bad luck" will be printed when the loop iterates with counter equal to 3, and "good luck" will be printed when counter is 7.

6. Superstitious numbers
when you run this bash script, it will print the numbers from 1 to 20, and for the values 4, 9, and 17, it will print additional lines with the corresponding "bad luck" messages from China, Japan, and Italy, respectively. Each output will be on separate lines.

7. Clock
when you run this script it dispalys time in hours and miniutesin between all in seperate lines

8. For ls
The cut command in Unix/Linux is used to extract sections of each line from a file or standard input (stdin) based on specified delimiter(s) or character positions.

- Here's the breakdown of the cut -d '-' -f2 command:
cut: This is the command itself, used for cutting sections from input lines.

-d '-': This option specifies the delimiter used to separate fields in each input line. In this case, the delimiter is set to the hyphen ('-'). This means that the cut command will treat the hyphen character as a separator, and it will split each line into fields based on hyphens.

-f2: This option specifies the field number to be extracted from each line. The number after -f represents the field number. In this case, it is set to 2, which means the command will extract the second field from each line after splitting using the hyphen as the delimiter.

9. To file, or not to file
The outer if statement [ -e "school" ] checks if the file named "school" exists in the current directory. Then, it checks if the file is not empty using the -s operator. Next, it checks if the file is a regular file (not a directory or a special file) using the -f operator. If the file "school" does not exist (outer if condition is false), the code inside the else block will execute.

10. FizzBuzz
when you run this bash script, it will print the FizzBuzz sequence for the numbers from 1 to 100, following the FizzBuzz rules.
