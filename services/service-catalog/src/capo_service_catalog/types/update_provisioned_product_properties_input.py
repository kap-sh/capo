"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisionedProductPropertiesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.provisioned_product_properties


class UpdateProvisionedProductPropertiesInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    provisioned_product_id: "capo_service_catalog.types.id.Id"
    """<p>The identifier of the provisioned product.</p>"""
    provisioned_product_properties: "capo_service_catalog.types.provisioned_product_properties.ProvisionedProductProperties"
    """<p>A map that contains the provisioned product properties to be updated.</p> <p>The <code>LAUNCH_ROLE</code> key accepts role ARNs. This key allows an administrator to call <code>UpdateProvisionedProductProperties</code> to update the launch role that is associated with a provisioned product. This role is used when an end user calls a provisioning operation such as <code>UpdateProvisionedProduct</code>, <code>TerminateProvisionedProduct</code>, or <code>ExecuteProvisionedProductServiceAction</code>. Only a role ARN is valid. A user ARN is invalid. </p> <p>The <code>OWNER</code> key accepts user ARNs, IAM role ARNs, and STS assumed-role ARNs. The owner is the user that has permission to see, update, terminate, and execute service actions in the provisioned product.</p> <p>The administrator can change the owner of a provisioned product to another IAM or STS entity within the same account. Both end user owners and administrators can see ownership history of the provisioned product using the <code>ListRecordHistory</code> API. The new owner can describe all past records for the provisioned product using the <code>DescribeRecord</code> API. The previous owner can no longer use <code>DescribeRecord</code>, but can still see the product's history from when he was an owner using <code>ListRecordHistory</code>.</p> <p>If a provisioned product ownership is assigned to an end user, they can see and perform any action through the API or Service Catalog console such as update, terminate, and execute service actions. If an end user provisions a product and the owner is updated to someone else, they will no longer be able to see or perform any actions through API or the Service Catalog console on that provisioned product.</p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>The idempotency token that uniquely identifies the provisioning product update request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisionedProductPropertiesInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProvisionedProductId"] = value["provisioned_product_id"]
    import capo_service_catalog.types.provisioned_product_properties

    out["ProvisionedProductProperties"] = (
        capo_service_catalog.types.provisioned_product_properties.serialize_aws_json_1_1(
            value["provisioned_product_properties"]
        )
    )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisionedProductPropertiesInput:
    out: UpdateProvisionedProductPropertiesInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    else:
        out["provisioned_product_id"] = ""
    if data.get("ProvisionedProductProperties") is not None:
        import capo_service_catalog.types.provisioned_product_properties

        out["provisioned_product_properties"] = (
            capo_service_catalog.types.provisioned_product_properties.deserialize_aws_json_1_1(
                data["ProvisionedProductProperties"]
            )
        )
    else:
        out["provisioned_product_properties"] = {}
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    return out
