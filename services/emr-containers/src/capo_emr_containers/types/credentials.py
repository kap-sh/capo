"""Generated from Smithy shape ``com.amazonaws.emrcontainers#Credentials``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_emr_containers.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_emr_containers.types.token


class _Credentials_token(TypedDict, closed=True):
    token: "capo_emr_containers.types.token.Token"


Credentials: TypeAlias = _Credentials_token


# --- restJson1 ser/de ---
def serialize_json(value: Credentials) -> dict:
    if "token" in value:
        return {"token": value["token"]}
    else:
        raise SerializationError("Credentials: no variant present")


def deserialize_json(data: dict) -> Credentials:
    if data.get("token") is not None:
        return {"token": data["token"]}
    else:
        raise DeserializationError("Credentials: no recognized variant key")


def redact_sensitive(value: Credentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token" in value:
        out["token"] = "*** Sensitive Data Redacted ***"
    return out
