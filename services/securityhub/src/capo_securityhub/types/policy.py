"""Generated from Smithy shape ``com.amazonaws.securityhub#Policy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityhub.errors import DeserializationError, SerializationError
from capo_securityhub.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityhub.types.security_hub_policy


class _Policy_SecurityHub(TypedDict, closed=True):
    SecurityHub: "capo_securityhub.types.security_hub_policy.SecurityHubPolicy"


Policy: TypeAlias = _Policy_SecurityHub | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Policy) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Policy: cannot serialize unknown variant {value.name!r}"
        )
    elif "SecurityHub" in value:
        import capo_securityhub.types.security_hub_policy

        return {
            "SecurityHub": capo_securityhub.types.security_hub_policy.serialize_json(
                value["SecurityHub"]
            )
        }
    else:
        raise SerializationError("Policy: no variant present")


def deserialize_json(data: dict) -> Policy:
    if data.get("SecurityHub") is not None:
        import capo_securityhub.types.security_hub_policy

        return {
            "SecurityHub": capo_securityhub.types.security_hub_policy.deserialize_json(
                data["SecurityHub"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Policy: no recognized variant key")
