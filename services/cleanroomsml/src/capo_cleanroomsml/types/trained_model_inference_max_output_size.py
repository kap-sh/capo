"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelInferenceMaxOutputSize``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type
    import capo_cleanroomsml.types.trained_model_inference_max_output_size_value


class TrainedModelInferenceMaxOutputSize(TypedDict, closed=True):
    unit: "capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type.TrainedModelInferenceMaxOutputSizeUnitType"
    """<p>The measurement unit to use.</p>"""
    value: "capo_cleanroomsml.types.trained_model_inference_max_output_size_value.TrainedModelInferenceMaxOutputSizeValue"
    """<p>The maximum output size value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelInferenceMaxOutputSize) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type

    out["unit"] = (
        capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type.serialize_json(
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


def deserialize_json(data: dict) -> TrainedModelInferenceMaxOutputSize:
    out: TrainedModelInferenceMaxOutputSize = {}  # type: ignore[typeddict-item]
    if data.get("unit") is not None:
        import capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type

        out["unit"] = (
            capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type.deserialize_json(
                data["unit"]
            )
        )
    else:
        import typing

        out["unit"] = typing.cast(
            "capo_cleanroomsml.types.trained_model_inference_max_output_size_unit_type.TrainedModelInferenceMaxOutputSizeUnitType",
            "",
        )
    if data.get("value") is not None:
        out["value"] = float(data["value"])
    else:
        out["value"] = 0.0
    return out
