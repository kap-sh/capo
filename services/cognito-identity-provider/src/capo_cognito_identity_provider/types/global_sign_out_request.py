"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#GlobalSignOutRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.token_model_type


class GlobalSignOutRequest(TypedDict, closed=True):
    access_token: "capo_cognito_identity_provider.types.token_model_type.TokenModelType"
    """<p>A valid access token that Amazon Cognito issued to the currently signed-in user. Must include a scope claim for <code>aws.cognito.signin.user.admin</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GlobalSignOutRequest) -> dict:
    out: dict = {}
    out["AccessToken"] = value["access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GlobalSignOutRequest:
    out: GlobalSignOutRequest = {}  # type: ignore[typeddict-item]
    if data.get("AccessToken") is not None:
        out["access_token"] = data["AccessToken"]
    else:
        raise DeserializationError("GlobalSignOutRequest.access_token required")
    return out


def redact_sensitive(value: GlobalSignOutRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
