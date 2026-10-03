"""Generated from Smithy shape ``com.amazonaws.rds#RemoveTagsFromResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.key_list
    import capo_rds.types.string


class RemoveTagsFromResourceMessage(TypedDict, closed=True):
    resource_name: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon RDS resource that the tags are removed from. This value is an Amazon Resource Name (ARN). For information about creating an ARN, see <a href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.ARN.html#USER_Tagging.ARN.Constructing"> Constructing an ARN for Amazon RDS</a> in the <i>Amazon RDS User Guide.</i> </p>"""
    tag_keys: NotRequired["capo_rds.types.key_list.KeyList"]
    """<p>The tag key (name) of the tag to be removed.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveTagsFromResourceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_name" in value:
        pairs.append((f"{key_prefix}ResourceName", str(value["resource_name"])))
    if "tag_keys" in value:
        import capo_rds.types.key_list

        capo_rds.types.key_list.serialize_query(
            value["tag_keys"], pairs, f"{key_prefix}TagKeys"
        )


def deserialize_query(el: Element) -> RemoveTagsFromResourceMessage:
    out: RemoveTagsFromResourceMessage = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_rds.types.key_list

        out["tag_keys"] = capo_rds.types.key_list.deserialize_query(child_tag_keys)
    return out
