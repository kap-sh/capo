"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#UserIdentifier``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.user_id_type
    import capo_bedrock_agentcore.types.user_token_type


class _UserIdentifier_userToken(TypedDict, closed=True):
    userToken: "capo_bedrock_agentcore.types.user_token_type.UserTokenType"


class _UserIdentifier_userId(TypedDict, closed=True):
    userId: "capo_bedrock_agentcore.types.user_id_type.UserIdType"


UserIdentifier: TypeAlias = (
    _UserIdentifier_userToken | _UserIdentifier_userId | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentifier) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"UserIdentifier: cannot serialize unknown variant {value.name!r}"
        )
    elif "userToken" in value:
        return {"userToken": value["userToken"]}
    elif "userId" in value:
        return {"userId": value["userId"]}
    else:
        raise SerializationError("UserIdentifier: no variant present")


def deserialize_json(data: dict) -> UserIdentifier:
    if data.get("userToken") is not None:
        return {"userToken": data["userToken"]}
    elif data.get("userId") is not None:
        return {"userId": data["userId"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("UserIdentifier: no recognized variant key")


def redact_sensitive(value: UserIdentifier) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "userToken" in value:
        out["userToken"] = "*** Sensitive Data Redacted ***"
    return out
