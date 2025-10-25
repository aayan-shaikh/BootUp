from subprocess import call


def setup_pkg_manager(pkg_manager):
    if pkg_manager == "1":
        call(["npm", "init", "--yes"])
    elif pkg_manager == "2":
        call(["pnpm", "init"])
    elif pkg_manager == "3":
        call(["yarn", "init", "--yes"])
    else:
        print(f"Invalid selection: {pkg_manager}\nChoose 1, 2 or 3 only. Exiting")
        exit(1)
