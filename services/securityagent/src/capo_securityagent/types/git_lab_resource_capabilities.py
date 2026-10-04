"""Generated from Smithy shape ``com.amazonaws.securityagent#GitLabResourceCapabilities``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityagent.types.trigger_filter_groups


class GitLabResourceCapabilities(TypedDict, closed=True):
    trigger_filter_groups: NotRequired[
        "capo_securityagent.types.trigger_filter_groups.TriggerFilterGroups"
    ]
    """<p>The filter groups that control which merge request events start an automatic code review when <code>leaveComments</code> is enabled. A review starts when any group matches. If you omit this, a review starts on <code>PULL_REQUEST_READY_FOR_REVIEW</code> events.</p>"""
    leave_comments: NotRequired["bool"]
    """<p>Whether to post code review comments on merge request discussions.</p>"""
    remediate_code: NotRequired["bool"]
    """<p>Whether to create merge requests with automated fixes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GitLabResourceCapabilities) -> dict:
    out: dict = {}
    if "trigger_filter_groups" in value:
        import capo_securityagent.types.trigger_filter_groups

        out["triggerFilterGroups"] = (
            capo_securityagent.types.trigger_filter_groups.serialize_json(
                value["trigger_filter_groups"]
            )
        )
    if "leave_comments" in value:
        out["leaveComments"] = value["leave_comments"]
    if "remediate_code" in value:
        out["remediateCode"] = value["remediate_code"]
    return out


def deserialize_json(data: dict) -> GitLabResourceCapabilities:
    out: GitLabResourceCapabilities = {}  # type: ignore[typeddict-item]
    if data.get("triggerFilterGroups") is not None:
        import capo_securityagent.types.trigger_filter_groups

        out["trigger_filter_groups"] = (
            capo_securityagent.types.trigger_filter_groups.deserialize_json(
                data["triggerFilterGroups"]
            )
        )
    if data.get("leaveComments") is not None:
        out["leave_comments"] = data["leaveComments"]
    if data.get("remediateCode") is not None:
        out["remediate_code"] = data["remediateCode"]
    return out
