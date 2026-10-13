"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetOpenIdTokenInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_id
    import capo_cognito_identity.types.logins_map


class GetOpenIdTokenInput(TypedDict, closed=True):
    identity_id: "capo_cognito_identity.types.identity_id.IdentityId"
    """<p>A unique identifier in the format REGION:GUID.</p>"""
    logins: NotRequired["capo_cognito_identity.types.logins_map.LoginsMap"]
    """<p>A set of optional name-value pairs that map provider names to provider tokens. When using graph.facebook.com and www.amazon.com, supply the access_token returned from the provider's authflow. For accounts.google.com, an Amazon Cognito user pool provider, or any other OpenID Connect provider, always include the <code>id_token</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetOpenIdTokenInput) -> dict:
    out: dict = {}
    out["IdentityId"] = value["identity_id"]
    if "logins" in value:
        import capo_cognito_identity.types.logins_map

        out["Logins"] = capo_cognito_identity.types.logins_map.serialize_aws_json_1_1(
            value["logins"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetOpenIdTokenInput:
    out: GetOpenIdTokenInput = {}  # type: ignore[typeddict-item]
    if data.get("IdentityId") is not None:
        out["identity_id"] = data["IdentityId"]
    else:
        raise DeserializationError("GetOpenIdTokenInput.identity_id required")
    if data.get("Logins") is not None:
        import capo_cognito_identity.types.logins_map

        out["logins"] = capo_cognito_identity.types.logins_map.deserialize_aws_json_1_1(
            data["Logins"]
        )
    return out


def redact_sensitive(value: GetOpenIdTokenInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "logins" in value:
        import capo_cognito_identity.types.logins_map

        out["logins"] = capo_cognito_identity.types.logins_map.redact_sensitive(
            value["logins"]
        )
    return out
