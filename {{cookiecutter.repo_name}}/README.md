# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Usage

To use this library, include the following Maven dependency:

    <dependency>
        <groupId>{{ cookiecutter.maven_group_id }}</groupId>
        <artifactId>{{ cookiecutter.maven_artifact_id }}</artifactId>
        <version>{{ cookiecutter.version }}</version>
    </dependency>
{%- if cookiecutter.open_source == 'y' %}

## License

This library is licensed under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for more information.
{%- endif %}
