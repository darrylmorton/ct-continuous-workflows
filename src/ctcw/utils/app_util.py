import json
import tomllib
from pathlib import Path

from logger import log


class AppUtil:
    valid_package_managers = ["npm", "poetry"]

    @staticmethod
    def validate_package_manager(package_manager: str) -> str:
        if package_manager not in AppUtil.valid_package_managers:
            error_message = (
                f"Invalid package manager '{package_manager}'. "
                f"Valid options are: {', '.join(AppUtil.valid_package_managers)}."
            )
            log.error(error_message)

            raise ValueError(error_message)

        return package_manager

    @staticmethod
    def get_app_version(package_manager: str) -> str:
        app_version = None

        if package_manager == "npm":
            package_json_file = (
                Path(__file__).parent.parent.parent.parent / "package.json"
            )

            try:
                with open(package_json_file, "r") as file:
                    data = json.load(file)
                app_version = data["version"]
            except FileNotFoundError:
                error_message = "The file 'package.json' was not found."
                log.error(error_message)

                raise FileNotFoundError(error_message)

        if package_manager == "poetry":
            pyproject_toml_file = (
                Path(__file__).parent.parent.parent.parent / "pyproject.toml"
            )

            try:
                with open(pyproject_toml_file, "rb") as f:
                    app_version = tomllib.load(f)["tool"]["poetry"]["version"]
            except FileNotFoundError:
                error_message = "The file 'pyproject.toml' was not found."
                log.error(error_message)

                raise FileNotFoundError(error_message)

        if not app_version:
            error_message = f"App version: {app_version} is invalid"
            log.error(error_message)

            raise ValueError(error_message)

        print(f"app_version {app_version}")

        return app_version
