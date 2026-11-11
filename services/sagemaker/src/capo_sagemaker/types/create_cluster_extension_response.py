"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateClusterExtensionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.extension_arn


class CreateClusterExtensionResponse(TypedDict, closed=True):
    extension_arn: NotRequired["capo_sagemaker.types.extension_arn.ExtensionArn"]
    """<p>The Amazon Resource Name (ARN) of the extension that you created. Use this ARN to describe, update, or delete the extension.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterExtensionResponse) -> dict:
    out: dict = {}
    if "extension_arn" in value:
        out["ExtensionArn"] = value["extension_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterExtensionResponse:
    out: CreateClusterExtensionResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExtensionArn") is not None:
        out["extension_arn"] = data["ExtensionArn"]
    return out
