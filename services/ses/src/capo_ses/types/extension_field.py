"""Generated from Smithy shape ``com.amazonaws.ses#ExtensionField``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element
from capo_ses.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ses.types.extension_field_name
    import capo_ses.types.extension_field_value


class ExtensionField(TypedDict, closed=True):
    name: "capo_ses.types.extension_field_name.ExtensionFieldName"
    """<p>The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.</p>"""
    value: "capo_ses.types.extension_field_value.ExtensionFieldValue"
    r"""<p>The value of the header to add. Must contain 2048 characters or fewer, and must not contain newline characters ("\r" or "\n").</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ExtensionField, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}Name", str(value["name"])))
    pairs.append((f"{key_prefix}Value", str(value["value"])))


def deserialize_query(el: Element) -> ExtensionField:
    out: ExtensionField = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("ExtensionField.name required")
    child_value = el.find("Value")
    if child_value is not None:
        out["value"] = str(child_value.text or "")
    else:
        raise DeserializationError("ExtensionField.value required")
    return out
