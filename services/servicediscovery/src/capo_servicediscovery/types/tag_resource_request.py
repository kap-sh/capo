"""Generated from Smithy shape ``com.amazonaws.servicediscovery#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_servicediscovery.types.amazon_resource_name
    import capo_servicediscovery.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_servicediscovery.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the resource that you want to retrieve tags for.</p>"""
    tags: "capo_servicediscovery.types.tag_list.TagList"
    """<p>The tags to add to the specified resource. Specifying the tag key is required. You can set the value of a tag to an empty string, but you can't set the value of a tag to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceARN"] = value["resource_arn"]
    import capo_servicediscovery.types.tag_list

    out["Tags"] = capo_servicediscovery.types.tag_list.serialize_aws_json_1_1(
        value["tags"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceARN") is not None:
        out["resource_arn"] = data["ResourceARN"]
    else:
        out["resource_arn"] = ""
    if data.get("Tags") is not None:
        import capo_servicediscovery.types.tag_list

        out["tags"] = capo_servicediscovery.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
