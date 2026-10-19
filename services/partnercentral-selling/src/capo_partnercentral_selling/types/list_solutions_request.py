"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListSolutionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_marketplace_solution_arn_list
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.filter_status
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.solution_identifiers
    import capo_partnercentral_selling.types.solution_sort
    import capo_partnercentral_selling.types.string_list


class ListSolutionsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the solutions are listed in. Use <code>AWS</code> to list solutions in the Amazon Web Services catalog, and <code>Sandbox</code> to list solutions in a secure and isolated testing environment.</p>"""
    max_results: NotRequired["capo_partnercentral_selling.types.page_size.PageSize"]
    """<p>The maximum number of results returned by a single call. This value must be provided in the next call to retrieve the next set of results.</p> <p>Default: 20</p>"""
    next_token: NotRequired["str"]
    """<p>A pagination token used to retrieve the next set of results in subsequent calls. This token is included in the response only if there are additional result pages available.</p>"""
    sort: NotRequired["capo_partnercentral_selling.types.solution_sort.SolutionSort"]
    """<p>Object that configures sorting done on the response. Default <code>Sort.SortBy</code> is <code>Identifier</code>.</p>"""
    status: NotRequired["capo_partnercentral_selling.types.filter_status.FilterStatus"]
    """<p>Filters solutions based on their status. This filter helps partners manage their solution portfolios effectively.</p>"""
    identifier: NotRequired[
        "capo_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
    ]
    """<p>Filters the solutions based on their unique identifier. Use this filter to retrieve specific solutions by providing the solution's identifier for accurate results.</p>"""
    category: NotRequired["capo_partnercentral_selling.types.string_list.StringList"]
    """<p>Filters the solutions based on the category to which they belong. This allows partners to search for solutions within specific categories, such as <code>Software</code>, <code>Consulting</code>, or <code>Managed Services</code>.</p>"""
    aws_marketplace_solution_arn: NotRequired[
        "capo_partnercentral_selling.types.aws_marketplace_solution_arn_list.AwsMarketplaceSolutionArnList"
    ]
    """<p>Filters results by AWS Marketplace solution ARN. You can provide up to 10 ARNs.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListSolutionsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort" in value:
        import capo_partnercentral_selling.types.solution_sort

        out["Sort"] = (
            capo_partnercentral_selling.types.solution_sort.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    if "status" in value:
        import capo_partnercentral_selling.types.filter_status

        out["Status"] = (
            capo_partnercentral_selling.types.filter_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "identifier" in value:
        import capo_partnercentral_selling.types.solution_identifiers

        out["Identifier"] = (
            capo_partnercentral_selling.types.solution_identifiers.serialize_aws_json_1_0(
                value["identifier"]
            )
        )
    if "category" in value:
        import capo_partnercentral_selling.types.string_list

        out["Category"] = (
            capo_partnercentral_selling.types.string_list.serialize_aws_json_1_0(
                value["category"]
            )
        )
    if "aws_marketplace_solution_arn" in value:
        import capo_partnercentral_selling.types.aws_marketplace_solution_arn_list

        out["AwsMarketplaceSolutionArn"] = (
            capo_partnercentral_selling.types.aws_marketplace_solution_arn_list.serialize_aws_json_1_0(
                value["aws_marketplace_solution_arn"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListSolutionsRequest:
    out: ListSolutionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Sort") is not None:
        import capo_partnercentral_selling.types.solution_sort

        out["sort"] = (
            capo_partnercentral_selling.types.solution_sort.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    if data.get("Status") is not None:
        import capo_partnercentral_selling.types.filter_status

        out["status"] = (
            capo_partnercentral_selling.types.filter_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("Identifier") is not None:
        import capo_partnercentral_selling.types.solution_identifiers

        out["identifier"] = (
            capo_partnercentral_selling.types.solution_identifiers.deserialize_aws_json_1_0(
                data["Identifier"]
            )
        )
    if data.get("Category") is not None:
        import capo_partnercentral_selling.types.string_list

        out["category"] = (
            capo_partnercentral_selling.types.string_list.deserialize_aws_json_1_0(
                data["Category"]
            )
        )
    if data.get("AwsMarketplaceSolutionArn") is not None:
        import capo_partnercentral_selling.types.aws_marketplace_solution_arn_list

        out["aws_marketplace_solution_arn"] = (
            capo_partnercentral_selling.types.aws_marketplace_solution_arn_list.deserialize_aws_json_1_0(
                data["AwsMarketplaceSolutionArn"]
            )
        )
    return out
