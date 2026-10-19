"""Generated from Smithy shape ``com.amazonaws.mturk#AssociateQualificationWithWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.boolean
    import capo_mturk.types.customer_id
    import capo_mturk.types.entity_id
    import capo_mturk.types.integer


class AssociateQualificationWithWorkerRequest(TypedDict, closed=True):
    qualification_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the Qualification type to use for the assigned Qualification.</p>"""
    worker_id: "capo_mturk.types.customer_id.CustomerId"
    """<p> The ID of the Worker to whom the Qualification is being assigned. Worker IDs are included with submitted HIT assignments and Qualification requests. </p>"""
    integer_value: NotRequired["capo_mturk.types.integer.Integer"]
    """<p>The value of the Qualification to assign.</p>"""
    send_notification: NotRequired["capo_mturk.types.boolean.Boolean"]
    """<p> Specifies whether to send a notification email message to the Worker saying that the qualification was assigned to the Worker. Note: this is true by default. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateQualificationWithWorkerRequest) -> dict:
    out: dict = {}
    out["QualificationTypeId"] = value["qualification_type_id"]
    out["WorkerId"] = value["worker_id"]
    if "integer_value" in value:
        out["IntegerValue"] = value["integer_value"]
    if "send_notification" in value:
        out["SendNotification"] = value["send_notification"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateQualificationWithWorkerRequest:
    out: AssociateQualificationWithWorkerRequest = {}  # type: ignore[typeddict-item]
    if data.get("QualificationTypeId") is not None:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        out["qualification_type_id"] = ""
    if data.get("WorkerId") is not None:
        out["worker_id"] = data["WorkerId"]
    else:
        out["worker_id"] = ""
    if data.get("IntegerValue") is not None:
        out["integer_value"] = data["IntegerValue"]
    if data.get("SendNotification") is not None:
        out["send_notification"] = data["SendNotification"]
    return out
