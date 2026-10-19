"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.tag_list
    import capo_partnercentral_selling.types.taggable_resource_arn


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: (
        "capo_partnercentral_selling.types.taggable_resource_arn.TaggableResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>"""
    tags: "capo_partnercentral_selling.types.tag_list.TagList"
    """<p>A map of the key-value pairs of the tag or tags to assign.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    import capo_partnercentral_selling.types.tag_list

    out["Tags"] = capo_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_partnercentral_selling.types.tag_list

        out["tags"] = (
            capo_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    else:
        out["tags"] = []
    return out
