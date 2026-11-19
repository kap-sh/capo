"""Generated from Smithy shape ``com.amazonaws.backupgateway#GatewayDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup_gateway.types.gateway_arn
    import capo_backup_gateway.types.gateway_type
    import capo_backup_gateway.types.hypervisor_id
    import capo_backup_gateway.types.maintenance_start_time
    import capo_backup_gateway.types.name
    import capo_backup_gateway.types.time
    import capo_backup_gateway.types.vpc_endpoint


class GatewayDetails(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_backup_gateway.types.gateway_arn.GatewayArn"]
    """<p>The Amazon Resource Name (ARN) of the gateway. Use the <code>ListGateways</code> operation to return a list of gateways for your account and Amazon Web Services Region.</p>"""
    gateway_display_name: NotRequired["capo_backup_gateway.types.name.Name"]
    """<p>The display name of the gateway.</p>"""
    gateway_type: NotRequired["capo_backup_gateway.types.gateway_type.GatewayType"]
    """<p>The type of the gateway type.</p>"""
    hypervisor_id: NotRequired["capo_backup_gateway.types.hypervisor_id.HypervisorId"]
    """<p>The hypervisor ID of the gateway.</p>"""
    last_seen_time: NotRequired["capo_backup_gateway.types.time.Time"]
    """<p>Details showing the last time Backup gateway communicated with the cloud, in Unix format and UTC time.</p>"""
    maintenance_start_time: NotRequired[
        "capo_backup_gateway.types.maintenance_start_time.MaintenanceStartTime"
    ]
    """<p>Returns your gateway's weekly maintenance start time including the day and time of the week. Note that values are in terms of the gateway's time zone. Can be weekly or monthly.</p>"""
    next_update_availability_time: NotRequired["capo_backup_gateway.types.time.Time"]
    """<p>Details showing the next update availability time of the gateway.</p>"""
    vpc_endpoint: NotRequired["capo_backup_gateway.types.vpc_endpoint.VpcEndpoint"]
    """<p>The DNS name for the virtual private cloud (VPC) endpoint the gateway uses to connect to the cloud for backup gateway.</p>"""
    deprecation_date: NotRequired["capo_backup_gateway.types.time.Time"]
    """<p>Date after which this gateway will not receive software updates for new features and bug fixes.</p>"""
    software_version: NotRequired["capo_backup_gateway.types.name.Name"]
    """<p>The version number of the software running on the gateway appliance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GatewayDetails) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    if "gateway_display_name" in value:
        out["GatewayDisplayName"] = value["gateway_display_name"]
    if "gateway_type" in value:
        out["GatewayType"] = value["gateway_type"]
    if "hypervisor_id" in value:
        out["HypervisorId"] = value["hypervisor_id"]
    if "last_seen_time" in value:
        import capo_backup_gateway.types.time

        out["LastSeenTime"] = capo_backup_gateway.types.time.serialize_aws_json_1_0(
            value["last_seen_time"]
        )
    if "maintenance_start_time" in value:
        import capo_backup_gateway.types.maintenance_start_time

        out["MaintenanceStartTime"] = (
            capo_backup_gateway.types.maintenance_start_time.serialize_aws_json_1_0(
                value["maintenance_start_time"]
            )
        )
    if "next_update_availability_time" in value:
        import capo_backup_gateway.types.time

        out["NextUpdateAvailabilityTime"] = (
            capo_backup_gateway.types.time.serialize_aws_json_1_0(
                value["next_update_availability_time"]
            )
        )
    if "vpc_endpoint" in value:
        out["VpcEndpoint"] = value["vpc_endpoint"]
    if "deprecation_date" in value:
        import capo_backup_gateway.types.time

        out["DeprecationDate"] = capo_backup_gateway.types.time.serialize_aws_json_1_0(
            value["deprecation_date"]
        )
    if "software_version" in value:
        out["SoftwareVersion"] = value["software_version"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GatewayDetails:
    out: GatewayDetails = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    if data.get("GatewayDisplayName") is not None:
        out["gateway_display_name"] = data["GatewayDisplayName"]
    if data.get("GatewayType") is not None:
        out["gateway_type"] = data["GatewayType"]
    if data.get("HypervisorId") is not None:
        out["hypervisor_id"] = data["HypervisorId"]
    if data.get("LastSeenTime") is not None:
        import capo_backup_gateway.types.time

        out["last_seen_time"] = capo_backup_gateway.types.time.deserialize_aws_json_1_0(
            data["LastSeenTime"]
        )
    if data.get("MaintenanceStartTime") is not None:
        import capo_backup_gateway.types.maintenance_start_time

        out["maintenance_start_time"] = (
            capo_backup_gateway.types.maintenance_start_time.deserialize_aws_json_1_0(
                data["MaintenanceStartTime"]
            )
        )
    if data.get("NextUpdateAvailabilityTime") is not None:
        import capo_backup_gateway.types.time

        out["next_update_availability_time"] = (
            capo_backup_gateway.types.time.deserialize_aws_json_1_0(
                data["NextUpdateAvailabilityTime"]
            )
        )
    if data.get("VpcEndpoint") is not None:
        out["vpc_endpoint"] = data["VpcEndpoint"]
    if data.get("DeprecationDate") is not None:
        import capo_backup_gateway.types.time

        out["deprecation_date"] = (
            capo_backup_gateway.types.time.deserialize_aws_json_1_0(
                data["DeprecationDate"]
            )
        )
    if data.get("SoftwareVersion") is not None:
        out["software_version"] = data["SoftwareVersion"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GatewayDetails) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayArn"] = value["gateway_arn"]
    if "gateway_display_name" in value:
        out["GatewayDisplayName"] = value["gateway_display_name"]
    if "gateway_type" in value:
        out["GatewayType"] = value["gateway_type"]
    if "hypervisor_id" in value:
        out["HypervisorId"] = value["hypervisor_id"]
    if "last_seen_time" in value:
        import capo_backup_gateway.types.time

        out["LastSeenTime"] = capo_backup_gateway.types.time.serialize_cbor(
            value["last_seen_time"]
        )
    if "maintenance_start_time" in value:
        import capo_backup_gateway.types.maintenance_start_time

        out["MaintenanceStartTime"] = (
            capo_backup_gateway.types.maintenance_start_time.serialize_cbor(
                value["maintenance_start_time"]
            )
        )
    if "next_update_availability_time" in value:
        import capo_backup_gateway.types.time

        out["NextUpdateAvailabilityTime"] = (
            capo_backup_gateway.types.time.serialize_cbor(
                value["next_update_availability_time"]
            )
        )
    if "vpc_endpoint" in value:
        out["VpcEndpoint"] = value["vpc_endpoint"]
    if "deprecation_date" in value:
        import capo_backup_gateway.types.time

        out["DeprecationDate"] = capo_backup_gateway.types.time.serialize_cbor(
            value["deprecation_date"]
        )
    if "software_version" in value:
        out["SoftwareVersion"] = value["software_version"]
    return out


def deserialize_cbor(data: dict) -> GatewayDetails:
    out: GatewayDetails = {}  # type: ignore[typeddict-item]
    if data.get("GatewayArn") is not None:
        out["gateway_arn"] = data["GatewayArn"]
    if data.get("GatewayDisplayName") is not None:
        out["gateway_display_name"] = data["GatewayDisplayName"]
    if data.get("GatewayType") is not None:
        out["gateway_type"] = data["GatewayType"]
    if data.get("HypervisorId") is not None:
        out["hypervisor_id"] = data["HypervisorId"]
    if data.get("LastSeenTime") is not None:
        import capo_backup_gateway.types.time

        out["last_seen_time"] = capo_backup_gateway.types.time.deserialize_cbor(
            data["LastSeenTime"]
        )
    if data.get("MaintenanceStartTime") is not None:
        import capo_backup_gateway.types.maintenance_start_time

        out["maintenance_start_time"] = (
            capo_backup_gateway.types.maintenance_start_time.deserialize_cbor(
                data["MaintenanceStartTime"]
            )
        )
    if data.get("NextUpdateAvailabilityTime") is not None:
        import capo_backup_gateway.types.time

        out["next_update_availability_time"] = (
            capo_backup_gateway.types.time.deserialize_cbor(
                data["NextUpdateAvailabilityTime"]
            )
        )
    if data.get("VpcEndpoint") is not None:
        out["vpc_endpoint"] = data["VpcEndpoint"]
    if data.get("DeprecationDate") is not None:
        import capo_backup_gateway.types.time

        out["deprecation_date"] = capo_backup_gateway.types.time.deserialize_cbor(
            data["DeprecationDate"]
        )
    if data.get("SoftwareVersion") is not None:
        out["software_version"] = data["SoftwareVersion"]
    return out
