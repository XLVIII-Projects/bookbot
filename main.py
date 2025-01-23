def main():
    with open("books/frankenstein.txt") as f:
        # Count the number of words in the file
        file_contents = f.read()
        words = file_contents.split()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"Number of words found in the document: {len(words)}")

        # Make dictionary of characters in the file
        count_characters = {}
        for char in file_contents:
            char = char.lower()
            if char.isalpha():
                if char in count_characters:
                    count_characters[char] += 1
                else:
                    count_characters[char] = 1

        # Make list of dictionary
        output_list = []
        for count in count_characters:
            output_list.append({"char": count, "count": count_characters[count]})
            # output_list.append(f"The '{count}' character was found {count_characters[count]} times")

        # Sort the output list based on the counts
        output_list.sort(key=lambda x: x["count"], reverse=True)
        # output_list.sort(key=lambda x: int(x.split()[-2]), reverse=True)

        # Print the list of dictionary
        for item in output_list:
            output_string = f"The '{item['char']}' character was found {item['count']} times"
            print(output_string)
        print("--- End report ---")

if __name__ == "__main__":
    main()