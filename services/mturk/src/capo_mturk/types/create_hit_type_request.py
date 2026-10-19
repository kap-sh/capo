"""Generated from Smithy shape ``com.amazonaws.mturk#CreateHITTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.currency_amount
    import capo_mturk.types.long
    import capo_mturk.types.qualification_requirement_list
    import capo_mturk.types.string


class CreateHITTypeRequest(TypedDict, closed=True):
    auto_approval_delay_in_seconds: NotRequired["capo_mturk.types.long.Long"]
    """<p> The number of seconds after an assignment for the HIT has been submitted, after which the assignment is considered Approved automatically unless the Requester explicitly rejects it. </p>"""
    assignment_duration_in_seconds: "capo_mturk.types.long.Long"
    """<p> The amount of time, in seconds, that a Worker has to complete the HIT after accepting it. If a Worker does not complete the assignment within the specified duration, the assignment is considered abandoned. If the HIT is still active (that is, its lifetime has not elapsed), the assignment becomes available for other users to find and accept. </p>"""
    reward: "capo_mturk.types.currency_amount.CurrencyAmount"
    """<p> The amount of money the Requester will pay a Worker for successfully completing the HIT. </p>"""
    title: "capo_mturk.types.string.String"
    """<p> The title of the HIT. A title should be short and descriptive about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT title appears in search results, and everywhere the HIT is mentioned. </p>"""
    keywords: NotRequired["capo_mturk.types.string.String"]
    """<p> One or more words or phrases that describe the HIT, separated by commas. These words are used in searches to find HITs. </p>"""
    description: "capo_mturk.types.string.String"
    """<p> A general description of the HIT. A description includes detailed information about the kind of task the HIT contains. On the Amazon Mechanical Turk web site, the HIT description appears in the expanded view of search results, and in the HIT and assignment screens. A good description gives the user enough information to evaluate the HIT before accepting it. </p>"""
    qualification_requirements: NotRequired[
        "capo_mturk.types.qualification_requirement_list.QualificationRequirementList"
    ]
    """<p> Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the <code>ActionsGuarded</code> field on each <code>QualificationRequirement</code> structure. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHITTypeRequest) -> dict:
    out: dict = {}
    if "auto_approval_delay_in_seconds" in value:
        out["AutoApprovalDelayInSeconds"] = value["auto_approval_delay_in_seconds"]
    out["AssignmentDurationInSeconds"] = value["assignment_duration_in_seconds"]
    out["Reward"] = value["reward"]
    out["Title"] = value["title"]
    if "keywords" in value:
        out["Keywords"] = value["keywords"]
    out["Description"] = value["description"]
    if "qualification_requirements" in value:
        import capo_mturk.types.qualification_requirement_list

        out["QualificationRequirements"] = (
            capo_mturk.types.qualification_requirement_list.serialize_aws_json_1_1(
                value["qualification_requirements"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHITTypeRequest:
    out: CreateHITTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("AutoApprovalDelayInSeconds") is not None:
        out["auto_approval_delay_in_seconds"] = data["AutoApprovalDelayInSeconds"]
    if data.get("AssignmentDurationInSeconds") is not None:
        out["assignment_duration_in_seconds"] = data["AssignmentDurationInSeconds"]
    else:
        out["assignment_duration_in_seconds"] = 0
    if data.get("Reward") is not None:
        out["reward"] = data["Reward"]
    else:
        out["reward"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("Keywords") is not None:
        out["keywords"] = data["Keywords"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    else:
        out["description"] = ""
    if data.get("QualificationRequirements") is not None:
        import capo_mturk.types.qualification_requirement_list

        out["qualification_requirements"] = (
            capo_mturk.types.qualification_requirement_list.deserialize_aws_json_1_1(
                data["QualificationRequirements"]
            )
        )
    return out
