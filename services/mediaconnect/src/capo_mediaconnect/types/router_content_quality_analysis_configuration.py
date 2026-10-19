"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RouterContentQualityAnalysisConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mediaconnect.errors import DeserializationError, SerializationError
from capo_mediaconnect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mediaconnect.types.content_quality_analysis_feature_configuration


class _RouterContentQualityAnalysisConfiguration_ContentLevel(TypedDict, closed=True):
    ContentLevel: "capo_mediaconnect.types.content_quality_analysis_feature_configuration.ContentQualityAnalysisFeatureConfiguration"


RouterContentQualityAnalysisConfiguration: TypeAlias = (
    _RouterContentQualityAnalysisConfiguration_ContentLevel | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RouterContentQualityAnalysisConfiguration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"RouterContentQualityAnalysisConfiguration: cannot serialize unknown variant {value.name!r}"
        )
    elif "ContentLevel" in value:
        import capo_mediaconnect.types.content_quality_analysis_feature_configuration

        return {
            "contentLevel": capo_mediaconnect.types.content_quality_analysis_feature_configuration.serialize_json(
                value["ContentLevel"]
            )
        }
    else:
        raise SerializationError(
            "RouterContentQualityAnalysisConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RouterContentQualityAnalysisConfiguration:
    if data.get("contentLevel") is not None:
        import capo_mediaconnect.types.content_quality_analysis_feature_configuration

        return {
            "ContentLevel": capo_mediaconnect.types.content_quality_analysis_feature_configuration.deserialize_json(
                data["contentLevel"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "RouterContentQualityAnalysisConfiguration: no recognized variant key"
        )
