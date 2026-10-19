"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListProvisionedProductPlansInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.access_level_filter
    import capo_service_catalog.types.id
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_token


class ListProvisionedProductPlansInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    provision_product_id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The product identifier.</p>"""
    page_size: NotRequired["capo_service_catalog.types.page_size.PageSize"]
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    access_level_filter: NotRequired[
        "capo_service_catalog.types.access_level_filter.AccessLevelFilter"
    ]
    """<p>The access level to use to obtain results. The default is <code>User</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListProvisionedProductPlansInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    if "provision_product_id" in value:
        out["ProvisionProductId"] = value["provision_product_id"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    if "access_level_filter" in value:
        import capo_service_catalog.types.access_level_filter

        out["AccessLevelFilter"] = (
            capo_service_catalog.types.access_level_filter.serialize_aws_json_1_1(
                value["access_level_filter"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListProvisionedProductPlansInput:
    out: ListProvisionedProductPlansInput = {}  # type: ignore[typeddict-item]
    if data.get("AcceptLanguage") is not None:
        out["accept_language"] = data["AcceptLanguage"]
    if data.get("ProvisionProductId") is not None:
        out["provision_product_id"] = data["ProvisionProductId"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    if data.get("AccessLevelFilter") is not None:
        import capo_service_catalog.types.access_level_filter

        out["access_level_filter"] = (
            capo_service_catalog.types.access_level_filter.deserialize_aws_json_1_1(
                data["AccessLevelFilter"]
            )
        )
    return out
