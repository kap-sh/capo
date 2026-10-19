"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TransformProcessingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_location
    import capo_iotsitewise.types.forwarding_config


class TransformProcessingConfig(TypedDict, closed=True):
    compute_location: "capo_iotsitewise.types.compute_location.ComputeLocation"
    """<p>The compute location for the given transform property. </p>"""
    forwarding_config: NotRequired[
        "capo_iotsitewise.types.forwarding_config.ForwardingConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TransformProcessingConfig) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.compute_location

    out["computeLocation"] = capo_iotsitewise.types.compute_location.serialize_json(
        value["compute_location"]
    )
    if "forwarding_config" in value:
        import capo_iotsitewise.types.forwarding_config

        out["forwardingConfig"] = (
            capo_iotsitewise.types.forwarding_config.serialize_json(
                value["forwarding_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> TransformProcessingConfig:
    out: TransformProcessingConfig = {}  # type: ignore[typeddict-item]
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
    if data.get("forwardingConfig") is not None:
        import capo_iotsitewise.types.forwarding_config

        out["forwarding_config"] = (
            capo_iotsitewise.types.forwarding_config.deserialize_json(
                data["forwardingConfig"]
            )
        )
    return out
