"""Generated from Smithy shape ``com.amazonaws.connect#DescribeSecurityProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.security_profile_id


class DescribeSecurityProfileRequest(TypedDict, closed=True):
    security_profile_id: "capo_connect.types.security_profile_id.SecurityProfileId"
    """<p>The identifier for the security profle.</p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSecurityProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSecurityProfileRequest:
    out: DescribeSecurityProfileRequest = {}  # type: ignore[typeddict-item]
    return out
