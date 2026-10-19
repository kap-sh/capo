"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListResourcesForTagOptionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.page_size
    import capo_service_catalog.types.page_token
    import capo_service_catalog.types.resource_type
    import capo_service_catalog.types.tag_option_id


class ListResourcesForTagOptionInput(TypedDict, closed=True):
    tag_option_id: "capo_service_catalog.types.tag_option_id.TagOptionId"
    """<p>The TagOption identifier.</p>"""
    resource_type: NotRequired["capo_service_catalog.types.resource_type.ResourceType"]
    """<p>The resource type.</p> <ul> <li> <p> <code>Portfolio</code> </p> </li> <li> <p> <code>Product</code> </p> </li> </ul>"""
    page_size: NotRequired["capo_service_catalog.types.page_size.PageSize"]
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["capo_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourcesForTagOptionInput) -> dict:
    out: dict = {}
    out["TagOptionId"] = value["tag_option_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourcesForTagOptionInput:
    out: ListResourcesForTagOptionInput = {}  # type: ignore[typeddict-item]
    if data.get("TagOptionId") is not None:
        out["tag_option_id"] = data["TagOptionId"]
    else:
        raise DeserializationError(
            "ListResourcesForTagOptionInput.tag_option_id required"
        )
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("PageSize") is not None:
        out["page_size"] = data["PageSize"]
    if data.get("PageToken") is not None:
        out["page_token"] = data["PageToken"]
    return out
