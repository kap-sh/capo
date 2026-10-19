"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancing#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing.types.tag_key
    import capo_elastic_load_balancing.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_elastic_load_balancing.types.tag_key.TagKey"
    """<p>The key of the tag.</p>"""
    value: NotRequired["capo_elastic_load_balancing.types.tag_value.TagValue"]
    """<p>The value of the tag.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Tag, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Key", str(value["key"])))
    if "value" in value:
        pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_query(el: Element) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    child_key = el.find("Key")
    if child_key is not None:
        out["key"] = str(child_key.text or "")
    else:
        out["key"] = ""
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    return out
