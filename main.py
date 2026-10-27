import os

from input_module import get_blog_details
from blog_module import generate_blog
from title_module import generate_titles
from keyword_module import generate_keywords
from summary_module import generate_summary
from meta_module import generate_meta_description
from intent_module import detect_intent


def save_blog(blog):
    os.makedirs("outputs", exist_ok=True)

    with open("outputs/generated_blog.txt", "w", encoding="utf-8") as file:
        file.write(blog)

    print("\nBlog saved successfully!")
    print("Location: outputs/generated_blog.txt")


def main():

    blog = ""

    while True:

        print("\n========================================")
        print("       AI BLOG CONTENT GENERATOR")
        print("========================================")

        print("1. Generate Blog")
        print("2. Generate Titles")
        print("3. Generate Keywords")
        print("4. Generate Summary")
        print("5. Generate Meta Description")
        print("6. Detect Intent")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        # Generate Blog
        if choice == "1":

            topic, style, tone, word_count = get_blog_details()

            blog = generate_blog(
                topic,
                style,
                tone,
                word_count
            )

            save_blog(blog)

        # Generate Titles
        elif choice == "2":

            topic = input("\nEnter Blog Topic: ")

            print("\nSuggested Titles")
            print("----------------------------------------")

            titles = generate_titles(topic)

            print(titles)

        # Generate Keywords
        elif choice == "3":

            if blog == "":
                print("\nPlease generate a blog first.")
            else:
                print("\nSEO Keywords")
                print("----------------------------------------")

                keywords = generate_keywords(blog)

                print(keywords)

        # Generate Summary
        elif choice == "4":

            if blog == "":
                print("\nPlease generate a blog first.")
            else:
                print("\nSummary")
                print("----------------------------------------")

                summary = generate_summary(blog)

                print(summary)

        # Generate Meta Description
        elif choice == "5":

            if blog == "":
                print("\nPlease generate a blog first.")
            else:
                print("\nMeta Description")
                print("----------------------------------------")

                meta = generate_meta_description(blog)

                print(meta)

        # Intent Detection
        elif choice == "6":

            user_input = input("\nEnter your request: ")

            intent = detect_intent(user_input)

            print("\nDetected Intent:")
            print(intent)

        # Exit
        elif choice == "7":

            print("\nThank you for using AI Blog Content Generator!")
            break

        else:

            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()