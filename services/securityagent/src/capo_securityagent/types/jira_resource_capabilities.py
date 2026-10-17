"""Generated from Smithy shape ``com.amazonaws.securityagent#JiraResourceCapabilities``."""

from typing_extensions import NotRequired, TypedDict


class JiraResourceCapabilities(TypedDict, closed=True):
    create_issue: NotRequired["bool"]
    """<p>Whether to create issues in the integrated jira project.</p>"""
    comment_issue: NotRequired["bool"]
    """<p>Whether to post comments on issues in the integrated jira project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JiraResourceCapabilities) -> dict:
    out: dict = {}
    if "create_issue" in value:
        out["createIssue"] = value["create_issue"]
    if "comment_issue" in value:
        out["commentIssue"] = value["comment_issue"]
    return out


def deserialize_json(data: dict) -> JiraResourceCapabilities:
    out: JiraResourceCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("createIssue") is not None:
        out["create_issue"] = data["createIssue"]
    if data.get("commentIssue") is not None:
        out["comment_issue"] = data["commentIssue"]
    return out
