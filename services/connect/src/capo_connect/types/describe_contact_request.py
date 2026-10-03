"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.instance_id


class DescribeContactRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeContactRequest:
    out: DescribeContactRequest = {}  # type: ignore[typeddict-item]
    return out
