"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MetricProcessingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_location


class MetricProcessingConfig(TypedDict, closed=True):
    compute_location: "capo_iotsitewise.types.compute_location.ComputeLocation"
    """<p>The compute location for the given metric property. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricProcessingConfig) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.compute_location

    out["computeLocation"] = capo_iotsitewise.types.compute_location.serialize_json(
        value["compute_location"]
    )
    return out


def deserialize_json(data: dict) -> MetricProcessingConfig:
    out: MetricProcessingConfig = {}  # type: ignore[typeddict-item]
    if data.get("computeLocation") is not None:
        import capo_iotsitewise.types.compute_location

        out["compute_location"] = (
            capo_iotsitewise.types.compute_location.deserialize_json(
                data["computeLocation"]
            )
        )
    else:
        import typing

        out["compute_location"] = typing.cast(
            "capo_iotsitewise.types.compute_location.ComputeLocation", ""
        )
    return out
