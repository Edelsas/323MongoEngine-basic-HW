class Menu:
    """
    Each Menu instance represents a list of options. Each option is just
    a prompt, and an action (text string) to take if that option is selected.
    Each prompt has exactly one corresponding action. The text of the action
    is returned, with the expectation that the calling routine will use the
    Python exec function to perform the user-selected action.
    """
    def __init__(self, name: str, prompt: str, options: [(str, str)]):
        # A descriptive name of the menu. No uniqueness is enforced.
        self.name = name
        # The prompt to show at the top of the menu each time it is displayed.
        self.prompt = prompt
        # The list of tuples, where each tuple is (option text, action text).
        self.options = options

    def menu_prompt(self) -> str:
        """
        Display the available options and their results and prompt the user for which
        option they will take.
        :return: The text to be executed in the calling function.
        """
        results = False                   # Flag to show if we are done
        final = -1                        # The chosen option
        n_options = len(self.options)     # Find the total number of options
        while not results:                # Loop until user makes a valid entry
            print(self.prompt)            # Display the menu prompt
            for index, (option_text, _) in enumerate(self.options, start=1):  # Show the list of options
                print(f"{index} - {option_text}")
            try:                          # Protect from non-integer input
                final = int(input('--> '))
                if final < 1 or final > n_options:  # Protect from out-of-range input
                    print("Choice is out of range, try again.")
                    results = False
                else:
                    results = True
            except ValueError:
                print("Not a valid integer, try again.")
        return self.options[final - 1][1]  # Return the action for the chosen option

    def last_action(self):
        """
        Find the last action in the menu. By convention, this is the
        option that exits from this menu. It does not have to be literally
        "exit", it could be any operation, including "pass". But it
        signifies that the user has elected to quit. At least so goes
        the normal convention.
        :return: The text of the very last action in the options list.
        """
        return self.options[-1][1]
