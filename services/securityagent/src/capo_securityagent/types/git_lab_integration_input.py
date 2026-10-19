"""Generated from Smithy shape ``com.amazonaws.securityagent#GitLabIntegrationInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.access_token
    import capo_securityagent.types.git_lab_token_type
    import capo_securityagent.types.target_url


class GitLabIntegrationInput(TypedDict, closed=True):
    access_token: "capo_securityagent.types.access_token.AccessToken"
    """<p>The GitLab access token used to authenticate. This can be a personal access token or a group access token.</p>"""
    target_url: NotRequired["capo_securityagent.types.target_url.TargetUrl"]
    """<p>The HTTPS URL of a self-managed GitLab instance. Omit this value for GitLab SaaS (gitlab.com).</p>"""
    token_type: "capo_securityagent.types.git_lab_token_type.GitLabTokenType"
    """<p>The type of GitLab access token provided in accessToken.</p>"""
    group_id: NotRequired["str"]
    """<p>The identifier of the GitLab group. Required when tokenType is group and ignored for personal tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabIntegrationInput) -> dict:
    out: dict = {}
    out["accessToken"] = value["access_token"]
    if "target_url" in value:
        out["targetUrl"] = value["target_url"]
    import capo_securityagent.types.git_lab_token_type

    out["tokenType"] = capo_securityagent.types.git_lab_token_type.serialize_json(
        value["token_type"]
    )
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> GitLabIntegrationInput:
    out: GitLabIntegrationInput = {}  # type: ignore[typeddict-item]
    if data.get("accessToken") is not None:
        out["access_token"] = data["accessToken"]
    else:
        out["access_token"] = ""
    if data.get("targetUrl") is not None:
        out["target_url"] = data["targetUrl"]
    if data.get("tokenType") is not None:
        import capo_securityagent.types.git_lab_token_type

        out["token_type"] = (
            capo_securityagent.types.git_lab_token_type.deserialize_json(
                data["tokenType"]
            )
        )
    else:
        import typing

        out["token_type"] = typing.cast(
            "capo_securityagent.types.git_lab_token_type.GitLabTokenType", ""
        )
    if data.get("groupId") is not None:
        out["group_id"] = data["groupId"]
    return out


def redact_sensitive(value: GitLabIntegrationInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "access_token" in value:
        out["access_token"] = "*** Sensitive Data Redacted ***"
    return out
