"""Generated from Smithy shape ``com.amazonaws.ssoadmin#DescribeInstanceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.account_id
    import capo_sso_admin.types.date
    import capo_sso_admin.types.encryption_configuration_details
    import capo_sso_admin.types.id
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.instance_identity_store_arn
    import capo_sso_admin.types.instance_status
    import capo_sso_admin.types.name_type
    import capo_sso_admin.types.reason
    import capo_sso_admin.types.region_metadata_list
    import capo_sso_admin.types.region_name


class DescribeInstanceResponse(TypedDict, closed=True):
    instance_arn: NotRequired["capo_sso_admin.types.instance_arn.InstanceArn"]
    """<p>The ARN of the instance of IAM Identity Center under which the operation will run. For more information about ARNs, see <a href="/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces</a> in the <i>Amazon Web Services General Reference</i>.</p>"""
    identity_store_id: NotRequired["capo_sso_admin.types.id.Id"]
    """<p>The identifier of the identity store that is connected to the instance of IAM Identity Center.</p>"""
    identity_store_arn: NotRequired[
        "capo_sso_admin.types.instance_identity_store_arn.InstanceIdentityStoreArn"
    ]
    """<p>The ARN of the identity store that is connected to the instance of IAM Identity Center.</p>"""
    owner_account_id: NotRequired["capo_sso_admin.types.account_id.AccountId"]
    """<p>The identifier of the Amazon Web Services account for which the instance was created.</p>"""
    name: NotRequired["capo_sso_admin.types.name_type.NameType"]
    """<p>Specifies the instance name.</p>"""
    created_date: NotRequired["capo_sso_admin.types.date.Date"]
    """<p>The date the instance was created.</p>"""
    status: NotRequired["capo_sso_admin.types.instance_status.InstanceStatus"]
    """<p>The status of the instance. </p>"""
    status_reason: NotRequired["capo_sso_admin.types.reason.Reason"]
    """<p>Provides additional context about the current status of the IAM Identity Center instance. This field is particularly useful when an instance is in a non-ACTIVE state, such as CREATE_FAILED. When an instance fails to create or update, this field contains information about the cause, which may include issues with KMS key configuration, permission problems with the specified KMS key, or service-related errors. </p>"""
    primary_region: NotRequired["capo_sso_admin.types.region_name.RegionName"]
    """<p>The primary Region where the IAM Identity Center instance was originally enabled. The primary Region cannot be removed.</p>"""
    regions: NotRequired["capo_sso_admin.types.region_metadata_list.RegionMetadataList"]
    """<p>The list of Regions enabled in the IAM Identity Center instance, including Regions with ACTIVE, ADDING, or REMOVING status.</p>"""
    encryption_configuration_details: NotRequired[
        "capo_sso_admin.types.encryption_configuration_details.EncryptionConfigurationDetails"
    ]
    """<p>Contains the encryption configuration for your IAM Identity Center instance, including the encryption status, KMS key type, and KMS key ARN.</p>"""
    permission_sets_enabled: NotRequired["bool"]
    """<p>Indicates whether permission sets are enabled for this Identity Center instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeInstanceResponse) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "identity_store_id" in value:
        out["IdentityStoreId"] = value["identity_store_id"]
    if "identity_store_arn" in value:
        out["IdentityStoreArn"] = value["identity_store_arn"]
    if "owner_account_id" in value:
        out["OwnerAccountId"] = value["owner_account_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_date" in value:
        import capo_sso_admin.types.date

        out["CreatedDate"] = capo_sso_admin.types.date.serialize_aws_json_1_1(
            value["created_date"]
        )
    if "status" in value:
        import capo_sso_admin.types.instance_status

        out["Status"] = capo_sso_admin.types.instance_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "status_reason" in value:
        out["StatusReason"] = value["status_reason"]
    if "primary_region" in value:
        out["PrimaryRegion"] = value["primary_region"]
    if "regions" in value:
        import capo_sso_admin.types.region_metadata_list

        out["Regions"] = (
            capo_sso_admin.types.region_metadata_list.serialize_aws_json_1_1(
                value["regions"]
            )
        )
    if "encryption_configuration_details" in value:
        import capo_sso_admin.types.encryption_configuration_details

        out["EncryptionConfigurationDetails"] = (
            capo_sso_admin.types.encryption_configuration_details.serialize_aws_json_1_1(
                value["encryption_configuration_details"]
            )
        )
    if "permission_sets_enabled" in value:
        out["PermissionSetsEnabled"] = value["permission_sets_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeInstanceResponse:
    out: DescribeInstanceResponse = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    if data.get("IdentityStoreId") is not None:
        out["identity_store_id"] = data["IdentityStoreId"]
    if data.get("IdentityStoreArn") is not None:
        out["identity_store_arn"] = data["IdentityStoreArn"]
    if data.get("OwnerAccountId") is not None:
        out["owner_account_id"] = data["OwnerAccountId"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("CreatedDate") is not None:
        import capo_sso_admin.types.date

        out["created_date"] = capo_sso_admin.types.date.deserialize_aws_json_1_1(
            data["CreatedDate"]
        )
    if data.get("Status") is not None:
        import capo_sso_admin.types.instance_status

        out["status"] = capo_sso_admin.types.instance_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StatusReason") is not None:
        out["status_reason"] = data["StatusReason"]
    if data.get("PrimaryRegion") is not None:
        out["primary_region"] = data["PrimaryRegion"]
    if data.get("Regions") is not None:
        import capo_sso_admin.types.region_metadata_list

        out["regions"] = (
            capo_sso_admin.types.region_metadata_list.deserialize_aws_json_1_1(
                data["Regions"]
            )
        )
    if data.get("EncryptionConfigurationDetails") is not None:
        import capo_sso_admin.types.encryption_configuration_details

        out["encryption_configuration_details"] = (
            capo_sso_admin.types.encryption_configuration_details.deserialize_aws_json_1_1(
                data["EncryptionConfigurationDetails"]
            )
        )
    if data.get("PermissionSetsEnabled") is not None:
        out["permission_sets_enabled"] = data["PermissionSetsEnabled"]
    return out
