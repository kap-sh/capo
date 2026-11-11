"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceFeedConfigurationSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__string_pattern_arn_aws_elemental_inference_feed_az0919


class ElementalInferenceFeedConfigurationSource(TypedDict, closed=True):
    feed_arn: NotRequired[
        "capo_mediaconvert.types.__string_pattern_arn_aws_elemental_inference_feed_az0919.__stringPatternArnAwsElementalInferenceFeedAZ0919"
    ]
    """The ARN of an Elemental Inference Feed."""


# --- restJson1 ser/de ---
def serialize_json(value: ElementalInferenceFeedConfigurationSource) -> dict:
    out: dict = {}
    if "feed_arn" in value:
        out["feedArn"] = value["feed_arn"]
    return out


def deserialize_json(data: dict) -> ElementalInferenceFeedConfigurationSource:
    out: ElementalInferenceFeedConfigurationSource = {}  # type: ignore[typeddict-item]
    if data.get("feedArn") is not None:
        out["feed_arn"] = data["feedArn"]
    return out
