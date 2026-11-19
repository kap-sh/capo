"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactView``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.product_view_summary
    import capo_service_catalog.types.provisioning_artifact


class ProvisioningArtifactView(TypedDict, closed=True):
    product_view_summary: NotRequired[
        "capo_service_catalog.types.product_view_summary.ProductViewSummary"
    ]
    """<p>Summary information about a product view.</p>"""
    provisioning_artifact: NotRequired[
        "capo_service_catalog.types.provisioning_artifact.ProvisioningArtifact"
    ]
    """<p>Information about a provisioning artifact. A provisioning artifact is also known as a product version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactView) -> dict:
    out: dict = {}
    if "product_view_summary" in value:
        import capo_service_catalog.types.product_view_summary

        out["ProductViewSummary"] = (
            capo_service_catalog.types.product_view_summary.serialize_aws_json_1_1(
                value["product_view_summary"]
            )
        )
    if "provisioning_artifact" in value:
        import capo_service_catalog.types.provisioning_artifact

        out["ProvisioningArtifact"] = (
            capo_service_catalog.types.provisioning_artifact.serialize_aws_json_1_1(
                value["provisioning_artifact"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactView:
    out: ProvisioningArtifactView = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewSummary") is not None:
        import capo_service_catalog.types.product_view_summary

        out["product_view_summary"] = (
            capo_service_catalog.types.product_view_summary.deserialize_aws_json_1_1(
                data["ProductViewSummary"]
            )
        )
    if data.get("ProvisioningArtifact") is not None:
        import capo_service_catalog.types.provisioning_artifact

        out["provisioning_artifact"] = (
            capo_service_catalog.types.provisioning_artifact.deserialize_aws_json_1_1(
                data["ProvisioningArtifact"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactView) -> dict:
    out: dict = {}
    if "product_view_summary" in value:
        import capo_service_catalog.types.product_view_summary

        out["ProductViewSummary"] = (
            capo_service_catalog.types.product_view_summary.serialize_cbor(
                value["product_view_summary"]
            )
        )
    if "provisioning_artifact" in value:
        import capo_service_catalog.types.provisioning_artifact

        out["ProvisioningArtifact"] = (
            capo_service_catalog.types.provisioning_artifact.serialize_cbor(
                value["provisioning_artifact"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ProvisioningArtifactView:
    out: ProvisioningArtifactView = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewSummary") is not None:
        import capo_service_catalog.types.product_view_summary

        out["product_view_summary"] = (
            capo_service_catalog.types.product_view_summary.deserialize_cbor(
                data["ProductViewSummary"]
            )
        )
    if data.get("ProvisioningArtifact") is not None:
        import capo_service_catalog.types.provisioning_artifact

        out["provisioning_artifact"] = (
            capo_service_catalog.types.provisioning_artifact.deserialize_cbor(
                data["ProvisioningArtifact"]
            )
        )
    return out
