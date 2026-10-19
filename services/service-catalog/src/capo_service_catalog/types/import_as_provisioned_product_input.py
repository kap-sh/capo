"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ImportAsProvisionedProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.physical_id
    import capo_service_catalog.types.provisioned_product_name


class ImportAsProvisionedProductInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    product_id: "capo_service_catalog.types.id.Id"
    """<p>The product identifier.</p>"""
    provisioning_artifact_id: "capo_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact.</p>"""
    provisioned_product_name: (
        "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    )
    """<p>The user-friendly name of the provisioned product. The value must be unique for the Amazon Web Services account. The name cannot be updated after the product is provisioned. </p>"""
    physical_id: "capo_service_catalog.types.physical_id.PhysicalId"
    """<p>The unique identifier of the resource to be imported. It only currently supports CloudFormation stack IDs.</p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportAsProvisionedProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProductId"] = value["product_id"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    out["ProvisionedProductName"] = value["provisioned_product_name"]
    out["PhysicalId"] = value["physical_id"]
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportAsProvisionedProductInput:
    out: ImportAsProvisionedProductInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        out["provisioning_artifact_id"] = ""
    if data.get("ProvisionedProductName") is not None:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    else:
        out["provisioned_product_name"] = ""
    if data.get("PhysicalId") is not None:
        out["physical_id"] = data["PhysicalId"]
    else:
        out["physical_id"] = ""
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    return out
