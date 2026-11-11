"""Generated from Smithy shape ``com.amazonaws.sagemaker#ExtensionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_arn
    import capo_sagemaker.types.extension_name
    import capo_sagemaker.types.extension_status
    import capo_sagemaker.types.extension_version
    import capo_sagemaker.types.timestamp


class ExtensionSummary(TypedDict, closed=True):
    extension_arn: NotRequired["capo_sagemaker.types.extension_arn.ExtensionArn"]
    """<p>The Amazon Resource Name (ARN) of the extension.</p>"""
    extension_name: NotRequired["capo_sagemaker.types.extension_name.ExtensionName"]
    """<p>The name of the extension.</p>"""
    extension_version: NotRequired[
        "capo_sagemaker.types.extension_version.ExtensionVersion"
    ]
    """<p>The version of the extension.</p>"""
    status: NotRequired["capo_sagemaker.types.extension_status.ExtensionStatus"]
    """<p>The status of the extension. For the meaning of each status, see <code>ExtensionDetails</code>.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the extension was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtensionSummary) -> dict:
    out: dict = {}
    if "extension_arn" in value:
        out["ExtensionArn"] = value["extension_arn"]
    if "extension_name" in value:
        out["ExtensionName"] = value["extension_name"]
    if "extension_version" in value:
        out["ExtensionVersion"] = value["extension_version"]
    if "status" in value:
        import capo_sagemaker.types.extension_status

        out["Status"] = capo_sagemaker.types.extension_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import capo_sagemaker.types.timestamp

        out["CreationTime"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExtensionSummary:
    out: ExtensionSummary = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionArn") is not None:
        out["extension_arn"] = data["ExtensionArn"]
    if data.get("ExtensionName") is not None:
        out["extension_name"] = data["ExtensionName"]
    if data.get("ExtensionVersion") is not None:
        out["extension_version"] = data["ExtensionVersion"]
    if data.get("Status") is not None:
        import capo_sagemaker.types.extension_status

        out["status"] = capo_sagemaker.types.extension_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("CreationTime") is not None:
        import capo_sagemaker.types.timestamp

        out["creation_time"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out
