"""Generated from Smithy shape ``com.amazonaws.connect#DescribeAuthenticationProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.authentication_profile_id
    import capo_connect.types.instance_id


class DescribeAuthenticationProfileRequest(TypedDict, closed=True):
    authentication_profile_id: (
        "capo_connect.types.authentication_profile_id.AuthenticationProfileId"
    )
    """<p>A unique identifier for the authentication profile. </p>"""
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAuthenticationProfileRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAuthenticationProfileRequest:
    out: DescribeAuthenticationProfileRequest = {}  # type: ignore[typeddict-item]
    return out
