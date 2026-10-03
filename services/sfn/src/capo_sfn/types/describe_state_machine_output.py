"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeStateMachineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.definition
    import capo_sfn.types.encryption_configuration
    import capo_sfn.types.logging_configuration
    import capo_sfn.types.map_run_label
    import capo_sfn.types.name
    import capo_sfn.types.revision_id
    import capo_sfn.types.state_machine_status
    import capo_sfn.types.state_machine_type
    import capo_sfn.types.timestamp
    import capo_sfn.types.tracing_configuration
    import capo_sfn.types.variable_references
    import capo_sfn.types.version_description


class DescribeStateMachineOutput(TypedDict, closed=True):
    state_machine_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the state machine.</p> <p>If you specified a state machine version ARN in your request, the API returns the version ARN. The version ARN is a combination of state machine ARN and the version number separated by a colon (:). For example, <code>stateMachineARN:1</code>.</p>"""
    name: "capo_sfn.types.name.Name"
    r"""<p>The name of the state machine.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    status: NotRequired["capo_sfn.types.state_machine_status.StateMachineStatus"]
    """<p>The current status of the state machine.</p>"""
    definition: "capo_sfn.types.definition.Definition"
    """<p>The Amazon States Language definition of the state machine. See <a href="https://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html">Amazon States Language</a>.</p> <p>If called with <code>includedData = METADATA_ONLY</code>, the returned definition will be <code>{}</code>.</p>"""
    role_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the IAM role used when creating this state machine. (The IAM role maintains security by granting Step Functions access to Amazon Web Services resources.)</p>"""
    type: "capo_sfn.types.state_machine_type.StateMachineType"
    """<p>The <code>type</code> of the state machine (<code>STANDARD</code> or <code>EXPRESS</code>).</p>"""
    creation_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the state machine is created.</p> <p>For a state machine version, <code>creationDate</code> is the date the version was created.</p>"""
    logging_configuration: NotRequired[
        "capo_sfn.types.logging_configuration.LoggingConfiguration"
    ]
    tracing_configuration: NotRequired[
        "capo_sfn.types.tracing_configuration.TracingConfiguration"
    ]
    """<p>Selects whether X-Ray tracing is enabled.</p>"""
    label: NotRequired["capo_sfn.types.map_run_label.MapRunLabel"]
    """<p>A user-defined or an auto-generated string that identifies a <code>Map</code> state. This parameter is present only if the <code>stateMachineArn</code> specified in input is a qualified state machine ARN.</p>"""
    revision_id: NotRequired["capo_sfn.types.revision_id.RevisionId"]
    """<p>The revision identifier for the state machine.</p> <p>Use the <code>revisionId</code> parameter to compare between versions of a state machine configuration used for executions without performing a diff of the properties, such as <code>definition</code> and <code>roleArn</code>.</p>"""
    description: NotRequired["capo_sfn.types.version_description.VersionDescription"]
    """<p>The description of the state machine version.</p>"""
    encryption_configuration: NotRequired[
        "capo_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings to configure server-side encryption. </p>"""
    variable_references: NotRequired[
        "capo_sfn.types.variable_references.VariableReferences"
    ]
    """<p>A map of <b>state name</b> to a list of variables referenced by that state. States that do not use variable references will not be shown in the response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeStateMachineOutput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    out["name"] = value["name"]
    if "status" in value:
        import capo_sfn.types.state_machine_status

        out["status"] = capo_sfn.types.state_machine_status.serialize_aws_json_1_0(
            value["status"]
        )
    out["definition"] = value["definition"]
    out["roleArn"] = value["role_arn"]
    import capo_sfn.types.state_machine_type

    out["type"] = capo_sfn.types.state_machine_type.serialize_aws_json_1_0(
        value["type"]
    )
    import capo_sfn.types.timestamp

    out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
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
    if "label" in value:
        out["label"] = value["label"]
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_configuration" in value:
        import capo_sfn.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_sfn.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    if "variable_references" in value:
        import capo_sfn.types.variable_references

        out["variableReferences"] = (
            capo_sfn.types.variable_references.serialize_aws_json_1_0(
                value["variable_references"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeStateMachineOutput:
    out: DescribeStateMachineOutput = {}  # type: ignore[typeddict-item]
    if data.get("stateMachineArn") is not None:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError(
            "DescribeStateMachineOutput.state_machine_arn required"
        )
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DescribeStateMachineOutput.name required")
    if data.get("status") is not None:
        import capo_sfn.types.state_machine_status

        out["status"] = capo_sfn.types.state_machine_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("definition") is not None:
        out["definition"] = data["definition"]
    else:
        raise DeserializationError("DescribeStateMachineOutput.definition required")
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("DescribeStateMachineOutput.role_arn required")
    if data.get("type") is not None:
        import capo_sfn.types.state_machine_type

        out["type"] = capo_sfn.types.state_machine_type.deserialize_aws_json_1_0(
            data["type"]
        )
    else:
        raise DeserializationError("DescribeStateMachineOutput.type required")
    if data.get("creationDate") is not None:
        import capo_sfn.types.timestamp

        out["creation_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("DescribeStateMachineOutput.creation_date required")
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
    if data.get("label") is not None:
        out["label"] = data["label"]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("encryptionConfiguration") is not None:
        import capo_sfn.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_sfn.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    if data.get("variableReferences") is not None:
        import capo_sfn.types.variable_references

        out["variable_references"] = (
            capo_sfn.types.variable_references.deserialize_aws_json_1_0(
                data["variableReferences"]
            )
        )
    return out
