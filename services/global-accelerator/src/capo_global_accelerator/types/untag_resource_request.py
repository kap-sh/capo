"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.resource_arn
    import capo_global_accelerator.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_global_accelerator.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the Global Accelerator resource to remove tags from. An ARN uniquely identifies a resource.</p>"""
    tag_keys: "capo_global_accelerator.types.tag_keys.TagKeys"
    """<p>The tag key pairs that you want to remove from the specified resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_global_accelerator.types.tag_keys

    out["TagKeys"] = capo_global_accelerator.types.tag_keys.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("TagKeys") is not None:
        import capo_global_accelerator.types.tag_keys

        out["tag_keys"] = (
            capo_global_accelerator.types.tag_keys.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
