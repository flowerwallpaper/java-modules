

# Greeter

<hr/>
<img src="./images/greeter.png"/>

## Goal:

Print a global greeting to the console. Then use input and message dialogs to join Strings and send the user a friendly greeting!

## Steps:

1. Create a new class called Greeter.
2. Add a main method. Eclipse has a helpful shortcut - main
3. Print "Hello World!" to the console. Eclipse has a helpful shortcut - syso
4. Now ask the user for their name. The code looks like this:
```

String input = JOptionPane.showInputDialog("What is your name?");
```
5. Join their name to the end of this greeting. The code looks like this.
```

JOptionPane.showMessageDialog(null,"Hello "+input);
```



