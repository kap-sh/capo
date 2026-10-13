"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GetClientTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.client_authentication_result_type


class GetClientTokenResponse(TypedDict, closed=True):
    client_authentication_result: NotRequired[
        "capo_cognito_identity_provider.types.client_authentication_result_type.ClientAuthenticationResultType"
    ]
    """<p>The access token that Amazon Cognito issues for the app client, and its metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetClientTokenResponse) -> dict:
    out: dict = {}
    if "client_authentication_result" in value:
        import capo_cognito_identity_provider.types.client_authentication_result_type

        out["ClientAuthenticationResult"] = (
            capo_cognito_identity_provider.types.client_authentication_result_type.serialize_aws_json_1_1(
                value["client_authentication_result"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetClientTokenResponse:
    out: GetClientTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("ClientAuthenticationResult") is not None:
        import capo_cognito_identity_provider.types.client_authentication_result_type

        out["client_authentication_result"] = (
            capo_cognito_identity_provider.types.client_authentication_result_type.deserialize_aws_json_1_1(
                data["ClientAuthenticationResult"]
            )
        )
    return out


def redact_sensitive(value: GetClientTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_authentication_result" in value:
        import capo_cognito_identity_provider.types.client_authentication_result_type

        out["client_authentication_result"] = (
            capo_cognito_identity_provider.types.client_authentication_result_type.redact_sensitive(
                value["client_authentication_result"]
            )
        )
    return out
