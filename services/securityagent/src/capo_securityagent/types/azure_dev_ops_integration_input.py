"""Generated from Smithy shape ``com.amazonaws.securityagent#AzureDevOpsIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.auth_code
    import capo_securityagent.types.csrf_state


class AzureDevOpsIntegrationInput(TypedDict, closed=True):
    code: "capo_securityagent.types.auth_code.AuthCode"
    """<p>The OAuth 2.0 authorization code returned to your redirect URL after the connection is authorized.</p>"""
    state: "capo_securityagent.types.csrf_state.CsrfState"
    """<p>The CSRF state value returned by <code>InitiateProviderRegistration</code> and echoed back on the authorization redirect.</p>"""
    organization_name: "str"
    """<p>The name of the Azure DevOps organization to connect, for example <code>my-org</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureDevOpsIntegrationInput) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["state"] = value["state"]
    out["organizationName"] = value["organization_name"]
    return out


def deserialize_json(data: dict) -> AzureDevOpsIntegrationInput:
    out: AzureDevOpsIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("AzureDevOpsIntegrationInput.code required")
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        raise DeserializationError("AzureDevOpsIntegrationInput.state required")
    if data.get("organizationName") is not None:
        out["organization_name"] = data["organizationName"]
    else:
        raise DeserializationError(
            "AzureDevOpsIntegrationInput.organization_name required"
        )
    return out
