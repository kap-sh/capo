"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProvisionedProductPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.notification_arns
    import capo_service_catalog.types.provisioned_product_name
    import capo_service_catalog.types.provisioned_product_plan_name
    import capo_service_catalog.types.provisioned_product_plan_type
    import capo_service_catalog.types.tags
    import capo_service_catalog.types.update_provisioning_parameters


class CreateProvisionedProductPlanInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    plan_name: "capo_service_catalog.types.provisioned_product_plan_name.ProvisionedProductPlanName"
    """<p>The name of the plan.</p>"""
    plan_type: "capo_service_catalog.types.provisioned_product_plan_type.ProvisionedProductPlanType"
    """<p>The plan type.</p>"""
    notification_arns: NotRequired[
        "capo_service_catalog.types.notification_arns.NotificationArns"
    ]
    """<p>Passed to CloudFormation. The SNS topic ARNs to which to publish stack-related events.</p>"""
    path_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use <a>ListLaunchPaths</a>.</p>"""
    product_id: "capo_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    provisioned_product_name: (
        "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    )
    """<p>A user-friendly name for the provisioned product. This value must be unique for the Amazon Web Services account and cannot be updated after the product is provisioned.</p>"""
    provisioning_artifact_id: "capo_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact.</p>"""
    provisioning_parameters: NotRequired[
        "capo_service_catalog.types.update_provisioning_parameters.UpdateProvisioningParameters"
    ]
    """<p>Parameters specified by the administrator that are required for provisioning the product.</p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>One or more tags.</p> <p>If the plan is for an existing provisioned product, the product must have a <code>RESOURCE_UPDATE</code> constraint with <code>TagUpdatesOnProvisionedProduct</code> set to <code>ALLOWED</code> to allow tag updates.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProvisionedProductPlanInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PlanName"] = value["plan_name"]
    import capo_service_catalog.types.provisioned_product_plan_type

    out["PlanType"] = (
        capo_service_catalog.types.provisioned_product_plan_type.serialize_aws_json_1_1(
            value["plan_type"]
        )
    )
    if "notification_arns" in value:
        import capo_service_catalog.types.notification_arns

        out["NotificationArns"] = (
            capo_service_catalog.types.notification_arns.serialize_aws_json_1_1(
                value["notification_arns"]
            )
        )
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    out["ProductId"] = value["product_id"]
    out["ProvisionedProductName"] = value["provisioned_product_name"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "provisioning_parameters" in value:
        import capo_service_catalog.types.update_provisioning_parameters

        out["ProvisioningParameters"] = (
            capo_service_catalog.types.update_provisioning_parameters.serialize_aws_json_1_1(
                value["provisioning_parameters"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProvisionedProductPlanInput:
    out: CreateProvisionedProductPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("PlanName") is not None:
        out["plan_name"] = data["PlanName"]
    else:
        out["plan_name"] = ""
    if data.get("PlanType") is not None:
        import capo_service_catalog.types.provisioned_product_plan_type

        out["plan_type"] = (
            capo_service_catalog.types.provisioned_product_plan_type.deserialize_aws_json_1_1(
                data["PlanType"]
            )
        )
    else:
        import typing

        out["plan_type"] = typing.cast(
            "capo_service_catalog.types.provisioned_product_plan_type.ProvisionedProductPlanType",
            "",
        )
    if data.get("NotificationArns") is not None:
        import capo_service_catalog.types.notification_arns

        out["notification_arns"] = (
            capo_service_catalog.types.notification_arns.deserialize_aws_json_1_1(
                data["NotificationArns"]
            )
        )
    if data.get("PathId") is not None:
        out["path_id"] = data["PathId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("ProvisionedProductName") is not None:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    else:
        out["provisioned_product_name"] = ""
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        out["provisioning_artifact_id"] = ""
    if data.get("ProvisioningParameters") is not None:
        import capo_service_catalog.types.update_provisioning_parameters

        out["provisioning_parameters"] = (
            capo_service_catalog.types.update_provisioning_parameters.deserialize_aws_json_1_1(
                data["ProvisioningParameters"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
