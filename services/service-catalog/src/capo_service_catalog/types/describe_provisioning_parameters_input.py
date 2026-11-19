"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisioningParametersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.portfolio_display_name
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.provisioning_artifact_name


class DescribeProvisioningParametersInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier. You must provide the product name or ID, but not both.</p>"""
    product_name: NotRequired[
        "capo_service_catalog.types.product_view_name.ProductViewName"
    ]
    """<p>The name of the product. You must provide the name or ID, but not both.</p>"""
    provisioning_artifact_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact. You must provide the name or ID, but not both.</p>"""
    provisioning_artifact_name: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The name of the provisioning artifact. You must provide the name or ID, but not both.</p>"""
    path_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The path identifier of the product. This value is optional if the product has a default path, and required if the product has more than one path. To list the paths for a product, use <a>ListLaunchPaths</a>. You must provide the name or ID, but not both.</p>"""
    path_name: NotRequired[
        "capo_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
    ]
    """<p>The name of the path. You must provide the name or ID, but not both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisioningParametersInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisioningParametersInput:
    out: DescribeProvisioningParametersInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
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
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProvisioningParametersInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
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
    return out


def deserialize_cbor(data: dict) -> DescribeProvisioningParametersInput:
    out: DescribeProvisioningParametersInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
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
    return out
