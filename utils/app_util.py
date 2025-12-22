from pathlib import Path

import toml


class AppUtil:
    valid_package_managers = ["npm", "poetry"]

    @staticmethod
    def validate_package_manager(package_manager: str) -> str:
        if package_manager not in AppUtil.valid_package_managers:
            error_message = (
                f"Invalid package manager '{package_manager}'. "
                f"Valid options are: {', '.join(AppUtil.valid_package_managers)}."
            )
            # log.error(error_message)

            raise ValueError(error_message)

        return package_manager

    @staticmethod
    def get_app_version(package_manager: str) -> str:
        app_version = None

        if package_manager == "npm":
            package_json_file = Path(__file__).parent.parent.parent / "package.json"

            if package_json_file.exists() and package_json_file.is_file():
                app_version = toml.load(package_json_file)["version"]

        if package_manager == "poetry":
            pyproject_toml_file = Path(__file__).parent.parent.parent / "pyproject.toml"

            if pyproject_toml_file.exists() and pyproject_toml_file.is_file():
                app_version = toml.load(pyproject_toml_file)["tool"]["poetry"]["version"]

        return app_version
