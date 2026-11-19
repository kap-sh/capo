"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductPlanDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.created_time
    import capo_service_catalog.types.id
    import capo_service_catalog.types.notification_arns
    import capo_service_catalog.types.provisioned_product_name
    import capo_service_catalog.types.provisioned_product_plan_name
    import capo_service_catalog.types.provisioned_product_plan_status
    import capo_service_catalog.types.provisioned_product_plan_type
    import capo_service_catalog.types.status_message
    import capo_service_catalog.types.tags
    import capo_service_catalog.types.update_provisioning_parameters
    import capo_service_catalog.types.updated_time


class ProvisionedProductPlanDetails(TypedDict, closed=True):
    created_time: NotRequired["capo_service_catalog.types.created_time.CreatedTime"]
    """<p>The UTC time stamp of the creation time.</p>"""
    path_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use <a>ListLaunchPaths</a>.</p>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    plan_name: NotRequired[
        "capo_service_catalog.types.provisioned_product_plan_name.ProvisionedProductPlanName"
    ]
    """<p>The name of the plan.</p>"""
    plan_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The plan identifier.</p>"""
    provision_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    provision_product_name: NotRequired[
        "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    ]
    """<p>The user-friendly name of the provisioned product.</p>"""
    plan_type: NotRequired[
        "capo_service_catalog.types.provisioned_product_plan_type.ProvisionedProductPlanType"
    ]
    """<p>The plan type.</p>"""
    provisioning_artifact_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    status: NotRequired[
        "capo_service_catalog.types.provisioned_product_plan_status.ProvisionedProductPlanStatus"
    ]
    """<p>The status.</p>"""
    updated_time: NotRequired["capo_service_catalog.types.updated_time.UpdatedTime"]
    """<p>The UTC time stamp when the plan was last updated.</p>"""
    notification_arns: NotRequired[
        "capo_service_catalog.types.notification_arns.NotificationArns"
    ]
    """<p>Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.</p>"""
    provisioning_parameters: NotRequired[
        "capo_service_catalog.types.update_provisioning_parameters.UpdateProvisioningParameters"
    ]
    """<p>Parameters specified by the administrator that are required for provisioning the product.</p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>One or more tags.</p>"""
    status_message: NotRequired[
        "capo_service_catalog.types.status_message.StatusMessage"
    ]
    """<p>The status message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductPlanDetails) -> dict:
    out: dict = {}
    if "created_time" in value:
        import capo_service_catalog.types.created_time

        out["CreatedTime"] = (
            capo_service_catalog.types.created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "plan_name" in value:
        out["PlanName"] = value["plan_name"]
    if "plan_id" in value:
        out["PlanId"] = value["plan_id"]
    if "provision_product_id" in value:
        out["ProvisionProductId"] = value["provision_product_id"]
    if "provision_product_name" in value:
        out["ProvisionProductName"] = value["provision_product_name"]
    if "plan_type" in value:
        import capo_service_catalog.types.provisioned_product_plan_type

        out["PlanType"] = (
            capo_service_catalog.types.provisioned_product_plan_type.serialize_aws_json_1_1(
                value["plan_type"]
            )
        )
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "status" in value:
        import capo_service_catalog.types.provisioned_product_plan_status

        out["Status"] = (
            capo_service_catalog.types.provisioned_product_plan_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "updated_time" in value:
        import capo_service_catalog.types.updated_time

        out["UpdatedTime"] = (
            capo_service_catalog.types.updated_time.serialize_aws_json_1_1(
                value["updated_time"]
            )
        )
    if "notification_arns" in value:
        import capo_service_catalog.types.notification_arns

        out["NotificationArns"] = (
            capo_service_catalog.types.notification_arns.serialize_aws_json_1_1(
                value["notification_arns"]
            )
        )
    if "provisioning_parameters" in value:
        import capo_service_catalog.types.update_provisioning_parameters

        out["ProvisioningParameters"] = (
            capo_service_catalog.types.update_provisioning_parameters.serialize_aws_json_1_1(
                value["provisioning_parameters"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedProductPlanDetails:
    out: ProvisionedProductPlanDetails = {}  # type: ignore[typeddict-item]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.created_time

        out["created_time"] = (
            capo_service_catalog.types.created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if data.get("PathId") is not None:
        out["path_id"] = data["PathId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("PlanName") is not None:
        out["plan_name"] = data["PlanName"]
    if data.get("PlanId") is not None:
        out["plan_id"] = data["PlanId"]
    if data.get("ProvisionProductId") is not None:
        out["provision_product_id"] = data["ProvisionProductId"]
    if data.get("ProvisionProductName") is not None:
        out["provision_product_name"] = data["ProvisionProductName"]
    if data.get("PlanType") is not None:
        import capo_service_catalog.types.provisioned_product_plan_type

        out["plan_type"] = (
            capo_service_catalog.types.provisioned_product_plan_type.deserialize_aws_json_1_1(
                data["PlanType"]
            )
        )
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.provisioned_product_plan_status

        out["status"] = (
            capo_service_catalog.types.provisioned_product_plan_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("UpdatedTime") is not None:
        import capo_service_catalog.types.updated_time

        out["updated_time"] = (
            capo_service_catalog.types.updated_time.deserialize_aws_json_1_1(
                data["UpdatedTime"]
            )
        )
    if data.get("NotificationArns") is not None:
        import capo_service_catalog.types.notification_arns

        out["notification_arns"] = (
            capo_service_catalog.types.notification_arns.deserialize_aws_json_1_1(
                data["NotificationArns"]
            )
        )
    if data.get("ProvisioningParameters") is not None:
        import capo_service_catalog.types.update_provisioning_parameters

        out["provisioning_parameters"] = (
            capo_service_catalog.types.update_provisioning_parameters.deserialize_aws_json_1_1(
                data["ProvisioningParameters"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionedProductPlanDetails) -> dict:
    out: dict = {}
    if "created_time" in value:
        import capo_service_catalog.types.created_time

        out["CreatedTime"] = capo_service_catalog.types.created_time.serialize_cbor(
            value["created_time"]
        )
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "plan_name" in value:
        out["PlanName"] = value["plan_name"]
    if "plan_id" in value:
        out["PlanId"] = value["plan_id"]
    if "provision_product_id" in value:
        out["ProvisionProductId"] = value["provision_product_id"]
    if "provision_product_name" in value:
        out["ProvisionProductName"] = value["provision_product_name"]
    if "plan_type" in value:
        import capo_service_catalog.types.provisioned_product_plan_type

        out["PlanType"] = (
            capo_service_catalog.types.provisioned_product_plan_type.serialize_cbor(
                value["plan_type"]
            )
        )
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "status" in value:
        import capo_service_catalog.types.provisioned_product_plan_status

        out["Status"] = (
            capo_service_catalog.types.provisioned_product_plan_status.serialize_cbor(
                value["status"]
            )
        )
    if "updated_time" in value:
        import capo_service_catalog.types.updated_time

        out["UpdatedTime"] = capo_service_catalog.types.updated_time.serialize_cbor(
            value["updated_time"]
        )
    if "notification_arns" in value:
        import capo_service_catalog.types.notification_arns

        out["NotificationArns"] = (
            capo_service_catalog.types.notification_arns.serialize_cbor(
                value["notification_arns"]
            )
        )
    if "provisioning_parameters" in value:
        import capo_service_catalog.types.update_provisioning_parameters

        out["ProvisioningParameters"] = (
            capo_service_catalog.types.update_provisioning_parameters.serialize_cbor(
                value["provisioning_parameters"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_cbor(value["tags"])
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_cbor(data: dict) -> ProvisionedProductPlanDetails:
    out: ProvisionedProductPlanDetails = {}  # type: ignore[typeddict-item]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.created_time

        out["created_time"] = capo_service_catalog.types.created_time.deserialize_cbor(
            data["CreatedTime"]
        )
    if data.get("PathId") is not None:
        out["path_id"] = data["PathId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("PlanName") is not None:
        out["plan_name"] = data["PlanName"]
    if data.get("PlanId") is not None:
        out["plan_id"] = data["PlanId"]
    if data.get("ProvisionProductId") is not None:
        out["provision_product_id"] = data["ProvisionProductId"]
    if data.get("ProvisionProductName") is not None:
        out["provision_product_name"] = data["ProvisionProductName"]
    if data.get("PlanType") is not None:
        import capo_service_catalog.types.provisioned_product_plan_type

        out["plan_type"] = (
            capo_service_catalog.types.provisioned_product_plan_type.deserialize_cbor(
                data["PlanType"]
            )
        )
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.provisioned_product_plan_status

        out["status"] = (
            capo_service_catalog.types.provisioned_product_plan_status.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("UpdatedTime") is not None:
        import capo_service_catalog.types.updated_time

        out["updated_time"] = capo_service_catalog.types.updated_time.deserialize_cbor(
            data["UpdatedTime"]
        )
    if data.get("NotificationArns") is not None:
        import capo_service_catalog.types.notification_arns

        out["notification_arns"] = (
            capo_service_catalog.types.notification_arns.deserialize_cbor(
                data["NotificationArns"]
            )
        )
    if data.get("ProvisioningParameters") is not None:
        import capo_service_catalog.types.update_provisioning_parameters

        out["provisioning_parameters"] = (
            capo_service_catalog.types.update_provisioning_parameters.deserialize_cbor(
                data["ProvisioningParameters"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_cbor(data["Tags"])
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
