"""Generated from Smithy shape ``com.amazonaws.dax#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dax.types.string
    import capo_dax.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_name: "capo_dax.types.string.String"
    """<p>The name of the DAX resource to which tags should be added.</p>"""
    tags: "capo_dax.types.tag_list.TagList"
    """<p>The tags to be assigned to the DAX resource. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    import capo_dax.types.tag_list

    out["Tags"] = capo_dax.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    else:
        out["resource_name"] = ""
    if data.get("Tags") is not None:
        import capo_dax.types.tag_list

        out["tags"] = capo_dax.types.tag_list.deserialize_aws_json_1_1(data["Tags"])
    else:
        out["tags"] = []
    return out
