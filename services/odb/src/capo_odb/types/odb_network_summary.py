"""Generated from Smithy shape ``com.amazonaws.odb#OdbNetworkSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_odb.types.managed_services
    import capo_odb.types.oci_dns_forwarding_config_list
    import capo_odb.types.resource_id_list
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.resource_status
    import capo_odb.types.string_list


class OdbNetworkSummary(TypedDict, closed=True):
    odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network.</p>"""
    display_name: NotRequired["str"]
    """<p>The user-friendly name of the ODB network.</p>"""
    status: NotRequired["capo_odb.types.resource_status.ResourceStatus"]
    """<p>The current status of the ODB network.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the ODB network.</p>"""
    odb_network_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the ODB network.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Amazon Web Services Availability Zone (AZ) where the ODB network is located.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The AZ ID of the AZ where the ODB network is located.</p>"""
    client_subnet_cidr: NotRequired["str"]
    """<p>The CIDR range of the client subnet in the ODB network.</p>"""
    backup_subnet_cidr: NotRequired["str"]
    """<p>The CIDR range of the backup subnet in the ODB network.</p>"""
    custom_domain_name: NotRequired["str"]
    """<p>The domain name for the resources in the ODB network.</p>"""
    default_dns_prefix: NotRequired["str"]
    """<p>The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.</p>"""
    peered_cidrs: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of CIDR ranges from the peered VPC that are allowed access to the ODB network.</p>"""
    oci_network_anchor_id: NotRequired["str"]
    """<p>The unique identifier of the OCI network anchor for the ODB network.</p>"""
    oci_network_anchor_url: NotRequired["str"]
    """<p>The URL of the OCI network anchor for the ODB network.</p>"""
    oci_resource_anchor_name: NotRequired["str"]
    """<p>The name of the OCI resource anchor associated with the ODB network.</p>"""
    oci_vcn_id: NotRequired["str"]
    """<p>The Oracle Cloud ID (OCID) for the Virtual Cloud Network (VCN) associated with the ODB network.</p>"""
    oci_vcn_url: NotRequired["str"]
    """<p>The URL for the VCN that's associated with the ODB network.</p>"""
    oci_dns_forwarding_configs: NotRequired[
        "capo_odb.types.oci_dns_forwarding_config_list.OciDnsForwardingConfigList"
    ]
    """<p>The DNS resolver endpoint in OCI for forwarding DNS queries for the ociPrivateZone domain.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time when the ODB network was created.</p>"""
    percent_progress: NotRequired["float"]
    """<p>The amount of progress made on the current operation on the ODB network, expressed as a percentage.</p>"""
    managed_services: NotRequired["capo_odb.types.managed_services.ManagedServices"]
    """<p>The managed services configuration for the ODB network.</p>"""
    ec2_placement_group_ids: NotRequired[
        "capo_odb.types.resource_id_list.ResourceIdList"
    ]
    """<p>The list of EC2 Placement Group IDs associated with your ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OdbNetworkSummary) -> dict:
    out: dict = {}
    out["odbNetworkId"] = value["odb_network_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "status" in value:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "odb_network_arn" in value:
        out["odbNetworkArn"] = value["odb_network_arn"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    if "client_subnet_cidr" in value:
        out["clientSubnetCidr"] = value["client_subnet_cidr"]
    if "backup_subnet_cidr" in value:
        out["backupSubnetCidr"] = value["backup_subnet_cidr"]
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "default_dns_prefix" in value:
        out["defaultDnsPrefix"] = value["default_dns_prefix"]
    if "peered_cidrs" in value:
        import capo_odb.types.string_list

        out["peeredCidrs"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["peered_cidrs"]
        )
    if "oci_network_anchor_id" in value:
        out["ociNetworkAnchorId"] = value["oci_network_anchor_id"]
    if "oci_network_anchor_url" in value:
        out["ociNetworkAnchorUrl"] = value["oci_network_anchor_url"]
    if "oci_resource_anchor_name" in value:
        out["ociResourceAnchorName"] = value["oci_resource_anchor_name"]
    if "oci_vcn_id" in value:
        out["ociVcnId"] = value["oci_vcn_id"]
    if "oci_vcn_url" in value:
        out["ociVcnUrl"] = value["oci_vcn_url"]
    if "oci_dns_forwarding_configs" in value:
        import capo_odb.types.oci_dns_forwarding_config_list

        out["ociDnsForwardingConfigs"] = (
            capo_odb.types.oci_dns_forwarding_config_list.serialize_aws_json_1_0(
                value["oci_dns_forwarding_configs"]
            )
        )
    if "created_at" in value:
        import capo_odb._protocol.serialize

        out["createdAt"] = capo_odb._protocol.serialize.fmt_date_time(
            value["created_at"]
        )
    if "percent_progress" in value:
        out["percentProgress"] = (
            "NaN"
            if value["percent_progress"] != value["percent_progress"]
            else "Infinity"
            if value["percent_progress"] == float("inf")
            else "-Infinity"
            if value["percent_progress"] == float("-inf")
            else value["percent_progress"]
        )
    if "managed_services" in value:
        import capo_odb.types.managed_services

        out["managedServices"] = capo_odb.types.managed_services.serialize_aws_json_1_0(
            value["managed_services"]
        )
    if "ec2_placement_group_ids" in value:
        import capo_odb.types.resource_id_list

        out["ec2PlacementGroupIds"] = (
            capo_odb.types.resource_id_list.serialize_aws_json_1_0(
                value["ec2_placement_group_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OdbNetworkSummary:
    out: OdbNetworkSummary = {}  # type: ignore[typeddict-item]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        out["odb_network_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("status") is not None:
        import capo_odb.types.resource_status

        out["status"] = capo_odb.types.resource_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("odbNetworkArn") is not None:
        out["odb_network_arn"] = data["odbNetworkArn"]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("clientSubnetCidr") is not None:
        out["client_subnet_cidr"] = data["clientSubnetCidr"]
    if data.get("backupSubnetCidr") is not None:
        out["backup_subnet_cidr"] = data["backupSubnetCidr"]
    if data.get("customDomainName") is not None:
        out["custom_domain_name"] = data["customDomainName"]
    if data.get("defaultDnsPrefix") is not None:
        out["default_dns_prefix"] = data["defaultDnsPrefix"]
    if data.get("peeredCidrs") is not None:
        import capo_odb.types.string_list

        out["peered_cidrs"] = capo_odb.types.string_list.deserialize_aws_json_1_0(
            data["peeredCidrs"]
        )
    if data.get("ociNetworkAnchorId") is not None:
        out["oci_network_anchor_id"] = data["ociNetworkAnchorId"]
    if data.get("ociNetworkAnchorUrl") is not None:
        out["oci_network_anchor_url"] = data["ociNetworkAnchorUrl"]
    if data.get("ociResourceAnchorName") is not None:
        out["oci_resource_anchor_name"] = data["ociResourceAnchorName"]
    if data.get("ociVcnId") is not None:
        out["oci_vcn_id"] = data["ociVcnId"]
    if data.get("ociVcnUrl") is not None:
        out["oci_vcn_url"] = data["ociVcnUrl"]
    if data.get("ociDnsForwardingConfigs") is not None:
        import capo_odb.types.oci_dns_forwarding_config_list

        out["oci_dns_forwarding_configs"] = (
            capo_odb.types.oci_dns_forwarding_config_list.deserialize_aws_json_1_0(
                data["ociDnsForwardingConfigs"]
            )
        )
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    if data.get("percentProgress") is not None:
        out["percent_progress"] = float(data["percentProgress"])
    if data.get("managedServices") is not None:
        import capo_odb.types.managed_services

        out["managed_services"] = (
            capo_odb.types.managed_services.deserialize_aws_json_1_0(
                data["managedServices"]
            )
        )
    if data.get("ec2PlacementGroupIds") is not None:
        import capo_odb.types.resource_id_list

        out["ec2_placement_group_ids"] = (
            capo_odb.types.resource_id_list.deserialize_aws_json_1_0(
                data["ec2PlacementGroupIds"]
            )
        )
    return out
