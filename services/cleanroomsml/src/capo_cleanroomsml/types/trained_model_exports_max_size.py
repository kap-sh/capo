"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportsMaxSize``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_exports_max_size_unit_type
    import capo_cleanroomsml.types.trained_model_exports_max_size_value


class TrainedModelExportsMaxSize(TypedDict, closed=True):
    unit: "capo_cleanroomsml.types.trained_model_exports_max_size_unit_type.TrainedModelExportsMaxSizeUnitType"
    """<p>The unit of measurement for the data size.</p>"""
    value: "capo_cleanroomsml.types.trained_model_exports_max_size_value.TrainedModelExportsMaxSizeValue"
    """<p>The maximum size of the dataset to export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportsMaxSize) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.trained_model_exports_max_size_unit_type

    out["unit"] = (
        capo_cleanroomsml.types.trained_model_exports_max_size_unit_type.serialize_json(
            value["unit"]
        )
    )
    out["value"] = (
        "NaN"
        if value["value"] != value["value"]
        else "Infinity"
        if value["value"] == float("inf")
        else "-Infinity"
        if value["value"] == float("-inf")
        else value["value"]
    )
    return out


def deserialize_json(data: dict) -> TrainedModelExportsMaxSize:
    out: TrainedModelExportsMaxSize = {}  # type: ignore[typeddict-item]
    if data.get("unit") is not None:
        import capo_cleanroomsml.types.trained_model_exports_max_size_unit_type

        out["unit"] = (
            capo_cleanroomsml.types.trained_model_exports_max_size_unit_type.deserialize_json(
                data["unit"]
            )
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_cleanroomsml.types.trained_model_exports_max_size_unit_type.TrainedModelExportsMaxSizeUnitType",
            "",
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0.0
    return out
