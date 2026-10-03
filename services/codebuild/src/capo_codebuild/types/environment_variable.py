"""Generated from Smithy shape ``com.amazonaws.codebuild#EnvironmentVariable``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codebuild.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codebuild.types.environment_variable_type
    import capo_codebuild.types.non_empty_string
    import capo_codebuild.types.string


class EnvironmentVariable(TypedDict, closed=True):
    name: "capo_codebuild.types.non_empty_string.NonEmptyString"
    """<p>The name or key of the environment variable.</p>"""
    value: "capo_codebuild.types.string.String"
    """<p>The value of the environment variable.</p> <important> <p>We strongly discourage the use of <code>PLAINTEXT</code> environment variables to store sensitive values, especially Amazon Web Services secret key IDs. <code>PLAINTEXT</code> environment variables can be displayed in plain text using the CodeBuild console and the CLI. For sensitive values, we recommend you use an environment variable of type <code>PARAMETER_STORE</code> or <code>SECRETS_MANAGER</code>. </p> </important>"""
    type: NotRequired[
        "capo_codebuild.types.environment_variable_type.EnvironmentVariableType"
    ]
    """<p>The type of environment variable. Valid values include:</p> <ul> <li> <p> <code>PARAMETER_STORE</code>: An environment variable stored in Systems Manager Parameter Store. For environment variables of this type, specify the name of the parameter as the <code>value</code> of the EnvironmentVariable. The parameter value will be substituted for the name at runtime. You can also define Parameter Store environment variables in the buildspec. To learn how to do so, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.parameter-store">env/parameter-store</a> in the <i>CodeBuild User Guide</i>.</p> </li> <li> <p> <code>PLAINTEXT</code>: An environment variable in plain text format. This is the default value.</p> </li> <li> <p> <code>SECRETS_MANAGER</code>: An environment variable stored in Secrets Manager. For environment variables of this type, specify the name of the secret as the <code>value</code> of the EnvironmentVariable. The secret value will be substituted for the name at runtime. You can also define Secrets Manager environment variables in the buildspec. To learn how to do so, see <a href="https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html#build-spec.env.secrets-manager">env/secrets-manager</a> in the <i>CodeBuild User Guide</i>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariable) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    if "type" in value:
        import capo_codebuild.types.environment_variable_type

        out["type"] = (
            capo_codebuild.types.environment_variable_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EnvironmentVariable:
    out: EnvironmentVariable = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("EnvironmentVariable.name required")
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        raise DeserializationError("EnvironmentVariable.value required")
    if data.get("type") is not None:
        import capo_codebuild.types.environment_variable_type

        out["type"] = (
            capo_codebuild.types.environment_variable_type.deserialize_aws_json_1_1(
                data["type"]
            )
        )
    return out
