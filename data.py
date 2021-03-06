# -*- coding: utf-8 -*-

# Throughout this file, remember to use {{ in place of { and }} in place of }, as all strings here will be treated with .format().

# Introductory message, sent when a user first joins. {0} will be replaced by the bot prefix.
msg = """
Welcome to hacked.!
This is a Discord Bot to teach people how to program.
You do so by finishing levels with tasks.
Type `{0}start` to start (you figured it out)
Type `{0}task` to view your current task
Type `{0}solve` to solve your current task in a code-style.

The codeblocks here use JavaScript syntax highlight because that's the most similar to Mamba, the coding language used by this bot.
Of course, any other highlight works, but it may not be as accurate.

e.g.
```
{0}solve
\u200b`\u200b`\u200b`js
say("Hello World!");
\u200b`\u200b`\u200b`
```

Every task has an input (in code referenced to as simply `input` and you have to generate output by making a variable called output.
Example:
This code has the task to return the first letter of the input.
```
{0}solve
\u200b`\u200b`\u200b`js
say(input); // just to see what the input is, you can skip this
output = input[0]; // the first letter is the output now and it will be tested against a few values!
\u200b`\u200b`\u200b`
```

You can always use `{0}run` to try out code outside from `{0}solve`.
"""

# Tasks, in a giant dictionary
# For checks, remember that arrays are outputted as strings from the checker. Therefore, expect string outputs for these data types.
# The format for names is just integers, and key values are ["task name", "description", [array of arrays of check inputs and expected outputs]]
tasks = {
    1: [
        "Variables",
        """
Let's get started. At the end of every line not ending with a `{{` or `}}`, add a `;`.
Assign variables by using `variableName = variableValue;`.
Variables are like a placeholder for something, they hold the value assigned until you change it.
Your first task is to make our `output` variable 1. That's it!
Type `{0}solve {{your code in a code block}}` to solve the task!
        """,
        [[0, 1], [1, 1], [2, 1]],  # data to test it against (in, out)
    ],
    2: [
        "Booleans",
        """
Well done! Now, there are some data types you should know.
First of all, the boolean.
Booleans are either `true` or `false`.
You can either do `a = true;` or compare using `>, >=, <, <=, ==, !=`.

`>`: Greater than (`a > b`)
`>=`: Greater than or equal (`a >= b`)
`<`: Smaller than (`a < b`)
`<=`: Smaller than or equal (`a <= b`))
`==`: Equals (`a == b`)
`!=`: Unequal (`a != b`)

This means you can do
`a = 2 > 1;`
and a will be true.

Your task is to make `output` show whether `input` is equal to 1 or not.
        """,
        [[0, False], [1, True], [2, False]],
    ],
    3: [
        "Integers and floats",
        """
Good job! The next data types are the integer and the float.
Integers are normal numbers like 0, 1, -3 or 501239201849231849320.
Floats are floating-point numbers like 0.5, 3.3335 or -7.801.

They support maths!
`5 / 2` is 2.5
`5 * 3` is 15
`20 + 34` is 54
`2 - 80` is -78
`2 ** 3` is 8 (it is the times operator, equals 2 * 2 * 2)

Make the `output` be the square of `input`, that divided by 2 and then plus 1/4 of `input`.
        """,
        [[-10, 47.5], [0, 0.0], [3, 5.25], [5, 13.75]],
    ],
    4: [
        "Strings",
        """
Very well done! The next data type is the string.
Strings are any characters, meaning text essentially..
You can put strings in `"my text"` (double quotes) or `'my text'` (single quotes), it's down to personal preferences.
Just make sure you use the same quotes for the beginning and end of a string (don't mix and match).

They can also be formatted, that will come later on.
For now, they also support additive arithmetic, or basic math operations like multiplication or addition.
`"hi" * 5` is `"hihihihihi"`
`"hi " + "how are you?"` is `"hi how are you?"`
They do not support `-` or `/`.

Your goal is to make output repeat the input text 4 times and add a `!` to the end.
        """,
        [
            ["'Nani'", "NaniNaniNaniNani!"],
            ["'Aloha!'", "Aloha!Aloha!Aloha!Aloha!!"],
            ["'Hacked.'", "Hacked.Hacked.Hacked.Hacked.!"],
        ],
    ],
    5: [
        "Arrays - 1",
        """
Awesome! The new data type introduced here is the array. It has many functions, so there will be several tasks to follow about it.
Arrays are a kind of list - they can hold any number of items.
Arrays themselves can hold anything - even more arrays!
They are notated like this:
`myArray = [1, 2, 3, 4, 5, 6, "7th item"];`
`myArray2 = [[1, 2, 3, 4], ["a second array in the array", "yes nice, isn't it?"]];`

You can append anything to the end of an array by using `array_push(array, item);`.
```js
array = [];
array_push(array, 1);
say(array); // is [1]
```

Your task is to make an array that consists of 3 sub-arrays. Each sub-array should contain two elements, both of which are the input.
If you can, try to use `array_push`, but it is possible without.
        """,
        [
            [
                "'A String'",
                "[['A String', 'A String'], ['A String', 'A String'], ['A String', 'A String']]",
            ],
            [100, "[[100, 100], [100, 100], [100, 100]]"],
            [[1], "[[[1], [1]], [[1], [1]], [[1], [1]]]"],
        ],
    ],
    6: [
        "Arrays - 2",
        """
Great job! Arrays feature even more!
You can select specific items, insert items at a specific point and remove items at a specific point.
Array items have a sorting, meaning the first item can be referenced as 0, the second as 1, the third as 2, and so on.
The last item can be referenced as -1, the second last as -2, etc.

The `[index]` determines that you want the specific item from the array at the index. (This even works with strings!)

```js
array = [1, 2, 3, 4, 5];
say(array[0]); // 1
say(array[-1]); // 5
string = "Hi Mom!";
say(string[1]); // 'i'
```

You can also append or remove a specific index.
```js
array = [1, 2, 3, 4, 5];
array_remove(array, 4); // remove item 4 (we start counting at 0)
say(array); // [1, 2, 3, 4]
array_insert(array, 2, 2.5); // insert 2.5 at the index 2
say(array); // [1, 2, 2.5, 3, 4]
item = array_pop(array); // this will remove the last item and return it
say(item, array); // 4, [1, 2, 2.5, 3]
```

Your task now is to make `output` be an array. The first element of `output` should be the last element of `input` and the last element of `output` should be the first element of `input`.
Between the first and last item should always be the rest of `input` (without the first and last element) as an array in the array (`[..., [my array], ...]`).
Good luck!
        """,
        [
            [[1, 2, 3, 4], "[4, [2, 3], 1]"],
            [
                ["hi", "owo", "what", "is", "this"],
                "['this', ['owo', 'what', 'is'], 'hi']",
            ],
            [[[1], [1]], "[[1], [], [1]]"],
        ],
    ],
    7: [
        "Arrays - 3",
        """
Nice job! That was quite a hard task, wasn't it?
Arrays can do even more: there is `array_sort(array)`, which will sort the array.
If it's an array of numbers, it will sort them ascending, strings will be sorted alphabetically.
`array_reverse(array)` is self-explanatory.

Your task now is to make `output` the sorted but reversed `input`, but the last item should be replaced by `2019`.
        """,
        [
            [[1, 3, 2, 4], "[4, 3, 2, 2018]"],
            [["b", "c", "d", "e", "a"], "['e', 'd', 'c', 'b', 2018]"],
            [[-1, -2], "[-1, 2018]"],
        ],
    ],
    8: [
        "For loops",
        """
That was nice! We will now be working with the `for` loop. This allows you to repeat a block of code a set amount of times,
or perform an action with each item in an array. An example:

```js
for thing in myArray {{
    say(thing);
}}
```

That code would go though every item in the array myArray, and print it out.
Remember, `thing` can be any variable name and will be the item that is currently being iterated.
After the array has been processed, the code continues running below.
Remember that everything inside the `{{}}` is considered part of the loop, everything else is not.
Now, your task is to take an input, and assign `output` to `input`'s reverse, with each item in the list being doubled.
        """,
        [[[1, 2, 3, 4], "[8, 6, 4, 2]"], [[1.5, 1, 0.5], "[1, 2, 3]"]],
    ],
    9: [
        "For loops - 2",
        """
Great! You learned how to use `for` with arrays. But did you know that you can use `for` to count too?

```js
for number in 1 -> 5 {{
    say(number);
}}
```

This means count up from one to five, and each time you count, set `number` to the number you're on. If you flipped the arrow to `<-`, it would count down.
Your challenge is to count down from `input` to 0, and add up all the numbers along the way. Set that final total to `output`.
        """,
        [[3, 6], [10, 55], [7, 28], [9, 45]],
    ],
}
