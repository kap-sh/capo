"""Generated from Smithy shape ``com.amazonaws.servicecatalog#GetProvisionedProductOutputsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.output_keys
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.provisioned_product_name


class GetProvisionedProductOutputsInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    provisioned_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioned product that you want the outputs from.</p>"""
    provisioned_product_name: NotRequired[
        "capo_service_catalog.types.provisioned_product_name.ProvisionedProductName"
    ]
    """<p>The name of the provisioned product that you want the outputs from.</p>"""
    output_keys: NotRequired["capo_service_catalog.types.output_keys.OutputKeys"]
    """<p>The list of keys that the API should return with their values. If none are provided, the API will return all outputs of the provisioned product.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size.PageSize"]
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetProvisionedProductOutputsInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "provisioned_product_id" in value:
        out["ProvisionedProductId"] = value["provisioned_product_id"]
    if "provisioned_product_name" in value:
        out["ProvisionedProductName"] = value["provisioned_product_name"]
    if "output_keys" in value:
        import capo_service_catalog.types.output_keys

        out["OutputKeys"] = (
            capo_service_catalog.types.output_keys.serialize_aws_json_1_1(
                value["output_keys"]
            )
        )
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetProvisionedProductOutputsInput:
    out: GetProvisionedProductOutputsInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("ProvisionedProductId") is not None:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    if data.get("ProvisionedProductName") is not None:
        out["provisioned_product_name"] = data["ProvisionedProductName"]
    if data.get("OutputKeys") is not None:
        import capo_service_catalog.types.output_keys

        out["output_keys"] = (
            capo_service_catalog.types.output_keys.deserialize_aws_json_1_1(
                data["OutputKeys"]
            )
        )
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    return out
