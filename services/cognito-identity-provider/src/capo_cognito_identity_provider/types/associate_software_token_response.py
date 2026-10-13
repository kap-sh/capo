"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssociateSoftwareTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.secret_code_type
    import capo_cognito_identity_provider.types.session_type


class AssociateSoftwareTokenResponse(TypedDict, closed=True):
    secret_code: NotRequired[
        "capo_cognito_identity_provider.types.secret_code_type.SecretCodeType"
    ]
    """<p>A unique generated shared secret code that is used by the TOTP algorithm to generate a one-time code.</p>"""
    session: NotRequired[
        "capo_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>The session identifier that maintains the state of authentication requests and challenge responses.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateSoftwareTokenResponse) -> dict:
    out: dict = {}
    if "secret_code" in value:
        out["SecretCode"] = value["secret_code"]
    if "session" in value:
        out["Session"] = value["session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateSoftwareTokenResponse:
    out: AssociateSoftwareTokenResponse = {}  # type: ignore[typeddict-item]
    if data.get("SecretCode") is not None:
        out["secret_code"] = data["SecretCode"]
    if data.get("Session") is not None:
        out["session"] = data["Session"]
    return out


def redact_sensitive(value: AssociateSoftwareTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "secret_code" in value:
        out["secret_code"] = "*** Sensitive Data Redacted ***"
    if "session" in value:
        out["session"] = "*** Sensitive Data Redacted ***"
    return out
