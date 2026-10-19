"""Generated from Smithy shape ``com.amazonaws.appsync#AuthProvider``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.authentication_type
    import capo_appsync.types.cognito_config
    import capo_appsync.types.lambda_authorizer_config
    import capo_appsync.types.open_id_connect_config


class AuthProvider(TypedDict, closed=True):
    auth_type: "capo_appsync.types.authentication_type.AuthenticationType"
    """<p>The authorization type.</p>"""
    cognito_config: NotRequired["capo_appsync.types.cognito_config.CognitoConfig"]
    """<p>Describes an Amazon Cognito user pool configuration.</p>"""
    open_id_connect_config: NotRequired[
        "capo_appsync.types.open_id_connect_config.OpenIDConnectConfig"
    ]
    lambda_authorizer_config: NotRequired[
        "capo_appsync.types.lambda_authorizer_config.LambdaAuthorizerConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AuthProvider) -> dict:
    out: dict = {}
    import capo_appsync.types.authentication_type

    out["authType"] = capo_appsync.types.authentication_type.serialize_json(
        value["auth_type"]
    )
    if "cognito_config" in value:
        import capo_appsync.types.cognito_config

        out["cognitoConfig"] = capo_appsync.types.cognito_config.serialize_json(
            value["cognito_config"]
        )
    if "open_id_connect_config" in value:
        import capo_appsync.types.open_id_connect_config

        out["openIDConnectConfig"] = (
            capo_appsync.types.open_id_connect_config.serialize_json(
                value["open_id_connect_config"]
            )
        )
    if "lambda_authorizer_config" in value:
        import capo_appsync.types.lambda_authorizer_config

        out["lambdaAuthorizerConfig"] = (
            capo_appsync.types.lambda_authorizer_config.serialize_json(
                value["lambda_authorizer_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> AuthProvider:
    out: AuthProvider = {}  # type: ignore[typeddict-item]
    if data.get("authType") is not None:
        import capo_appsync.types.authentication_type

        out["auth_type"] = capo_appsync.types.authentication_type.deserialize_json(
            data["authType"]
        )
    else:
        import typing

        out["auth_type"] = typing.cast(
            "capo_appsync.types.authentication_type.AuthenticationType", ""
        )
    if data.get("cognitoConfig") is not None:
        import capo_appsync.types.cognito_config

        out["cognito_config"] = capo_appsync.types.cognito_config.deserialize_json(
            data["cognitoConfig"]
        )
    if data.get("openIDConnectConfig") is not None:
        import capo_appsync.types.open_id_connect_config

        out["open_id_connect_config"] = (
            capo_appsync.types.open_id_connect_config.deserialize_json(
                data["openIDConnectConfig"]
            )
        )
    if data.get("lambdaAuthorizerConfig") is not None:
        import capo_appsync.types.lambda_authorizer_config

        out["lambda_authorizer_config"] = (
            capo_appsync.types.lambda_authorizer_config.deserialize_json(
                data["lambdaAuthorizerConfig"]
            )
        )
    return out
