"""Generated from Smithy shape ``com.amazonaws.quicksight#CustomColor``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.field_value
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.special_value


class CustomColor(TypedDict, closed=True):
    field_value: NotRequired["capo_quicksight.types.field_value.FieldValue"]
    """<p>The data value that the color is applied to.</p>"""
    color: "capo_quicksight.types.hex_color.HexColor"
    """<p>The color that is applied to the data value.</p>"""
    special_value: NotRequired["capo_quicksight.types.special_value.SpecialValue"]
    """<p>The value of a special data value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomColor) -> dict:
    out: dict = {}
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    out["Color"] = value["color"]
    if "special_value" in value:
        import capo_quicksight.types.special_value

        out["SpecialValue"] = capo_quicksight.types.special_value.serialize_json(
            value["special_value"]
        )
    return out


def deserialize_json(data: dict) -> CustomColor:
    out: CustomColor = {}  # type: ignore[typeddict-item]
    if data.get("FieldValue") is not None:
        out["field_value"] = data["FieldValue"]
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    else:
        raise DeserializationError("CustomColor.color required")
    if data.get("SpecialValue") is not None:
        import capo_quicksight.types.special_value

        out["special_value"] = capo_quicksight.types.special_value.deserialize_json(
            data["SpecialValue"]
        )
    return out


def redact_sensitive(value: CustomColor) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_value" in value:
        out["field_value"] = "*** Sensitive Data Redacted ***"
    return out
