"""Generated from Smithy shape ``com.amazonaws.mturk#CreateHITRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.currency_amount
    import capo_mturk.types.entity_id
    import capo_mturk.types.hit_layout_parameter_list
    import capo_mturk.types.idempotency_token
    import capo_mturk.types.integer
    import capo_mturk.types.long
    import capo_mturk.types.qualification_requirement_list
    import capo_mturk.types.review_policy
    import capo_mturk.types.string


class CreateHITRequest(TypedDict, closed=True):
    max_assignments: NotRequired["capo_mturk.types.integer.Integer"]
    """<p> The number of times the HIT can be accepted and completed before the HIT becomes unavailable. </p>"""
    auto_approval_delay_in_seconds: NotRequired["capo_mturk.types.long.Long"]
    """<p> The number of seconds after an assignment for the HIT has been submitted, after which the assignment is considered Approved automatically unless the Requester explicitly rejects it. </p>"""
    lifetime_in_seconds: "capo_mturk.types.long.Long"
    """<p> An amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted. </p>"""
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
    question: NotRequired["capo_mturk.types.string.String"]
    """<p> The data the person completing the HIT uses to produce the results. </p> <p> Constraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace. </p> <p>Either a Question parameter or a HITLayoutId parameter must be provided.</p>"""
    requester_annotation: NotRequired["capo_mturk.types.string.String"]
    """<p> An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester's application that corresponds with the HIT. </p> <p> The RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester. </p> <p> The RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped. </p>"""
    qualification_requirements: NotRequired[
        "capo_mturk.types.qualification_requirement_list.QualificationRequirementList"
    ]
    """<p> Conditions that a Worker's Qualifications must meet in order to accept the HIT. A HIT can have between zero and ten Qualification requirements. All requirements must be met in order for a Worker to accept the HIT. Additionally, other actions can be restricted using the <code>ActionsGuarded</code> field on each <code>QualificationRequirement</code> structure. </p>"""
    unique_request_token: NotRequired[
        "capo_mturk.types.idempotency_token.IdempotencyToken"
    ]
    """<p> A unique identifier for this request which allows you to retry the call on error without creating duplicate HITs. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the HIT already exists in the system from a previous call using the same UniqueRequestToken, subsequent calls will return a AWS.MechanicalTurk.HitAlreadyExists error with a message containing the HITId. </p> <note> <p> Note: It is your responsibility to ensure uniqueness of the token. The unique token expires after 24 hours. Subsequent calls using the same UniqueRequestToken made after the 24 hour limit could create duplicate HITs. </p> </note>"""
    assignment_review_policy: NotRequired["capo_mturk.types.review_policy.ReviewPolicy"]
    """<p> The Assignment-level Review Policy applies to the assignments under the HIT. You can specify for Mechanical Turk to take various actions based on the policy. </p>"""
    hit_review_policy: NotRequired["capo_mturk.types.review_policy.ReviewPolicy"]
    """<p> The HIT-level Review Policy applies to the HIT. You can specify for Mechanical Turk to take various actions based on the policy. </p>"""
    hit_layout_id: NotRequired["capo_mturk.types.entity_id.EntityId"]
    """<p> The HITLayoutId allows you to use a pre-existing HIT design with placeholder values and create an additional HIT by providing those values as HITLayoutParameters. </p> <p> Constraints: Either a Question parameter or a HITLayoutId parameter must be provided. </p>"""
    hit_layout_parameters: NotRequired[
        "capo_mturk.types.hit_layout_parameter_list.HITLayoutParameterList"
    ]
    """<p> If the HITLayoutId is provided, any placeholder values must be filled in with values using the HITLayoutParameter structure. For more information, see HITLayout. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHITRequest) -> dict:
    out: dict = {}
    if "max_assignments" in value:
        out["MaxAssignments"] = value["max_assignments"]
    if "auto_approval_delay_in_seconds" in value:
        out["AutoApprovalDelayInSeconds"] = value["auto_approval_delay_in_seconds"]
    out["LifetimeInSeconds"] = value["lifetime_in_seconds"]
    out["AssignmentDurationInSeconds"] = value["assignment_duration_in_seconds"]
    out["Reward"] = value["reward"]
    out["Title"] = value["title"]
    if "keywords" in value:
        out["Keywords"] = value["keywords"]
    out["Description"] = value["description"]
    if "question" in value:
        out["Question"] = value["question"]
    if "requester_annotation" in value:
        out["RequesterAnnotation"] = value["requester_annotation"]
    if "qualification_requirements" in value:
        import capo_mturk.types.qualification_requirement_list

        out["QualificationRequirements"] = (
            capo_mturk.types.qualification_requirement_list.serialize_aws_json_1_1(
                value["qualification_requirements"]
            )
        )
    if "unique_request_token" in value:
        out["UniqueRequestToken"] = value["unique_request_token"]
    if "assignment_review_policy" in value:
        import capo_mturk.types.review_policy

        out["AssignmentReviewPolicy"] = (
            capo_mturk.types.review_policy.serialize_aws_json_1_1(
                value["assignment_review_policy"]
            )
        )
    if "hit_review_policy" in value:
        import capo_mturk.types.review_policy

        out["HITReviewPolicy"] = capo_mturk.types.review_policy.serialize_aws_json_1_1(
            value["hit_review_policy"]
        )
    if "hit_layout_id" in value:
        out["HITLayoutId"] = value["hit_layout_id"]
    if "hit_layout_parameters" in value:
        import capo_mturk.types.hit_layout_parameter_list

        out["HITLayoutParameters"] = (
            capo_mturk.types.hit_layout_parameter_list.serialize_aws_json_1_1(
                value["hit_layout_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHITRequest:
    out: CreateHITRequest = {}  # type: ignore[typeddict-item]
    if data.get("MaxAssignments") is not None:
        out["max_assignments"] = data["MaxAssignments"]
    if data.get("AutoApprovalDelayInSeconds") is not None:
        out["auto_approval_delay_in_seconds"] = data["AutoApprovalDelayInSeconds"]
    if data.get("LifetimeInSeconds") is not None:
        out["lifetime_in_seconds"] = data["LifetimeInSeconds"]
    else:
        out["lifetime_in_seconds"] = 0
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
    if data.get("Question") is not None:
        out["question"] = data["Question"]
    if data.get("RequesterAnnotation") is not None:
        out["requester_annotation"] = data["RequesterAnnotation"]
    if data.get("QualificationRequirements") is not None:
        import capo_mturk.types.qualification_requirement_list

        out["qualification_requirements"] = (
            capo_mturk.types.qualification_requirement_list.deserialize_aws_json_1_1(
                data["QualificationRequirements"]
            )
        )
    if data.get("UniqueRequestToken") is not None:
        out["unique_request_token"] = data["UniqueRequestToken"]
    if data.get("AssignmentReviewPolicy") is not None:
        import capo_mturk.types.review_policy

        out["assignment_review_policy"] = (
            capo_mturk.types.review_policy.deserialize_aws_json_1_1(
                data["AssignmentReviewPolicy"]
            )
        )
    if data.get("HITReviewPolicy") is not None:
        import capo_mturk.types.review_policy

        out["hit_review_policy"] = (
            capo_mturk.types.review_policy.deserialize_aws_json_1_1(
                data["HITReviewPolicy"]
            )
        )
    if data.get("HITLayoutId") is not None:
        out["hit_layout_id"] = data["HITLayoutId"]
    if data.get("HITLayoutParameters") is not None:
        import capo_mturk.types.hit_layout_parameter_list

        out["hit_layout_parameters"] = (
            capo_mturk.types.hit_layout_parameter_list.deserialize_aws_json_1_1(
                data["HITLayoutParameters"]
            )
        )
    return out
