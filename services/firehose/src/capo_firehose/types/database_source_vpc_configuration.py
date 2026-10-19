"""Generated from Smithy shape ``com.amazonaws.firehose#DatabaseSourceVPCConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_firehose.types.vpc_endpoint_service_name


class DatabaseSourceVPCConfiguration(TypedDict, closed=True):
    vpc_endpoint_service_name: (
        "capo_firehose.types.vpc_endpoint_service_name.VpcEndpointServiceName"
    )
    """<p> The VPC endpoint service name which Firehose uses to create a PrivateLink to the database. The endpoint service must have the Firehose service principle <code>firehose.amazonaws.com</code> as an allowed principal on the VPC endpoint service. The VPC endpoint service name is a string that looks like <code>com.amazonaws.vpce.<region>.<vpc-endpoint-service-id></code>. </p> <p>Amazon Data Firehose is in preview release and is subject to change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseSourceVPCConfiguration) -> dict:
    out: dict = {}
    out["VpcEndpointServiceName"] = value["vpc_endpoint_service_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DatabaseSourceVPCConfiguration:
    out: DatabaseSourceVPCConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("VpcEndpointServiceName") is not None:
        out["vpc_endpoint_service_name"] = data["VpcEndpointServiceName"]
    else:
        out["vpc_endpoint_service_name"] = ""
    return out
