"""Generated from Smithy shape ``com.amazonaws.emr#Credentials``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_emr.errors import DeserializationError, SerializationError
from capo_emr.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_emr.types.username_password


class _Credentials_UsernamePassword(TypedDict, closed=True):
    UsernamePassword: "capo_emr.types.username_password.UsernamePassword"


Credentials: TypeAlias = _Credentials_UsernamePassword | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Credentials) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Credentials: cannot serialize unknown variant {value.name!r}"
        )
    elif "UsernamePassword" in value:
        import capo_emr.types.username_password

        return {
            "UsernamePassword": capo_emr.types.username_password.serialize_aws_json_1_1(
                value["UsernamePassword"]
            )
        }
    else:
        raise SerializationError("Credentials: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Credentials:
    if data.get("UsernamePassword") is not None:
        import capo_emr.types.username_password

        return {
            "UsernamePassword": capo_emr.types.username_password.deserialize_aws_json_1_1(
                data["UsernamePassword"]
            )
        }
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
    if "UsernamePassword" in value:
        out["UsernamePassword"] = "*** Sensitive Data Redacted ***"
    return out
