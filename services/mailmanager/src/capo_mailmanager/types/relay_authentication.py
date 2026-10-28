"""Generated from Smithy shape ``com.amazonaws.mailmanager#RelayAuthentication``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError
from capo_mailmanager.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_mailmanager.types.no_authentication
    import capo_mailmanager.types.secret_arn


class RelayAuthenticationSecretArnMember(TypedDict, closed=True):
    SecretArn: "capo_mailmanager.types.secret_arn.SecretArn"


class RelayAuthenticationNoAuthenticationMember(TypedDict, closed=True):
    NoAuthentication: "capo_mailmanager.types.no_authentication.NoAuthentication"


RelayAuthentication: TypeAlias = (
    RelayAuthenticationSecretArnMember
    | RelayAuthenticationNoAuthenticationMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelayAuthentication) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RelayAuthentication: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "SecretArn" in value:
        return {"SecretArn": value["SecretArn"]}
    elif "NoAuthentication" in value:
        import capo_mailmanager.types.no_authentication

        return {
            "NoAuthentication": capo_mailmanager.types.no_authentication.serialize_aws_json_1_0(
                value["NoAuthentication"]
            )
        }
    else:
        raise SerializationError("RelayAuthentication: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RelayAuthentication:
    if data.get("SecretArn") is not None:
        return {"SecretArn": data["SecretArn"]}
    elif data.get("NoAuthentication") is not None:
        import capo_mailmanager.types.no_authentication

        return {
            "NoAuthentication": capo_mailmanager.types.no_authentication.deserialize_aws_json_1_0(
                data["NoAuthentication"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("RelayAuthentication: no recognized variant key")
