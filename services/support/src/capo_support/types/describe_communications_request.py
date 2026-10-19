"""Generated from Smithy shape ``com.amazonaws.support#DescribeCommunicationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_support.types.after_time
    import capo_support.types.before_time
    import capo_support.types.case_id
    import capo_support.types.max_results
    import capo_support.types.next_token
    import capo_support.types.nullable_boolean_type


class DescribeCommunicationsRequest(TypedDict, closed=True):
    case_id: "capo_support.types.case_id.CaseId"
    """<p>The support case ID requested or returned in the call. The case ID is an alphanumeric string formatted as shown in this example: case-<i>12345678910-exen-2025-c4c1d2bf33c5cf47</i> </p>"""
    before_time: NotRequired["capo_support.types.before_time.BeforeTime"]
    """<p>The end date for a filtered date search on support case communications. Case communications are available for 24 months after creation.</p>"""
    after_time: NotRequired["capo_support.types.after_time.AfterTime"]
    """<p>The start date for a filtered date search on support case communications. Case communications are available for 24 months after creation.</p>"""
    next_token: NotRequired["capo_support.types.next_token.NextToken"]
    """<p>A resumption point for pagination.</p>"""
    max_results: NotRequired["capo_support.types.max_results.MaxResults"]
    """<p>The maximum number of results to return before paginating.</p>"""
    dry_run: NotRequired["capo_support.types.nullable_boolean_type.NullableBooleanType"]
    """<p>Specifies whether to validate the request without actually returning communications. When set to <code>true</code>, the request is validated but no communications are returned, and the operation returns a <code>DryRunOperationException</code>. When omitted or set to <code>false</code>, the request runs normally.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCommunicationsRequest) -> dict:
    out: dict = {}
    out["caseId"] = value["case_id"]
    if "before_time" in value:
        out["beforeTime"] = value["before_time"]
    if "after_time" in value:
        out["afterTime"] = value["after_time"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "dry_run" in value:
        out["dryRun"] = value["dry_run"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCommunicationsRequest:
    out: DescribeCommunicationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("caseId") is not None:
        out["case_id"] = data["caseId"]
    else:
        out["case_id"] = ""
    if data.get("beforeTime") is not None:
        out["before_time"] = data["beforeTime"]
    if data.get("afterTime") is not None:
        out["after_time"] = data["afterTime"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("dryRun") is not None:
        out["dry_run"] = data["dryRun"]
    return out
