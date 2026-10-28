"""Generated from Smithy shape ``com.amazonaws.emr#Credentials``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_emr.errors import DeserializationError, SerializationError
from capo_emr.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_emr.types.username_password


class CredentialsUsernamePasswordMember(TypedDict, closed=True):
    UsernamePassword: "capo_emr.types.username_password.UsernamePassword"


Credentials: TypeAlias = CredentialsUsernamePasswordMember | UnknownUnionMember


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Credentials) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Credentials: cannot serialize unknown variant {value['$unknown']['name']!r}"
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
            return {"$unknown": {"name": name}}
        raise DeserializationError("Credentials: no recognized variant key")


def redact_sensitive(value: Credentials) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "UsernamePassword" in value:
        out["UsernamePassword"] = "*** Sensitive Data Redacted ***"
    return out
