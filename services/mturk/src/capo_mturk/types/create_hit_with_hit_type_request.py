"""Generated from Smithy shape ``com.amazonaws.mturk#CreateHITWithHITTypeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id
    import capo_mturk.types.hit_layout_parameter_list
    import capo_mturk.types.idempotency_token
    import capo_mturk.types.integer
    import capo_mturk.types.long
    import capo_mturk.types.review_policy
    import capo_mturk.types.string


class CreateHITWithHITTypeRequest(TypedDict, closed=True):
    hit_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The HIT type ID you want to create this HIT with.</p>"""
    max_assignments: NotRequired["capo_mturk.types.integer.Integer"]
    """<p> The number of times the HIT can be accepted and completed before the HIT becomes unavailable. </p>"""
    lifetime_in_seconds: "capo_mturk.types.long.Long"
    """<p> An amount of time, in seconds, after which the HIT is no longer available for users to accept. After the lifetime of the HIT elapses, the HIT no longer appears in HIT searches, even if not all of the assignments for the HIT have been accepted. </p>"""
    question: NotRequired["capo_mturk.types.string.String"]
    """<p> The data the person completing the HIT uses to produce the results. </p> <p> Constraints: Must be a QuestionForm data structure, an ExternalQuestion data structure, or an HTMLQuestion data structure. The XML question data must not be larger than 64 kilobytes (65,535 bytes) in size, including whitespace. </p> <p>Either a Question parameter or a HITLayoutId parameter must be provided.</p>"""
    requester_annotation: NotRequired["capo_mturk.types.string.String"]
    """<p> An arbitrary data field. The RequesterAnnotation parameter lets your application attach arbitrary data to the HIT for tracking purposes. For example, this parameter could be an identifier internal to the Requester's application that corresponds with the HIT. </p> <p> The RequesterAnnotation parameter for a HIT is only visible to the Requester who created the HIT. It is not shown to the Worker, or any other Requester. </p> <p> The RequesterAnnotation parameter may be different for each HIT you submit. It does not affect how your HITs are grouped. </p>"""
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
def serialize_aws_json_1_1(value: CreateHITWithHITTypeRequest) -> dict:
    out: dict = {}
    out["HITTypeId"] = value["hit_type_id"]
    if "max_assignments" in value:
        out["MaxAssignments"] = value["max_assignments"]
    out["LifetimeInSeconds"] = value["lifetime_in_seconds"]
    if "question" in value:
        out["Question"] = value["question"]
    if "requester_annotation" in value:
        out["RequesterAnnotation"] = value["requester_annotation"]
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


def deserialize_aws_json_1_1(data: dict) -> CreateHITWithHITTypeRequest:
    out: CreateHITWithHITTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("HITTypeId") is not None:
        out["hit_type_id"] = data["HITTypeId"]
    else:
        out["hit_type_id"] = ""
    if data.get("MaxAssignments") is not None:
        out["max_assignments"] = data["MaxAssignments"]
    if data.get("LifetimeInSeconds") is not None:
        out["lifetime_in_seconds"] = data["LifetimeInSeconds"]
    else:
        out["lifetime_in_seconds"] = 0
    if data.get("Question") is not None:
        out["question"] = data["Question"]
    if data.get("RequesterAnnotation") is not None:
        out["requester_annotation"] = data["RequesterAnnotation"]
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
