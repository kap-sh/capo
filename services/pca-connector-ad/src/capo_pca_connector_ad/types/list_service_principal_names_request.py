"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#ListServicePrincipalNamesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pca_connector_ad.types.directory_registration_arn
    import capo_pca_connector_ad.types.max_results
    import capo_pca_connector_ad.types.next_token


class ListServicePrincipalNamesRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_pca_connector_ad.types.max_results.MaxResults"]
    """<p>Use this parameter when paginating results to specify the maximum number of items to return in the response on each page. If additional items exist beyond the number you specify, the <code>NextToken</code> element is sent in the response. Use this <code>NextToken</code> value in a subsequent request to retrieve additional items.</p>"""
    next_token: NotRequired["capo_pca_connector_ad.types.next_token.NextToken"]
    """<p>Use this parameter when paginating results in a subsequent request after you receive a response with truncated results. Set it to the value of the <code>NextToken</code> parameter from the response you just received.</p>"""
    directory_registration_arn: "capo_pca_connector_ad.types.directory_registration_arn.DirectoryRegistrationArn"
    """<p>The Amazon Resource Name (ARN) that was returned when you called <a href="https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_CreateDirectoryRegistration.html">CreateDirectoryRegistration</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListServicePrincipalNamesRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListServicePrincipalNamesRequest:
    out: ListServicePrincipalNamesRequest = {}  # type: ignore[typeddict-item]
    return out
