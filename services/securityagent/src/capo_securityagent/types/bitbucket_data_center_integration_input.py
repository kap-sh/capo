"""Generated from Smithy shape ``com.amazonaws.securityagent#BitbucketDataCenterIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.auth_code
    import capo_securityagent.types.csrf_state
    import capo_securityagent.types.target_url


class BitbucketDataCenterIntegrationInput(TypedDict, closed=True):
    target_url: "capo_securityagent.types.target_url.TargetUrl"
    """<p>The HTTPS URL of your Bitbucket Data Center instance, for example <code>https://bitbucket.example.com</code>.</p>"""
    code: "capo_securityagent.types.auth_code.AuthCode"
    """<p>The OAuth 2.0 authorization code returned to your redirect URL after the connection is authorized.</p>"""
    state: "capo_securityagent.types.csrf_state.CsrfState"
    """<p>The CSRF state value returned by <code>InitiateProviderRegistration</code> and echoed back on the authorization redirect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BitbucketDataCenterIntegrationInput) -> dict:
    out: dict = {}
    out["targetUrl"] = value["target_url"]
    out["code"] = value["code"]
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> BitbucketDataCenterIntegrationInput:
    out: BitbucketDataCenterIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("targetUrl") is not None:
        out["target_url"] = data["targetUrl"]
    else:
        raise DeserializationError(
            "BitbucketDataCenterIntegrationInput.target_url required"
        )
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("BitbucketDataCenterIntegrationInput.code required")
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        raise DeserializationError("BitbucketDataCenterIntegrationInput.state required")
    return out
