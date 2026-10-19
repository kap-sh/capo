"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldOption``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.field_option_name
    import capo_connectcases.types.field_option_value


class FieldOption(TypedDict, closed=True):
    name: "capo_connectcases.types.field_option_name.FieldOptionName"
    """<p> <code>FieldOptionName</code> has max length 100 and disallows trailing spaces.</p>"""
    value: "capo_connectcases.types.field_option_value.FieldOptionValue"
    """<p> <code>FieldOptionValue</code> has max length 100 and must be alphanumeric with hyphens and underscores.</p>"""
    active: "bool"
    """<p>Describes whether the <code>FieldOption</code> is active (displayed) or inactive.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldOption) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["value"] = value["value"]
    out["active"] = value["active"]
    return out


def deserialize_json(data: dict) -> FieldOption:
    out: FieldOption = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    if data.get("active") is not None:
        out["active"] = data["active"]
    else:
        out["active"] = False
    return out
