"""Generated from Smithy shape ``com.amazonaws.bedrock#KnowledgeBaseConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.retrieve_and_generate_configuration
    import capo_bedrock.types.retrieve_config


class _KnowledgeBaseConfig_retrieveConfig(TypedDict, closed=True):
    retrieveConfig: "capo_bedrock.types.retrieve_config.RetrieveConfig"


class _KnowledgeBaseConfig_retrieveAndGenerateConfig(TypedDict, closed=True):
    retrieveAndGenerateConfig: "capo_bedrock.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"


KnowledgeBaseConfig: TypeAlias = (
    _KnowledgeBaseConfig_retrieveConfig
    | _KnowledgeBaseConfig_retrieveAndGenerateConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"KnowledgeBaseConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "retrieveConfig" in value:
        import capo_bedrock.types.retrieve_config

        return {
            "retrieveConfig": capo_bedrock.types.retrieve_config.serialize_json(
                value["retrieveConfig"]
            )
        }
    elif "retrieveAndGenerateConfig" in value:
        import capo_bedrock.types.retrieve_and_generate_configuration

        return {
            "retrieveAndGenerateConfig": capo_bedrock.types.retrieve_and_generate_configuration.serialize_json(
                value["retrieveAndGenerateConfig"]
            )
        }
    else:
        raise SerializationError("KnowledgeBaseConfig: no variant present")


def deserialize_json(data: dict) -> KnowledgeBaseConfig:
    if data.get("retrieveConfig") is not None:
        import capo_bedrock.types.retrieve_config

        return {
            "retrieveConfig": capo_bedrock.types.retrieve_config.deserialize_json(
                data["retrieveConfig"]
            )
        }
    elif data.get("retrieveAndGenerateConfig") is not None:
        import capo_bedrock.types.retrieve_and_generate_configuration

        return {
            "retrieveAndGenerateConfig": capo_bedrock.types.retrieve_and_generate_configuration.deserialize_json(
                data["retrieveAndGenerateConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("KnowledgeBaseConfig: no recognized variant key")


def redact_sensitive(value: KnowledgeBaseConfig) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "retrieveConfig" in value:
        import capo_bedrock.types.retrieve_config

        out["retrieveConfig"] = capo_bedrock.types.retrieve_config.redact_sensitive(
            value["retrieveConfig"]
        )
    if "retrieveAndGenerateConfig" in value:
        import capo_bedrock.types.retrieve_and_generate_configuration

        out["retrieveAndGenerateConfig"] = (
            capo_bedrock.types.retrieve_and_generate_configuration.redact_sensitive(
                value["retrieveAndGenerateConfig"]
            )
        )
    return out
