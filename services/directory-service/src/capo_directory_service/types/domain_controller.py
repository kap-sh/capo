"""Generated from Smithy shape ``com.amazonaws.directoryservice#DomainController``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_directory_service.types.availability_zone
    import capo_directory_service.types.directory_id
    import capo_directory_service.types.domain_controller_id
    import capo_directory_service.types.domain_controller_status
    import capo_directory_service.types.domain_controller_status_reason
    import capo_directory_service.types.ip_addr
    import capo_directory_service.types.ipv6_addr
    import capo_directory_service.types.last_updated_date_time
    import capo_directory_service.types.launch_time
    import capo_directory_service.types.subnet_id
    import capo_directory_service.types.vpc_id


class DomainController(TypedDict, closed=True):
    directory_id: NotRequired["capo_directory_service.types.directory_id.DirectoryId"]
    """<p>Identifier of the directory where the domain controller resides.</p>"""
    domain_controller_id: NotRequired[
        "capo_directory_service.types.domain_controller_id.DomainControllerId"
    ]
    """<p>Identifies a specific domain controller in the directory.</p>"""
    dns_ip_addr: NotRequired["capo_directory_service.types.ip_addr.IpAddr"]
    """<p>The IP address of the domain controller.</p>"""
    dns_ipv6_addr: NotRequired["capo_directory_service.types.ipv6_addr.Ipv6Addr"]
    """<p>The IPv6 address of the domain controller.</p>"""
    vpc_id: NotRequired["capo_directory_service.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC that contains the domain controller.</p>"""
    subnet_id: NotRequired["capo_directory_service.types.subnet_id.SubnetId"]
    """<p>Identifier of the subnet in the VPC that contains the domain controller.</p>"""
    availability_zone: NotRequired[
        "capo_directory_service.types.availability_zone.AvailabilityZone"
    ]
    """<p>The Availability Zone where the domain controller is located.</p>"""
    status: NotRequired[
        "capo_directory_service.types.domain_controller_status.DomainControllerStatus"
    ]
    """<p>The status of the domain controller.</p>"""
    status_reason: NotRequired[
        "capo_directory_service.types.domain_controller_status_reason.DomainControllerStatusReason"
    ]
    """<p>A description of the domain controller state.</p>"""
    launch_time: NotRequired["capo_directory_service.types.launch_time.LaunchTime"]
    """<p>Specifies when the domain controller was created.</p>"""
    status_last_updated_date_time: NotRequired[
        "capo_directory_service.types.last_updated_date_time.LastUpdatedDateTime"
    ]
    """<p>The date and time that the status was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DomainController) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "domain_controller_id" in value:
        out["DomainControllerId"] = value["domain_controller_id"]
    if "dns_ip_addr" in value:
        out["DnsIpAddr"] = value["dns_ip_addr"]
    if "dns_ipv6_addr" in value:
        out["DnsIpv6Addr"] = value["dns_ipv6_addr"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "status" in value:
        import capo_directory_service.types.domain_controller_status

        out["Status"] = (
            capo_directory_service.types.domain_controller_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "launch_time" in value:
        import capo_directory_service.types.launch_time

        out["LaunchTime"] = (
            capo_directory_service.types.launch_time.serialize_aws_json_1_1(
                value["launch_time"]
            )
        )
    if "status_last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["StatusLastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_aws_json_1_1(
                value["status_last_updated_date_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DomainController:
    out: DomainController = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("DomainControllerId") is not None:
        out["domain_controller_id"] = data["DomainControllerId"]
    if data.get("DnsIpAddr") is not None:
        out["dns_ip_addr"] = data["DnsIpAddr"]
    if data.get("DnsIpv6Addr") is not None:
        out["dns_ipv6_addr"] = data["DnsIpv6Addr"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("Status") is not None:
        import capo_directory_service.types.domain_controller_status

        out["status"] = (
            capo_directory_service.types.domain_controller_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("LaunchTime") is not None:
        import capo_directory_service.types.launch_time

        out["launch_time"] = (
            capo_directory_service.types.launch_time.deserialize_aws_json_1_1(
                data["LaunchTime"]
            )
        )
    if data.get("StatusLastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["status_last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_aws_json_1_1(
                data["StatusLastUpdatedDateTime"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DomainController) -> dict:
    out: dict = {}
    if "directory_id" in value:
        out["DirectoryId"] = value["directory_id"]
    if "domain_controller_id" in value:
        out["DomainControllerId"] = value["domain_controller_id"]
    if "dns_ip_addr" in value:
        out["DnsIpAddr"] = value["dns_ip_addr"]
    if "dns_ipv6_addr" in value:
        out["DnsIpv6Addr"] = value["dns_ipv6_addr"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "status" in value:
        import capo_directory_service.types.domain_controller_status

        out["Status"] = (
            capo_directory_service.types.domain_controller_status.serialize_cbor(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "launch_time" in value:
        import capo_directory_service.types.launch_time

        out["LaunchTime"] = capo_directory_service.types.launch_time.serialize_cbor(
            value["launch_time"]
        )
    if "status_last_updated_date_time" in value:
        import capo_directory_service.types.last_updated_date_time

        out["StatusLastUpdatedDateTime"] = (
            capo_directory_service.types.last_updated_date_time.serialize_cbor(
                value["status_last_updated_date_time"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DomainController:
    out: DomainController = {}  # type: ignore[typeddict-item]
    if data.get("DirectoryId") is not None:
        out["directory_id"] = data["DirectoryId"]
    if data.get("DomainControllerId") is not None:
        out["domain_controller_id"] = data["DomainControllerId"]
    if data.get("DnsIpAddr") is not None:
        out["dns_ip_addr"] = data["DnsIpAddr"]
    if data.get("DnsIpv6Addr") is not None:
        out["dns_ipv6_addr"] = data["DnsIpv6Addr"]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("Status") is not None:
        import capo_directory_service.types.domain_controller_status

        out["status"] = (
            capo_directory_service.types.domain_controller_status.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("LaunchTime") is not None:
        import capo_directory_service.types.launch_time

        out["launch_time"] = capo_directory_service.types.launch_time.deserialize_cbor(
            data["LaunchTime"]
        )
    if data.get("StatusLastUpdatedDateTime") is not None:
        import capo_directory_service.types.last_updated_date_time

        out["status_last_updated_date_time"] = (
            capo_directory_service.types.last_updated_date_time.deserialize_cbor(
                data["StatusLastUpdatedDateTime"]
            )
        )
    return out
