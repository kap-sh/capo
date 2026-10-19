"""Generated from Smithy shape ``com.amazonaws.securityagent#IssueDestination``."""

from typing_extensions import TypedDict


class IssueDestination(TypedDict, closed=True):
    integration_id: "str"
    """<p>The integration identifier for the issue-tracker provider.</p>"""
    project_key: "str"
    """<p>The identifier of the project the issues are filed under.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IssueDestination) -> dict:
    out: dict = {}
    out["integrationId"] = value["integration_id"]
    out["projectKey"] = value["project_key"]
    return out


def deserialize_json(data: dict) -> IssueDestination:
    out: IssueDestination = {}  # type: ignore[typeddict-item]
    if data.get("integrationId") is not None:
        out["integration_id"] = data["integrationId"]
    else:
        out["integration_id"] = ""
    if data.get("projectKey") is not None:
        out["project_key"] = data["projectKey"]
    else:
        out["project_key"] = ""
    return out
