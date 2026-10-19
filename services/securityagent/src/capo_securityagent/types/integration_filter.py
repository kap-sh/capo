"""Generated from Smithy shape ``com.amazonaws.securityagent#IntegrationFilter``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityagent.types.provider
    import capo_securityagent.types.provider_type


class _IntegrationFilter_provider(TypedDict, closed=True):
    provider: "capo_securityagent.types.provider.Provider"


class _IntegrationFilter_providerType(TypedDict, closed=True):
    providerType: "capo_securityagent.types.provider_type.ProviderType"


IntegrationFilter: TypeAlias = (
    _IntegrationFilter_provider | _IntegrationFilter_providerType | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationFilter) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IntegrationFilter: cannot serialize unknown variant {value.name!r}"
        )
    elif "provider" in value:
        import capo_securityagent.types.provider

        return {
            "provider": capo_securityagent.types.provider.serialize_json(
                value["provider"]
            )
        }
    elif "providerType" in value:
        import capo_securityagent.types.provider_type

        return {
            "providerType": capo_securityagent.types.provider_type.serialize_json(
                value["providerType"]
            )
        }
    else:
        raise SerializationError("IntegrationFilter: no variant present")


def deserialize_json(data: dict) -> IntegrationFilter:
    if data.get("provider") is not None:
        import capo_securityagent.types.provider

        return {
            "provider": capo_securityagent.types.provider.deserialize_json(
                data["provider"]
            )
        }
    elif data.get("providerType") is not None:
        import capo_securityagent.types.provider_type

        return {
            "providerType": capo_securityagent.types.provider_type.deserialize_json(
                data["providerType"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("IntegrationFilter: no recognized variant key")
