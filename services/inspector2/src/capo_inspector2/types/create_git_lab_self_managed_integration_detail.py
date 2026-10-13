"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateGitLabSelfManagedIntegrationDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.git_lab_access_token
    import capo_inspector2.types.instance_url


class CreateGitLabSelfManagedIntegrationDetail(TypedDict, closed=True):
    instance_url: "capo_inspector2.types.instance_url.InstanceUrl"
    """<p>The URL of the self-managed GitLab instance.</p>"""
    access_token: "capo_inspector2.types.git_lab_access_token.GitLabAccessToken"
    """<p>The personal access token used to authenticate with the self-managed GitLab instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGitLabSelfManagedIntegrationDetail) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    out["accessToken"] = value["access_token"]
    return out


def deserialize_json(data: dict) -> CreateGitLabSelfManagedIntegrationDetail:
    out: CreateGitLabSelfManagedIntegrationDetail = {}  # type: ignore[typeddict-item]
    if data.get("instanceUrl") is not None:
        out["instance_url"] = data["instanceUrl"]
    else:
        raise DeserializationError(
            "CreateGitLabSelfManagedIntegrationDetail.instance_url required"
        )
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    else:
        raise DeserializationError(
            "CreateGitLabSelfManagedIntegrationDetail.access_token required"
        )
    return out


def redact_sensitive(value: CreateGitLabSelfManagedIntegrationDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "instance_url" in value:
        out["instance_url"] = "*** Sensitive Data Redacted ***"
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
