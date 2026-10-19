"""Generated from Smithy shape ``com.amazonaws.dax#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dax.types.key_list
    import capo_dax.types.string


class UntagResourceRequest(TypedDict, closed=True):
    resource_name: "capo_dax.types.string.String"
    """<p>The name of the DAX resource from which the tags should be removed.</p>"""
    tag_keys: "capo_dax.types.key_list.KeyList"
    """<p>A list of tag keys. If the DAX cluster has any tags with these keys, then the tags are removed from the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    import capo_dax.types.key_list

    out["TagKeys"] = capo_dax.types.key_list.serialize_aws_json_1_1(value["tag_keys"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceName") is not None:
        out["resource_name"] = data["ResourceName"]
    else:
        out["resource_name"] = ""
    if data.get("TagKeys") is not None:
        import capo_dax.types.key_list

        out["tag_keys"] = capo_dax.types.key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        out["tag_keys"] = []
    return out
