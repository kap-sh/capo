"""Generated from Smithy shape ``com.amazonaws.sns#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.amazon_resource_name
    import capo_sns.types.tag_key_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_sns.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the topic from which to remove tags.</p>"""
    tag_keys: "capo_sns.types.tag_key_list.TagKeyList"
    """<p>The list of tag keys to remove from the specified topic.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: UntagResourceRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}ResourceArn", str(value["resource_arn"])))
    import capo_sns.types.tag_key_list

    capo_sns.types.tag_key_list.serialize_query(
        value["tag_keys"], pairs, f"{key_prefix}TagKeys"
    )


def deserialize_query(el: Element) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    child_resource_arn = el.find("ResourceArn")
    if child_resource_arn is not None:
        out["resource_arn"] = str(child_resource_arn.text or "")
    else:
        out["resource_arn"] = ""
    child_tag_keys = el.find("TagKeys")
    if child_tag_keys is not None:
        import capo_sns.types.tag_key_list

        out["tag_keys"] = capo_sns.types.tag_key_list.deserialize_query(child_tag_keys)
    else:
        out["tag_keys"] = []
    return out
