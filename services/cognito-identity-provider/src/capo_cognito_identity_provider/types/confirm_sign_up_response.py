"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ConfirmSignUpResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.session_type


class ConfirmSignUpResponse(TypedDict, closed=True):
    session: NotRequired[
        "capo_cognito_identity_provider.types.session_type.SessionType"
    ]
    """<p>A session identifier that you can use to immediately sign in the confirmed user. You can automatically sign users in with the one-time password that they provided in a successful <code>ConfirmSignUp</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmSignUpResponse) -> dict:
    out: dict = {}
    if "session" in value:
        out["Session"] = value["session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmSignUpResponse:
    out: ConfirmSignUpResponse = {}  # type: ignore[typeddict-item]
    if data.get("Session") is not None:
        out["session"] = data["Session"]
    return out


def redact_sensitive(value: ConfirmSignUpResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "session" in value:
        out["session"] = "*** Sensitive Data Redacted ***"
    return out
