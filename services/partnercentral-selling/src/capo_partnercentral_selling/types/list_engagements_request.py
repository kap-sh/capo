"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListEngagementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account_list
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.engagement_context_type_list
    import capo_partnercentral_selling.types.engagement_identifiers
    import capo_partnercentral_selling.types.engagement_page_size
    import capo_partnercentral_selling.types.engagement_sort


class ListEngagementsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog related to the request. </p>"""
    created_by: NotRequired[
        "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
    ]
    """<p> A list of AWS account IDs. When specified, the response includes engagements created by these accounts. This filter is useful for finding engagements created by specific team members. </p>"""
    exclude_created_by: NotRequired[
        "capo_partnercentral_selling.types.aws_account_list.AwsAccountList"
    ]
    """<p>An array of strings representing AWS Account IDs. Use this to exclude engagements created by specific users. </p>"""
    context_types: NotRequired[
        "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
    ]
    """<p>Filters engagements to include only those containing the specified context types, such as "CustomerProject" or "Lead". Use this to find engagements that have specific types of contextual information associated with them.</p>"""
    exclude_context_types: NotRequired[
        "capo_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
    ]
    """<p>Filters engagements to exclude those containing the specified context types. Use this to find engagements that do not have certain types of contextual information, helping to narrow results based on context exclusion criteria.</p>"""
    sort: NotRequired[
        "capo_partnercentral_selling.types.engagement_sort.EngagementSort"
    ]
    max_results: (
        "capo_partnercentral_selling.types.engagement_page_size.EngagementPageSize"
    )
    """<p>The maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. This value is returned from a previous call.</p>"""
    engagement_identifier: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifiers.EngagementIdentifiers"
    ]
    """<p>An array of strings representing engagement identifiers to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEngagementsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "created_by" in value:
        import capo_partnercentral_selling.types.aws_account_list

        out["CreatedBy"] = (
            capo_partnercentral_selling.types.aws_account_list.serialize_aws_json_1_0(
                value["created_by"]
            )
        )
    if "exclude_created_by" in value:
        import capo_partnercentral_selling.types.aws_account_list

        out["ExcludeCreatedBy"] = (
            capo_partnercentral_selling.types.aws_account_list.serialize_aws_json_1_0(
                value["exclude_created_by"]
            )
        )
    if "context_types" in value:
        import capo_partnercentral_selling.types.engagement_context_type_list

        out["ContextTypes"] = (
            capo_partnercentral_selling.types.engagement_context_type_list.serialize_aws_json_1_0(
                value["context_types"]
            )
        )
    if "exclude_context_types" in value:
        import capo_partnercentral_selling.types.engagement_context_type_list

        out["ExcludeContextTypes"] = (
            capo_partnercentral_selling.types.engagement_context_type_list.serialize_aws_json_1_0(
                value["exclude_context_types"]
            )
        )
    if "sort" in value:
        import capo_partnercentral_selling.types.engagement_sort

        out["Sort"] = (
            capo_partnercentral_selling.types.engagement_sort.serialize_aws_json_1_0(
                value["sort"]
            )
        )
    out["MaxResults"] = value.get("max_results", 20)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "engagement_identifier" in value:
        import capo_partnercentral_selling.types.engagement_identifiers

        out["EngagementIdentifier"] = (
            capo_partnercentral_selling.types.engagement_identifiers.serialize_aws_json_1_0(
                value["engagement_identifier"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEngagementsRequest:
    out: ListEngagementsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListEngagementsRequest.catalog required")
    if data.get("CreatedBy") is not None:
        import capo_partnercentral_selling.types.aws_account_list

        out["created_by"] = (
            capo_partnercentral_selling.types.aws_account_list.deserialize_aws_json_1_0(
                data["CreatedBy"]
            )
        )
    if data.get("ExcludeCreatedBy") is not None:
        import capo_partnercentral_selling.types.aws_account_list

        out["exclude_created_by"] = (
            capo_partnercentral_selling.types.aws_account_list.deserialize_aws_json_1_0(
                data["ExcludeCreatedBy"]
            )
        )
    if data.get("ContextTypes") is not None:
        import capo_partnercentral_selling.types.engagement_context_type_list

        out["context_types"] = (
            capo_partnercentral_selling.types.engagement_context_type_list.deserialize_aws_json_1_0(
                data["ContextTypes"]
            )
        )
    if data.get("ExcludeContextTypes") is not None:
        import capo_partnercentral_selling.types.engagement_context_type_list

        out["exclude_context_types"] = (
            capo_partnercentral_selling.types.engagement_context_type_list.deserialize_aws_json_1_0(
                data["ExcludeContextTypes"]
            )
        )
    if data.get("Sort") is not None:
        import capo_partnercentral_selling.types.engagement_sort

        out["sort"] = (
            capo_partnercentral_selling.types.engagement_sort.deserialize_aws_json_1_0(
                data["Sort"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 20
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("EngagementIdentifier") is not None:
        import capo_partnercentral_selling.types.engagement_identifiers

        out["engagement_identifier"] = (
            capo_partnercentral_selling.types.engagement_identifiers.deserialize_aws_json_1_0(
                data["EngagementIdentifier"]
            )
        )
    return out
