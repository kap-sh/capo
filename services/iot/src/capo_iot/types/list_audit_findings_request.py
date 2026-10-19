"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditFindingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_check_name
    import capo_iot.types.audit_task_id
    import capo_iot.types.list_suppressed_findings
    import capo_iot.types.max_results
    import capo_iot.types.next_token
    import capo_iot.types.resource_identifier
    import capo_iot.types.timestamp


class ListAuditFindingsRequest(TypedDict, closed=True):
    task_id: NotRequired["capo_iot.types.audit_task_id.AuditTaskId"]
    """<p>A filter to limit results to the audit with the specified ID. You must specify either the taskId or the startTime and endTime, but not both.</p>"""
    check_name: NotRequired["capo_iot.types.audit_check_name.AuditCheckName"]
    """<p>A filter to limit results to the findings for the specified audit check.</p>"""
    resource_identifier: NotRequired[
        "capo_iot.types.resource_identifier.ResourceIdentifier"
    ]
    """<p>Information identifying the noncompliant resource.</p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    start_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.</p>"""
    end_time: NotRequired["capo_iot.types.timestamp.Timestamp"]
    """<p>A filter to limit results to those found before the specified time. You must specify either the startTime and endTime or the taskId, but not both.</p>"""
    list_suppressed_findings: NotRequired[
        "capo_iot.types.list_suppressed_findings.ListSuppressedFindings"
    ]
    """<p> Boolean flag indicating whether only the suppressed findings or the unsuppressed findings should be listed. If this parameter isn't provided, the response will list both suppressed and unsuppressed findings. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditFindingsRequest) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "check_name" in value:
        out["checkName"] = value["check_name"]
    if "resource_identifier" in value:
        import capo_iot.types.resource_identifier

        out["resourceIdentifier"] = capo_iot.types.resource_identifier.serialize_json(
            value["resource_identifier"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "start_time" in value:
        import capo_iot.types.timestamp

        out["startTime"] = capo_iot.types.timestamp.serialize_json(value["start_time"])
    if "end_time" in value:
        import capo_iot.types.timestamp

        out["endTime"] = capo_iot.types.timestamp.serialize_json(value["end_time"])
    if "list_suppressed_findings" in value:
        out["listSuppressedFindings"] = value["list_suppressed_findings"]
    return out


def deserialize_json(data: dict) -> ListAuditFindingsRequest:
    out: ListAuditFindingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("checkName") is not None:
        out["check_name"] = data["checkName"]
    if data.get("resourceIdentifier") is not None:
        import capo_iot.types.resource_identifier

        out["resource_identifier"] = (
            capo_iot.types.resource_identifier.deserialize_json(
                data["resourceIdentifier"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("startTime") is not None:
        import capo_iot.types.timestamp

        out["start_time"] = capo_iot.types.timestamp.deserialize_json(data["startTime"])
    if data.get("endTime") is not None:
        import capo_iot.types.timestamp

        out["end_time"] = capo_iot.types.timestamp.deserialize_json(data["endTime"])
    if data.get("listSuppressedFindings") is not None:
        out["list_suppressed_findings"] = data["listSuppressedFindings"]
    return out
