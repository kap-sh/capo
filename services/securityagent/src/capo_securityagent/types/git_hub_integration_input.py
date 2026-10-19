"""Generated from Smithy shape ``com.amazonaws.securityagent#GitHubIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.auth_code
    import capo_securityagent.types.csrf_state
    import capo_securityagent.types.target_url


class GitHubIntegrationInput(TypedDict, closed=True):
    code: "capo_securityagent.types.auth_code.AuthCode"
    """<p>The OAuth authorization code received from GitHub.</p>"""
    state: "capo_securityagent.types.csrf_state.CsrfState"
    """<p>The CSRF state token for validating the OAuth flow.</p>"""
    organization_name: NotRequired["str"]
    """<p>The name of the GitHub organization to integrate with.</p>"""
    target_url: NotRequired["capo_securityagent.types.target_url.TargetUrl"]
    """<p>The HTTPS URL of a self-hosted GitHub Enterprise Server instance. Omit this value for GitHub.com.</p>"""
    installation_id: NotRequired["str"]
    """<p>The installation identifier provided by GitHub Enterprise Server on the install callback. Required for GitHub Enterprise Server integrations and ignored for GitHub.com.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitHubIntegrationInput) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["state"] = value["state"]
    if "organization_name" in value:
        out["organizationName"] = value["organization_name"]
    if "target_url" in value:
        out["targetUrl"] = value["target_url"]
    if "installation_id" in value:
        out["installationId"] = value["installation_id"]
    return out


def deserialize_json(data: dict) -> GitHubIntegrationInput:
    out: GitHubIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("organizationName") is not None:
        out["organization_name"] = data["organizationName"]
    if data.get("targetUrl") is not None:
        out["target_url"] = data["targetUrl"]
    if data.get("installationId") is not None:
        out["installation_id"] = data["installationId"]
    return out
