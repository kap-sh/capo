"""Generated from Smithy shape ``com.amazonaws.mturk#ListAssignmentsForHITRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.assignment_status_list
    import capo_mturk.types.entity_id
    import capo_mturk.types.pagination_token
    import capo_mturk.types.result_size


class ListAssignmentsForHITRequest(TypedDict, closed=True):
    hit_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the HIT.</p>"""
    next_token: NotRequired["capo_mturk.types.pagination_token.PaginationToken"]
    """<p>Pagination token</p>"""
    max_results: NotRequired["capo_mturk.types.result_size.ResultSize"]
    assignment_statuses: NotRequired[
        "capo_mturk.types.assignment_status_list.AssignmentStatusList"
    ]
    """<p>The status of the assignments to return: Submitted | Approved | Rejected</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssignmentsForHITRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "assignment_statuses" in value:
        import capo_mturk.types.assignment_status_list

        out["AssignmentStatuses"] = (
            capo_mturk.types.assignment_status_list.serialize_aws_json_1_1(
                value["assignment_statuses"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssignmentsForHITRequest:
    out: ListAssignmentsForHITRequest = {}  # type: ignore[typeddict-item]
    if data.get("HITId") is not None:
        out["hit_id"] = data["HITId"]
    else:
        out["hit_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("AssignmentStatuses") is not None:
        import capo_mturk.types.assignment_status_list

        out["assignment_statuses"] = (
            capo_mturk.types.assignment_status_list.deserialize_aws_json_1_1(
                data["AssignmentStatuses"]
            )
        )
    return out
