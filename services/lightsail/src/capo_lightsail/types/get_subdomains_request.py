"""Generated from Smithy shape ``com.amazonaws.lightsail#GetSubdomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string


class GetSubdomainsRequest(TypedDict, closed=True):
    subdomain_name: NotRequired["capo_lightsail.types.string.string"]
    """<p>The subdomain for which to return information (for example, <code>mysite</code> or <code>blog.mysite</code>), not its web address.</p> <p>When omitted, the response includes all of your subdomains.</p> <p>You can't specify this parameter together with the <code>pageToken</code> parameter.</p>"""
    page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>To get a page token, perform an initial <code>GetSubdomains</code> request. If your results are paginated, the response will return a next page token that you can specify as the page token in a subsequent request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSubdomainsRequest) -> dict:
    out: dict = {}
    if "subdomain_name" in value:
        out["subdomainName"] = value["subdomain_name"]
    if "page_token" in value:
        out["pageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSubdomainsRequest:
    out: GetSubdomainsRequest = {}  # type: ignore[typeddict-item]
    if data.get("subdomainName") is not None:
        out["subdomain_name"] = data["subdomainName"]
    if data.get("pageToken") is not None:
        out["page_token"] = data["pageToken"]
    return out
