"""Generated from Smithy shape ``com.amazonaws.quicksight#UserIdentifier``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.sensitive_string


class _UserIdentifier_UserName(TypedDict, closed=True):
    UserName: "capo_quicksight.types.sensitive_string.SensitiveString"


class _UserIdentifier_Email(TypedDict, closed=True):
    Email: "capo_quicksight.types.sensitive_string.SensitiveString"


class _UserIdentifier_UserArn(TypedDict, closed=True):
    UserArn: "capo_quicksight.types.arn.Arn"


UserIdentifier: TypeAlias = (
    _UserIdentifier_UserName
    | _UserIdentifier_Email
    | _UserIdentifier_UserArn
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: UserIdentifier) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"UserIdentifier: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "UserName" in value:
        return {"UserName": value["UserName"]}
    elif "Email" in value:
        return {"Email": value["Email"]}
    elif "UserArn" in value:
        return {"UserArn": value["UserArn"]}
    else:
        raise SerializationError("UserIdentifier: no variant present")


def deserialize_json(data: dict) -> UserIdentifier:
    if data.get("UserName") is not None:
        return {"UserName": data["UserName"]}
    elif data.get("Email") is not None:
        return {"Email": data["Email"]}
    elif data.get("UserArn") is not None:
        return {"UserArn": data["UserArn"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("UserIdentifier: no recognized variant key")


def redact_sensitive(value: UserIdentifier) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "UserName" in value:
        out["UserName"] = "*** Sensitive Data Redacted ***"
    if "Email" in value:
        out["Email"] = "*** Sensitive Data Redacted ***"
    return out
