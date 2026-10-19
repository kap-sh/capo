"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormInputValuePropertyBindingProperties``."""

from typing_extensions import NotRequired, TypedDict


class FormInputValuePropertyBindingProperties(TypedDict, closed=True):
    property: "str"
    """<p>The form property to bind to the data field.</p>"""
    field: NotRequired["str"]
    """<p>The data field to bind the property to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputValuePropertyBindingProperties) -> dict:
    out: dict = {}
    out["property"] = value["property"]
    if "field" in value:
        out["field"] = value["field"]
    return out


def deserialize_json(data: dict) -> FormInputValuePropertyBindingProperties:
    out: FormInputValuePropertyBindingProperties = {}  # type: ignore[typeddict-item]
    if data.get("property") is not None:
        out["property"] = data["property"]
    else:
        out["property"] = ""
    if data.get("field") is not None:
        out["field"] = data["field"]
    return out
