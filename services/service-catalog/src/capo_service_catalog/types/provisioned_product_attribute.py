"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisionedProductAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.created_time
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.physical_id
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.provisioned_product_name_or_arn
    import capo_service_catalog.types.provisioned_product_status
    import capo_service_catalog.types.provisioned_product_status_message
    import capo_service_catalog.types.provisioned_product_type
    import capo_service_catalog.types.provisioning_artifact_name
    import capo_service_catalog.types.tags
    import capo_service_catalog.types.user_arn
    import capo_service_catalog.types.user_arn_session


class ProvisionedProductAttribute(TypedDict, closed=True):
    name: NotRequired[
        "capo_service_catalog.types.provisioned_product_name_or_arn.ProvisionedProductNameOrArn"
    ]
    """<p>The user-friendly name of the provisioned product.</p>"""
    arn: NotRequired[
        "capo_service_catalog.types.provisioned_product_name_or_arn.ProvisionedProductNameOrArn"
    ]
    """<p>The ARN of the provisioned product.</p>"""
    type: NotRequired[
        "capo_service_catalog.types.provisioned_product_type.ProvisionedProductType"
    ]
    """<p>The type of provisioned product. The supported values are <code>CFN_STACK</code>, <code>CFN_STACKSET</code>, <code>TERRAFORM_OPEN_SOURCE</code>, <code>TERRAFORM_CLOUD</code>, and <code>EXTERNAL</code>.</p>"""
    id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioned product.</p>"""
    status: NotRequired[
        "capo_service_catalog.types.provisioned_product_status.ProvisionedProductStatus"
    ]
    """<p>The current status of the provisioned product.</p> <ul> <li> <p> <code>AVAILABLE</code> - Stable state, ready to perform any operation. The most recent operation succeeded and completed.</p> </li> <li> <p> <code>UNDER_CHANGE</code> - Transitive state. Operations performed might not have valid results. Wait for an <code>AVAILABLE</code> status before performing operations.</p> </li> <li> <p> <code>TAINTED</code> - Stable state, ready to perform any operation. The stack has completed the requested operation but is not exactly what was requested. For example, a request to update to a new version failed and the stack rolled back to the current version.</p> </li> <li> <p> <code>ERROR</code> - An unexpected error occurred. The provisioned product exists but the stack is not running. For example, CloudFormation received a parameter value that was not valid and could not launch the stack.</p> </li> <li> <p> <code>PLAN_IN_PROGRESS</code> - Transitive state. The plan operations were performed to provision a new product, but resources have not yet been created. After reviewing the list of resources to be created, execute the plan. Wait for an <code>AVAILABLE</code> status before performing operations.</p> </li> </ul>"""
    status_message: NotRequired[
        "capo_service_catalog.types.provisioned_product_status_message.ProvisionedProductStatusMessage"
    ]
    """<p>The current status message of the provisioned product.</p>"""
    created_time: NotRequired["capo_service_catalog.types.created_time.CreatedTime"]
    """<p>The UTC time stamp of the creation time.</p>"""
    idempotency_token: NotRequired[
        "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""
    last_record_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The record identifier of the last request performed on this provisioned product.</p>"""
    last_provisioning_record_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The record identifier of the last request performed on this provisioned product of the following types:</p> <ul> <li> <p> ProvisionProduct </p> </li> <li> <p> UpdateProvisionedProduct </p> </li> <li> <p> ExecuteProvisionedProductPlan </p> </li> <li> <p> TerminateProvisionedProduct </p> </li> </ul>"""
    last_successful_provisioning_record_id: NotRequired[
        "capo_service_catalog.types.id.Id"
    ]
    """<p>The record identifier of the last successful request performed on this provisioned product of the following types:</p> <ul> <li> <p> ProvisionProduct </p> </li> <li> <p> UpdateProvisionedProduct </p> </li> <li> <p> ExecuteProvisionedProductPlan </p> </li> <li> <p> TerminateProvisionedProduct </p> </li> </ul>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>One or more tags.</p>"""
    physical_id: NotRequired["capo_service_catalog.types.physical_id.PhysicalId"]
    """<p>The assigned identifier for the resource, such as an EC2 instance ID or an S3 bucket name.</p>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    product_name: NotRequired[
        "capo_service_catalog.types.product_view_name.ProductViewName"
    ]
    """<p>The name of the product.</p>"""
    provisioning_artifact_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    provisioning_artifact_name: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The name of the provisioning artifact.</p>"""
    user_arn: NotRequired["capo_service_catalog.types.user_arn.UserArn"]
    """<p>The Amazon Resource Name (ARN) of the user.</p>"""
    user_arn_session: NotRequired[
        "capo_service_catalog.types.user_arn_session.UserArnSession"
    ]
    """<p>The ARN of the user in the session. This ARN might contain a session ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisionedProductAttribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_service_catalog.types.provisioned_product_status

        out["Status"] = (
            capo_service_catalog.types.provisioned_product_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "created_time" in value:
        import capo_service_catalog.types.created_time

        out["CreatedTime"] = (
            capo_service_catalog.types.created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "last_record_id" in value:
        out["LastRecordId"] = value["last_record_id"]
    if "last_provisioning_record_id" in value:
        out["LastProvisioningRecordId"] = value["last_provisioning_record_id"]
    if "last_successful_provisioning_record_id" in value:
        out["LastSuccessfulProvisioningRecordId"] = value[
            "last_successful_provisioning_record_id"
        ]
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "physical_id" in value:
        out["PhysicalId"] = value["physical_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "provisioning_artifact_name" in value:
        out["ProvisioningArtifactName"] = value["provisioning_artifact_name"]
    if "user_arn" in value:
        out["UserArn"] = value["user_arn"]
    if "user_arn_session" in value:
        out["UserArnSession"] = value["user_arn_session"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisionedProductAttribute:
    out: ProvisionedProductAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.provisioned_product_status

        out["status"] = (
            capo_service_catalog.types.provisioned_product_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.created_time

        out["created_time"] = (
            capo_service_catalog.types.created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("LastRecordId") is not None:
        out["last_record_id"] = data["LastRecordId"]
    if data.get("LastProvisioningRecordId") is not None:
        out["last_provisioning_record_id"] = data["LastProvisioningRecordId"]
    if data.get("LastSuccessfulProvisioningRecordId") is not None:
        out["last_successful_provisioning_record_id"] = data[
            "LastSuccessfulProvisioningRecordId"
        ]
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("PhysicalId") is not None:
        out["physical_id"] = data["PhysicalId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("ProvisioningArtifactName") is not None:
        out["provisioning_artifact_name"] = data["ProvisioningArtifactName"]
    if data.get("UserArn") is not None:
        out["user_arn"] = data["UserArn"]
    if data.get("UserArnSession") is not None:
        out["user_arn_session"] = data["UserArnSession"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisionedProductAttribute) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "type" in value:
        out["Type"] = value["type"]
    if "id" in value:
        out["Id"] = value["id"]
    if "status" in value:
        import capo_service_catalog.types.provisioned_product_status

        out["Status"] = (
            capo_service_catalog.types.provisioned_product_status.serialize_cbor(
                value["status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "created_time" in value:
        import capo_service_catalog.types.created_time

        out["CreatedTime"] = capo_service_catalog.types.created_time.serialize_cbor(
            value["created_time"]
        )
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    if "last_record_id" in value:
        out["LastRecordId"] = value["last_record_id"]
    if "last_provisioning_record_id" in value:
        out["LastProvisioningRecordId"] = value["last_provisioning_record_id"]
    if "last_successful_provisioning_record_id" in value:
        out["LastSuccessfulProvisioningRecordId"] = value[
            "last_successful_provisioning_record_id"
        ]
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_cbor(value["tags"])
    if "physical_id" in value:
        out["PhysicalId"] = value["physical_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "provisioning_artifact_name" in value:
        out["ProvisioningArtifactName"] = value["provisioning_artifact_name"]
    if "user_arn" in value:
        out["UserArn"] = value["user_arn"]
    if "user_arn_session" in value:
        out["UserArnSession"] = value["user_arn_session"]
    return out


def deserialize_cbor(data: dict) -> ProvisionedProductAttribute:
    out: ProvisionedProductAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Status") is not None:
        import capo_service_catalog.types.provisioned_product_status

        out["status"] = (
            capo_service_catalog.types.provisioned_product_status.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.created_time

        out["created_time"] = capo_service_catalog.types.created_time.deserialize_cbor(
            data["CreatedTime"]
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    if data.get("LastRecordId") is not None:
        out["last_record_id"] = data["LastRecordId"]
    if data.get("LastProvisioningRecordId") is not None:
        out["last_provisioning_record_id"] = data["LastProvisioningRecordId"]
    if data.get("LastSuccessfulProvisioningRecordId") is not None:
        out["last_successful_provisioning_record_id"] = data[
            "LastSuccessfulProvisioningRecordId"
        ]
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_cbor(data["Tags"])
    if data.get("PhysicalId") is not None:
        out["physical_id"] = data["PhysicalId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("ProvisioningArtifactName") is not None:
        out["provisioning_artifact_name"] = data["ProvisioningArtifactName"]
    if data.get("UserArn") is not None:
        out["user_arn"] = data["UserArn"]
    if data.get("UserArnSession") is not None:
        out["user_arn_session"] = data["UserArnSession"]
    return out
