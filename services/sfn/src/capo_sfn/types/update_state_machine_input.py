"""Generated from Smithy shape ``com.amazonaws.sfn#UpdateStateMachineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.definition
    import capo_sfn.types.encryption_configuration
    import capo_sfn.types.logging_configuration
    import capo_sfn.types.publish
    import capo_sfn.types.tracing_configuration
    import capo_sfn.types.version_description


class UpdateStateMachineInput(TypedDict, closed=True):
    state_machine_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine.</p>"""
    definition: NotRequired["capo_sfn.types.definition.Definition"]
    """<p>The Amazon States Language definition of the state machine. See <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a>.</p>"""
    role_arn: NotRequired["capo_sfn.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role of the state machine.</p>"""
    logging_configuration: NotRequired[
        "capo_sfn.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>Use the <code>LoggingConfiguration</code> data type to set CloudWatch Logs options.</p>"""
    tracing_configuration: NotRequired[
        "capo_sfn.types.tracing_configuration.TracingConfiguration"
    ]
    """<p>Selects whether X-Ray tracing is enabled.</p>"""
    publish: "capo_sfn.types.publish.Publish"
    """<p>Specifies whether the state machine version is published. The default is <code>false</code>. To publish a version after updating the state machine, set <code>publish</code> to <code>true</code>.</p>"""
    version_description: NotRequired[
        "capo_sfn.types.version_description.VersionDescription"
    ]
    """<p>An optional description of the state machine version to publish.</p> <p>You can only specify the <code>versionDescription</code> parameter if you've set <code>publish</code> to <code>true</code>.</p>"""
    encryption_configuration: NotRequired[
        "capo_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings to configure server-side encryption. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateMachineInput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    if "definition" in value:
        out["definition"] = value["definition"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "logging_configuration" in value:
        import capo_sfn.types.logging_configuration

        out["loggingConfiguration"] = (
            capo_sfn.types.logging_configuration.serialize_aws_json_1_0(
                value["logging_configuration"]
            )
        )
    if "tracing_configuration" in value:
        import capo_sfn.types.tracing_configuration

        out["tracingConfiguration"] = (
            capo_sfn.types.tracing_configuration.serialize_aws_json_1_0(
                value["tracing_configuration"]
            )
        )
    out["publish"] = value.get("publish", False)
    if "version_description" in value:
        out["versionDescription"] = value["version_description"]
    if "encryption_configuration" in value:
        import capo_sfn.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_sfn.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateMachineInput:
    out: UpdateStateMachineInput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("UpdateStateMachineInput.state_machine_arn required")
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("loggingConfiguration") is not None:
        import capo_sfn.types.logging_configuration

        out["logging_configuration"] = (
            capo_sfn.types.logging_configuration.deserialize_aws_json_1_0(
                data["loggingConfiguration"]
            )
        )
    if data.get("tracingConfiguration") is not None:
        import capo_sfn.types.tracing_configuration

        out["tracing_configuration"] = (
            capo_sfn.types.tracing_configuration.deserialize_aws_json_1_0(
                data["tracingConfiguration"]
            )
        )
    if data.get("publish") is not None:
        out["publish"] = data["publish"]
    else:
        out["publish"] = False
    if data.get("versionDescription") is not None:
        out["version_description"] = data["versionDescription"]
    if data.get("encryptionConfiguration") is not None:
        import capo_sfn.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_sfn.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    return out
