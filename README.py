from main import app
import os

def generate_readme():
    if os.path.exists("README.txt"):
        os.remove("README.txt")

    # Start building the README content
    readme_content = "API Endpoints Documentation\n"
    readme_content += "documentation http://127.0.0.1:8000/docs \n"
    readme_content += "-----------------------------------------------------------------\n"

    # Add each route's path to the README content
    for route in app.routes:
        readme_content += f"Endpoint: {route.path}\n"

    # Write the content to README.txt
    with open("README.txt", "w") as f:
        f.write(readme_content)

    print("aaaaaaaaaaaaa")

if __name__ == "__main__":
    generate_readme()