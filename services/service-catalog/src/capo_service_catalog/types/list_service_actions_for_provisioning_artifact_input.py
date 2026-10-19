"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListServiceActionsForProvisioningArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_token


class ListServiceActionsForProvisioningArtifactInput(TypedDict, closed=True):
    product_id: "capo_service_catalog.types.id.Id"
    """<p>The product identifier. For example, <code>prod-abcdzk7xy33qa</code>.</p>"""
    provisioning_artifact_id: "capo_service_catalog.types.id.Id"
    """<p>The identifier of the provisioning artifact. For example, <code>pa-4abcdjnxjj6ne</code>.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size.PageSize"]
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListServiceActionsForProvisioningArtifactInput,
) -> dict:
    out: dict = {}
    out["ProductId"] = value["product_id"]
    out["ProvisioningArtifactId"] = value["provisioning_artifact_id"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListServiceActionsForProvisioningArtifactInput:
    out: ListServiceActionsForProvisioningArtifactInput = {}  # type: ignore[typeddict-item]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    else:
        out["product_id"] = ""
    if data.get("ProvisioningArtifactId") is not None:
        out["provisioning_artifact_id"] = data["ProvisioningArtifactId"]
    else:
        out["provisioning_artifact_id"] = ""
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    return out
