"""Generated from Smithy shape ``com.amazonaws.securityagent#JiraIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.auth_code
    import capo_securityagent.types.csrf_state
    import capo_securityagent.types.jira_installation_id
    import capo_securityagent.types.jira_site_url


class JiraIntegrationInput(TypedDict, closed=True):
    installation_id: "capo_securityagent.types.jira_installation_id.JiraInstallationId"
    """<p>The Atlassian installation identifier, available from the Atlassian administration console.</p>"""
    code: "capo_securityagent.types.auth_code.AuthCode"
    """<p>The OAuth 2.0 authorization code returned from the consent redirect.</p>"""
    state: "capo_securityagent.types.csrf_state.CsrfState"
    """<p>The CSRF state token echoed back from the OAuth redirect.</p>"""
    site_url: "capo_securityagent.types.jira_site_url.JiraSiteUrl"
    """<p>The Jira Cloud site URL, for example https://mysite.atlassian.net.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraIntegrationInput) -> dict:
    out: dict = {}
    out["installationId"] = value["installation_id"]
    out["code"] = value["code"]
    out["state"] = value["state"]
    out["siteUrl"] = value["site_url"]
    return out


def deserialize_json(data: dict) -> JiraIntegrationInput:
    out: JiraIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("installationId") is not None:
        out["installation_id"] = data["installationId"]
    else:
        raise DeserializationError("JiraIntegrationInput.installation_id required")
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        raise DeserializationError("JiraIntegrationInput.code required")
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        raise DeserializationError("JiraIntegrationInput.state required")
    if data.get("siteUrl") is not None:
        out["site_url"] = data["siteUrl"]
    else:
        raise DeserializationError("JiraIntegrationInput.site_url required")
    return out
