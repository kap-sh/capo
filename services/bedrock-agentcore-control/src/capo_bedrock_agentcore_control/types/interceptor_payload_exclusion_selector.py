"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#InterceptorPayloadExclusionSelector``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion


class _InterceptorPayloadExclusionSelector_field(TypedDict, closed=True):
    field: "capo_bedrock_agentcore_control.types.interceptor_payload_exclusion.InterceptorPayloadExclusion"


InterceptorPayloadExclusionSelector: TypeAlias = (
    _InterceptorPayloadExclusionSelector_field | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: InterceptorPayloadExclusionSelector) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"InterceptorPayloadExclusionSelector: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "field" in value:
        import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion

        return {
            "field": capo_bedrock_agentcore_control.types.interceptor_payload_exclusion.serialize_json(
                value["field"]
            )
        }
    else:
        raise SerializationError(
            "InterceptorPayloadExclusionSelector: no variant present"
        )


def deserialize_json(data: dict) -> InterceptorPayloadExclusionSelector:
    if data.get("field") is not None:
        import capo_bedrock_agentcore_control.types.interceptor_payload_exclusion

        return {
            "field": capo_bedrock_agentcore_control.types.interceptor_payload_exclusion.deserialize_json(
                data["field"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "InterceptorPayloadExclusionSelector: no recognized variant key"
        )
