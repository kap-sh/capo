"""Generated from Smithy shape ``com.amazonaws.mturk#CreateAdditionalAssignmentsForHITRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.entity_id
    import capo_mturk.types.idempotency_token
    import capo_mturk.types.integer


class CreateAdditionalAssignmentsForHITRequest(TypedDict, closed=True):
    hit_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the HIT to extend.</p>"""
    number_of_additional_assignments: "capo_mturk.types.integer.Integer"
    """<p>The number of additional assignments to request for this HIT.</p>"""
    unique_request_token: NotRequired[
        "capo_mturk.types.idempotency_token.IdempotencyToken"
    ]
    """<p> A unique identifier for this request, which allows you to retry the call on error without extending the HIT multiple times. This is useful in cases such as network timeouts where it is unclear whether or not the call succeeded on the server. If the extend HIT already exists in the system from a previous call using the same <code>UniqueRequestToken</code>, subsequent calls will return an error with a message containing the request ID. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAdditionalAssignmentsForHITRequest) -> dict:
    out: dict = {}
    out["HITId"] = value["hit_id"]
    out["NumberOfAdditionalAssignments"] = value["number_of_additional_assignments"]
    if "unique_request_token" in value:
        out["UniqueRequestToken"] = value["unique_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAdditionalAssignmentsForHITRequest:
    out: CreateAdditionalAssignmentsForHITRequest = {}  # type: ignore[typeddict-item]
    if data.get("HITId") is not None:
        out["hit_id"] = data["HITId"]
    else:
        out["hit_id"] = ""
    if data.get("NumberOfAdditionalAssignments") is not None:
        out["number_of_additional_assignments"] = data["NumberOfAdditionalAssignments"]
    else:
        out["number_of_additional_assignments"] = 0
    if data.get("UniqueRequestToken") is not None:
        out["unique_request_token"] = data["UniqueRequestToken"]
    return out
