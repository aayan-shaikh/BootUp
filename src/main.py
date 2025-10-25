import subprocess
from functions.create_folders import create_folders
from functions.setup_pkg_manager import setup_pkg_manager
import os
from subprocess import call


def main():
    print("Welcome to BootUp scaffolding project!")
    print("Please enter the name of your project (will be used for folders)")
    project_name = input()
    print(f"DEBUG name: {project_name}")

    print("Choose your package manager [1/2/3]:\n1. npm\n2. pnpm\n3. yarn")
    pkg_manager = input()

    if pkg_manager == "1":
        call(["mkdir", f"{project_name}"])
        call(["mkdir", f"{project_name}/public"])

        call(["mkdir", f"{project_name}/src/"])
        call(["mkdir", f"{project_name}/src/pages/"])

        call(["npm", "init", "--yes"], cwd=project_name)
        call(["npm", "install", "astro"], cwd=project_name)
    elif pkg_manager == "2":
        call(["mkdir", f"{project_name}"])
        call(["mkdir", f"{project_name}/public"])

        call(["mkdir", f"{project_name}/src/"])
        call(["mkdir", f"{project_name}/src/pages/"])

        call(["pnpm", "init"], cwd=project_name)
        call(["pnpm", "add", "astro"], cwd=project_name)

    elif pkg_manager == "3":
        call(["mkdir", f"{project_name}"])
        call(["mkdir", f"{project_name}/public"])

        call(["mkdir", f"{project_name}/src/"])
        call(["mkdir", f"{project_name}/src/pages/"])

        call(["yarn", "init", "--yes"], cwd=project_name)
        call(["yarn", "add", "astro"], cwd=project_name)

    else:
        print(f"Invalid selection: {pkg_manager}\nChoose 1, 2 or 3 only")
        exit(1)

    with open(f"{project_name}/package.json", "w") as package_json:
        package_json.write(
            r"""{
  "name": "astro-project",
  "version": "1.0.0",
  "description": "add your description",
  "main": "index.js",
  "scripts": { 
    "test": "echo \"Error: no test specified\" && exit 1",
    "dev": "astro dev",
    "build": "astro build",
    "preview": "astro preview"
  },
  "keywords": [],
  "author": "name",
  "license": "ISC"
}"""
        )

    call(["touch", f"{project_name}/src/pages/index.astro"])
    with open(f"{project_name}/src/pages/index.astro", "w") as index_astro:
        index_astro.write(
            r"""---
// Welcome to Astro! Everything between these triple-dash code fences
// is your "component frontmatter". It never runs in the browser.
console.log('This runs in your terminal, not the browser!');
---
<!-- Below is your "component template." It's just HTML, but with
    some magic sprinkled in to help you build great templates. -->
<html>
<body>
    <h1>Hello, World!</h1>
</body>
</html>
<style>
h1 {
    color: orange;
}
</style>"""
        )

    if pkg_manager == "1":

        call(["npm", "run", "dev"], cwd=project_name)
    elif pkg_manager == "2":

        call(["pnpm", "run", "dev"], cwd=project_name)

    elif pkg_manager == "3":

        call(["yarn", "run", "dev"], cwd=project_name)

    # SETTING UP ASTRO


main()
