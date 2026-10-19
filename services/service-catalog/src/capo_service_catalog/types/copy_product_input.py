"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CopyProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.copy_options
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.product_arn
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.source_provisioning_artifact_properties


class CopyProductInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    source_product_arn: "capo_service_catalog.types.product_arn.ProductArn"
    """<p>The Amazon Resource Name (ARN) of the source product.</p>"""
    target_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the target product. By default, a new product is created.</p>"""
    target_product_name: NotRequired[
        "capo_service_catalog.types.product_view_name.ProductViewName"
    ]
    """<p>A name for the target product. The default is the name of the source product.</p>"""
    source_provisioning_artifact_identifiers: NotRequired[
        "capo_service_catalog.types.source_provisioning_artifact_properties.SourceProvisioningArtifactProperties"
    ]
    """<p>The identifiers of the provisioning artifacts (also known as versions) of the product to copy. By default, all provisioning artifacts are copied.</p>"""
    copy_options: NotRequired["capo_service_catalog.types.copy_options.CopyOptions"]
    """<p>The copy options. If the value is <code>CopyTags</code>, the tags from the source product are copied to the target product.</p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p> A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["SourceProductArn"] = value["source_product_arn"]
    if "target_product_id" in value:
        out["TargetProductId"] = value["target_product_id"]
    if "target_product_name" in value:
        out["TargetProductName"] = value["target_product_name"]
    if "source_provisioning_artifact_identifiers" in value:
        import capo_service_catalog.types.source_provisioning_artifact_properties

        out["SourceProvisioningArtifactIdentifiers"] = (
            capo_service_catalog.types.source_provisioning_artifact_properties.serialize_aws_json_1_1(
                value["source_provisioning_artifact_identifiers"]
            )
        )
    if "copy_options" in value:
        import capo_service_catalog.types.copy_options

        out["CopyOptions"] = (
            capo_service_catalog.types.copy_options.serialize_aws_json_1_1(
                value["copy_options"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CopyProductInput:
    out: CopyProductInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("SourceProductArn") is not None:
        out["source_product_arn"] = data["SourceProductArn"]
    else:
        out["source_product_arn"] = ""
    if data.get("TargetProductId") is not None:
        out["target_product_id"] = data["TargetProductId"]
    if data.get("TargetProductName") is not None:
        out["target_product_name"] = data["TargetProductName"]
    if data.get("SourceProvisioningArtifactIdentifiers") is not None:
        import capo_service_catalog.types.source_provisioning_artifact_properties

        out["source_provisioning_artifact_identifiers"] = (
            capo_service_catalog.types.source_provisioning_artifact_properties.deserialize_aws_json_1_1(
                data["SourceProvisioningArtifactIdentifiers"]
            )
        )
    if data.get("CopyOptions") is not None:
        import capo_service_catalog.types.copy_options

        out["copy_options"] = (
            capo_service_catalog.types.copy_options.deserialize_aws_json_1_1(
                data["CopyOptions"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    return out
