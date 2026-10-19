"""Generated from Smithy shape ``com.amazonaws.mailmanager#PrivateNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.vpc_endpoint_id


class PrivateNetworkConfiguration(TypedDict, closed=True):
    vpc_endpoint_id: "capo_mailmanager.types.vpc_endpoint_id.VpcEndpointId"
    """<p>The identifier of the VPC endpoint to associate with this private ingress point.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrivateNetworkConfiguration) -> dict:
    out: dict = {}
    out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PrivateNetworkConfiguration:
    out: PrivateNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    else:
        out["vpc_endpoint_id"] = ""
    return out
