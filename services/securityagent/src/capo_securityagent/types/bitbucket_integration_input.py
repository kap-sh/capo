"""Generated from Smithy shape ``com.amazonaws.securityagent#BitbucketIntegrationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.auth_code
    import capo_securityagent.types.bitbucket_installation_id
    import capo_securityagent.types.bitbucket_workspace
    import capo_securityagent.types.csrf_state


class BitbucketIntegrationInput(TypedDict, closed=True):
    installation_id: (
        "capo_securityagent.types.bitbucket_installation_id.BitbucketInstallationId"
    )
    """<p>The Atlassian installation identifier, available from the Atlassian administration console.</p>"""
    workspace: "capo_securityagent.types.bitbucket_workspace.BitbucketWorkspace"
    """<p>The Bitbucket workspace slug that identifies the workspace to integrate, for example acme-corp.</p>"""
    code: "capo_securityagent.types.auth_code.AuthCode"
    """<p>The OAuth 2.0 authorization code returned from the consent redirect.</p>"""
    state: "capo_securityagent.types.csrf_state.CsrfState"
    """<p>The CSRF state token echoed back from the OAuth redirect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BitbucketIntegrationInput) -> dict:
    out: dict = {}
    out["installationId"] = value["installation_id"]
    out["workspace"] = value["workspace"]
    out["code"] = value["code"]
    out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> BitbucketIntegrationInput:
    out: BitbucketIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("installationId") is not None:
        out["installation_id"] = data["installationId"]
    else:
        out["installation_id"] = ""
    if data.get("workspace") is not None:
        out["workspace"] = data["workspace"]
    else:
        out["workspace"] = ""
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    return out
