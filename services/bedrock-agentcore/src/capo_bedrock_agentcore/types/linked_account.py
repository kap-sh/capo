"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#LinkedAccount``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.linked_account_developer_jwt
    import capo_bedrock_agentcore.types.linked_account_email
    import capo_bedrock_agentcore.types.linked_account_o_auth2
    import capo_bedrock_agentcore.types.linked_account_sms


class _LinkedAccount_email(TypedDict, closed=True):
    email: "capo_bedrock_agentcore.types.linked_account_email.LinkedAccountEmail"


class _LinkedAccount_sms(TypedDict, closed=True):
    sms: "capo_bedrock_agentcore.types.linked_account_sms.LinkedAccountSms"


class _LinkedAccount_developerJwt(TypedDict, closed=True):
    developerJwt: "capo_bedrock_agentcore.types.linked_account_developer_jwt.LinkedAccountDeveloperJwt"


class _LinkedAccount_oAuth2(TypedDict, closed=True):
    oAuth2: "capo_bedrock_agentcore.types.linked_account_o_auth2.LinkedAccountOAuth2"


LinkedAccount: TypeAlias = (
    _LinkedAccount_email
    | _LinkedAccount_sms
    | _LinkedAccount_developerJwt
    | _LinkedAccount_oAuth2
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: LinkedAccount) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"LinkedAccount: cannot serialize unknown variant {value.name!r}"
        )
    elif "email" in value:
        import capo_bedrock_agentcore.types.linked_account_email

        return {
            "email": capo_bedrock_agentcore.types.linked_account_email.serialize_json(
                value["email"]
            )
        }
    elif "sms" in value:
        import capo_bedrock_agentcore.types.linked_account_sms

        return {
            "sms": capo_bedrock_agentcore.types.linked_account_sms.serialize_json(
                value["sms"]
            )
        }
    elif "developerJwt" in value:
        import capo_bedrock_agentcore.types.linked_account_developer_jwt

        return {
            "developerJwt": capo_bedrock_agentcore.types.linked_account_developer_jwt.serialize_json(
                value["developerJwt"]
            )
        }
    elif "oAuth2" in value:
        import capo_bedrock_agentcore.types.linked_account_o_auth2

        return {
            "oAuth2": capo_bedrock_agentcore.types.linked_account_o_auth2.serialize_json(
                value["oAuth2"]
            )
        }
    else:
        raise SerializationError("LinkedAccount: no variant present")


def deserialize_json(data: dict) -> LinkedAccount:
    if data.get("email") is not None:
        import capo_bedrock_agentcore.types.linked_account_email

        return {
            "email": capo_bedrock_agentcore.types.linked_account_email.deserialize_json(
                data["email"]
            )
        }
    elif data.get("sms") is not None:
        import capo_bedrock_agentcore.types.linked_account_sms

        return {
            "sms": capo_bedrock_agentcore.types.linked_account_sms.deserialize_json(
                data["sms"]
            )
        }
    elif data.get("developerJwt") is not None:
        import capo_bedrock_agentcore.types.linked_account_developer_jwt

        return {
            "developerJwt": capo_bedrock_agentcore.types.linked_account_developer_jwt.deserialize_json(
                data["developerJwt"]
            )
        }
    elif data.get("oAuth2") is not None:
        import capo_bedrock_agentcore.types.linked_account_o_auth2

        return {
            "oAuth2": capo_bedrock_agentcore.types.linked_account_o_auth2.deserialize_json(
                data["oAuth2"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("LinkedAccount: no recognized variant key")
