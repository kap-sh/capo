"""Generated from Smithy shape ``com.amazonaws.quicksight#ColorsConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.custom_colors_list


class ColorsConfiguration(TypedDict, closed=True):
    custom_colors: NotRequired[
        "capo_quicksight.types.custom_colors_list.CustomColorsList"
    ]
    """<p>A list of up to 50 custom colors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColorsConfiguration) -> dict:
    out: dict = {}
    if "custom_colors" in value:
        import capo_quicksight.types.custom_colors_list

        out["CustomColors"] = capo_quicksight.types.custom_colors_list.serialize_json(
            value["custom_colors"]
        )
    return out


def deserialize_json(data: dict) -> ColorsConfiguration:
    out: ColorsConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("CustomColors") is not None:
        import capo_quicksight.types.custom_colors_list

        out["custom_colors"] = (
            capo_quicksight.types.custom_colors_list.deserialize_json(
                data["CustomColors"]
            )
        )
    return out


def redact_sensitive(value: ColorsConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "custom_colors" in value:
        import capo_quicksight.types.custom_colors_list

        out["custom_colors"] = (
            capo_quicksight.types.custom_colors_list.redact_sensitive(
                value["custom_colors"]
            )
        )
    return out
