"""Generated from Smithy shape ``com.amazonaws.securitylake#ListDataLakeExceptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.max_results
    import capo_securitylake.types.next_token
    import capo_securitylake.types.region_list


class ListDataLakeExceptionsRequest(TypedDict, closed=True):
    regions: NotRequired["capo_securitylake.types.region_list.RegionList"]
    """<p>The Amazon Web Services Regions from which exceptions are retrieved.</p>"""
    max_results: NotRequired["capo_securitylake.types.max_results.MaxResults"]
    """<p>Lists the maximum number of failures in Security Lake.</p>"""
    next_token: NotRequired["capo_securitylake.types.next_token.NextToken"]
    """<p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return an HTTP 400 InvalidToken error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataLakeExceptionsRequest) -> dict:
    out: dict = {}
    if "regions" in value:
        import capo_securitylake.types.region_list

        out["regions"] = capo_securitylake.types.region_list.serialize_json(
            value["regions"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataLakeExceptionsRequest:
    out: ListDataLakeExceptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("regions") is not None:
        import capo_securitylake.types.region_list

        out["regions"] = capo_securitylake.types.region_list.deserialize_json(
            data["regions"]
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
