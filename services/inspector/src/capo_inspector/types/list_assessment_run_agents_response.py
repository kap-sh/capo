"""Generated from Smithy shape ``com.amazonaws.inspector#ListAssessmentRunAgentsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector.types.assessment_run_agent_list
    import capo_inspector.types.pagination_token


class ListAssessmentRunAgentsResponse(TypedDict, closed=True):
    assessment_run_agents: (
        "capo_inspector.types.assessment_run_agent_list.AssessmentRunAgentList"
    )
    """<p>A list of ARNs that specifies the agents returned by the action.</p>"""
    next_token: NotRequired["capo_inspector.types.pagination_token.PaginationToken"]
    """<p> When a response is generated, if there is more data to be listed, this parameter is present in the response and contains the value to use for the <b>nextToken</b> parameter in a subsequent pagination request. If there is no more data to be listed, this parameter is set to null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAssessmentRunAgentsResponse) -> dict:
    out: dict = {}
    import capo_inspector.types.assessment_run_agent_list

    out["assessmentRunAgents"] = (
        capo_inspector.types.assessment_run_agent_list.serialize_aws_json_1_1(
            value["assessment_run_agents"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAssessmentRunAgentsResponse:
    out: ListAssessmentRunAgentsResponse = {}  # type: ignore[typeddict-item]
    if data.get("assessmentRunAgents") is not None:
        import capo_inspector.types.assessment_run_agent_list

        out["assessment_run_agents"] = (
            capo_inspector.types.assessment_run_agent_list.deserialize_aws_json_1_1(
                data["assessmentRunAgents"]
            )
        )
    else:
        out["assessment_run_agents"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
