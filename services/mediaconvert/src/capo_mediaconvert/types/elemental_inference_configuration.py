"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconvert.types.__list_of_elemental_inference_feature
    import capo_mediaconvert.types.__list_of_elemental_inference_feed


class ElementalInferenceConfiguration(TypedDict, closed=True):
    features: NotRequired[
        "capo_mediaconvert.types.__list_of_elemental_inference_feature.__listOfElementalInferenceFeature"
    ]
    """A list of Elemental Inference features used in this job."""
    feeds: NotRequired[
        "capo_mediaconvert.types.__list_of_elemental_inference_feed.__listOfElementalInferenceFeed"
    ]
    """A list of Elemental Inference feeds created during this job."""


# --- restJson1 ser/de ---
def serialize_json(value: ElementalInferenceConfiguration) -> dict:
    out: dict = {}
    if "features" in value:
        import capo_mediaconvert.types.__list_of_elemental_inference_feature

        out["features"] = (
            capo_mediaconvert.types.__list_of_elemental_inference_feature.serialize_json(
                value["features"]
            )
        )
    if "feeds" in value:
        import capo_mediaconvert.types.__list_of_elemental_inference_feed

        out["feeds"] = (
            capo_mediaconvert.types.__list_of_elemental_inference_feed.serialize_json(
                value["feeds"]
            )
        )
    return out


def deserialize_json(data: dict) -> ElementalInferenceConfiguration:
    out: ElementalInferenceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("features") is not None:
        import capo_mediaconvert.types.__list_of_elemental_inference_feature

        out["features"] = (
            capo_mediaconvert.types.__list_of_elemental_inference_feature.deserialize_json(
                data["features"]
            )
        )
    if data.get("feeds") is not None:
        import capo_mediaconvert.types.__list_of_elemental_inference_feed

        out["feeds"] = (
            capo_mediaconvert.types.__list_of_elemental_inference_feed.deserialize_json(
                data["feeds"]
            )
        )
    return out
