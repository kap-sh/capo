"""Generated from Smithy shape ``com.amazonaws.acm#SearchCertificatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_acm.types.certificate_filter_statement
    import capo_acm.types.next_token
    import capo_acm.types.search_certificates_sort_by
    import capo_acm.types.search_certificates_sort_order
    import capo_acm.types.search_max_results


class SearchCertificatesRequest(TypedDict, closed=True):
    filter_statement: NotRequired[
        "capo_acm.types.certificate_filter_statement.CertificateFilterStatement"
    ]
    """<p>A filter statement that defines the search criteria. You can combine multiple filters using AND, OR, and NOT logical operators to create complex queries.</p>"""
    max_results: NotRequired["capo_acm.types.search_max_results.SearchMaxResults"]
    """<p>The maximum number of results to return in the response. Default is 100.</p>"""
    next_token: NotRequired["capo_acm.types.next_token.NextToken"]
    """<p>Use this parameter only when paginating results and only in a subsequent request after you receive a response with truncated results. Set it to the value of <code>NextToken</code> from the response you just received.</p>"""
    sort_by: NotRequired[
        "capo_acm.types.search_certificates_sort_by.SearchCertificatesSortBy"
    ]
    """<p>Specifies the field to sort results by. Valid values are CREATED_AT, NOT_AFTER, STATUS, RENEWAL_STATUS, EXPORTED, IN_USE, NOT_BEFORE, KEY_ALGORITHM, TYPE, CERTIFICATE_ARN, COMMON_NAME, REVOKED_AT, RENEWAL_ELIGIBILITY, ISSUED_AT, MANAGED_BY, EXPORT_OPTION, VALIDATION_METHOD, and IMPORTED_AT.</p>"""
    sort_order: NotRequired[
        "capo_acm.types.search_certificates_sort_order.SearchCertificatesSortOrder"
    ]
    """<p>Specifies the order of sorted results. Valid values are ASCENDING or DESCENDING.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchCertificatesRequest) -> dict:
    out: dict = {}
    if "filter_statement" in value:
        import capo_acm.types.certificate_filter_statement

        out["FilterStatement"] = (
            capo_acm.types.certificate_filter_statement.serialize_aws_json_1_1(
                value["filter_statement"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "sort_by" in value:
        import capo_acm.types.search_certificates_sort_by

        out["SortBy"] = (
            capo_acm.types.search_certificates_sort_by.serialize_aws_json_1_1(
                value["sort_by"]
            )
        )
    if "sort_order" in value:
        import capo_acm.types.search_certificates_sort_order

        out["SortOrder"] = (
            capo_acm.types.search_certificates_sort_order.serialize_aws_json_1_1(
                value["sort_order"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SearchCertificatesRequest:
    out: SearchCertificatesRequest = {}  # type: ignore[typeddict-item]
    if data.get("FilterStatement") is not None:
        import capo_acm.types.certificate_filter_statement

        out["filter_statement"] = (
            capo_acm.types.certificate_filter_statement.deserialize_aws_json_1_1(
                data["FilterStatement"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("SortBy") is not None:
        import capo_acm.types.search_certificates_sort_by

        out["sort_by"] = (
            capo_acm.types.search_certificates_sort_by.deserialize_aws_json_1_1(
                data["SortBy"]
            )
        )
    if data.get("SortOrder") is not None:
        import capo_acm.types.search_certificates_sort_order

        out["sort_order"] = (
            capo_acm.types.search_certificates_sort_order.deserialize_aws_json_1_1(
                data["SortOrder"]
            )
        )
    return out
