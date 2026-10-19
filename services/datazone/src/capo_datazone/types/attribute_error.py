"""Generated from Smithy shape ``com.amazonaws.datazone#AttributeError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.attribute_identifier


class AttributeError(TypedDict, closed=True):
    attribute_identifier: "capo_datazone.types.attribute_identifier.AttributeIdentifier"
    """<p>The attribute ID as part of the attribute error.</p>"""
    code: "str"
    """<p>The code generated as part of the attribute error.</p>"""
    message: "str"
    """<p>The message generated as part of the attribute error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeError) -> dict:
    out: dict = {}
    out["attributeIdentifier"] = value["attribute_identifier"]
    out["code"] = value["code"]
    out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> AttributeError:
    out: AttributeError = {}  # type: ignore[typeddict-item]
    if data.get("attributeIdentifier") is not None:
        out["attribute_identifier"] = data["attributeIdentifier"]
    else:
        out["attribute_identifier"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    return out
