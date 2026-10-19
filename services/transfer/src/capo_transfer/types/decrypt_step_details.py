"""Generated from Smithy shape ``com.amazonaws.transfer#DecryptStepDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.encryption_type
    import capo_transfer.types.input_file_location
    import capo_transfer.types.overwrite_existing
    import capo_transfer.types.source_file_location
    import capo_transfer.types.workflow_step_name


class DecryptStepDetails(TypedDict, closed=True):
    name: NotRequired["capo_transfer.types.workflow_step_name.WorkflowStepName"]
    """<p>The name of the step, used as an identifier.</p>"""
    type: "capo_transfer.types.encryption_type.EncryptionType"
    """<p>The type of encryption used. Currently, this value must be <code>PGP</code>.</p>"""
    source_file_location: NotRequired[
        "capo_transfer.types.source_file_location.SourceFileLocation"
    ]
    """<p>Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.</p> <ul> <li> <p>To use the previous file as the input, enter <code>${previous.file}</code>. In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.</p> </li> <li> <p>To use the originally uploaded file location as input for this step, enter <code>${original.file}</code>.</p> </li> </ul>"""
    overwrite_existing: NotRequired[
        "capo_transfer.types.overwrite_existing.OverwriteExisting"
    ]
    """<p>A flag that indicates whether to overwrite an existing file of the same name. The default is <code>FALSE</code>.</p> <p>If the workflow is processing a file that has the same name as an existing file, the behavior is as follows:</p> <ul> <li> <p>If <code>OverwriteExisting</code> is <code>TRUE</code>, the existing file is replaced with the file being processed.</p> </li> <li> <p>If <code>OverwriteExisting</code> is <code>FALSE</code>, nothing happens, and the workflow processing stops.</p> </li> </ul>"""
    destination_file_location: (
        "capo_transfer.types.input_file_location.InputFileLocation"
    )
    """<p>Specifies the location for the file being decrypted. Use <code>${Transfer:UserName}</code> or <code>${Transfer:UploadDate}</code> in this field to parametrize the destination prefix by username or uploaded date.</p> <ul> <li> <p>Set the value of <code>DestinationFileLocation</code> to <code>${Transfer:UserName}</code> to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file.</p> </li> <li> <p>Set the value of <code>DestinationFileLocation</code> to <code>${Transfer:UploadDate}</code> to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload.</p> <note> <p>The system resolves <code>UploadDate</code> to a date format of <i>YYYY-MM-DD</i>, based on the date the file is uploaded in UTC.</p> </note> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DecryptStepDetails) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    import capo_transfer.types.encryption_type

    out["Type"] = capo_transfer.types.encryption_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "source_file_location" in value:
        out["SourceFileLocation"] = value["source_file_location"]
    if "overwrite_existing" in value:
        import capo_transfer.types.overwrite_existing

        out["OverwriteExisting"] = (
            capo_transfer.types.overwrite_existing.serialize_aws_json_1_1(
                value["overwrite_existing"]
            )
        )
    import capo_transfer.types.input_file_location

    out["DestinationFileLocation"] = (
        capo_transfer.types.input_file_location.serialize_aws_json_1_1(
            value["destination_file_location"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DecryptStepDetails:
    out: DecryptStepDetails = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Type") is not None:
        import capo_transfer.types.encryption_type

        out["type"] = capo_transfer.types.encryption_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_transfer.types.encryption_type.EncryptionType", ""
        )
    if data.get("SourceFileLocation") is not None:
        out["source_file_location"] = data["SourceFileLocation"]
    if data.get("OverwriteExisting") is not None:
        import capo_transfer.types.overwrite_existing

        out["overwrite_existing"] = (
            capo_transfer.types.overwrite_existing.deserialize_aws_json_1_1(
                data["OverwriteExisting"]
            )
        )
    if data.get("DestinationFileLocation") is not None:
        import capo_transfer.types.input_file_location

        out["destination_file_location"] = (
            capo_transfer.types.input_file_location.deserialize_aws_json_1_1(
                data["DestinationFileLocation"]
            )
        )
    else:
        raise DeserializationError(
            "DecryptStepDetails.destination_file_location required"
        )
    return out
