"""Generated from Smithy shape ``com.amazonaws.ssoadmin#Grant``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_sso_admin.errors import DeserializationError, SerializationError
from capo_sso_admin.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sso_admin.types.authorization_code_grant
    import capo_sso_admin.types.jwt_bearer_grant
    import capo_sso_admin.types.refresh_token_grant
    import capo_sso_admin.types.token_exchange_grant


class _Grant_AuthorizationCode(TypedDict, closed=True):
    AuthorizationCode: (
        "capo_sso_admin.types.authorization_code_grant.AuthorizationCodeGrant"
    )


class _Grant_JwtBearer(TypedDict, closed=True):
    JwtBearer: "capo_sso_admin.types.jwt_bearer_grant.JwtBearerGrant"


class _Grant_RefreshToken(TypedDict, closed=True):
    RefreshToken: "capo_sso_admin.types.refresh_token_grant.RefreshTokenGrant"


class _Grant_TokenExchange(TypedDict, closed=True):
    TokenExchange: "capo_sso_admin.types.token_exchange_grant.TokenExchangeGrant"


Grant: TypeAlias = (
    _Grant_AuthorizationCode
    | _Grant_JwtBearer
    | _Grant_RefreshToken
    | _Grant_TokenExchange
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Grant) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Grant: cannot serialize unknown variant {value.name!r}"
        )
    elif "AuthorizationCode" in value:
        import capo_sso_admin.types.authorization_code_grant

        return {
            "AuthorizationCode": capo_sso_admin.types.authorization_code_grant.serialize_aws_json_1_1(
                value["AuthorizationCode"]
            )
        }
    elif "JwtBearer" in value:
        import capo_sso_admin.types.jwt_bearer_grant

        return {
            "JwtBearer": capo_sso_admin.types.jwt_bearer_grant.serialize_aws_json_1_1(
                value["JwtBearer"]
            )
        }
    elif "RefreshToken" in value:
        import capo_sso_admin.types.refresh_token_grant

        return {
            "RefreshToken": capo_sso_admin.types.refresh_token_grant.serialize_aws_json_1_1(
                value["RefreshToken"]
            )
        }
    elif "TokenExchange" in value:
        import capo_sso_admin.types.token_exchange_grant

        return {
            "TokenExchange": capo_sso_admin.types.token_exchange_grant.serialize_aws_json_1_1(
                value["TokenExchange"]
            )
        }
    else:
        raise SerializationError("Grant: no variant present")


def deserialize_aws_json_1_1(data: dict) -> Grant:
    if data.get("AuthorizationCode") is not None:
        import capo_sso_admin.types.authorization_code_grant

        return {
            "AuthorizationCode": capo_sso_admin.types.authorization_code_grant.deserialize_aws_json_1_1(
                data["AuthorizationCode"]
            )
        }
    elif data.get("JwtBearer") is not None:
        import capo_sso_admin.types.jwt_bearer_grant

        return {
            "JwtBearer": capo_sso_admin.types.jwt_bearer_grant.deserialize_aws_json_1_1(
                data["JwtBearer"]
            )
        }
    elif data.get("RefreshToken") is not None:
        import capo_sso_admin.types.refresh_token_grant

        return {
            "RefreshToken": capo_sso_admin.types.refresh_token_grant.deserialize_aws_json_1_1(
                data["RefreshToken"]
            )
        }
    elif data.get("TokenExchange") is not None:
        import capo_sso_admin.types.token_exchange_grant

        return {
            "TokenExchange": capo_sso_admin.types.token_exchange_grant.deserialize_aws_json_1_1(
                data["TokenExchange"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Grant: no recognized variant key")
