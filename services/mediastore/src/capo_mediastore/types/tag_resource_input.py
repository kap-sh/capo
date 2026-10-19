"""Generated from Smithy shape ``com.amazonaws.mediastore#TagResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mediastore.types.container_arn
    import capo_mediastore.types.tag_list


class TagResourceInput(TypedDict, closed=True):
    resource: "capo_mediastore.types.container_arn.ContainerARN"
    """<p>The Amazon Resource Name (ARN) for the container. </p>"""
    tags: "capo_mediastore.types.tag_list.TagList"
    """<p>An array of key:value pairs that you want to add to the container. You need to specify only the tags that you want to add or update. For example, suppose a container already has two tags (customer:CompanyA and priority:High). You want to change the priority tag and also add a third tag (type:Contract). For TagResource, you specify the following tags: priority:Medium, type:Contract. The result is that your container has three tags: customer:CompanyA, priority:Medium, and type:Contract.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceInput) -> dict:
    out: dict = {}
    out["Resource"] = value["resource"]
    import capo_mediastore.types.tag_list

    out["Tags"] = capo_mediastore.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceInput:
    out: TagResourceInput = {}  # type: ignore[typeddict-item]
    if data.get("Resource") is not None:
        out["resource"] = data["Resource"]
    else:
        out["resource"] = ""
    if data.get("Tags") is not None:
        import capo_mediastore.types.tag_list

        out["tags"] = capo_mediastore.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        out["tags"] = []
    return out
