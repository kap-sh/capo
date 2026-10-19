"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListStackInstancesForProvisionedProductInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_token


class ListStackInstancesForProvisionedProductInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    provisioned_product_id: "capo_service_catalog.types.id.Id"
    """<p>The identifier of the provisioned product.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size.PageSize"]
    """<p>The maximum number of items to return with this call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStackInstancesForProvisionedProductInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListStackInstancesForProvisionedProductInput:
    out: ListStackInstancesForProvisionedProductInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    else:
        raise DeserializationError(
            "ListStackInstancesForProvisionedProductInput.provisioned_product_id required"
        )
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    return out
