"""Generated from Smithy shape ``com.amazonaws.quicksight#KPIVisualStandardLayout``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.kpi_visual_standard_layout_type


class KPIVisualStandardLayout(TypedDict, closed=True):
    type: "capo_quicksight.types.kpi_visual_standard_layout_type.KPIVisualStandardLayoutType"
    """<p>The standard layout type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KPIVisualStandardLayout) -> dict:
    out: dict = {}
    import capo_quicksight.types.kpi_visual_standard_layout_type

    out["Type"] = capo_quicksight.types.kpi_visual_standard_layout_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> KPIVisualStandardLayout:
    out: KPIVisualStandardLayout = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_quicksight.types.kpi_visual_standard_layout_type

        out["type"] = (
            capo_quicksight.types.kpi_visual_standard_layout_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_quicksight.types.kpi_visual_standard_layout_type.KPIVisualStandardLayoutType",
            "",
        )
    return out
