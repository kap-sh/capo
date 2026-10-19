"""Generated from Smithy shape ``com.amazonaws.sns#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_sns._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sns.types.tag_key
    import capo_sns.types.tag_value


class Tag(TypedDict, closed=True):
    key: "capo_sns.types.tag_key.TagKey"
    """<p>The required key portion of the tag.</p>"""
    value: "capo_sns.types.tag_value.TagValue"
    """<p>The optional value portion of the tag.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Tag, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Key", str(value["key"])))
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
    else:
        out["value"] = ""
    return out
