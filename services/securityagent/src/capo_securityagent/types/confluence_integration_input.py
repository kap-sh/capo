"""Generated from Smithy shape ``com.amazonaws.securityagent#ConfluenceIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.auth_code
    import capo_securityagent.types.confluence_installation_id
    import capo_securityagent.types.confluence_site_url
    import capo_securityagent.types.csrf_state


class ConfluenceIntegrationInput(TypedDict, closed=True):
    installation_id: (
        "capo_securityagent.types.confluence_installation_id.ConfluenceInstallationId"
    )
    """<p>The Atlassian installation identifier, available from the Atlassian administration console.</p>"""
    code: "capo_securityagent.types.auth_code.AuthCode"
    """<p>The OAuth 2.0 authorization code returned from the consent redirect.</p>"""
    state: "capo_securityagent.types.csrf_state.CsrfState"
    """<p>The CSRF state token echoed back from the OAuth redirect.</p>"""
    site_url: "capo_securityagent.types.confluence_site_url.ConfluenceSiteUrl"
    """<p>The Confluence Cloud site URL, for example https://mysite.atlassian.net.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfluenceIntegrationInput) -> dict:
    out: dict = {}
    out["installationId"] = value["installation_id"]
    out["code"] = value["code"]
    out["state"] = value["state"]
    out["siteUrl"] = value["site_url"]
    return out


def deserialize_json(data: dict) -> ConfluenceIntegrationInput:
    out: ConfluenceIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("installationId") is not None:
        out["installation_id"] = data["installationId"]
    else:
        out["installation_id"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("siteUrl") is not None:
        out["site_url"] = data["siteUrl"]
    else:
        out["site_url"] = ""
    return out
