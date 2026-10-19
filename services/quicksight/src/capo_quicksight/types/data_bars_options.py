"""Generated from Smithy shape ``com.amazonaws.quicksight#DataBarsOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.field_id
    import capo_quicksight.types.hex_color


class DataBarsOptions(TypedDict, closed=True):
    field_id: "capo_quicksight.types.field_id.FieldId"
    """<p>The field ID for the data bars options.</p>"""
    positive_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color of the positive data bar.</p>"""
    negative_color: NotRequired["capo_quicksight.types.hex_color.HexColor"]
    """<p>The color of the negative data bar.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataBarsOptions) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "positive_color" in value:
        out["PositiveColor"] = value["positive_color"]
    if "negative_color" in value:
        out["NegativeColor"] = value["negative_color"]
    return out


def deserialize_json(data: dict) -> DataBarsOptions:
    out: DataBarsOptions = {}  # type: ignore[typeddict-item]
    if data.get("FieldId") is not None:
        out["field_id"] = data["FieldId"]
    else:
        out["field_id"] = ""
    if data.get("PositiveColor") is not None:
        out["positive_color"] = data["PositiveColor"]
    if data.get("NegativeColor") is not None:
        out["negative_color"] = data["NegativeColor"]
    return out
