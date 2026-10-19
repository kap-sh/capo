"""Generated from Smithy shape ``com.amazonaws.servicecatalog#TerminateProvisionedProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.ignore_errors
    import capo_service_catalog.types.provisioned_product_name_or_arn
    import capo_service_catalog.types.retain_physical_resources


class TerminateProvisionedProductInput(TypedDict, closed=True):
    provisioned_product_name: NotRequired[
        "capo_service_catalog.types.provisioned_product_name_or_arn.ProvisionedProductNameOrArn"
    ]
    """<p>The name of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>"""
    provisioned_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>"""
    terminate_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>An idempotency token that uniquely identifies the termination request. This token is only valid during the termination process. After the provisioned product is terminated, subsequent requests to terminate the same provisioned product always return <b>ResourceNotFound</b>.</p>"""
    ignore_errors: NotRequired["capo_service_catalog.types.ignore_errors.IgnoreErrors"]
    """<p>If set to true, Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.</p>"""
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    retain_physical_resources: NotRequired[
        "capo_service_catalog.types.retain_physical_resources.RetainPhysicalResources"
    ]
    """<p>When this boolean parameter is set to true, the <code>TerminateProvisionedProduct</code> API deletes the Service Catalog provisioned product. However, it does not remove the CloudFormation stack, stack set, or the underlying resources of the deleted provisioned product. The default value is false.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TerminateProvisionedProductInput) -> dict:
    out: dict = {}
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    out["TerminateToken"] = value["terminate_token"]
    if "ignore_errors" in value:
        out["IgnoreErrors"] = value["ignore_errors"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "retain_physical_resources" in value:
        out["RetainPhysicalResources"] = value["retain_physical_resources"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TerminateProvisionedProductInput:
    out: TerminateProvisionedProductInput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisionedProductName") is not None:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if data.get("TerminateToken") is not None:
        out["terminate_token"] = data["TerminateToken"]
    else:
        raise DeserializationError(
            "TerminateProvisionedProductInput.terminate_token required"
        )
    if data.get("IgnoreErrors") is not None:
        out["ignore_errors"] = data["IgnoreErrors"]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("RetainPhysicalResources") is not None:
        out["retain_physical_resources"] = data["RetainPhysicalResources"]
    return out
