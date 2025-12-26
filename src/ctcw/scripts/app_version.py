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
    parser.add_argument(
        "--workspace-path",
        required=True,
        help="Workspace path",
    )
    args = parser.parse_args(arg_list)

    package_manager = AppUtil.validate_package_manager(args.package_manager)
    workspace_path = AppUtil.validate_workspace_path(args.workspace_path)

    app_version = AppUtil.get_app_version(package_manager, workspace_path)

    print(app_version)


if __name__ == "__main__":
    main()
