"""Generated from Smithy shape ``com.amazonaws.sfn#CreateStateMachineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.definition
    import capo_sfn.types.encryption_configuration
    import capo_sfn.types.logging_configuration
    import capo_sfn.types.name
    import capo_sfn.types.publish
    import capo_sfn.types.state_machine_type
    import capo_sfn.types.tag_list
    import capo_sfn.types.tracing_configuration
    import capo_sfn.types.version_description


class CreateStateMachineInput(TypedDict, closed=True):
    name: "capo_sfn.types.name.Name"
    r"""<p>The name of the state machine. </p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    definition: "capo_sfn.types.definition.Definition"
    """<p>The Amazon States Language definition of the state machine. See <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a>.</p>"""
    role_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to use for this state machine.</p>"""
    type: NotRequired["capo_sfn.types.state_machine_type.StateMachineType"]
    """<p>Determines whether a Standard or Express state machine is created. The default is <code>STANDARD</code>. You cannot update the <code>type</code> of a state machine once it has been created.</p>"""
    logging_configuration: NotRequired[
        "capo_sfn.types.logging_configuration.LoggingConfiguration"
    ]
    """<p>Defines what execution history events are logged and where they are logged.</p> <note> <p>By default, the <code>level</code> is set to <code>OFF</code>. For more information see <a href="https://docs.aws.amazon.com/step-functions/latest/dg/cloudwatch-log-level.html">Log Levels</a> in the Step Functions User Guide.</p> </note>"""
    tags: NotRequired["capo_sfn.types.tag_list.TagList"]
    """<p>Tags to be added when creating a state machine.</p> <p>An array of key-value pairs. For more information, see <a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html">Using Cost Allocation Tags</a> in the <i>Amazon Web Services Billing and Cost Management User Guide</i>, and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html">Controlling Access Using IAM Tags</a>.</p> <p>Tags may only contain Unicode letters, digits, white space, or these symbols: <code>_ . : / = + - @</code>.</p>"""
    tracing_configuration: NotRequired[
        "capo_sfn.types.tracing_configuration.TracingConfiguration"
    ]
    """<p>Selects whether X-Ray tracing is enabled.</p>"""
    publish: "capo_sfn.types.publish.Publish"
    """<p>Set to <code>true</code> to publish the first version of the state machine during creation. The default is <code>false</code>.</p>"""
    version_description: NotRequired[
        "capo_sfn.types.version_description.VersionDescription"
    ]
    """<p>Sets description about the state machine version. You can only set the description if the <code>publish</code> parameter is set to <code>true</code>. Otherwise, if you set <code>versionDescription</code>, but <code>publish</code> to <code>false</code>, this API action throws <code>ValidationException</code>.</p>"""
    encryption_configuration: NotRequired[
        "capo_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings to configure server-side encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateMachineInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["definition"] = value["definition"]
    out["roleArn"] = value["role_arn"]
    if "type" in value:
        import capo_sfn.types.state_machine_type

        out["type"] = capo_sfn.types.state_machine_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "logging_configuration" in value:
        import capo_sfn.types.logging_configuration

        out["loggingConfiguration"] = (
            capo_sfn.types.logging_configuration.serialize_aws_json_1_0(
                value["logging_configuration"]
            )
        )
    if "tags" in value:
        import capo_sfn.types.tag_list

        out["tags"] = capo_sfn.types.tag_list.serialize_aws_json_1_0(value["tags"])
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


def deserialize_aws_json_1_0(data: dict) -> CreateStateMachineInput:
    out: CreateStateMachineInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateStateMachineInput.name required")
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("CreateStateMachineInput.definition required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateStateMachineInput.role_arn required")
    if data.get("type") is not None:
        import capo_sfn.types.state_machine_type

        out["type"] = capo_sfn.types.state_machine_type.deserialize_aws_json_1_0(
            data["type"]
        )
    if data.get("loggingConfiguration") is not None:
        import capo_sfn.types.logging_configuration

        out["logging_configuration"] = (
            capo_sfn.types.logging_configuration.deserialize_aws_json_1_0(
                data["loggingConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_sfn.types.tag_list

        out["tags"] = capo_sfn.types.tag_list.deserialize_aws_json_1_0(data["tags"])
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
