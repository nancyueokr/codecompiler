import os
import subprocess

class CodeCompiler:
    def __init__(self, script_path):
        self.script_path = script_path

    def compile_and_run(self):
        if not os.path.exists(self.script_path):
            print(f"Error: The script {self.script_path} does not exist.")
            return

        script_extension = os.path.splitext(self.script_path)[1].lower()

        if script_extension == '.py':
            self.run_python_script()
        elif script_extension == '.java':
            self.compile_and_run_java()
        elif script_extension == '.cpp':
            self.compile_and_run_cpp()
        else:
            print(f"Error: Unsupported script type {script_extension}")

    def run_python_script(self):
        try:
            print(f"Running Python script: {self.script_path}")
            subprocess.run(['python', self.script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to run Python script: {e}")

    def compile_and_run_java(self):
        try:
            print(f"Compiling Java file: {self.script_path}")
            subprocess.run(['javac', self.script_path], check=True)
            class_file = os.path.splitext(self.script_path)[0]
            print(f"Running Java class: {class_file}")
            subprocess.run(['java', class_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to compile or run Java file: {e}")

    def compile_and_run_cpp(self):
        try:
            output_file = os.path.splitext(self.script_path)[0] + '.exe'
            print(f"Compiling C++ file: {self.script_path}")
            subprocess.run(['g++', self.script_path, '-o', output_file], check=True)
            print(f"Running C++ executable: {output_file}")
            subprocess.run([output_file], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to compile or run C++ file: {e}")

if __name__ == "__main__":
    script_path = input("Enter the path to your script: ")
    compiler = CodeCompiler(script_path)
    compiler.compile_and_run()