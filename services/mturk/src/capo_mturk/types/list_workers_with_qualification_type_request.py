"""Generated from Smithy shape ``com.amazonaws.mturk#ListWorkersWithQualificationTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id
    import capo_mturk.types.pagination_token
    import capo_mturk.types.qualification_status
    import capo_mturk.types.result_size


class ListWorkersWithQualificationTypeRequest(TypedDict, closed=True):
    qualification_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the Qualification type of the Qualifications to return.</p>"""
    status: NotRequired["capo_mturk.types.qualification_status.QualificationStatus"]
    """<p> The status of the Qualifications to return. Can be <code>Granted | Revoked</code>. </p>"""
    next_token: NotRequired["capo_mturk.types.pagination_token.PaginationToken"]
    """<p>Pagination Token</p>"""
    max_results: NotRequired["capo_mturk.types.result_size.ResultSize"]
    """<p> Limit the number of results returned. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWorkersWithQualificationTypeRequest) -> dict:
    out: dict = {}
    out["QualificationTypeId"] = value["qualification_type_id"]
    if "status" in value:
        import capo_mturk.types.qualification_status

        out["Status"] = capo_mturk.types.qualification_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWorkersWithQualificationTypeRequest:
    out: ListWorkersWithQualificationTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("QualificationTypeId") is not None:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        out["qualification_type_id"] = ""
    if data.get("Status") is not None:
        import capo_mturk.types.qualification_status

        out["status"] = capo_mturk.types.qualification_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    return out
