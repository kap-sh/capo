"""Generated from Smithy shape ``com.amazonaws.guardduty#ListInvestigationRecordsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.detector_id
    import capo_guardduty.types.investigation_id
    import capo_guardduty.types.max_results
    import capo_guardduty.types.next_token
    import capo_guardduty.types.record_types


class ListInvestigationRecordsRequest(TypedDict, closed=True):
    detector_id: "capo_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the GuardDuty detector associated with the investigation.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href="https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html">ListDetectors</a> API.</p>"""
    investigation_id: NotRequired[
        "capo_guardduty.types.investigation_id.InvestigationId"
    ]
    """<p>The unique identifier of the investigation whose records you want to list.</p>"""
    record_types: NotRequired["capo_guardduty.types.record_types.RecordTypes"]
    """<p>The types of records to return. Possible values are <code>UPDATE</code>, <code>FETCH</code>, <code>OBSERVATION</code>, <code>ANALYSIS</code>, and <code>METADATA</code>. If you don't specify this parameter, GuardDuty returns records of all types.</p>"""
    max_results: NotRequired["capo_guardduty.types.max_results.MaxResults"]
    """<p>The maximum number of records to return in a single response. Valid values are 1 to 50. The default value is 20. A response can contain fewer records than this value, or no records, and still include a <code>NextToken</code>.</p>"""
    next_token: NotRequired["capo_guardduty.types.next_token.NextToken"]
    """<p>You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill nextToken in the request with the value of NextToken from the previous response to continue listing data. Use the same <code>InvestigationId</code> and <code>RecordTypes</code> values that you used in the previous request.</p> <p>If you specify this parameter for an investigation whose status isn't <code>COMPLETED</code>, the operation returns a <code>BadRequestException</code>. A <code>NextToken</code> expires 24 hours after it's returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationRecordsRequest) -> dict:
    out: dict = {}
    if "investigation_id" in value:
        out["investigationId"] = value["investigation_id"]
    if "record_types" in value:
        import capo_guardduty.types.record_types

        out["recordTypes"] = capo_guardduty.types.record_types.serialize_json(
            value["record_types"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInvestigationRecordsRequest:
    out: ListInvestigationRecordsRequest = {}  # type: ignore[typeddict-item]
    if data.get("investigationId") is not None:
        out["investigation_id"] = data["investigationId"]
    if data.get("recordTypes") is not None:
        import capo_guardduty.types.record_types

        out["record_types"] = capo_guardduty.types.record_types.deserialize_json(
            data["recordTypes"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
