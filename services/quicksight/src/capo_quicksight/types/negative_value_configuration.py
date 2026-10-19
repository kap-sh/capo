"""Generated from Smithy shape ``com.amazonaws.quicksight#NegativeValueConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.negative_value_display_mode


class NegativeValueConfiguration(TypedDict, closed=True):
    display_mode: (
        "capo_quicksight.types.negative_value_display_mode.NegativeValueDisplayMode"
    )
    """<p>Determines the display mode of the negative value configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NegativeValueConfiguration) -> dict:
    out: dict = {}
    import capo_quicksight.types.negative_value_display_mode

    out["DisplayMode"] = (
        capo_quicksight.types.negative_value_display_mode.serialize_json(
            value["display_mode"]
        )
    )
    return out


def deserialize_json(data: dict) -> NegativeValueConfiguration:
    out: NegativeValueConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("DisplayMode") is not None:
        import capo_quicksight.types.negative_value_display_mode

        out["display_mode"] = (
            capo_quicksight.types.negative_value_display_mode.deserialize_json(
                data["DisplayMode"]
            )
        )
    else:
        import typing

        out["display_mode"] = typing.cast(
            "capo_quicksight.types.negative_value_display_mode.NegativeValueDisplayMode",
            "",
        )
    return out
