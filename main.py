import warnings
from datasets import load_dataset
import pandas as pd

# Ignore all warnings
warnings.filterwarnings("ignore")

# Function to load the dataset and convert it to a pandas DataFrame
def load_and_prepare_data():
    # Load the dataset
    dataset = load_dataset("fka/awesome-chatgpt-prompts")

    # Convert the training dataset to a pandas DataFrame
    df = pd.DataFrame(dataset['train'])
    return df

# Function to display available acts and prompt the user to select one
def get_user_selected_act(df):
    # Display the unique acts in the dataset
    print("Available acts in the dataset:")
    print(df['act'].unique())
    print("\n")

    # Prompt the user to select an act
    selected_act = input("Please select an act from the above list: ")
    return selected_act

# Function to print prompts for the selected act
def display_prompts_for_act(df, selected_act):
    # Filter the DataFrame based on the selected act
    filtered_prompts = df[df['act'] == selected_act]['prompt']

    print("\nPrompts for the selected act:")
    for prompt in filtered_prompts:
        print(prompt)

# Main function to orchestrate the operations
def main():
    df = load_and_prepare_data()
    selected_act = get_user_selected_act(df)
    display_prompts_for_act(df, selected_act)

if __name__ == "__main__":
    main()
