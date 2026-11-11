"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateClusterExtensionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_arn


class UpdateClusterExtensionResponse(TypedDict, closed=True):
    extension_arn: NotRequired["capo_sagemaker.types.extension_arn.ExtensionArn"]
    """<p>The Amazon Resource Name (ARN) of the extension that is being updated. To track the update, call <code>DescribeClusterExtension</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateClusterExtensionResponse) -> dict:
    out: dict = {}
    if "extension_arn" in value:
        out["ExtensionArn"] = value["extension_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateClusterExtensionResponse:
    out: UpdateClusterExtensionResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionArn") is not None:
        out["extension_arn"] = data["ExtensionArn"]
    return out
