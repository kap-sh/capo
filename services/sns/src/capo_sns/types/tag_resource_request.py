"""Generated from Smithy shape ``com.amazonaws.sns#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.amazon_resource_name
    import capo_sns.types.tag_list


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_sns.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the topic to which to add tags.</p>"""
    tags: "capo_sns.types.tag_list.TagList"
    """<p>The tags to be added to the specified topic. A tag consists of a required key and an optional value.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagResourceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    import capo_sns.types.tag_list

    capo_sns.types.tag_list.serialize_query(value["tags"], pairs, f"{key_prefix}Tags")


def deserialize_query(el: Element) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        out["resource_arn"] = ""
    child_tags = el.find("Tags")
    if child_tags is not None:
        import capo_sns.types.tag_list

        out["tags"] = capo_sns.types.tag_list.deserialize_query(child_tags)
    else:
        out["tags"] = []
    return out
