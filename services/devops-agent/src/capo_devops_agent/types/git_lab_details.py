"""Generated from Smithy shape ``com.amazonaws.devopsagent#GitLabDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.git_lab_token_type
    import capo_devops_agent.types.git_lab_token_value


class GitLabDetails(TypedDict, closed=True):
    target_url: "str"
    """<p>GitLab instance URL (e.g., https://gitlab.com or self-hosted instance).</p>"""
    token_type: "capo_devops_agent.types.git_lab_token_type.GitLabTokenType"
    """<p>Type of GitLab access token</p>"""
    token_value: "capo_devops_agent.types.git_lab_token_value.GitLabTokenValue"
    """<p>GitLab access token value</p>"""
    group_id: NotRequired["str"]
    """<p>Optional GitLab group ID for group-level access tokens</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabDetails) -> dict:
    out: dict = {}
    out["targetUrl"] = value["target_url"]
    import capo_devops_agent.types.git_lab_token_type

    out["tokenType"] = capo_devops_agent.types.git_lab_token_type.serialize_json(
        value["token_type"]
    )
    out["tokenValue"] = value["token_value"]
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> GitLabDetails:
    out: GitLabDetails = {}  # type: ignore[typeddict-item]
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
    if data.get("tokenValue") is not None:
        out["token_value"] = data["tokenValue"]
    else:
        out["token_value"] = ""
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    return out


def redact_sensitive(value: GitLabDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "token_value" in value:
        out["token_value"] = "*** Sensitive Data Redacted ***"
    return out
