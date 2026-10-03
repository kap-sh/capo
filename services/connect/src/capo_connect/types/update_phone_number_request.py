"""Generated from Smithy shape ``com.amazonaws.connect#UpdatePhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.phone_number_id


class UpdatePhoneNumberRequest(TypedDict, closed=True):
    phone_number_id: "capo_connect.types.phone_number_id.PhoneNumberId"
    """<p>A unique identifier for the phone number.</p>"""
    target_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) for Connect Customer instances or traffic distribution groups that phone number inbound traffic is routed through. You must enter <code>InstanceId</code> or <code>TargetArn</code>. </p>"""
    instance_id: NotRequired["capo_connect.types.instance_id.InstanceId"]
    """<p>The identifier of the Connect Customer instance that phone numbers are claimed to. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance. You must enter <code>InstanceId</code> or <code>TargetArn</code>. </p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePhoneNumberRequest) -> dict:
    out: dict = {}
    if "target_arn" in value:
        out["TargetArn"] = value["target_arn"]
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdatePhoneNumberRequest:
    out: UpdatePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    if data.get("TargetArn") is not None:
        out["target_arn"] = data["TargetArn"]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
