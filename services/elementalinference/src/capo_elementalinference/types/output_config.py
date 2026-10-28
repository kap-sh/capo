"""Generated from Smithy shape ``com.amazonaws.elementalinference#OutputConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_elementalinference.errors import DeserializationError, SerializationError
from capo_elementalinference.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_elementalinference.types.clipping_config
    import capo_elementalinference.types.contextual_metadata_config
    import capo_elementalinference.types.cropping_config
    import capo_elementalinference.types.subtitling_config


class OutputConfigCroppingMember(TypedDict, closed=True):
    cropping: "capo_elementalinference.types.cropping_config.CroppingConfig"


class OutputConfigClippingMember(TypedDict, closed=True):
    clipping: "capo_elementalinference.types.clipping_config.ClippingConfig"


class OutputConfigSubtitlingMember(TypedDict, closed=True):
    subtitling: "capo_elementalinference.types.subtitling_config.SubtitlingConfig"


class OutputConfigContextualMetadataMember(TypedDict, closed=True):
    contextualMetadata: "capo_elementalinference.types.contextual_metadata_config.ContextualMetadataConfig"


OutputConfig: TypeAlias = (
    OutputConfigCroppingMember
    | OutputConfigClippingMember
    | OutputConfigSubtitlingMember
    | OutputConfigContextualMetadataMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: OutputConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"OutputConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "cropping" in value:
        import capo_elementalinference.types.cropping_config

        return {
            "cropping": capo_elementalinference.types.cropping_config.serialize_json(
                value["cropping"]
            )
        }
    elif "clipping" in value:
        import capo_elementalinference.types.clipping_config

        return {
            "clipping": capo_elementalinference.types.clipping_config.serialize_json(
                value["clipping"]
            )
        }
    elif "subtitling" in value:
        import capo_elementalinference.types.subtitling_config

        return {
            "subtitling": capo_elementalinference.types.subtitling_config.serialize_json(
                value["subtitling"]
            )
        }
    elif "contextualMetadata" in value:
        import capo_elementalinference.types.contextual_metadata_config

        return {
            "contextualMetadata": capo_elementalinference.types.contextual_metadata_config.serialize_json(
                value["contextualMetadata"]
            )
        }
    else:
        raise SerializationError("OutputConfig: no variant present")


def deserialize_json(data: dict) -> OutputConfig:
    if data.get("cropping") is not None:
        import capo_elementalinference.types.cropping_config

        return {
            "cropping": capo_elementalinference.types.cropping_config.deserialize_json(
                data["cropping"]
            )
        }
    elif data.get("clipping") is not None:
        import capo_elementalinference.types.clipping_config

        return {
            "clipping": capo_elementalinference.types.clipping_config.deserialize_json(
                data["clipping"]
            )
        }
    elif data.get("subtitling") is not None:
        import capo_elementalinference.types.subtitling_config

        return {
            "subtitling": capo_elementalinference.types.subtitling_config.deserialize_json(
                data["subtitling"]
            )
        }
    elif data.get("contextualMetadata") is not None:
        import capo_elementalinference.types.contextual_metadata_config

        return {
            "contextualMetadata": capo_elementalinference.types.contextual_metadata_config.deserialize_json(
                data["contextualMetadata"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("OutputConfig: no recognized variant key")
