"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.tag_list
    import capo_partnercentral_channel.types.taggable_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_partnercentral_channel.types.taggable_arn.TaggableArn"
    """<p>The Amazon Resource Name (ARN) of the resource to tag.</p>"""
    tags: "capo_partnercentral_channel.types.tag_list.TagList"
    """<p>Key-value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    import capo_partnercentral_channel.types.tag_list

    out["tags"] = capo_partnercentral_channel.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("tags") is not None:
        import capo_partnercentral_channel.types.tag_list

        out["tags"] = (
            capo_partnercentral_channel.types.tag_list.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    else:
        out["tags"] = []
    return out
