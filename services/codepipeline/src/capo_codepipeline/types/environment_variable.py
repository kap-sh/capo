"""Generated from Smithy shape ``com.amazonaws.codepipeline#EnvironmentVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.environment_variable_name
    import capo_codepipeline.types.environment_variable_type
    import capo_codepipeline.types.environment_variable_value


class EnvironmentVariable(TypedDict, closed=True):
    name: "capo_codepipeline.types.environment_variable_name.EnvironmentVariableName"
    """<p>The environment variable name in the key-value pair.</p>"""
    value: "capo_codepipeline.types.environment_variable_value.EnvironmentVariableValue"
    """<p>The environment variable value in the key-value pair.</p>"""
    type: NotRequired[
        "capo_codepipeline.types.environment_variable_type.EnvironmentVariableType"
    ]
    """<p>Specifies the type of use for the environment variable value. The value can be either <code>PLAINTEXT</code> or <code>SECRETS_MANAGER</code>. If the value is <code>SECRETS_MANAGER</code>, provide the Secrets reference in the EnvironmentVariable value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    if "type" in value:
        import capo_codepipeline.types.environment_variable_type

        out["type"] = (
            capo_codepipeline.types.environment_variable_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentVariable:
    out: EnvironmentVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("type") is not None:
        import capo_codepipeline.types.environment_variable_type

        out["type"] = (
            capo_codepipeline.types.environment_variable_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    return out
