"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateGitHubIntegrationDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.git_hub_auth_code
    import capo_inspector2.types.git_hub_installation_id


class UpdateGitHubIntegrationDetail(TypedDict, closed=True):
    code: "capo_inspector2.types.git_hub_auth_code.GitHubAuthCode"
    """<p>The authorization code received from GitHub to update the integration.</p>"""
    installation_id: (
        "capo_inspector2.types.git_hub_installation_id.GitHubInstallationId"
    )
    """<p>The installation ID of the GitHub App associated with the integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGitHubIntegrationDetail) -> dict:
    out: dict = {}
    out["code"] = value["code"]
    out["installationId"] = value["installation_id"]
    return out


def deserialize_json(data: dict) -> UpdateGitHubIntegrationDetail:
    out: UpdateGitHubIntegrationDetail = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        out["code"] = data["code"]
    else:
        out["code"] = ""
    if data.get("installationId") is not None:
        out["installation_id"] = data["installationId"]
    else:
        out["installation_id"] = ""
    return out


def redact_sensitive(value: UpdateGitHubIntegrationDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "code" in value:
        out["code"] = "*** Sensitive Data Redacted ***"
    return out
