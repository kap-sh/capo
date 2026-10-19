"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.add_tags
    import capo_service_catalog.types.idempotency_token
    import capo_service_catalog.types.product_type
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.product_view_owner
    import capo_service_catalog.types.product_view_short_description
    import capo_service_catalog.types.provisioning_artifact_properties
    import capo_service_catalog.types.source_connection
    import capo_service_catalog.types.support_description
    import capo_service_catalog.types.support_email
    import capo_service_catalog.types.support_url


class CreateProductInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    name: "capo_service_catalog.types.product_view_name.ProductViewName"
    """<p>The name of the product.</p>"""
    owner: "capo_service_catalog.types.product_view_owner.ProductViewOwner"
    """<p>The owner of the product.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.product_view_short_description.ProductViewShortDescription"
    ]
    """<p>The description of the product.</p>"""
    distributor: NotRequired[
        "capo_service_catalog.types.product_view_owner.ProductViewOwner"
    ]
    """<p>The distributor of the product.</p>"""
    support_description: NotRequired[
        "capo_service_catalog.types.support_description.SupportDescription"
    ]
    """<p>The support information about the product.</p>"""
    support_email: NotRequired["capo_service_catalog.types.support_email.SupportEmail"]
    """<p>The contact email for product support.</p>"""
    support_url: NotRequired["capo_service_catalog.types.support_url.SupportUrl"]
    r"""<p>The contact URL for product support.</p> <p> <code>^https?:\/\// </code>/ is the pattern used to validate SupportUrl.</p>"""
    product_type: "capo_service_catalog.types.product_type.ProductType"
    """<p>The type of product.</p>"""
    tags: NotRequired["capo_service_catalog.types.add_tags.AddTags"]
    """<p>One or more tags.</p>"""
    provisioning_artifact_parameters: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_properties.ProvisioningArtifactProperties"
    ]
    """<p>The configuration of the provisioning artifact. </p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""
    source_connection: NotRequired[
        "capo_service_catalog.types.source_connection.SourceConnection"
    ]
    """<p>Specifies connection details for the created product and syncs the product to the connection source artifact. This automatically manages the product's artifacts based on changes to the source. The <code>SourceConnection</code> parameter consists of the following sub-fields.</p> <ul> <li> <p> <code>Type</code> </p> </li> <li> <p> <code>ConnectionParamters</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["Name"] = value["name"]
    out["Owner"] = value["owner"]
    if "description" in value:
        out["Description"] = value["description"]
    if "distributor" in value:
        out["Distributor"] = value["distributor"]
    if "support_description" in value:
        out["SupportDescription"] = value["support_description"]
    if "support_email" in value:
        out["SupportEmail"] = value["support_email"]
    if "support_url" in value:
        out["SupportUrl"] = value["support_url"]
    import capo_service_catalog.types.product_type

    out["ProductType"] = capo_service_catalog.types.product_type.serialize_aws_json_1_1(
        value["product_type"]
    )
    if "tags" in value:
        import capo_service_catalog.types.add_tags

        out["Tags"] = capo_service_catalog.types.add_tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "provisioning_artifact_parameters" in value:
        import capo_service_catalog.types.provisioning_artifact_properties

        out["ProvisioningArtifactParameters"] = (
            capo_service_catalog.types.provisioning_artifact_properties.serialize_aws_json_1_1(
                value["provisioning_artifact_parameters"]
            )
        )
    out["IdempotencyToken"] = value["idempotency_token"]
    if "source_connection" in value:
        import capo_service_catalog.types.source_connection

        out["SourceConnection"] = (
            capo_service_catalog.types.source_connection.serialize_aws_json_1_1(
                value["source_connection"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProductInput:
    out: CreateProductInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    else:
        out["owner"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Distributor") is not None:
        out["distributor"] = data["Distributor"]
    if data.get("SupportDescription") is not None:
        out["support_description"] = data["SupportDescription"]
    if data.get("SupportEmail") is not None:
        out["support_email"] = data["SupportEmail"]
    if data.get("SupportUrl") is not None:
        out["support_url"] = data["SupportUrl"]
    if data.get("ProductType") is not None:
        import capo_service_catalog.types.product_type

        out["product_type"] = (
            capo_service_catalog.types.product_type.deserialize_aws_json_1_1(
                data["ProductType"]
            )
        )
    else:
        import typing

        out["product_type"] = typing.cast(
            "capo_service_catalog.types.product_type.ProductType", ""
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.add_tags

        out["tags"] = capo_service_catalog.types.add_tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("ProvisioningArtifactParameters") is not None:
        import capo_service_catalog.types.provisioning_artifact_properties

        out["provisioning_artifact_parameters"] = (
            capo_service_catalog.types.provisioning_artifact_properties.deserialize_aws_json_1_1(
                data["ProvisioningArtifactParameters"]
            )
        )
    if data.get("IdempotencyToken") is not None:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        out["idempotency_token"] = ""
    if data.get("SourceConnection") is not None:
        import capo_service_catalog.types.source_connection

        out["source_connection"] = (
            capo_service_catalog.types.source_connection.deserialize_aws_json_1_1(
                data["SourceConnection"]
            )
        )
    return out
