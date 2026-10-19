"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetCostCategoriesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.cost_category_names_list
    import capo_cost_explorer.types.cost_category_values_list
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.page_size


class GetCostCategoriesResponse(TypedDict, closed=True):
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>If the number of objects that are still available for retrieval exceeds the quota, Amazon Web Services returns a NextPageToken value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    cost_category_names: NotRequired[
        "capo_cost_explorer.types.cost_category_names_list.CostCategoryNamesList"
    ]
    """<p>The names of the cost categories.</p>"""
    cost_category_values: NotRequired[
        "capo_cost_explorer.types.cost_category_values_list.CostCategoryValuesList"
    ]
    """<p>The cost category values.</p> <p>If the <code>CostCategoryName</code> key isn't specified in the request, the <code>CostCategoryValues</code> fields aren't returned. </p>"""
    return_size: "capo_cost_explorer.types.page_size.PageSize"
    """<p>The number of objects that are returned.</p>"""
    total_size: "capo_cost_explorer.types.page_size.PageSize"
    """<p>The total number of objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCostCategoriesResponse) -> dict:
    out: dict = {}
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "cost_category_names" in value:
        import capo_cost_explorer.types.cost_category_names_list

        out["CostCategoryNames"] = (
            capo_cost_explorer.types.cost_category_names_list.serialize_aws_json_1_1(
                value["cost_category_names"]
            )
        )
    if "cost_category_values" in value:
        import capo_cost_explorer.types.cost_category_values_list

        out["CostCategoryValues"] = (
            capo_cost_explorer.types.cost_category_values_list.serialize_aws_json_1_1(
                value["cost_category_values"]
            )
        )
    out["ReturnSize"] = value["return_size"]
    out["TotalSize"] = value["total_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCostCategoriesResponse:
    out: GetCostCategoriesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextPageToken") is not None:
        out["next_page_token"] = data["NextPageToken"]
    if data.get("CostCategoryNames") is not None:
        import capo_cost_explorer.types.cost_category_names_list

        out["cost_category_names"] = (
            capo_cost_explorer.types.cost_category_names_list.deserialize_aws_json_1_1(
                data["CostCategoryNames"]
            )
        )
    if data.get("CostCategoryValues") is not None:
        import capo_cost_explorer.types.cost_category_values_list

        out["cost_category_values"] = (
            capo_cost_explorer.types.cost_category_values_list.deserialize_aws_json_1_1(
                data["CostCategoryValues"]
            )
        )
    if data.get("ReturnSize") is not None:
        out["return_size"] = data["ReturnSize"]
    else:
        out["return_size"] = 0
    if data.get("TotalSize") is not None:
        out["total_size"] = data["TotalSize"]
    else:
        out["total_size"] = 0
    return out
