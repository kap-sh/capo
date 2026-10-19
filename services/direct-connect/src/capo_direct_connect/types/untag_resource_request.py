"""Generated from Smithy shape ``com.amazonaws.directconnect#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_direct_connect.types.resource_arn
    import capo_direct_connect.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_direct_connect.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tag_keys: "capo_direct_connect.types.tag_key_list.TagKeyList"
    """<p>The tag keys of the tags to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_direct_connect.types.tag_key_list

    out["tagKeys"] = capo_direct_connect.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_direct_connect.types.tag_key_list

        out["tag_keys"] = (
            capo_direct_connect.types.tag_key_list.deserialize_aws_json_1_1(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
