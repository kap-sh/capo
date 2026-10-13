"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateGitLabSelfManagedIntegrationDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.git_lab_auth_code


class UpdateGitLabSelfManagedIntegrationDetail(TypedDict, closed=True):
    auth_code: "capo_inspector2.types.git_lab_auth_code.GitLabAuthCode"
    """<p>The authorization code received from the self-managed GitLab instance to update the integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGitLabSelfManagedIntegrationDetail) -> dict:
    out: dict = {}
    out["authCode"] = value["auth_code"]
    return out


def deserialize_json(data: dict) -> UpdateGitLabSelfManagedIntegrationDetail:
    out: UpdateGitLabSelfManagedIntegrationDetail = {}  # type: ignore[typeddict-item]
    if data.get("authCode") is not None:
        out["auth_code"] = data["authCode"]
    else:
        raise DeserializationError(
            "UpdateGitLabSelfManagedIntegrationDetail.auth_code required"
        )
    return out


def redact_sensitive(value: UpdateGitLabSelfManagedIntegrationDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_code" in value:
        out["auth_code"] = "*** Sensitive Data Redacted ***"
    return out
