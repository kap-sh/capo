"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPathColor``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.data_path_value
    import capo_quicksight.types.hex_color
    import capo_quicksight.types.time_granularity


class DataPathColor(TypedDict, closed=True):
    element: "capo_quicksight.types.data_path_value.DataPathValue"
    """<p>The element that the color needs to be applied to.</p>"""
    color: "capo_quicksight.types.hex_color.HexColor"
    """<p>The color that needs to be applied to the element.</p>"""
    time_granularity: NotRequired[
        "capo_quicksight.types.time_granularity.TimeGranularity"
    ]
    """<p>The time granularity of the field that the color needs to be applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPathColor) -> dict:
    out: dict = {}
    import capo_quicksight.types.data_path_value

    out["Element"] = capo_quicksight.types.data_path_value.serialize_json(
        value["element"]
    )
    out["Color"] = value["color"]
    if "time_granularity" in value:
        import capo_quicksight.types.time_granularity

        out["TimeGranularity"] = capo_quicksight.types.time_granularity.serialize_json(
            value["time_granularity"]
        )
    return out


def deserialize_json(data: dict) -> DataPathColor:
    out: DataPathColor = {}  # type: ignore[typeddict-item]
    if data.get("Element") is not None:
        import capo_quicksight.types.data_path_value

        out["element"] = capo_quicksight.types.data_path_value.deserialize_json(
            data["Element"]
        )
    else:
        raise DeserializationError("DataPathColor.element required")
    if data.get("Color") is not None:
        out["color"] = data["Color"]
    else:
        raise DeserializationError("DataPathColor.color required")
    if data.get("TimeGranularity") is not None:
        import capo_quicksight.types.time_granularity

        out["time_granularity"] = (
            capo_quicksight.types.time_granularity.deserialize_json(
                data["TimeGranularity"]
            )
        )
    return out


def redact_sensitive(value: DataPathColor) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "element" in value:
        import capo_quicksight.types.data_path_value

        out["element"] = capo_quicksight.types.data_path_value.redact_sensitive(
            value["element"]
        )
    return out
