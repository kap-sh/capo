"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListOpportunitiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.created_date_filter
    import capo_partnercentral_selling.types.filter_identifier
    import capo_partnercentral_selling.types.filter_life_cycle_review_status
    import capo_partnercentral_selling.types.filter_life_cycle_stage
    import capo_partnercentral_selling.types.last_modified_date
    import capo_partnercentral_selling.types.opportunity_sort
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.string_list
    import capo_partnercentral_selling.types.target_close_date_filter


class ListOpportunitiesRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunities are listed in. Use <code>AWS</code> for listing real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>"""
    max_results: NotRequired["capo_partnercentral_selling.types.page_size.PageSize"]
    """<p>Specifies the maximum number of results to return in a single call. This limits the number of opportunities returned in the response to avoid providing too many results at once.</p> <p>Default: 20</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>"""
    sort: NotRequired[
        "capo_partnercentral_selling.types.opportunity_sort.OpportunitySort"
    ]
    """<p>An object that specifies how the response is sorted. The default <code>Sort.SortBy</code> value is <code>LastModifiedDate</code>.</p>"""
    last_modified_date: NotRequired[
        "capo_partnercentral_selling.types.last_modified_date.LastModifiedDate"
    ]
    """<p>Filters the opportunities based on their last modified date. This filter helps retrieve opportunities that were updated after the specified date, allowing partners to track recent changes or updates.</p>"""
    identifier: NotRequired[
        "capo_partnercentral_selling.types.filter_identifier.FilterIdentifier"
    ]
    """<p>Filters the opportunities based on the opportunity identifier. This allows partners to retrieve specific opportunities by providing their unique identifiers, ensuring precise results.</p>"""
    life_cycle_stage: NotRequired[
        "capo_partnercentral_selling.types.filter_life_cycle_stage.FilterLifeCycleStage"
    ]
    """<p>Filters the opportunities based on their lifecycle stage. This filter allows partners to retrieve opportunities at various stages in the sales cycle, such as <code>Qualified</code>, <code>Technical Validation</code>, <code>Business Validation</code>, or <code>Closed Won</code>.</p>"""
    life_cycle_review_status: NotRequired[
        "capo_partnercentral_selling.types.filter_life_cycle_review_status.FilterLifeCycleReviewStatus"
    ]
    """<p>Filters the opportunities based on their current lifecycle approval status. Use this filter to retrieve opportunities with statuses such as <code>Pending Submission</code>, <code>In Review</code>, <code>Action Required</code>, or <code>Approved</code>.</p>"""
    customer_company_name: NotRequired[
        "capo_partnercentral_selling.types.string_list.StringList"
    ]
    """<p>Filters the opportunities based on the customer's company name. This allows partners to search for opportunities associated with a specific customer by matching the provided company name string.</p>"""
    created_date: NotRequired[
        "capo_partnercentral_selling.types.created_date_filter.CreatedDateFilter"
    ]
    """<p>Filter opportunities by creation date criteria.</p>"""
    target_close_date: NotRequired[
        "capo_partnercentral_selling.types.target_close_date_filter.TargetCloseDateFilter"
    ]
    """<p>Filters opportunities based on their target close date. This filter helps retrieve opportunities with an expected close date before or after a specified date.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListOpportunitiesRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort" in value:
        import capo_partnercentral_selling.types.opportunity_sort

        out["Sort"] = (
            capo_partnercentral_selling.types.opportunity_sort.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    if "last_modified_date" in value:
        import capo_partnercentral_selling.types.last_modified_date

        out["LastModifiedDate"] = (
            capo_partnercentral_selling.types.last_modified_date.serialize_aws_json_1_0(
                value["last_modified_date"]
            )
        )
    if "identifier" in value:
        import capo_partnercentral_selling.types.filter_identifier

        out["Identifier"] = (
            capo_partnercentral_selling.types.filter_identifier.serialize_aws_json_1_0(
                value["identifier"]
            )
        )
    if "life_cycle_stage" in value:
        import capo_partnercentral_selling.types.filter_life_cycle_stage

        out["LifeCycleStage"] = (
            capo_partnercentral_selling.types.filter_life_cycle_stage.serialize_aws_json_1_0(
                value["life_cycle_stage"]
            )
        )
    if "life_cycle_review_status" in value:
        import capo_partnercentral_selling.types.filter_life_cycle_review_status

        out["LifeCycleReviewStatus"] = (
            capo_partnercentral_selling.types.filter_life_cycle_review_status.serialize_aws_json_1_0(
                value["life_cycle_review_status"]
            )
        )
    if "customer_company_name" in value:
        import capo_partnercentral_selling.types.string_list

        out["CustomerCompanyName"] = (
            capo_partnercentral_selling.types.string_list.serialize_aws_json_1_0(
                value["customer_company_name"]
            )
        )
    if "created_date" in value:
        import capo_partnercentral_selling.types.created_date_filter

        out["CreatedDate"] = (
            capo_partnercentral_selling.types.created_date_filter.serialize_aws_json_1_0(
                value["created_date"]
            )
        )
    if "target_close_date" in value:
        import capo_partnercentral_selling.types.target_close_date_filter

        out["TargetCloseDate"] = (
            capo_partnercentral_selling.types.target_close_date_filter.serialize_aws_json_1_0(
                value["target_close_date"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListOpportunitiesRequest:
    out: ListOpportunitiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Sort") is not None:
        import capo_partnercentral_selling.types.opportunity_sort

        out["sort"] = (
            capo_partnercentral_selling.types.opportunity_sort.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    if data.get("LastModifiedDate") is not None:
        import capo_partnercentral_selling.types.last_modified_date

        out["last_modified_date"] = (
            capo_partnercentral_selling.types.last_modified_date.deserialize_aws_json_1_0(
                data["LastModifiedDate"]
            )
        )
    if data.get("Identifier") is not None:
        import capo_partnercentral_selling.types.filter_identifier

        out["identifier"] = (
            capo_partnercentral_selling.types.filter_identifier.deserialize_aws_json_1_0(
                data["Identifier"]
            )
        )
    if data.get("LifeCycleStage") is not None:
        import capo_partnercentral_selling.types.filter_life_cycle_stage

        out["life_cycle_stage"] = (
            capo_partnercentral_selling.types.filter_life_cycle_stage.deserialize_aws_json_1_0(
                data["LifeCycleStage"]
            )
        )
    if data.get("LifeCycleReviewStatus") is not None:
        import capo_partnercentral_selling.types.filter_life_cycle_review_status

        out["life_cycle_review_status"] = (
            capo_partnercentral_selling.types.filter_life_cycle_review_status.deserialize_aws_json_1_0(
                data["LifeCycleReviewStatus"]
            )
        )
    if data.get("CustomerCompanyName") is not None:
        import capo_partnercentral_selling.types.string_list

        out["customer_company_name"] = (
            capo_partnercentral_selling.types.string_list.deserialize_aws_json_1_0(
                data["CustomerCompanyName"]
            )
        )
    if data.get("CreatedDate") is not None:
        import capo_partnercentral_selling.types.created_date_filter

        out["created_date"] = (
            capo_partnercentral_selling.types.created_date_filter.deserialize_aws_json_1_0(
                data["CreatedDate"]
            )
        )
    if data.get("TargetCloseDate") is not None:
        import capo_partnercentral_selling.types.target_close_date_filter

        out["target_close_date"] = (
            capo_partnercentral_selling.types.target_close_date_filter.deserialize_aws_json_1_0(
                data["TargetCloseDate"]
            )
        )
    return out
