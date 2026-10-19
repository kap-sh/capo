"""Generated from Smithy shape ``com.amazonaws.interconnect#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.amazon_resource_name
    import capo_interconnect.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    arn: "capo_interconnect.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the resource from which the specified tags should be removed.</p>"""
    tag_keys: "capo_interconnect.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys that should be removed from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    import capo_interconnect.types.tag_key_list

    out["tagKeys"] = capo_interconnect.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_interconnect.types.tag_key_list

        out["tag_keys"] = capo_interconnect.types.tag_key_list.deserialize_aws_json_1_0(
            data["tagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
