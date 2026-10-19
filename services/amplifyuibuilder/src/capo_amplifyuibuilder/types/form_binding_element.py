"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FormBindingElement``."""

from typing_extensions import TypedDict


class FormBindingElement(TypedDict, closed=True):
    element: "str"
    """<p>The name of the component to retrieve a value from.</p>"""
    property: "str"
    """<p>The property to retrieve a value from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormBindingElement) -> dict:
    out: dict = {}
    out["element"] = value["element"]
    out["property"] = value["property"]
    return out


def deserialize_json(data: dict) -> FormBindingElement:
    out: FormBindingElement = {}  # type: ignore[typeddict-item]
    if data.get("element") is not None:
        out["element"] = data["element"]
    else:
        out["element"] = ""
    if data.get("property") is not None:
        out["property"] = data["property"]
    else:
        out["property"] = ""
    return out
