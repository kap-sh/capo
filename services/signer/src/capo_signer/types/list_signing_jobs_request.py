"""Generated from Smithy shape ``com.amazonaws.signer#ListSigningJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.account_id
    import capo_signer.types.bool
    import capo_signer.types.max_results
    import capo_signer.types.next_token
    import capo_signer.types.platform_id
    import capo_signer.types.requested_by
    import capo_signer.types.signing_status
    import capo_signer.types.timestamp


class ListSigningJobsRequest(TypedDict, closed=True):
    status: NotRequired["capo_signer.types.signing_status.SigningStatus"]
    """<p>A status value with which to filter your results.</p>"""
    platform_id: NotRequired["capo_signer.types.platform_id.PlatformId"]
    """<p>The ID of microcontroller platform that you specified for the distribution of your code image.</p>"""
    requested_by: NotRequired["capo_signer.types.requested_by.RequestedBy"]
    """<p>The IAM principal that requested the signing job.</p>"""
    max_results: NotRequired["capo_signer.types.max_results.MaxResults"]
    """<p>Specifies the maximum number of items to return in the response. Use this parameter when paginating results. If additional items exist beyond the number you specify, the <code>nextToken</code> element is set in the response. Use the <code>nextToken</code> value in a subsequent request to retrieve additional items. </p>"""
    next_token: NotRequired["capo_signer.types.next_token.NextToken"]
    """<p>String for specifying the next set of paginated results to return. After you receive a response with truncated results, use this parameter in a subsequent request. Set it to the value of <code>nextToken</code> from the response that you just received.</p>"""
    is_revoked: NotRequired["capo_signer.types.bool.bool"]
    """<p>Filters results to return only signing jobs with revoked signatures.</p>"""
    signature_expires_before: NotRequired["capo_signer.types.timestamp.Timestamp"]
    """<p>Filters results to return only signing jobs with signatures expiring before a specified timestamp.</p>"""
    signature_expires_after: NotRequired["capo_signer.types.timestamp.Timestamp"]
    """<p>Filters results to return only signing jobs with signatures expiring after a specified timestamp.</p>"""
    job_invoker: NotRequired["capo_signer.types.account_id.AccountId"]
    """<p>Filters results to return only signing jobs initiated by a specified IAM entity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSigningJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListSigningJobsRequest:
    out: ListSigningJobsRequest = {}  # type: ignore[typeddict-item]
    return out
