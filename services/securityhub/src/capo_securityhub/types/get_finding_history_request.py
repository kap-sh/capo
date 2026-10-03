"""Generated from Smithy shape ``com.amazonaws.securityhub#GetFindingHistoryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_security_finding_identifier
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.timestamp


class GetFindingHistoryRequest(TypedDict, closed=True):
    finding_identifier: NotRequired[
        "capo_securityhub.types.aws_security_finding_identifier.AwsSecurityFindingIdentifier"
    ]
    start_time: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p>A timestamp that indicates the start time of the requested finding history.</p> <p>If you provide values for both <code>StartTime</code> and <code>EndTime</code>, Security Hub CSPM returns finding history for the specified time period. If you provide a value for <code>StartTime</code> but not for <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>StartTime</code> to the time at which the API is called. If you provide a value for <code>EndTime</code> but not for <code>StartTime</code>, Security Hub CSPM returns finding history from the <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html#securityhub-Type-AwsSecurityFindingFilters-CreatedAt">CreatedAt</a> timestamp of the finding to the <code>EndTime</code>. If you provide neither <code>StartTime</code> nor <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>CreatedAt</code> timestamp of the finding to the time at which the API is called. In all of these scenarios, the response is limited to 100 results.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    end_time: NotRequired["capo_securityhub.types.timestamp.Timestamp"]
    """<p> An ISO 8601-formatted timestamp that indicates the end time of the requested finding history.</p> <p>If you provide values for both <code>StartTime</code> and <code>EndTime</code>, Security Hub CSPM returns finding history for the specified time period. If you provide a value for <code>StartTime</code> but not for <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>StartTime</code> to the time at which the API is called. If you provide a value for <code>EndTime</code> but not for <code>StartTime</code>, Security Hub CSPM returns finding history from the <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsSecurityFindingFilters.html#securityhub-Type-AwsSecurityFindingFilters-CreatedAt">CreatedAt</a> timestamp of the finding to the <code>EndTime</code>. If you provide neither <code>StartTime</code> nor <code>EndTime</code>, Security Hub CSPM returns finding history from the <code>CreatedAt</code> timestamp of the finding to the time at which the API is called. In all of these scenarios, the response is limited to 100 results.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p> A token for pagination purposes. Provide <code>NULL</code> as the initial value. In subsequent requests, provide the token included in the response to get up to an additional 100 results of finding history. If you don’t provide <code>NextToken</code>, Security Hub CSPM returns up to 100 results of finding history for each request. </p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p> The maximum number of results to be returned. If you don’t provide it, Security Hub CSPM returns up to 100 results of finding history. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingHistoryRequest) -> dict:
    out: dict = {}
    if "finding_identifier" in value:
        import capo_securityhub.types.aws_security_finding_identifier

        out["FindingIdentifier"] = (
            capo_securityhub.types.aws_security_finding_identifier.serialize_json(
                value["finding_identifier"]
            )
        )
    if "start_time" in value:
        import capo_securityhub.types.timestamp

        out["StartTime"] = capo_securityhub.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_securityhub.types.timestamp

        out["EndTime"] = capo_securityhub.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetFindingHistoryRequest:
    out: GetFindingHistoryRequest = {}  # type: ignore[typeddict-item]
    if data.get("FindingIdentifier") is not None:
        import capo_securityhub.types.aws_security_finding_identifier

        out["finding_identifier"] = (
            capo_securityhub.types.aws_security_finding_identifier.deserialize_json(
                data["FindingIdentifier"]
            )
        )
    if data.get("StartTime") is not None:
        import capo_securityhub.types.timestamp

        out["start_time"] = capo_securityhub.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if data.get("EndTime") is not None:
        import capo_securityhub.types.timestamp

        out["end_time"] = capo_securityhub.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
