"""Generated from Smithy shape ``com.amazonaws.servicecatalog#RecordDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.created_time
    import capo_service_catalog.types.id
    import capo_service_catalog.types.provisioned_product_name
    import capo_service_catalog.types.provisioned_product_type
    import capo_service_catalog.types.record_errors
    import capo_service_catalog.types.record_status
    import capo_service_catalog.types.record_tags
    import capo_service_catalog.types.record_type
    import capo_service_catalog.types.role_arn
    import capo_service_catalog.types.updated_time


class RecordDetail(TypedDict, closed=True):
    record_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the record.</p>"""
    provisioned_product_name: NotRequired[
        "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    ]
    """<p>The user-friendly name of the provisioned product.</p>"""
    status: NotRequired["capo_service_catalog.types.record_status.RecordStatus"]
    """<p>The status of the provisioned product.</p> <ul> <li> <p> <code>CREATED</code> - The request was created but the operation has not started.</p> </li> <li> <p> <code>IN_PROGRESS</code> - The requested operation is in progress.</p> </li> <li> <p> <code>IN_PROGRESS_IN_ERROR</code> - The provisioned product is under change but the requested operation failed and some remediation is occurring. For example, a rollback.</p> </li> <li> <p> <code>SUCCEEDED</code> - The requested operation has successfully completed.</p> </li> <li> <p> <code>FAILED</code> - The requested operation has unsuccessfully completed. Investigate using the error messages returned.</p> </li> </ul>"""
    created_time: NotRequired["capo_service_catalog.types.created_time.CreatedTime"]
    """<p>The UTC time stamp of the creation time.</p>"""
    updated_time: NotRequired["capo_service_catalog.types.updated_time.UpdatedTime"]
    """<p>The time when the record was last updated.</p>"""
    provisioned_product_type: NotRequired[
        "capo_service_catalog.types.provisioned_product_type.ProvisionedProductType"
    ]
    """<p>The type of provisioned product. The supported values are <code>CFN_STACK</code>, <code>CFN_STACKSET</code>, <code>TERRAFORM_OPEN_SOURCE</code>, <code>TERRAFORM_CLOUD</code>, and <code>EXTERNAL</code>.</p>"""
    record_type: NotRequired["capo_service_catalog.types.record_type.RecordType"]
    """<p>The record type.</p> <ul> <li> <p> <code>PROVISION_PRODUCT</code> </p> </li> <li> <p> <code>UPDATE_PROVISIONED_PRODUCT</code> </p> </li> <li> <p> <code>TERMINATE_PROVISIONED_PRODUCT</code> </p> </li> </ul>"""
    provisioned_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioned product.</p>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    provisioning_artifact_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    path_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The path identifier.</p>"""
    record_errors: NotRequired["capo_service_catalog.types.record_errors.RecordErrors"]
    """<p>The errors that occurred.</p>"""
    record_tags: NotRequired["capo_service_catalog.types.record_tags.RecordTags"]
    """<p>One or more tags.</p>"""
    launch_role_arn: NotRequired["capo_service_catalog.types.role_arn.RoleArn"]
    """<p>The ARN of the launch role associated with the provisioned product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordDetail) -> dict:
    out: dict = {}
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "status" in value:
        import capo_service_catalog.types.record_status

        out["Status"] = capo_service_catalog.types.record_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "created_time" in value:
        import capo_service_catalog.types.created_time

        out["CreatedTime"] = (
            capo_service_catalog.types.created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "updated_time" in value:
        import capo_service_catalog.types.updated_time

        out["UpdatedTime"] = (
            capo_service_catalog.types.updated_time.serialize_aws_json_1_1(
                value["updated_time"]
            )
        )
    if "provisioned_product_type" in value:
        out["ProvisionedProductType"] = value["provisioned_product_type"]
    if "record_type" in value:
        out["RecordType"] = value["record_type"]
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "record_errors" in value:
        import capo_service_catalog.types.record_errors

        out["RecordErrors"] = (
            capo_service_catalog.types.record_errors.serialize_aws_json_1_1(
                value["record_errors"]
            )
        )
    if "record_tags" in value:
        import capo_service_catalog.types.record_tags

        out["RecordTags"] = (
            capo_service_catalog.types.record_tags.serialize_aws_json_1_1(
                value["record_tags"]
            )
        )
    if "launch_role_arn" in value:
        out["LaunchRoleArn"] = value["launch_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecordDetail:
    out: RecordDetail = {}  # type: ignore[typeddict-item]
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    if data.get("ProvisionedProductName") is not None:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.record_status

        out["status"] = (
            capo_service_catalog.types.record_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.created_time

        out["created_time"] = (
            capo_service_catalog.types.created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if data.get("UpdatedTime") is not None:
        import capo_service_catalog.types.updated_time

        out["updated_time"] = (
            capo_service_catalog.types.updated_time.deserialize_aws_json_1_1(
                data["UpdatedTime"]
            )
        )
    if data.get("ProvisionedProductType") is not None:
        out["provisioned_product_type"] = data["ProvisionedProductType"]
    if data.get("RecordType") is not None:
        out["record_type"] = data["RecordType"]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("PathId") is not None:
        out["path_id"] = data["PathId"]
    if data.get("RecordErrors") is not None:
        import capo_service_catalog.types.record_errors

        out["record_errors"] = (
            capo_service_catalog.types.record_errors.deserialize_aws_json_1_1(
                data["RecordErrors"]
            )
        )
    if data.get("RecordTags") is not None:
        import capo_service_catalog.types.record_tags

        out["record_tags"] = (
            capo_service_catalog.types.record_tags.deserialize_aws_json_1_1(
                data["RecordTags"]
            )
        )
    if data.get("LaunchRoleArn") is not None:
        out["launch_role_arn"] = data["LaunchRoleArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RecordDetail) -> dict:
    out: dict = {}
    if "record_id" in value:
        out["RecordId"] = value["record_id"]
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "status" in value:
        import capo_service_catalog.types.record_status

        out["Status"] = capo_service_catalog.types.record_status.serialize_cbor(
            value["status"]
        )
    if "created_time" in value:
        import capo_service_catalog.types.created_time

        out["CreatedTime"] = capo_service_catalog.types.created_time.serialize_cbor(
            value["created_time"]
        )
    if "updated_time" in value:
        import capo_service_catalog.types.updated_time

        out["UpdatedTime"] = capo_service_catalog.types.updated_time.serialize_cbor(
            value["updated_time"]
        )
    if "provisioned_product_type" in value:
        out["ProvisionedProductType"] = value["provisioned_product_type"]
    if "record_type" in value:
        out["RecordType"] = value["record_type"]
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "record_errors" in value:
        import capo_service_catalog.types.record_errors

        out["RecordErrors"] = capo_service_catalog.types.record_errors.serialize_cbor(
            value["record_errors"]
        )
    if "record_tags" in value:
        import capo_service_catalog.types.record_tags

        out["RecordTags"] = capo_service_catalog.types.record_tags.serialize_cbor(
            value["record_tags"]
        )
    if "launch_role_arn" in value:
        out["LaunchRoleArn"] = value["launch_role_arn"]
    return out


def deserialize_cbor(data: dict) -> RecordDetail:
    out: RecordDetail = {}  # type: ignore[typeddict-item]
    if data.get("RecordId") is not None:
        out["record_id"] = data["RecordId"]
    if data.get("ProvisionedProductName") is not None:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.record_status

        out["status"] = capo_service_catalog.types.record_status.deserialize_cbor(
            data["Status"]
        )
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.created_time

        out["created_time"] = capo_service_catalog.types.created_time.deserialize_cbor(
            data["CreatedTime"]
        )
    if data.get("UpdatedTime") is not None:
        import capo_service_catalog.types.updated_time

        out["updated_time"] = capo_service_catalog.types.updated_time.deserialize_cbor(
            data["UpdatedTime"]
        )
    if data.get("ProvisionedProductType") is not None:
        out["provisioned_product_type"] = data["ProvisionedProductType"]
    if data.get("RecordType") is not None:
        out["record_type"] = data["RecordType"]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("PathId") is not None:
        out["path_id"] = data["PathId"]
    if data.get("RecordErrors") is not None:
        import capo_service_catalog.types.record_errors

        out["record_errors"] = (
            capo_service_catalog.types.record_errors.deserialize_cbor(
                data["RecordErrors"]
            )
        )
    if data.get("RecordTags") is not None:
        import capo_service_catalog.types.record_tags

        out["record_tags"] = capo_service_catalog.types.record_tags.deserialize_cbor(
            data["RecordTags"]
        )
    if data.get("LaunchRoleArn") is not None:
        out["launch_role_arn"] = data["LaunchRoleArn"]
    return out
