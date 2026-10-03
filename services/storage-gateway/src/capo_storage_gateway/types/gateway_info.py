"""Generated from Smithy shape ``com.amazonaws.storagegateway#GatewayInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.deprecation_date
    import capo_storage_gateway.types.ec2_instance_id
    import capo_storage_gateway.types.ec2_instance_region
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.gateway_id
    import capo_storage_gateway.types.gateway_operational_state
    import capo_storage_gateway.types.gateway_type
    import capo_storage_gateway.types.host_environment
    import capo_storage_gateway.types.host_environment_id
    import capo_storage_gateway.types.software_version
    import capo_storage_gateway.types.string


class GatewayInfo(TypedDict, closed=True):
    gateway_id: NotRequired["capo_storage_gateway.types.gateway_id.GatewayId"]
    """<p>The unique identifier assigned to your gateway during activation. This ID becomes part of the gateway Amazon Resource Name (ARN), which you use as input for other operations.</p>"""
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <a>ListGateways</a> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    gateway_type: NotRequired["capo_storage_gateway.types.gateway_type.GatewayType"]
    """<p>The type of the gateway.</p> <important> <p>Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit <a href="https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/">this blog post</a>.</p> </important>"""
    gateway_operational_state: NotRequired[
        "capo_storage_gateway.types.gateway_operational_state.GatewayOperationalState"
    ]
    """<p>The state of the gateway.</p> <p>Valid Values: <code>DISABLED</code> | <code>ACTIVE</code> </p>"""
    gateway_name: NotRequired["capo_storage_gateway.types.string.string"]
    """<p>The name of the gateway.</p>"""
    ec2_instance_id: NotRequired[
        "capo_storage_gateway.types.ec2_instance_id.Ec2InstanceId"
    ]
    """<p>The ID of the Amazon EC2 instance that was used to launch the gateway.</p>"""
    ec2_instance_region: NotRequired[
        "capo_storage_gateway.types.ec2_instance_region.Ec2InstanceRegion"
    ]
    """<p>The Amazon Web Services Region where the Amazon EC2 instance is located.</p>"""
    host_environment: NotRequired[
        "capo_storage_gateway.types.host_environment.HostEnvironment"
    ]
    """<p>The type of hardware or software platform on which the gateway is running.</p> <note> <p>Tape Gateway is no longer available on Snow Family devices.</p> </note>"""
    host_environment_id: NotRequired[
        "capo_storage_gateway.types.host_environment_id.HostEnvironmentId"
    ]
    """<p>A unique identifier for the specific instance of the host platform running the gateway. This value is only available for certain host environments, and its format depends on the host environment type.</p>"""
    deprecation_date: NotRequired[
        "capo_storage_gateway.types.deprecation_date.DeprecationDate"
    ]
    """<p>Date after which this gateway will not receive software updates for new features and bug fixes.</p>"""
    software_version: NotRequired[
        "capo_storage_gateway.types.software_version.SoftwareVersion"
    ]
    """<p>The version number of the software running on the gateway appliance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayInfo) -> dict:
    out: dict = {}
    if "gateway_id" in value:
        out["GatewayId"] = value["gateway_id"]
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "gateway_type" in value:
        out["GatewayType"] = value["gateway_type"]
    if "gateway_operational_state" in value:
        out["GatewayOperationalState"] = value["gateway_operational_state"]
    if "gateway_name" in value:
        out["GatewayName"] = value["gateway_name"]
    if "ec2_instance_id" in value:
        out["Ec2InstanceId"] = value["ec2_instance_id"]
    if "ec2_instance_region" in value:
        out["Ec2InstanceRegion"] = value["ec2_instance_region"]
    if "host_environment" in value:
        import capo_storage_gateway.types.host_environment

        out["HostEnvironment"] = (
            capo_storage_gateway.types.host_environment.serialize_aws_json_1_1(
                value["host_environment"]
            )
        )
    if "host_environment_id" in value:
        out["HostEnvironmentId"] = value["host_environment_id"]
    if "deprecation_date" in value:
        out["DeprecationDate"] = value["deprecation_date"]
    if "software_version" in value:
        out["SoftwareVersion"] = value["software_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayInfo:
    out: GatewayInfo = {}  # type: ignore[typeddict-item]
    if data.get("GatewayId") is not None:
        out["gateway_id"] = data["GatewayId"]
    if data.get("GatewayARN") is not None:
        out["gateway_arn"] = data["GatewayARN"]
    if data.get("GatewayType") is not None:
        out["gateway_type"] = data["GatewayType"]
    if data.get("GatewayOperationalState") is not None:
        out["gateway_operational_state"] = data["GatewayOperationalState"]
    if data.get("GatewayName") is not None:
        out["gateway_name"] = data["GatewayName"]
    if data.get("Ec2InstanceId") is not None:
        out["ec2_instance_id"] = data["Ec2InstanceId"]
    if data.get("Ec2InstanceRegion") is not None:
        out["ec2_instance_region"] = data["Ec2InstanceRegion"]
    if data.get("HostEnvironment") is not None:
        import capo_storage_gateway.types.host_environment

        out["host_environment"] = (
            capo_storage_gateway.types.host_environment.deserialize_aws_json_1_1(
                data["HostEnvironment"]
            )
        )
    if data.get("HostEnvironmentId") is not None:
        out["host_environment_id"] = data["HostEnvironmentId"]
    if data.get("DeprecationDate") is not None:
        out["deprecation_date"] = data["DeprecationDate"]
    if data.get("SoftwareVersion") is not None:
        out["software_version"] = data["SoftwareVersion"]
    return out
