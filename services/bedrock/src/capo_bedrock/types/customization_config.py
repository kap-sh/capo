"""Generated from Smithy shape ``com.amazonaws.bedrock#CustomizationConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.distillation_config
    import capo_bedrock.types.rft_config


class _CustomizationConfig_distillationConfig(TypedDict, closed=True):
    distillationConfig: "capo_bedrock.types.distillation_config.DistillationConfig"


class _CustomizationConfig_rftConfig(TypedDict, closed=True):
    rftConfig: "capo_bedrock.types.rft_config.RFTConfig"


CustomizationConfig: TypeAlias = (
    _CustomizationConfig_distillationConfig
    | _CustomizationConfig_rftConfig
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CustomizationConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CustomizationConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "distillationConfig" in value:
        import capo_bedrock.types.distillation_config

        return {
            "distillationConfig": capo_bedrock.types.distillation_config.serialize_json(
                value["distillationConfig"]
            )
        }
    elif "rftConfig" in value:
        import capo_bedrock.types.rft_config

        return {
            "rftConfig": capo_bedrock.types.rft_config.serialize_json(
                value["rftConfig"]
            )
        }
    else:
        raise SerializationError("CustomizationConfig: no variant present")


def deserialize_json(data: dict) -> CustomizationConfig:
    if data.get("distillationConfig") is not None:
        import capo_bedrock.types.distillation_config

        return {
            "distillationConfig": capo_bedrock.types.distillation_config.deserialize_json(
                data["distillationConfig"]
            )
        }
    elif data.get("rftConfig") is not None:
        import capo_bedrock.types.rft_config

        return {
            "rftConfig": capo_bedrock.types.rft_config.deserialize_json(
                data["rftConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("CustomizationConfig: no recognized variant key")
