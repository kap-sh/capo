"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisioningArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.boolean
    import capo_service_catalog.types.id
    import capo_service_catalog.types.product_view_name
    import capo_service_catalog.types.provisioning_artifact_name
    import capo_service_catalog.types.verbose


class DescribeProvisioningArtifactInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    provisioning_artifact_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    provisioning_artifact_name: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The provisioning artifact name.</p>"""
    product_name: NotRequired[
        "capo_service_catalog.types.product_view_name.ProductViewName"
    ]
    """<p>The product name.</p>"""
    verbose: NotRequired["capo_service_catalog.types.verbose.Verbose"]
    """<p>Indicates whether a verbose level of detail is enabled.</p>"""
    include_provisioning_artifact_parameters: NotRequired[
        "capo_service_catalog.types.boolean.Boolean"
    ]
    """<p>Indicates if the API call response does or does not include additional details about the provisioning parameters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisioningArtifactInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "provisioning_artifact_id" in value:
        out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "provisioning_artifact_name" in value:
        out["ProvisioningArtifactName"] = value["provisioning_artifact_name"]
    if "product_name" in value:
        out["ProductName"] = value["product_name"]
    if "verbose" in value:
        out["Verbose"] = value["verbose"]
    if "include_provisioning_artifact_parameters" in value:
        out["IncludeProvisioningArtifactParameters"] = value[
            "include_provisioning_artifact_parameters"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisioningArtifactInput:
    out: DescribeProvisioningArtifactInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProvisioningArtifactName") is not None:
        out["provisioning_artifact_name"] = data["ProvisioningArtifactName"]
    if data.get("ProductName") is not None:
        out["product_name"] = data["ProductName"]
    if data.get("Verbose") is not None:
        out["verbose"] = data["Verbose"]
    if data.get("IncludeProvisioningArtifactParameters") is not None:
        out["include_provisioning_artifact_parameters"] = data[
            "IncludeProvisioningArtifactParameters"
        ]
    return out
