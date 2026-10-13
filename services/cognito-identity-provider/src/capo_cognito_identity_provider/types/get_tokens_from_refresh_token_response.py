"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetTokensFromRefreshTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.authentication_result_type


class GetTokensFromRefreshTokenResponse(TypedDict, closed=True):
    authentication_result: NotRequired[
        "capo_cognito_identity_provider.types.authentication_result_type.AuthenticationResultType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetTokensFromRefreshTokenResponse) -> dict:
    out: dict = {}
    if "authentication_result" in value:
        import capo_cognito_identity_provider.types.authentication_result_type

        out["AuthenticationResult"] = (
            capo_cognito_identity_provider.types.authentication_result_type.serialize_aws_json_1_1(
                value["authentication_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetTokensFromRefreshTokenResponse:
    out: GetTokensFromRefreshTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("AuthenticationResult") is not None:
        import capo_cognito_identity_provider.types.authentication_result_type

        out["authentication_result"] = (
            capo_cognito_identity_provider.types.authentication_result_type.deserialize_aws_json_1_1(
                data["AuthenticationResult"]
            )
        )
    return out


def redact_sensitive(value: GetTokensFromRefreshTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_result" in value:
        import capo_cognito_identity_provider.types.authentication_result_type

        out["authentication_result"] = (
            capo_cognito_identity_provider.types.authentication_result_type.redact_sensitive(
                value["authentication_result"]
            )
        )
    return out
