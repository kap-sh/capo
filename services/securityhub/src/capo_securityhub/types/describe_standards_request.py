"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeStandardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.standards_providers


class DescribeStandardsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>DescribeStandards</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of standards to return.</p>"""
    providers: NotRequired[
        "capo_securityhub.types.standards_providers.StandardsProviders"
    ]
    """<p>A list of cloud providers to filter the standards by. For example, specify <code>Azure</code> to return only standards that evaluate Azure resources, or <code>GCP</code> to return only standards that evaluate GCP resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStandardsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeStandardsRequest:
    out: DescribeStandardsRequest = {}  # type: ignore[typeddict-item]
    return out
