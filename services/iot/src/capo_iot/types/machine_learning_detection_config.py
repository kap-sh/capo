"""Generated from Smithy shape ``com.amazonaws.iot#MachineLearningDetectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.confidence_level


class MachineLearningDetectionConfig(TypedDict, closed=True):
    confidence_level: "capo_iot.types.confidence_level.ConfidenceLevel"
    """<p> The sensitivity of anomalous behavior evaluation. Can be <code>Low</code>, <code>Medium</code>, or <code>High</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningDetectionConfig) -> dict:
    out: dict = {}
    import capo_iot.types.confidence_level

    out["confidenceLevel"] = capo_iot.types.confidence_level.serialize_json(
        value["confidence_level"]
    )
    return out


def deserialize_json(data: dict) -> MachineLearningDetectionConfig:
    out: MachineLearningDetectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("confidenceLevel") is not None:
        import capo_iot.types.confidence_level

        out["confidence_level"] = capo_iot.types.confidence_level.deserialize_json(
            data["confidenceLevel"]
        )
    else:
        import typing

        out["confidence_level"] = typing.cast(
            "capo_iot.types.confidence_level.ConfidenceLevel", ""
        )
    return out
