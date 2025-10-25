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
const title = "Your Site Title";
const description = "A minimal, production-ready Astro template";
---

<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="description" content={description} />
    <title>{title}</title>
    <link rel="icon" type="image/svg+xml" href="/favicon.svg" />
  </head>
  <body>
    <header>
      <nav>
        <h1>Your Brand</h1>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <section id="home" class="hero">
        <h2>Welcome</h2>
        <p>A minimal, production-ready template</p>
        <button id="cta">Get Started</button>
      </section>

      <section id="about">
        <h2>About</h2>
        <p>Built with vanilla HTML, CSS, and JavaScript.</p>
      </section>

      <section id="contact">
        <h2>Contact</h2>
        <form id="contact-form">
          <input type="email" placeholder="Your email" required />
          <button type="submit">Submit</button>
        </form>
      </section>
    </main>

    <footer>
      <p>&copy; {new Date().getFullYear()} Your Brand. All rights reserved.</p>
    </footer>
  </body>
</html>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  :root {
    --primary: #3b82f6;
    --text: #1f2937;
    --bg: #ffffff;
    --gray: #6b7280;
  }
  #cta {
    margin-top: 1rem;
  }

  body {
    font-family:
      system-ui,
      -apple-system,
      sans-serif;
    line-height: 1.6;
    color: var(--text);
    background: var(--bg);
  }

  header {
    padding: 1rem 2rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  nav {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  nav ul {
    display: flex;
    gap: 2rem;
    list-style: none;
  }

  nav a {
    text-decoration: none;
    color: var(--text);
    transition: color 0.3s;
  }

  nav a:hover {
    color: var(--primary);
  }

  main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
  }

  section {
    min-height: 50vh;
    padding: 4rem 2rem;
  }

  .hero {
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }

  h1 {
    font-size: 1.5rem;
  }

  h2 {
    font-size: 2.5rem;
    margin-bottom: 1rem;
  }

  button {
    padding: 0.75rem 2rem;
    font-size: 1rem;
    background: var(--primary);
    color: white;
    border: none;
    border-radius: 0.5rem;
    cursor: pointer;
    transition: opacity 0.3s;
  }

  button:hover {
    opacity: 0.9;
  }

  form {
    display: flex;
    gap: 1rem;
    max-width: 500px;
  }

  input {
    flex: 1;
    padding: 0.75rem;
    border: 1px solid #d1d5db;
    border-radius: 0.5rem;
    font-size: 1rem;
  }

  footer {
    text-align: center;
    padding: 2rem;
    background: #f9fafb;
    color: var(--gray);
  }

  @media (max-width: 768px) {
    nav {
      flex-direction: column;
      gap: 1rem;
    }

    nav ul {
      gap: 1rem;
    }

    h2 {
      font-size: 2rem;
    }

    form {
      flex-direction: column;
    }
  }
</style>

<script>
  const cta = document.getElementById("cta");
  const form = document.getElementById("contact-form");

  cta?.addEventListener("click", () => {
    document.getElementById("contact")?.scrollIntoView({ behavior: "smooth" });
  });

  form?.addEventListener("submit", (e) => {
    e.preventDefault();
    alert("Form submitted!");
    form.reset();
  });
</script>
"""
        )

    if pkg_manager == "1":

        call(["npm", "run", "dev"], cwd=project_name)
    elif pkg_manager == "2":

        call(["pnpm", "run", "dev"], cwd=project_name)

    elif pkg_manager == "3":

        call(["yarn", "run", "dev"], cwd=project_name)

    # SETTING UP ASTRO


main()
