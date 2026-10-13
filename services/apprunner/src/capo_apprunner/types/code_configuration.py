"""Generated from Smithy shape ``com.amazonaws.apprunner#CodeConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_apprunner.errors import DeserializationError

if TYPE_CHECKING:
    import capo_apprunner.types.code_configuration_values
    import capo_apprunner.types.configuration_source


class CodeConfiguration(TypedDict, closed=True):
    configuration_source: (
        "capo_apprunner.types.configuration_source.ConfigurationSource"
    )
    """<p>The source of the App Runner configuration. Values are interpreted as follows:</p> <ul> <li> <p> <code>REPOSITORY</code> – App Runner reads configuration values from the <code>apprunner.yaml</code> file in the source code repository and ignores <code>CodeConfigurationValues</code>.</p> </li> <li> <p> <code>API</code> – App Runner uses configuration values provided in <code>CodeConfigurationValues</code> and ignores the <code>apprunner.yaml</code> file in the source code repository.</p> </li> </ul>"""
    code_configuration_values: NotRequired[
        "capo_apprunner.types.code_configuration_values.CodeConfigurationValues"
    ]
    """<p>The basic configuration for building and running the App Runner service. Use it to quickly launch an App Runner service without providing a <code>apprunner.yaml</code> file in the source code repository (or ignoring the file if it exists).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CodeConfiguration) -> dict:
    out: dict = {}
    import capo_apprunner.types.configuration_source

    out["ConfigurationSource"] = (
        capo_apprunner.types.configuration_source.serialize_aws_json_1_0(
            value["configuration_source"]
        )
    )
    if "code_configuration_values" in value:
        import capo_apprunner.types.code_configuration_values

        out["CodeConfigurationValues"] = (
            capo_apprunner.types.code_configuration_values.serialize_aws_json_1_0(
                value["code_configuration_values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CodeConfiguration:
    out: CodeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSource") is not None:
        import capo_apprunner.types.configuration_source

        out["configuration_source"] = (
            capo_apprunner.types.configuration_source.deserialize_aws_json_1_0(
                data["ConfigurationSource"]
            )
        )
    else:
        raise DeserializationError("CodeConfiguration.configuration_source required")
    if data.get("CodeConfigurationValues") is not None:
        import capo_apprunner.types.code_configuration_values

        out["code_configuration_values"] = (
            capo_apprunner.types.code_configuration_values.deserialize_aws_json_1_0(
                data["CodeConfigurationValues"]
            )
        )
    return out


def redact_sensitive(value: CodeConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code_configuration_values" in value:
        import capo_apprunner.types.code_configuration_values

        out["code_configuration_values"] = (
            capo_apprunner.types.code_configuration_values.redact_sensitive(
                value["code_configuration_values"]
            )
        )
    return out
