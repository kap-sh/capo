"""Generated from Smithy shape ``com.amazonaws.devopsagent#RegisteredGitLabServiceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.git_lab_token_type


class RegisteredGitLabServiceDetails(TypedDict, closed=True):
    target_url: "str"
    """<p>The GitLab instance URL.</p>"""
    token_type: "capo_devops_agent.types.git_lab_token_type.GitLabTokenType"
    """<p>Type of GitLab access token</p>"""
    group_id: NotRequired["str"]
    """<p>Optional GitLab group ID for group-level access tokens</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredGitLabServiceDetails) -> dict:
    out: dict = {}
    out["targetUrl"] = value["target_url"]
    import capo_devops_agent.types.git_lab_token_type

    out["tokenType"] = capo_devops_agent.types.git_lab_token_type.serialize_json(
        value["token_type"]
    )
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> RegisteredGitLabServiceDetails:
    out: RegisteredGitLabServiceDetails = {}  # type: ignore[typeddict-item]
    if data.get("targetUrl") is not None:
        out["target_url"] = data["targetUrl"]
    else:
        out["target_url"] = ""
    if data.get("tokenType") is not None:
        import capo_devops_agent.types.git_lab_token_type

        out["token_type"] = capo_devops_agent.types.git_lab_token_type.deserialize_json(
            data["tokenType"]
        )
    else:
        import typing

        out["token_type"] = typing.cast(
            "capo_devops_agent.types.git_lab_token_type.GitLabTokenType", ""
        )
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    return out
