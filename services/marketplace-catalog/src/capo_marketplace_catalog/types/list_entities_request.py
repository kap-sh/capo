"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ListEntitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_catalog.types.catalog
    import capo_marketplace_catalog.types.entity_type
    import capo_marketplace_catalog.types.entity_type_filters
    import capo_marketplace_catalog.types.entity_type_sort
    import capo_marketplace_catalog.types.filter_list
    import capo_marketplace_catalog.types.list_entities_max_result_integer
    import capo_marketplace_catalog.types.next_token
    import capo_marketplace_catalog.types.ownership_type
    import capo_marketplace_catalog.types.sort


class ListEntitiesRequest(TypedDict, closed=True):
    catalog: "capo_marketplace_catalog.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    entity_type: "capo_marketplace_catalog.types.entity_type.EntityType"
    """<p>The type of entities to retrieve. Valid values are: <code>AmiProduct</code>, <code>ContainerProduct</code>, <code>DataProduct</code>, <code>SaaSProduct</code>, <code>ProcurementPolicy</code>, <code>Experience</code>, <code>Audience</code>, <code>BrandingSettings</code>, <code>Offer</code>, <code>OfferSet</code>, <code>Seller</code>, <code>ResaleAuthorization</code>, <code>Solution</code>.</p>"""
    filter_list: NotRequired["capo_marketplace_catalog.types.filter_list.FilterList"]
    """<p>An array of filter objects. Each filter object contains two attributes, <code>filterName</code> and <code>filterValues</code>.</p>"""
    sort: NotRequired["capo_marketplace_catalog.types.sort.Sort"]
    """<p>An object that contains two attributes, <code>SortBy</code> and <code>SortOrder</code>.</p>"""
    next_token: NotRequired["capo_marketplace_catalog.types.next_token.NextToken"]
    """<p>The value of the next token, if it exists. Null if there are no more results.</p>"""
    max_results: NotRequired[
        "capo_marketplace_catalog.types.list_entities_max_result_integer.ListEntitiesMaxResultInteger"
    ]
    """<p>Specifies the upper limit of the elements on a single page. If a value isn't provided, the default value is 20.</p>"""
    ownership_type: NotRequired[
        "capo_marketplace_catalog.types.ownership_type.OwnershipType"
    ]
    """<p>Filters the returned set of entities based on their owner. The default is <code>SELF</code>. To list entities shared with you through AWS Resource Access Manager (AWS RAM), set to <code>SHARED</code>. Entities shared through the AWS Marketplace Catalog API <code>PutResourcePolicy</code> operation can't be discovered through the <code>SHARED</code> parameter.</p>"""
    entity_type_filters: NotRequired[
        "capo_marketplace_catalog.types.entity_type_filters.EntityTypeFilters"
    ]
    """<p>A Union object containing filter shapes for all <code>EntityType</code>s. Each <code>EntityTypeFilter</code> shape will have filters applicable for that <code>EntityType</code> that can be used to search or filter entities.</p>"""
    entity_type_sort: NotRequired[
        "capo_marketplace_catalog.types.entity_type_sort.EntityTypeSort"
    ]
    """<p>A Union object containing <code>Sort</code> shapes for all <code>EntityType</code>s. Each <code>EntityTypeSort</code> shape will have <code>SortBy</code> and <code>SortOrder</code> applicable for fields on that <code>EntityType</code>. This can be used to sort the results of the filter query.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntitiesRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["EntityType"] = value["entity_type"]
    if "filter_list" in value:
        import capo_marketplace_catalog.types.filter_list

        out["FilterList"] = capo_marketplace_catalog.types.filter_list.serialize_json(
            value["filter_list"]
        )
    if "sort" in value:
        import capo_marketplace_catalog.types.sort

        out["Sort"] = capo_marketplace_catalog.types.sort.serialize_json(value["sort"])
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "ownership_type" in value:
        import capo_marketplace_catalog.types.ownership_type

        out["OwnershipType"] = (
            capo_marketplace_catalog.types.ownership_type.serialize_json(
                value["ownership_type"]
            )
        )
    if "entity_type_filters" in value:
        import capo_marketplace_catalog.types.entity_type_filters

        out["EntityTypeFilters"] = (
            capo_marketplace_catalog.types.entity_type_filters.serialize_json(
                value["entity_type_filters"]
            )
        )
    if "entity_type_sort" in value:
        import capo_marketplace_catalog.types.entity_type_sort

        out["EntityTypeSort"] = (
            capo_marketplace_catalog.types.entity_type_sort.serialize_json(
                value["entity_type_sort"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListEntitiesRequest:
    out: ListEntitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("EntityType") is not None:
        out["entity_type"] = data["EntityType"]
    else:
        out["entity_type"] = ""
    if data.get("FilterList") is not None:
        import capo_marketplace_catalog.types.filter_list

        out["filter_list"] = (
            capo_marketplace_catalog.types.filter_list.deserialize_json(
                data["FilterList"]
            )
        )
    if data.get("Sort") is not None:
        import capo_marketplace_catalog.types.sort

        out["sort"] = capo_marketplace_catalog.types.sort.deserialize_json(data["Sort"])
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("OwnershipType") is not None:
        import capo_marketplace_catalog.types.ownership_type

        out["ownership_type"] = (
            capo_marketplace_catalog.types.ownership_type.deserialize_json(
                data["OwnershipType"]
            )
        )
    if data.get("EntityTypeFilters") is not None:
        import capo_marketplace_catalog.types.entity_type_filters

        out["entity_type_filters"] = (
            capo_marketplace_catalog.types.entity_type_filters.deserialize_json(
                data["EntityTypeFilters"]
            )
        )
    if data.get("EntityTypeSort") is not None:
        import capo_marketplace_catalog.types.entity_type_sort

        out["entity_type_sort"] = (
            capo_marketplace_catalog.types.entity_type_sort.deserialize_json(
                data["EntityTypeSort"]
            )
        )
    return out
