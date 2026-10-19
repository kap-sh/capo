"""Generated from Smithy shape ``com.amazonaws.securityagent#InitiateProviderRegistrationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.csrf_state
    import capo_securityagent.types.location


class InitiateProviderRegistrationOutput(TypedDict, closed=True):
    redirect_to: "capo_securityagent.types.location.Location"
    """<p>The URL to redirect the user to for completing the OAuth authorization.</p>"""
    csrf_state: "capo_securityagent.types.csrf_state.CsrfState"
    """<p>The CSRF state token to use when completing the OAuth flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InitiateProviderRegistrationOutput) -> dict:
    out: dict = {}
    out["redirectTo"] = value["redirect_to"]
    out["csrfState"] = value["csrf_state"]
    return out


def deserialize_json(data: dict) -> InitiateProviderRegistrationOutput:
    out: InitiateProviderRegistrationOutput = {}  # type: ignore[typeddict-item]
    if data.get("redirectTo") is not None:
        out["redirect_to"] = data["redirectTo"]
    else:
        out["redirect_to"] = ""
    if data.get("csrfState") is not None:
        out["csrf_state"] = data["csrfState"]
    else:
        out["csrf_state"] = ""
    return out
