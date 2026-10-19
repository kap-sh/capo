"""Generated from Smithy shape ``com.amazonaws.odb#UpdateOdbNetworkInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.access
    import capo_odb.types.policy_document
    import capo_odb.types.resource_display_name
    import capo_odb.types.resource_id_or_arn
    import capo_odb.types.string_list


class UpdateOdbNetworkInput(TypedDict, closed=True):
    odb_network_id: "capo_odb.types.resource_id_or_arn.ResourceIdOrArn"
    """<p>The unique identifier of the ODB network to update.</p>"""
    display_name: NotRequired[
        "capo_odb.types.resource_display_name.ResourceDisplayName"
    ]
    """<p>The new user-friendly name of the ODB network.</p>"""
    peered_cidrs_to_be_added: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of CIDR ranges from the peered VPC that allow access to the ODB network.</p>"""
    peered_cidrs_to_be_removed: NotRequired["capo_odb.types.string_list.StringList"]
    """<p>The list of CIDR ranges from the peered VPC to remove from the ODB network.</p>"""
    s3_access: NotRequired["capo_odb.types.access.Access"]
    """<p>Specifies the updated configuration for Amazon S3 access from the ODB network.</p>"""
    zero_etl_access: NotRequired["capo_odb.types.access.Access"]
    """<p>Specifies the updated configuration for Zero-ETL access from the ODB network.</p>"""
    sts_access: NotRequired["capo_odb.types.access.Access"]
    """<p>The Amazon Web Services Security Token Service (STS) access configuration for the ODB network.</p>"""
    kms_access: NotRequired["capo_odb.types.access.Access"]
    """<p>The Amazon Web Services Key Management Service (KMS) access configuration for the ODB network.</p>"""
    s3_policy_document: NotRequired["capo_odb.types.policy_document.PolicyDocument"]
    """<p>Specifies the updated endpoint policy for Amazon S3 access from the ODB network.</p>"""
    sts_policy_document: NotRequired["capo_odb.types.policy_document.PolicyDocument"]
    """<p>The Amazon Web Services Security Token Service (STS) policy document that defines permissions for token service usage within the ODB network.</p>"""
    kms_policy_document: NotRequired["capo_odb.types.policy_document.PolicyDocument"]
    """<p>The Amazon Web Services Key Management Service (KMS) policy document that defines permissions for key usage within the ODB network.</p>"""
    cross_region_s3_restore_sources_to_enable: NotRequired[
        "capo_odb.types.string_list.StringList"
    ]
    """<p>The cross-Region Amazon S3 restore sources to enable for the ODB network.</p>"""
    cross_region_s3_restore_sources_to_disable: NotRequired[
        "capo_odb.types.string_list.StringList"
    ]
    """<p>The cross-Region Amazon S3 restore sources to disable for the ODB network.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateOdbNetworkInput) -> dict:
    out: dict = {}
    out["odbNetworkId"] = value["odb_network_id"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "peered_cidrs_to_be_added" in value:
        import capo_odb.types.string_list

        out["peeredCidrsToBeAdded"] = capo_odb.types.string_list.serialize_aws_json_1_0(
            value["peered_cidrs_to_be_added"]
        )
    if "peered_cidrs_to_be_removed" in value:
        import capo_odb.types.string_list

        out["peeredCidrsToBeRemoved"] = (
            capo_odb.types.string_list.serialize_aws_json_1_0(
                value["peered_cidrs_to_be_removed"]
            )
        )
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
    if "cross_region_s3_restore_sources_to_disable" in value:
        import capo_odb.types.string_list

        out["crossRegionS3RestoreSourcesToDisable"] = (
            capo_odb.types.string_list.serialize_aws_json_1_0(
                value["cross_region_s3_restore_sources_to_disable"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateOdbNetworkInput:
    out: UpdateOdbNetworkInput = {}  # type: ignore[typeddict-item]
    if data.get("odbNetworkId") is not None:
        out["odb_network_id"] = data["odbNetworkId"]
    else:
        out["odb_network_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("peeredCidrsToBeAdded") is not None:
        import capo_odb.types.string_list

        out["peered_cidrs_to_be_added"] = (
            capo_odb.types.string_list.deserialize_aws_json_1_0(
                data["peeredCidrsToBeAdded"]
            )
        )
    if data.get("peeredCidrsToBeRemoved") is not None:
        import capo_odb.types.string_list

        out["peered_cidrs_to_be_removed"] = (
            capo_odb.types.string_list.deserialize_aws_json_1_0(
                data["peeredCidrsToBeRemoved"]
            )
        )
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
    if data.get("crossRegionS3RestoreSourcesToDisable") is not None:
        import capo_odb.types.string_list

        out["cross_region_s3_restore_sources_to_disable"] = (
            capo_odb.types.string_list.deserialize_aws_json_1_0(
                data["crossRegionS3RestoreSourcesToDisable"]
            )
        )
    return out
