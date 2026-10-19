"""Generated from Smithy shape ``com.amazonaws.iam#TagTemplate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.tag_template_key_type
    import capo_iam.types.tag_template_value_type


class TagTemplate(TypedDict, closed=True):
    key: "capo_iam.types.tag_template_key_type.tagTemplateKeyType"
    """<p>The key name of the tag.</p>"""
    value: "capo_iam.types.tag_template_value_type.tagTemplateValueType"
    """<p>The value associated with the tag key.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TagTemplate, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Key", str(value["key"])))
    pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_query(el: Element) -> TagTemplate:
    out: TagTemplate = {}  # type: ignore[typeddict-item]
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
