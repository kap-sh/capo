"""Generated from Smithy shape ``com.amazonaws.continuum#GitLabDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_continuum.types.git_lab_instance_url
    import capo_continuum.types.git_lab_target_path
    import capo_continuum.types.git_lab_target_type
    import capo_continuum.types.git_lab_token_rotation


class GitLabDetails(TypedDict, closed=True):
    instance_url: "capo_continuum.types.git_lab_instance_url.GitLabInstanceUrl"
    """The HTTPS base URL of the GitLab instance."""
    target_type: "capo_continuum.types.git_lab_target_type.GitLabTargetType"
    """Whether the integration targets a group or a single project."""
    target_path: "capo_continuum.types.git_lab_target_path.GitLabTargetPath"
    """The group or project path the integration targets."""
    token_rotation: "capo_continuum.types.git_lab_token_rotation.GitLabTokenRotation"
    """How the integration's access token is rotated. AUTOMATIC only when the pasted token had the self-rotate scope and rotation was opted in at installation time."""
    expires_at: NotRequired["datetime.datetime"]
    """The expiry of the stored access token, for non-rotating tokens only. A rotated token's original expiry is stale, so this is omitted when tokenRotation is AUTOMATIC."""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabDetails) -> dict:
    out: dict = {}
    out["instanceUrl"] = value["instance_url"]
    import capo_continuum.types.git_lab_target_type

    out["targetType"] = capo_continuum.types.git_lab_target_type.serialize_json(
        value["target_type"]
    )
    out["targetPath"] = value["target_path"]
    import capo_continuum.types.git_lab_token_rotation

    out["tokenRotation"] = capo_continuum.types.git_lab_token_rotation.serialize_json(
        value["token_rotation"]
    )
    if "expires_at" in value:
        import capo_continuum._protocol.serialize

        out["expiresAt"] = capo_continuum._protocol.serialize.fmt_date_time(
            value["expires_at"]
        )
    return out


def deserialize_json(data: dict) -> GitLabDetails:
    out: GitLabDetails = {}  # type: ignore[typeddict-item]
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
    if data.get("tokenRotation") is not None:
        import capo_continuum.types.git_lab_token_rotation

        out["token_rotation"] = (
            capo_continuum.types.git_lab_token_rotation.deserialize_json(
                data["tokenRotation"]
            )
        )
    else:
        import typing

        out["token_rotation"] = typing.cast(
            "capo_continuum.types.git_lab_token_rotation.GitLabTokenRotation", ""
        )
    if data.get("expiresAt") is not None:
        import datetime

        out["expires_at"] = datetime.datetime.fromisoformat(
            data["expiresAt"].replace("Z", "+00:00")
        )
    return out
