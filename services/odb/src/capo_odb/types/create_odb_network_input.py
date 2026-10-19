"""Generated from Smithy shape ``com.amazonaws.odb#CreateOdbNetworkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.access
    import capo_odb.types.general_input_string
    import capo_odb.types.policy_document
    import capo_odb.types.request_tag_map
    import capo_odb.types.resource_display_name
    import capo_odb.types.string_list


class CreateOdbNetworkInput(TypedDict, closed=True):
    display_name: "capo_odb.types.resource_display_name.ResourceDisplayName"
    """<p>A user-friendly name for the ODB network.</p>"""
    availability_zone: NotRequired["str"]
    """<p>The Amazon Web Services Availability Zone (AZ) where the ODB network is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The AZ ID of the AZ where the ODB network is located.</p> <p>This operation requires that you specify a value for either <code>availabilityZone</code> or <code>availabilityZoneId</code>.</p>"""
    client_subnet_cidr: "str"
    """<p>The CIDR range of the client subnet for the ODB network.</p> <p>Constraints:</p> <ul> <li> <p>Must not overlap with the CIDR range of the backup subnet.</p> </li> <li> <p>Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.</p> </li> <li> <p>Must not use the following CIDR ranges that are reserved by OCI:</p> <ul> <li> <p> <code>100.106.0.0/16</code> and <code>100.107.0.0/16</code> </p> </li> <li> <p> <code>169.254.0.0/16</code> </p> </li> <li> <p> <code>224.0.0.0 - 239.255.255.255</code> </p> </li> <li> <p> <code>240.0.0.0 - 255.255.255.255</code> </p> </li> </ul> </li> </ul>"""
    backup_subnet_cidr: NotRequired["str"]
    """<p>The CIDR range of the backup subnet for the ODB network.</p> <p>Constraints:</p> <ul> <li> <p>Must not overlap with the CIDR range of the client subnet.</p> </li> <li> <p>Must not overlap with the CIDR ranges of the VPCs that are connected to the ODB network.</p> </li> <li> <p>Must not use the following CIDR ranges that are reserved by OCI:</p> <ul> <li> <p> <code>100.106.0.0/16</code> and <code>100.107.0.0/16</code> </p> </li> <li> <p> <code>169.254.0.0/16</code> </p> </li> <li> <p> <code>224.0.0.0 - 239.255.255.255</code> </p> </li> <li> <p> <code>240.0.0.0 - 255.255.255.255</code> </p> </li> </ul> </li> </ul>"""
    custom_domain_name: NotRequired["str"]
    """<p>The domain name to use for the resources in the ODB network.</p>"""
    default_dns_prefix: NotRequired["str"]
    """<p>The DNS prefix to the default DNS domain name. The default DNS domain name is oraclevcn.com.</p>"""
    client_token: NotRequired["capo_odb.types.general_input_string.GeneralInputString"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, the Amazon Web Services SDK automatically generates a client token and uses it for the request to ensure idempotency. The client token is valid for up to 24 hours after it's first used.</p>"""
    s3_access: NotRequired["capo_odb.types.access.Access"]
    """<p>Specifies the configuration for Amazon S3 access from the ODB network.</p>"""
    zero_etl_access: NotRequired["capo_odb.types.access.Access"]
    """<p>Specifies the configuration for Zero-ETL access from the ODB network.</p>"""
    sts_access: NotRequired["capo_odb.types.access.Access"]
    """<p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>"""
    kms_access: NotRequired["capo_odb.types.access.Access"]
    """<p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>"""
    s3_policy_document: NotRequired["capo_odb.types.policy_document.PolicyDocument"]
    """<p>Specifies the endpoint policy for Amazon S3 access from the ODB network.</p>"""
    sts_policy_document: NotRequired["capo_odb.types.policy_document.PolicyDocument"]
    """<p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>"""
    kms_policy_document: NotRequired["capo_odb.types.policy_document.PolicyDocument"]
    """<p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>"""
    cross_region_s3_restore_sources_to_enable: NotRequired[
        "capo_odb.types.string_list.StringList"
    ]
    """<p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>"""
    tags: NotRequired["capo_odb.types.request_tag_map.RequestTagMap"]
    """<p>The list of resource tags to apply to the ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateOdbNetworkInput) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "availability_zone_id" in value:
        out["availabilityZoneId"] = value["availability_zone_id"]
    out["clientSubnetCidr"] = value["client_subnet_cidr"]
    if "backup_subnet_cidr" in value:
        out["backupSubnetCidr"] = value["backup_subnet_cidr"]
    if "custom_domain_name" in value:
        out["customDomainName"] = value["custom_domain_name"]
    if "default_dns_prefix" in value:
        out["defaultDnsPrefix"] = value["default_dns_prefix"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "s3_access" in value:
        import capo_odb.types.access

        out["s3Access"] = capo_odb.types.access.serialize_aws_json_1_0(
            value["s3_access"]
        )
    if "zero_etl_access" in value:
        import capo_odb.types.access

        out["zeroEtlAccess"] = capo_odb.types.access.serialize_aws_json_1_0(
            value["zero_etl_access"]
        )
    if "sts_access" in value:
        import capo_odb.types.access

        out["stsAccess"] = capo_odb.types.access.serialize_aws_json_1_0(
            value["sts_access"]
        )
    if "kms_access" in value:
        import capo_odb.types.access

        out["kmsAccess"] = capo_odb.types.access.serialize_aws_json_1_0(
            value["kms_access"]
        )
    if "s3_policy_document" in value:
        out["s3PolicyDocument"] = value["s3_policy_document"]
    if "sts_policy_document" in value:
        out["stsPolicyDocument"] = value["sts_policy_document"]
    if "kms_policy_document" in value:
        out["kmsPolicyDocument"] = value["kms_policy_document"]
    if "cross_region_s3_restore_sources_to_enable" in value:
        import capo_odb.types.string_list

        out["crossRegionS3RestoreSourcesToEnable"] = (
            capo_odb.types.string_list.serialize_aws_json_1_0(
                value["cross_region_s3_restore_sources_to_enable"]
            )
        )
    if "tags" in value:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateOdbNetworkInput:
    out: CreateOdbNetworkInput = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("availabilityZoneId") is not None:
        out["availability_zone_id"] = data["availabilityZoneId"]
    if data.get("clientSubnetCidr") is not None:
        out["client_subnet_cidr"] = data["clientSubnetCidr"]
    else:
        out["client_subnet_cidr"] = ""
    if data.get("backupSubnetCidr") is not None:
        out["backup_subnet_cidr"] = data["backupSubnetCidr"]
    if data.get("customDomainName") is not None:
        out["custom_domain_name"] = data["customDomainName"]
    if data.get("defaultDnsPrefix") is not None:
        out["default_dns_prefix"] = data["defaultDnsPrefix"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("s3Access") is not None:
        import capo_odb.types.access

        out["s3_access"] = capo_odb.types.access.deserialize_aws_json_1_0(
            data["s3Access"]
        )
    if data.get("zeroEtlAccess") is not None:
        import capo_odb.types.access

        out["zero_etl_access"] = capo_odb.types.access.deserialize_aws_json_1_0(
            data["zeroEtlAccess"]
        )
    if data.get("stsAccess") is not None:
        import capo_odb.types.access

        out["sts_access"] = capo_odb.types.access.deserialize_aws_json_1_0(
            data["stsAccess"]
        )
    if data.get("kmsAccess") is not None:
        import capo_odb.types.access

        out["kms_access"] = capo_odb.types.access.deserialize_aws_json_1_0(
            data["kmsAccess"]
        )
    if data.get("s3PolicyDocument") is not None:
        out["s3_policy_document"] = data["s3PolicyDocument"]
    if data.get("stsPolicyDocument") is not None:
        out["sts_policy_document"] = data["stsPolicyDocument"]
    if data.get("kmsPolicyDocument") is not None:
        out["kms_policy_document"] = data["kmsPolicyDocument"]
    if data.get("crossRegionS3RestoreSourcesToEnable") is not None:
        import capo_odb.types.string_list

        out["cross_region_s3_restore_sources_to_enable"] = (
            capo_odb.types.string_list.deserialize_aws_json_1_0(
                data["crossRegionS3RestoreSourcesToEnable"]
            )
        )
    if data.get("tags") is not None:
        import capo_odb.types.request_tag_map

        out["tags"] = capo_odb.types.request_tag_map.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
