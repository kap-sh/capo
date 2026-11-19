"""Generated from Smithy shape ``com.amazonaws.lightsail#GetSubdomainsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.string
    import capo_lightsail.types.subdomain_list


class GetSubdomainsResult(TypedDict, closed=True):
    subdomains: NotRequired["capo_lightsail.types.subdomain_list.SubdomainList"]
    """<p>An array of objects that describe your subdomains.</p>"""
    next_page_token: NotRequired["capo_lightsail.types.string.string"]
    """<p>The token to advance to the next page of results from your request.</p> <p>A next page token is not returned if there are no more results to display.</p> <p>To get the next page of results, perform another <code>GetSubdomains</code> request and specify the next page token using the <code>pageToken</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSubdomainsResult) -> dict:
    out: dict = {}
    if "subdomains" in value:
        import capo_lightsail.types.subdomain_list

        out["subdomains"] = capo_lightsail.types.subdomain_list.serialize_aws_json_1_1(
            value["subdomains"]
        )
    if "next_page_token" in value:
        out["nextPageToken"] = value["next_page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSubdomainsResult:
    out: GetSubdomainsResult = {}  # type: ignore[typeddict-item]
    if data.get("subdomains") is not None:
        import capo_lightsail.types.subdomain_list

        out["subdomains"] = (
            capo_lightsail.types.subdomain_list.deserialize_aws_json_1_1(
                data["subdomains"]
            )
        )
    if data.get("nextPageToken") is not None:
        out["next_page_token"] = data["nextPageToken"]
    return out
