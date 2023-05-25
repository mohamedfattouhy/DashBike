# MANAGE ENVIRONNEMENT
import os


def format_json_files(dir_json_path: str, dir_save_json: str) -> None:

    for filename in os.listdir(dir_json_path):

        if filename.endswith(".json"):

            json_file = os.path.join(dir_json_path, filename)
            with open(json_file, "r+") as f:

                data = f.read()

                data = data.replace("}{", "}\n{")
                data = data.replace("}\n{", "},\n{")
                data = data.replace("} \n{", "},\n{")

                data = [line for line in data.split("\n") if line.strip()]

                # Join the lines into a single string
                data = "\n".join(data)

                data = data.replace("} \n{", "},\n{")
                data = data.replace("}\n{", "},\n{")

                # Return the cursor to the beginning of the file
                f.seek(0)

            file_save_json = os.path.join(dir_save_json, filename)

            with open(file_save_json, "w") as f:
                # Write the modified string to the file
                f.write("[" + data + "]")
                # Truncate the file to remove excess data
                f.truncate()


dir_json_path = os.path.join("..", "data", "raw")
dir_save_json = os.path.join("..", "data", "preprocess")
format_json_files(dir_json_path=dir_json_path, dir_save_json=dir_save_json)
