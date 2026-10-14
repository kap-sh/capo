"""Generated from Smithy shape ``com.amazonaws.fsx#InvalidNetworkSettings``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_fsx.errors import ServiceError

if TYPE_CHECKING:
    import capo_fsx.types.error_message
    import capo_fsx.types.route_table_id
    import capo_fsx.types.security_group_id
    import capo_fsx.types.subnet_id


class InvalidNetworkSettings_(TypedDict, closed=True):
    message: NotRequired["capo_fsx.types.error_message.ErrorMessage"]
    """<p>Error message explaining what's wrong with network settings.</p>"""
    invalid_subnet_id: NotRequired["capo_fsx.types.subnet_id.SubnetId"]
    """<p>The subnet ID that is either invalid or not part of the VPC specified.</p>"""
    invalid_security_group_id: NotRequired[
        "capo_fsx.types.security_group_id.SecurityGroupId"
    ]
    """<p>The security group ID is either invalid or not part of the VPC specified.</p>"""
    invalid_route_table_id: NotRequired["capo_fsx.types.route_table_id.RouteTableId"]
    """<p>The route table ID is either invalid or not part of the VPC specified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InvalidNetworkSettings_) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    if "invalid_subnet_id" in value:
        out["InvalidSubnetId"] = value["invalid_subnet_id"]
    if "invalid_security_group_id" in value:
        out["InvalidSecurityGroupId"] = value["invalid_security_group_id"]
    if "invalid_route_table_id" in value:
        out["InvalidRouteTableId"] = value["invalid_route_table_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InvalidNetworkSettings_:
    out: InvalidNetworkSettings_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    if data.get("InvalidSubnetId") is not None:
        out["invalid_subnet_id"] = data["InvalidSubnetId"]
    if data.get("InvalidSecurityGroupId") is not None:
        out["invalid_security_group_id"] = data["InvalidSecurityGroupId"]
    if data.get("InvalidRouteTableId") is not None:
        out["invalid_route_table_id"] = data["InvalidRouteTableId"]
    return out


class InvalidNetworkSettings(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.fsx#InvalidNetworkSettings``."""

    code: str | None = "InvalidNetworkSettings"

    def __init__(
        self,
        data: InvalidNetworkSettings_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="InvalidNetworkSettings",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_aws_json_1_1(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "InvalidNetworkSettings":
        return cls(deserialize_aws_json_1_1(data), message, response=response)
