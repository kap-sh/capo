"""Generated from Smithy shape ``com.amazonaws.opensearchmemory#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_opensearchmemory.types.space_arn
    import capo_opensearchmemory.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_opensearchmemory.types.space_arn.SpaceArn"
    """<p>The Amazon Resource Name (ARN) of the space.</p>"""
    tag_keys: "capo_opensearchmemory.types.tag_key_list.TagKeyList"
    """<p>The keys of the tags to remove from the space.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_opensearchmemory.types.tag_key_list

    out["tagKeys"] = capo_opensearchmemory.types.tag_key_list.serialize_aws_json_1_0(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_opensearchmemory.types.tag_key_list

        out["tag_keys"] = (
            capo_opensearchmemory.types.tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
