import argparse

from ctcw.utils.app_util import AppUtil


def main(arg_list: list[str] | None = None):
    parser = argparse.ArgumentParser(
        description="Retrieve and print the application version for the given package manager."
    )
    parser.add_argument(
        "--package-manager",
        required=True,
        help="Package manager selected",
    )
    args = parser.parse_args(arg_list)

    package_manager = AppUtil.validate_package_manager(args.package_manager)

    app_version = AppUtil.get_app_version(package_manager)

    print(app_version)


if __name__ == "__main__":
    main()
