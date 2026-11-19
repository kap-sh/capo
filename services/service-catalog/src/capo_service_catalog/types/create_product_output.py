"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.product_view_detail
    import capo_service_catalog.types.provisioning_artifact_detail
    import capo_service_catalog.types.tags


class CreateProductOutput(TypedDict, closed=True):
    product_view_detail: NotRequired[
        "capo_service_catalog.types.product_view_detail.ProductViewDetail"
    ]
    """<p>Information about the product view.</p>"""
    provisioning_artifact_detail: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_detail.ProvisioningArtifactDetail"
    ]
    """<p>Information about the provisioning artifact. </p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProductOutput) -> dict:
    out: dict = {}
    if "product_view_detail" in value:
        import capo_service_catalog.types.product_view_detail

        out["ProductViewDetail"] = (
            capo_service_catalog.types.product_view_detail.serialize_aws_json_1_1(
                value["product_view_detail"]
            )
        )
    if "provisioning_artifact_detail" in value:
        import capo_service_catalog.types.provisioning_artifact_detail

        out["ProvisioningArtifactDetail"] = (
            capo_service_catalog.types.provisioning_artifact_detail.serialize_aws_json_1_1(
                value["provisioning_artifact_detail"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProductOutput:
    out: CreateProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewDetail") is not None:
        import capo_service_catalog.types.product_view_detail

        out["product_view_detail"] = (
            capo_service_catalog.types.product_view_detail.deserialize_aws_json_1_1(
                data["ProductViewDetail"]
            )
        )
    if data.get("ProvisioningArtifactDetail") is not None:
        import capo_service_catalog.types.provisioning_artifact_detail

        out["provisioning_artifact_detail"] = (
            capo_service_catalog.types.provisioning_artifact_detail.deserialize_aws_json_1_1(
                data["ProvisioningArtifactDetail"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateProductOutput) -> dict:
    out: dict = {}
    if "product_view_detail" in value:
        import capo_service_catalog.types.product_view_detail

        out["ProductViewDetail"] = (
            capo_service_catalog.types.product_view_detail.serialize_cbor(
                value["product_view_detail"]
            )
        )
    if "provisioning_artifact_detail" in value:
        import capo_service_catalog.types.provisioning_artifact_detail

        out["ProvisioningArtifactDetail"] = (
            capo_service_catalog.types.provisioning_artifact_detail.serialize_cbor(
                value["provisioning_artifact_detail"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_cbor(value["tags"])
    return out


def deserialize_cbor(data: dict) -> CreateProductOutput:
    out: CreateProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewDetail") is not None:
        import capo_service_catalog.types.product_view_detail

        out["product_view_detail"] = (
            capo_service_catalog.types.product_view_detail.deserialize_cbor(
                data["ProductViewDetail"]
            )
        )
    if data.get("ProvisioningArtifactDetail") is not None:
        import capo_service_catalog.types.provisioning_artifact_detail

        out["provisioning_artifact_detail"] = (
            capo_service_catalog.types.provisioning_artifact_detail.deserialize_cbor(
                data["ProvisioningArtifactDetail"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_cbor(data["Tags"])
    return out
