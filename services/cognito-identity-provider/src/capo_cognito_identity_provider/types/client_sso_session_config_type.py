"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ClientSSOSessionConfigType``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.sso_session_max_validity_minutes_type


class ClientSSOSessionConfigType(TypedDict, closed=True):
    max_validity_minutes: "capo_cognito_identity_provider.types.sso_session_max_validity_minutes_type.SSOSessionMaxValidityMinutesType"
    """<p>The maximum amount of time, in minutes, that this app client silently reuses an existing SSO session, returning a new set of tokens without requiring the user to re-authenticate, measured from the user's last fresh authentication. The minimum value is <code>0</code> and the maximum value is <code>129600</code> (90 days). The default is <code>60</code>. A value of <code>0</code> means that this app client never silently reuses the SSO session and always re-authenticates the user. The SSO session record and its cookie are still created regardless of this value, and other app clients in the same user pool can still reuse the session.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientSSOSessionConfigType) -> dict:
    out: dict = {}
    out["MaxValidityMinutes"] = value["max_validity_minutes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientSSOSessionConfigType:
    out: ClientSSOSessionConfigType = {}  # type: ignore[typeddict-item]
    if data.get("MaxValidityMinutes") is not None:
        out["max_validity_minutes"] = data["MaxValidityMinutes"]
    else:
        out["max_validity_minutes"] = 0
    return out
