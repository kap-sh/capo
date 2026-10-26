"""Generated from Smithy shape ``com.amazonaws.opensearch#CapabilityBaseResponseConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError, SerializationError
from capo_opensearch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearch.types.ai_config


class _CapabilityBaseResponseConfig_aiConfig(TypedDict, closed=True):
    aiConfig: "capo_opensearch.types.ai_config.AIConfig"


CapabilityBaseResponseConfig: TypeAlias = (
    _CapabilityBaseResponseConfig_aiConfig | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: CapabilityBaseResponseConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CapabilityBaseResponseConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "aiConfig" in value:
        import capo_opensearch.types.ai_config

        return {
            "aiConfig": capo_opensearch.types.ai_config.serialize_json(
                value["aiConfig"]
            )
        }
    else:
        raise SerializationError("CapabilityBaseResponseConfig: no variant present")


def deserialize_json(data: dict) -> CapabilityBaseResponseConfig:
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
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CapabilityBaseResponseConfig: no recognized variant key"
        )
