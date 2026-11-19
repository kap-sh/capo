"""Generated from Smithy shape ``com.amazonaws.servicecatalog#FailedServiceActionAssociation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id
    import capo_service_catalog.types.service_action_association_error_code
    import capo_service_catalog.types.service_action_association_error_message


class FailedServiceActionAssociation(TypedDict, closed=True):
    service_action_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>"""
    provisioning_artifact_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>"""
    error_code: NotRequired[
        "capo_service_catalog.types.service_action_association_error_code.ServiceActionAssociationErrorCode"
    ]
    """<p>The error code. Valid values are listed below.</p>"""
    error_message: NotRequired[
        "capo_service_catalog.types.service_action_association_error_message.ServiceActionAssociationErrorMessage"
    ]
    """<p>A text description of the error.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FailedServiceActionAssociation) -> dict:
    out: dict = {}
    if "service_action_id" in value:
        out["ServiceActionId"] = value["service_action_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "error_code" in value:
        import capo_service_catalog.types.service_action_association_error_code

        out["ErrorCode"] = (
            capo_service_catalog.types.service_action_association_error_code.serialize_aws_json_1_1(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FailedServiceActionAssociation:
    out: FailedServiceActionAssociation = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionId") is not None:
        out["service_action_id"] = data["ServiceActionId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("ErrorCode") is not None:
        import capo_service_catalog.types.service_action_association_error_code

        out["error_code"] = (
            capo_service_catalog.types.service_action_association_error_code.deserialize_aws_json_1_1(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FailedServiceActionAssociation) -> dict:
    out: dict = {}
    if "service_action_id" in value:
        out["ServiceActionId"] = value["service_action_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "error_code" in value:
        import capo_service_catalog.types.service_action_association_error_code

        out["ErrorCode"] = (
            capo_service_catalog.types.service_action_association_error_code.serialize_cbor(
                value["error_code"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_cbor(data: dict) -> FailedServiceActionAssociation:
    out: FailedServiceActionAssociation = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionId") is not None:
        out["service_action_id"] = data["ServiceActionId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("ErrorCode") is not None:
        import capo_service_catalog.types.service_action_association_error_code

        out["error_code"] = (
            capo_service_catalog.types.service_action_association_error_code.deserialize_cbor(
                data["ErrorCode"]
            )
        )
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    return out
