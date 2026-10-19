"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.tag_key_list
    import capo_partnercentral_benefits.types.taggable_resource_arn


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_benefits.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource to remove tags from.</p>"""
    tag_keys: "capo_partnercentral_benefits.types.tag_key_list.TagKeyList"
    """<p>A list of tag keys to remove from the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_partnercentral_benefits.types.tag_key_list

    out["tagKeys"] = (
        capo_partnercentral_benefits.types.tag_key_list.serialize_aws_json_1_0(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tagKeys") is not None:
        import capo_partnercentral_benefits.types.tag_key_list

        out["tag_keys"] = (
            capo_partnercentral_benefits.types.tag_key_list.deserialize_aws_json_1_0(
                data["tagKeys"]
            )
        )
    else:
        out["tag_keys"] = []
    return out
