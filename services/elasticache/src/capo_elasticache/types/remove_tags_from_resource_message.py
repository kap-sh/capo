"""Generated from Smithy shape ``com.amazonaws.elasticache#RemoveTagsFromResourceMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.key_list
    import capo_elasticache.types.string


class RemoveTagsFromResourceMessage(TypedDict, closed=True):
    resource_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the resource from which you want the tags removed, for example <code>arn:aws:elasticache:us-west-2:0123456789:cluster:myCluster</code> or <code>arn:aws:elasticache:us-west-2:0123456789:snapshot:mySnapshot</code>.</p> <p>For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Service Namespaces</a>.</p>"""
    tag_keys: NotRequired["capo_elasticache.types.key_list.KeyList"]
    """<p>A list of <code>TagKeys</code> identifying the tags you want removed from the named resource.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: RemoveTagsFromResourceMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "resource_name" in value:
        pairs.append((f"{key_prefix}ResourceName", str(value["resource_name"])))
    if "tag_keys" in value:
        import capo_elasticache.types.key_list

        capo_elasticache.types.key_list.serialize_query(
            value["tag_keys"], pairs, f"{key_prefix}TagKeys"
        )


def deserialize_query(el: Element) -> RemoveTagsFromResourceMessage:
    out: RemoveTagsFromResourceMessage = {}  # type: ignore[typeddict-item]
    child_resource_name = el.find("ResourceName")
    if child_resource_name is not None:
        out["resource_name"] = str(child_resource_name.text or "")
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_elasticache.types.key_list

        out["tag_keys"] = capo_elasticache.types.key_list.deserialize_query(
            child_tag_keys
        )
    return out
