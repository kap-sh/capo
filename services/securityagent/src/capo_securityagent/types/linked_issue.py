"""Generated from Smithy shape ``com.amazonaws.securityagent#LinkedIssue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.provider


class LinkedIssue(TypedDict, closed=True):
    provider: NotRequired["capo_securityagent.types.provider.Provider"]
    """<p>The issue-tracker provider.</p>"""
    integration_id: NotRequired["str"]
    """<p>The integration identifier for the issue-tracker provider.</p>"""
    project_key: NotRequired["str"]
    """<p>The key of the project the issue belongs to.</p>"""
    issue_key: NotRequired["str"]
    """<p>The issue key.</p>"""
    issue_id: NotRequired["str"]
    """<p>The stable numeric issue identifier.</p>"""
    issue_url: NotRequired["str"]
    """<p>The issue URL.</p>"""
    site_url: NotRequired["str"]
    """<p>The Atlassian Cloud site URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LinkedIssue) -> dict:
    out: dict = {}
    if "provider" in value:
        import capo_securityagent.types.provider

        out["provider"] = capo_securityagent.types.provider.serialize_json(
            value["provider"]
        )
    if "integration_id" in value:
        out["integrationId"] = value["integration_id"]
    if "project_key" in value:
        out["projectKey"] = value["project_key"]
    if "issue_key" in value:
        out["issueKey"] = value["issue_key"]
    if "issue_id" in value:
        out["issueId"] = value["issue_id"]
    if "issue_url" in value:
        out["issueUrl"] = value["issue_url"]
    if "site_url" in value:
        out["siteUrl"] = value["site_url"]
    return out


def deserialize_json(data: dict) -> LinkedIssue:
    out: LinkedIssue = {}  # type: ignore[typeddict-item]
    if data.get("provider") is not None:
        import capo_securityagent.types.provider

        out["provider"] = capo_securityagent.types.provider.deserialize_json(
            data["provider"]
        )
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    if data.get("projectKey") is not None:
        out["project_key"] = data["projectKey"]
    if data.get("issueKey") is not None:
        out["issue_key"] = data["issueKey"]
    if data.get("issueId") is not None:
        out["issue_id"] = data["issueId"]
    if data.get("issueUrl") is not None:
        out["issue_url"] = data["issueUrl"]
    if data.get("siteUrl") is not None:
        out["site_url"] = data["siteUrl"]
    return out
