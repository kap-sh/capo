"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdateProvisionedProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.portfolio_display_name
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.provisioned_product_name_or_arn
    import capo_service_catalog.types.provisioning_artifact_name
    import capo_service_catalog.types.tags
    import capo_service_catalog.types.update_provisioning_parameters
    import capo_service_catalog.types.update_provisioning_preferences


class UpdateProvisionedProductInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    provisioned_product_name: NotRequired[
        "capo_service_catalog.types.provisioned_product_name_or_arn.ProvisionedProductNameOrArn"
    ]
    """<p>The name of the provisioned product. You cannot specify both <code>ProvisionedProductName</code> and <code>ProvisionedProductId</code>.</p>"""
    provisioned_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioned product. You must provide the name or ID, but not both.</p>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the product. You must provide the name or ID, but not both.</p>"""
    product_name: NotRequired[
        "capo_service_catalog.types.product_view_name.ProductViewName"
    ]
    """<p>The name of the product. You must provide the name or ID, but not both.</p>"""
    provisioning_artifact_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    provisioning_artifact_name: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The name of the provisioning artifact. You must provide the name or ID, but not both.</p>"""
    path_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The path identifier. This value is optional if the product has a default path, and required if the product has more than one path. You must provide the name or ID, but not both.</p>"""
    path_name: NotRequired[
        "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
    ]
    """<p>The name of the path. You must provide the name or ID, but not both.</p>"""
    provisioning_parameters: NotRequired[
        "capo_service_catalog.types.update_provisioning_parameters.UpdateProvisioningParameters"
    ]
    """<p>The new parameters.</p>"""
    provisioning_preferences: NotRequired[
        "capo_service_catalog.types.update_provisioning_preferences.UpdateProvisioningPreferences"
    ]
    """<p>An object that contains information about the provisioning preferences for a stack set.</p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>One or more tags. Requires the product to have <code>RESOURCE_UPDATE</code> constraint with <code>TagUpdatesOnProvisionedProduct</code> set to <code>ALLOWED</code> to allow tag updates.</p>"""
    update_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>The idempotency token that uniquely identifies the provisioning update request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateProvisionedProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "provisioning_artifact_name" in value:
        out["ProvisioningArtifactName"] = value["provisioning_artifact_name"]
    if "path_id" in value:
        out["PathId"] = value["path_id"]
    if "path_name" in value:
        out["PathName"] = value["path_name"]
    if "provisioning_parameters" in value:
        import capo_service_catalog.types.update_provisioning_parameters

        out["ProvisioningParameters"] = (
            capo_service_catalog.types.update_provisioning_parameters.serialize_aws_json_1_1(
                value["provisioning_parameters"]
            )
        )
    if "provisioning_preferences" in value:
        import capo_service_catalog.types.update_provisioning_preferences

        out["ProvisioningPreferences"] = (
            capo_service_catalog.types.update_provisioning_preferences.serialize_aws_json_1_1(
                value["provisioning_preferences"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateProvisionedProductInput:
    out: UpdateProvisionedProductInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("ProvisionedProductName") is not None:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("ProvisioningArtifactName") is not None:
        out["provisioning_artifact_name"] = data["ProvisioningArtifactName"]
    if data.get("PathId") is not None:
        out["path_id"] = data["PathId"]
    if data.get("PathName") is not None:
        out["path_name"] = data["PathName"]
    if data.get("ProvisioningParameters") is not None:
        import capo_service_catalog.types.update_provisioning_parameters

        out["provisioning_parameters"] = (
            capo_service_catalog.types.update_provisioning_parameters.deserialize_aws_json_1_1(
                data["ProvisioningParameters"]
            )
        )
    if data.get("ProvisioningPreferences") is not None:
        import capo_service_catalog.types.update_provisioning_preferences

        out["provisioning_preferences"] = (
            capo_service_catalog.types.update_provisioning_preferences.deserialize_aws_json_1_1(
                data["ProvisioningPreferences"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    return out
