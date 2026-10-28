"""Generated from Smithy shape ``com.amazonaws.connectcases#UserUnion``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.custom_entity
    import capo_connectcases.types.user_arn


class UserUnionUserArnMember(TypedDict, closed=True):
    userArn: "capo_connectcases.types.user_arn.UserArn"


class UserUnionCustomEntityMember(TypedDict, closed=True):
    customEntity: "capo_connectcases.types.custom_entity.CustomEntity"


UserUnion: TypeAlias = (
    UserUnionUserArnMember | UserUnionCustomEntityMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UserUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UserUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "userArn" in value:
        return {"userArn": value["userArn"]}
    elif "customEntity" in value:
        return {"customEntity": value["customEntity"]}
    else:
        raise SerializationError("UserUnion: no variant present")


def deserialize_json(data: dict) -> UserUnion:
    if data.get("userArn") is not None:
        return {"userArn": data["userArn"]}
    elif data.get("customEntity") is not None:
        return {"customEntity": data["customEntity"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("UserUnion: no recognized variant key")


def redact_sensitive(value: UserUnion) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "customEntity" in value:
        out["customEntity"] = "*** Sensitive Data Redacted ***"
    return out
