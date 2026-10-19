"""Generated from Smithy shape ``com.amazonaws.s3control#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.tag_key_string
    import capo_s3_control.types.tag_value_string


class Tag(TypedDict, closed=True):
    key: "capo_s3_control.types.tag_key_string.TagKeyString"
    """<p>The key of the key-value pair of a tag added to your Amazon Web Services resource. A tag key can be up to 128 Unicode characters in length and is case-sensitive. System created tags that begin with <code>aws:</code> aren’t supported. </p>"""
    value: "capo_s3_control.types.tag_value_string.TagValueString"
    """<p> The value of the key-value pair of a tag added to your Amazon Web Services resource. A tag value can be up to 256 Unicode characters in length and is case-sensitive. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: Tag, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Key").text = str(value["key"])
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> Tag:
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
