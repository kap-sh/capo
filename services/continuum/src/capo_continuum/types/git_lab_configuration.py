"""Generated from Smithy shape ``com.amazonaws.continuum#GitLabConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.git_lab_access_token
    import capo_continuum.types.git_lab_instance_url
    import capo_continuum.types.git_lab_target_path
    import capo_continuum.types.git_lab_target_type


class GitLabConfiguration(TypedDict, closed=True):
    instance_url: "capo_continuum.types.git_lab_instance_url.GitLabInstanceUrl"
    """The HTTPS base URL of the GitLab instance (gitlab.com or self-managed)."""
    target_type: "capo_continuum.types.git_lab_target_type.GitLabTargetType"
    """Whether the integration targets a group or a single project."""
    target_path: "capo_continuum.types.git_lab_target_path.GitLabTargetPath"
    """The group or project path the integration targets."""
    access_token: "capo_continuum.types.git_lab_access_token.GitLabAccessToken"
    """The GitLab access token (personal, group or project). Write-only; not stored or returned after creation. If the token carries the self-rotate scope, rotation is opted in and Continuum manages the token thereafter."""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabConfiguration) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    import capo_continuum.types.git_lab_target_type

    out["targetType"] = capo_continuum.types.git_lab_target_type.serialize_json(
        value["target_type"]
    )
    out["targetPath"] = value["target_path"]
    out["accessToken"] = value["access_token"]
    return out


def deserialize_json(data: dict) -> GitLabConfiguration:
    out: GitLabConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("instanceUrl") is not None:
        out["instance_url"] = data["instanceUrl"]
    else:
        out["instance_url"] = ""
    if data.get("targetType") is not None:
        import capo_continuum.types.git_lab_target_type

        out["target_type"] = capo_continuum.types.git_lab_target_type.deserialize_json(
            data["targetType"]
        )
    else:
        import typing

        out["target_type"] = typing.cast(
            "capo_continuum.types.git_lab_target_type.GitLabTargetType", ""
        )
    if data.get("targetPath") is not None:
        out["target_path"] = data["targetPath"]
    else:
        out["target_path"] = ""
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    else:
        out["access_token"] = ""
    return out


def redact_sensitive(value: GitLabConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
