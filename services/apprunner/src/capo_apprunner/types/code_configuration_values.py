"""Generated from Smithy shape ``com.amazonaws.apprunner#CodeConfigurationValues``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_apprunner.types.build_command
    import capo_apprunner.types.runtime
    import capo_apprunner.types.runtime_environment_secrets
    import capo_apprunner.types.runtime_environment_variables
    import capo_apprunner.types.start_command
    import capo_apprunner.types.string


class CodeConfigurationValues(TypedDict, closed=True):
    runtime: "capo_apprunner.types.runtime.Runtime"
    """<p>A runtime environment type for building and running an App Runner service. It represents a programming language runtime.</p>"""
    build_command: NotRequired["capo_apprunner.types.build_command.BuildCommand"]
    """<p>The command App Runner runs to build your application.</p>"""
    start_command: NotRequired["capo_apprunner.types.start_command.StartCommand"]
    """<p>The command App Runner runs to start your application.</p>"""
    port: NotRequired["capo_apprunner.types.string.String"]
    """<p>The port that your application listens to in the container.</p> <p>Default: <code>8080</code> </p>"""
    runtime_environment_variables: NotRequired[
        "capo_apprunner.types.runtime_environment_variables.RuntimeEnvironmentVariables"
    ]
    """<p>The environment variables that are available to your running App Runner service. An array of key-value pairs.</p>"""
    runtime_environment_secrets: NotRequired[
        "capo_apprunner.types.runtime_environment_secrets.RuntimeEnvironmentSecrets"
    ]
    """<p>An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.</p> <note> <ul> <li> <p> If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Amazon Web Services Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified. </p> </li> <li> <p> Currently, cross account referencing of Amazon Web Services Systems Manager Parameter Store parameter is not supported. </p> </li> </ul> </note>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CodeConfigurationValues) -> dict:
    out: dict = {}
    import capo_apprunner.types.runtime

    out["Runtime"] = capo_apprunner.types.runtime.serialize_aws_json_1_0(
        value["runtime"]
    )
    if "build_command" in value:
        out["BuildCommand"] = value["build_command"]
    if "start_command" in value:
        out["StartCommand"] = value["start_command"]
    if "port" in value:
        out["Port"] = value["port"]
    if "runtime_environment_variables" in value:
        import capo_apprunner.types.runtime_environment_variables

        out["RuntimeEnvironmentVariables"] = (
            capo_apprunner.types.runtime_environment_variables.serialize_aws_json_1_0(
                value["runtime_environment_variables"]
            )
        )
    if "runtime_environment_secrets" in value:
        import capo_apprunner.types.runtime_environment_secrets

        out["RuntimeEnvironmentSecrets"] = (
            capo_apprunner.types.runtime_environment_secrets.serialize_aws_json_1_0(
                value["runtime_environment_secrets"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CodeConfigurationValues:
    out: CodeConfigurationValues = {}  # type: ignore[typeddict-item]
    if data.get("Runtime") is not None:
        import capo_apprunner.types.runtime

        out["runtime"] = capo_apprunner.types.runtime.deserialize_aws_json_1_0(
            data["Runtime"]
        )
    else:
        import typing

        out["runtime"] = typing.cast("capo_apprunner.types.runtime.Runtime", "")
    if data.get("BuildCommand") is not None:
        out["build_command"] = data["BuildCommand"]
    if data.get("StartCommand") is not None:
        out["start_command"] = data["StartCommand"]
    if data.get("Port") is not None:
        out["port"] = data["Port"]
    if data.get("RuntimeEnvironmentVariables") is not None:
        import capo_apprunner.types.runtime_environment_variables

        out["runtime_environment_variables"] = (
            capo_apprunner.types.runtime_environment_variables.deserialize_aws_json_1_0(
                data["RuntimeEnvironmentVariables"]
            )
        )
    if data.get("RuntimeEnvironmentSecrets") is not None:
        import capo_apprunner.types.runtime_environment_secrets

        out["runtime_environment_secrets"] = (
            capo_apprunner.types.runtime_environment_secrets.deserialize_aws_json_1_0(
                data["RuntimeEnvironmentSecrets"]
            )
        )
    return out


def redact_sensitive(value: CodeConfigurationValues) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "build_command" in value:
        out["build_command"] = "*** Sensitive Data Redacted ***"
    if "start_command" in value:
        out["start_command"] = "*** Sensitive Data Redacted ***"
    if "runtime_environment_variables" in value:
        out["runtime_environment_variables"] = "*** Sensitive Data Redacted ***"
    if "runtime_environment_secrets" in value:
        out["runtime_environment_secrets"] = "*** Sensitive Data Redacted ***"
    return out
