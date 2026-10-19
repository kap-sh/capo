"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Credentials``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_emr_containers.errors import DeserializationError, SerializationError
from capo_emr_containers.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_emr_containers.types.token


class _Credentials_token(TypedDict, closed=True):
    token: "capo_emr_containers.types.token.Token"


Credentials: TypeAlias = _Credentials_token | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Credentials) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Credentials: cannot serialize unknown variant {value.name!r}"
        )
    elif "token" in value:
        return {"token": value["token"]}
    else:
        raise SerializationError("Credentials: no variant present")


def deserialize_json(data: dict) -> Credentials:
    if data.get("token") is not None:
        return {"token": data["token"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Credentials: no recognized variant key")


def redact_sensitive(value: Credentials) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
