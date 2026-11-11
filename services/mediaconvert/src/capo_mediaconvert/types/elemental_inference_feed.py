"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceFeed``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string
    import capo_mediaconvert.types.elemental_inference_feed_management_state


class ElementalInferenceFeed(TypedDict, closed=True):
    arn: NotRequired["capo_mediaconvert.types.__string.__string"]
    """The ARN of an AWS Elemental Inference Feed."""
    feed_management_state: NotRequired[
        "capo_mediaconvert.types.elemental_inference_feed_management_state.ElementalInferenceFeedManagementState"
    ]
    """Elemental Inference Feed management state."""


# --- restJson1 ser/de ---
def serialize_json(value: ElementalInferenceFeed) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "feed_management_state" in value:
        import capo_mediaconvert.types.elemental_inference_feed_management_state

        out["feedManagementState"] = (
            capo_mediaconvert.types.elemental_inference_feed_management_state.serialize_json(
                value["feed_management_state"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElementalInferenceFeed:
    out: ElementalInferenceFeed = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("feedManagementState") is not None:
        import capo_mediaconvert.types.elemental_inference_feed_management_state

        out["feed_management_state"] = (
            capo_mediaconvert.types.elemental_inference_feed_management_state.deserialize_json(
                data["feedManagementState"]
            )
        )
    return out
