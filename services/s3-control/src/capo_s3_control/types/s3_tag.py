"""Generated from Smithy shape ``com.amazonaws.s3control#S3Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3_control._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3_control.types.tag_key_string
    import capo_s3_control.types.tag_value_string


class S3Tag(TypedDict, closed=True):
    key: "capo_s3_control.types.tag_key_string.TagKeyString"
    """<p>Key of the tag</p>"""
    value: "capo_s3_control.types.tag_value_string.TagValueString"
    """<p>Value of the tag</p>"""


# --- restXml ser/de ---
def serialize_xml(value: S3Tag, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Key").text = str(value["key"])
    SubElement(el, "Value").text = str(value["value"])


def deserialize_xml(el: Element) -> S3Tag:
    out: S3Tag = {}  # type: ignore[typeddict-item]
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
