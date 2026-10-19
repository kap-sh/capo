"""Generated from Smithy shape ``com.amazonaws.pcs#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.arn
    import capo_pcs.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_pcs.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "capo_pcs.types.tag_keys.TagKeys"
    """<p>1 or more tag keys to remove from the resource. Specify only tag keys and not tag values.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_pcs.types.tag_keys

    out["tagKeys"] = capo_pcs.types.tag_keys.serialize_aws_json_1_0(value["tag_keys"])
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_pcs.types.tag_keys

        out["tag_keys"] = capo_pcs.types.tag_keys.deserialize_aws_json_1_0(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
