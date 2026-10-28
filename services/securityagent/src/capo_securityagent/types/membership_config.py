"""Generated from Smithy shape ``com.amazonaws.securityagent#MembershipConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError, SerializationError
from capo_securityagent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_securityagent.types.user_config


class MembershipConfigUserMember(TypedDict, closed=True):
    user: "capo_securityagent.types.user_config.UserConfig"


MembershipConfig: TypeAlias = MembershipConfigUserMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: MembershipConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MembershipConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "user" in value:
        import capo_securityagent.types.user_config

        return {
            "user": capo_securityagent.types.user_config.serialize_json(value["user"])
        }
    else:
        raise SerializationError("MembershipConfig: no variant present")


def deserialize_json(data: dict) -> MembershipConfig:
    if data.get("user") is not None:
        import capo_securityagent.types.user_config

        return {
            "user": capo_securityagent.types.user_config.deserialize_json(data["user"])
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MembershipConfig: no recognized variant key")
