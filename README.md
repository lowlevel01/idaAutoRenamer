# idaAutoRenamer
An IDA plugin to rename global variables and functions based on JSON file.

## Main purpose:
I had the API Hashing problem in mind when I wrote this plugin. You could write an x64dbg script to retrieve the addresses and the names and then use this plugin to rename them in IDA.

## How to use:
- Put the plugin in the /plugins folder.
- Click on Edit-> Plugins
- Choose AutoRenamer
- Choose between renaming global variables and functions
- Open the JSON File
- That's it. Check the Output for details.

## Example:
- Let's say we want to rename the global variables at these adresses

  ![json_file](images/json_file.png)

- Choose global variables in the prompt

  ![prompt](images/choices.png)

- The global variables are renamed successfuly

  ![renamed](images/renamed.png)
  
- See the details in the Output window in the bottom

  ![output](images/result.png)

- You can follow the same steps when it goes to renaming functions
