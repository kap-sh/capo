"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetCredentialsForIdentityResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.credentials
    import capo_cognito_identity.types.identity_id


class GetCredentialsForIdentityResponse(TypedDict, closed=True):
    identity_id: NotRequired["capo_cognito_identity.types.identity_id.IdentityId"]
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    credentials: NotRequired["capo_cognito_identity.types.credentials.Credentials"]
    """<p>Credentials for the provided identity ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCredentialsForIdentityResponse) -> dict:
    out: dict = {}
    if "identity_id" in value:
        out["IdentityId"] = value["identity_id"]
    if "credentials" in value:
        import capo_cognito_identity.types.credentials

        out["Credentials"] = (
            capo_cognito_identity.types.credentials.serialize_aws_json_1_1(
                value["credentials"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCredentialsForIdentityResponse:
    out: GetCredentialsForIdentityResponse = {}  # type: ignore[typeddict-item]
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    if data.get("Credentials") is not None:
        import capo_cognito_identity.types.credentials

        out["credentials"] = (
            capo_cognito_identity.types.credentials.deserialize_aws_json_1_1(
                data["Credentials"]
            )
        )
    return out


def redact_sensitive(value: GetCredentialsForIdentityResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_cognito_identity.types.credentials

        out["credentials"] = capo_cognito_identity.types.credentials.redact_sensitive(
            value["credentials"]
        )
    return out
