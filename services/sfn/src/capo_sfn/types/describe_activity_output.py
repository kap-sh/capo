"""Generated from Smithy shape ``com.amazonaws.sfn#DescribeActivityOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.arn
    import capo_sfn.types.encryption_configuration
    import capo_sfn.types.name
    import capo_sfn.types.timestamp


class DescribeActivityOutput(TypedDict, closed=True):
    activity_arn: "capo_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) that identifies the activity.</p>"""
    name: "capo_sfn.types.name.Name"
    r"""<p>The name of the activity.</p> <p>A name must <i>not</i> contain:</p> <ul> <li> <p>white space</p> </li> <li> <p>brackets <code>< > { } [ ]</code> </p> </li> <li> <p>wildcard characters <code>? *</code> </p> </li> <li> <p>special characters <code>" # % \ ^ | ~ ` $ & , ; : /</code> </p> </li> <li> <p>control characters (<code>U+0000-001F</code>, <code>U+007F-009F</code>, <code>U+FFFE-FFFF</code>)</p> </li> <li> <p>surrogates (<code>U+D800-DFFF</code>)</p> </li> <li> <p>invalid characters (<code> U+10FFFF</code>)</p> </li> </ul> <p>To enable logging with CloudWatch Logs, the name should only contain 0-9, A-Z, a-z, - and _.</p>"""
    creation_date: "capo_sfn.types.timestamp.Timestamp"
    """<p>The date the activity is created.</p>"""
    encryption_configuration: NotRequired[
        "capo_sfn.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>Settings for configured server-side encryption.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeActivityOutput) -> dict:
    out: dict = {}
    out["activityArn"] = value["activity_arn"]
    out["name"] = value["name"]
    import capo_sfn.types.timestamp

    out["creationDate"] = capo_sfn.types.timestamp.serialize_aws_json_1_0(
        value["creation_date"]
    )
    if "encryption_configuration" in value:
        import capo_sfn.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_sfn.types.encryption_configuration.serialize_aws_json_1_0(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeActivityOutput:
    out: DescribeActivityOutput = {}  # type: ignore[typeddict-item]
    if data.get("activityArn") is not None:
        out["activity_arn"] = data["activityArn"]
    else:
        raise DeserializationError("DescribeActivityOutput.activity_arn required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("DescribeActivityOutput.name required")
    if data.get("creationDate") is not None:
        import capo_sfn.types.timestamp

        out["creation_date"] = capo_sfn.types.timestamp.deserialize_aws_json_1_0(
            data["creationDate"]
        )
    else:
        raise DeserializationError("DescribeActivityOutput.creation_date required")
    if data.get("encryptionConfiguration") is not None:
        import capo_sfn.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_sfn.types.encryption_configuration.deserialize_aws_json_1_0(
                data["encryptionConfiguration"]
            )
        )
    return out
