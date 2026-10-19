"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetIdInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity.types.account_id
    import capo_cognito_identity.types.identity_pool_id
    import capo_cognito_identity.types.logins_map


class GetIdInput(TypedDict, closed=True):
    account_id: NotRequired["capo_cognito_identity.types.account_id.AccountId"]
    """<p>A standard Amazon Web Services account ID (9+ digits).</p>"""
    identity_pool_id: "capo_cognito_identity.types.identity_pool_id.IdentityPoolId"
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    logins: NotRequired["capo_cognito_identity.types.logins_map.LoginsMap"]
    """<p>A set of optional name-value pairs that map provider names to provider tokens. The available provider names for <code>Logins</code> are as follows:</p> <ul> <li> <p>Facebook: <code>graph.facebook.com</code> </p> </li> <li> <p>Amazon Cognito user pool: <code>cognito-idp.<region>.amazonaws.com/<YOUR_USER_POOL_ID></code>, for example, <code>cognito-idp.us-east-1.amazonaws.com/us-east-1_123456789</code>. </p> </li> <li> <p>Google: <code>accounts.google.com</code> </p> </li> <li> <p>Amazon: <code>www.amazon.com</code> </p> </li> <li> <p>Twitter: <code>api.twitter.com</code> </p> </li> <li> <p>Digits: <code>www.digits.com</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdInput) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    out["IdentityPoolId"] = value["identity_pool_id"]
    if "logins" in value:
        import capo_cognito_identity.types.logins_map

        out["Logins"] = capo_cognito_identity.types.logins_map.serialize_aws_json_1_1(
            value["logins"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdInput:
    out: GetIdInput = {}  # type: ignore[typeddict-item]
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    if data.get("IdentityPoolId") is not None:
        out["identity_pool_id"] = data["IdentityPoolId"]
    else:
        out["identity_pool_id"] = ""
    if data.get("Logins") is not None:
        import capo_cognito_identity.types.logins_map

        out["logins"] = capo_cognito_identity.types.logins_map.deserialize_aws_json_1_1(
            data["Logins"]
        )
    return out


def redact_sensitive(value: GetIdInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "logins" in value:
        import capo_cognito_identity.types.logins_map

        out["logins"] = capo_cognito_identity.types.logins_map.redact_sensitive(
            value["logins"]
        )
    return out
