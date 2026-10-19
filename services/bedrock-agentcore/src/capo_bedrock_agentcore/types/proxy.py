"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Proxy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.external_proxy


class _Proxy_externalProxy(TypedDict, closed=True):
    externalProxy: "capo_bedrock_agentcore.types.external_proxy.ExternalProxy"


Proxy: TypeAlias = _Proxy_externalProxy | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Proxy) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Proxy: cannot serialize unknown variant {value.name!r}"
        )
    elif "externalProxy" in value:
        import capo_bedrock_agentcore.types.external_proxy

        return {
            "externalProxy": capo_bedrock_agentcore.types.external_proxy.serialize_json(
                value["externalProxy"]
            )
        }
    else:
        raise SerializationError("Proxy: no variant present")


def deserialize_json(data: dict) -> Proxy:
    if data.get("externalProxy") is not None:
        import capo_bedrock_agentcore.types.external_proxy

        return {
            "externalProxy": capo_bedrock_agentcore.types.external_proxy.deserialize_json(
                data["externalProxy"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Proxy: no recognized variant key")
