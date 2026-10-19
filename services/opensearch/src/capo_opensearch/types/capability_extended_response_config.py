"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityExtendedResponseConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError, SerializationError
from capo_opensearch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearch.types.ai_config


class _CapabilityExtendedResponseConfig_aiConfig(TypedDict, closed=True):
    aiConfig: "capo_opensearch.types.ai_config.AIConfig"


CapabilityExtendedResponseConfig: TypeAlias = (
    _CapabilityExtendedResponseConfig_aiConfig | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityExtendedResponseConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"CapabilityExtendedResponseConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "aiConfig" in value:
        import capo_opensearch.types.ai_config

        return {
            "aiConfig": capo_opensearch.types.ai_config.serialize_json(
                value["aiConfig"]
            )
        }
    else:
        raise SerializationError("CapabilityExtendedResponseConfig: no variant present")


def deserialize_json(data: dict) -> CapabilityExtendedResponseConfig:
    if data.get("aiConfig") is not None:
        import capo_opensearch.types.ai_config

        return {
            "aiConfig": capo_opensearch.types.ai_config.deserialize_json(
                data["aiConfig"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "CapabilityExtendedResponseConfig: no recognized variant key"
        )
