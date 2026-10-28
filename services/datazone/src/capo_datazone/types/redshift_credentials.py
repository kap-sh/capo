"""Generated from Smithy shape ``com.amazonaws.datazone#RedshiftCredentials``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.username_password


class RedshiftCredentialsSecretArnMember(TypedDict, closed=True):
    secretArn: "str"


class RedshiftCredentialsUsernamePasswordMember(TypedDict, closed=True):
    usernamePassword: "capo_datazone.types.username_password.UsernamePassword"


RedshiftCredentials: TypeAlias = (
    RedshiftCredentialsSecretArnMember
    | RedshiftCredentialsUsernamePasswordMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftCredentials) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RedshiftCredentials: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "secretArn" in value:
        return {"secretArn": value["secretArn"]}
    elif "usernamePassword" in value:
        import capo_datazone.types.username_password

        return {
            "usernamePassword": capo_datazone.types.username_password.serialize_json(
                value["usernamePassword"]
            )
        }
    else:
        raise SerializationError("RedshiftCredentials: no variant present")


def deserialize_json(data: dict) -> RedshiftCredentials:
    if data.get("secretArn") is not None:
        return {"secretArn": data["secretArn"]}
    elif data.get("usernamePassword") is not None:
        import capo_datazone.types.username_password

        return {
            "usernamePassword": capo_datazone.types.username_password.deserialize_json(
                data["usernamePassword"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RedshiftCredentials: no recognized variant key")
