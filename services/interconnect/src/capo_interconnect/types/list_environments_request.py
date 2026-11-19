"""Generated from Smithy shape ``com.amazonaws.interconnect#ListEnvironmentsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_interconnect.types.location
    import capo_interconnect.types.max_results
    import capo_interconnect.types.next_token
    import capo_interconnect.types.provider


class ListEnvironmentsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_interconnect.types.max_results.MaxResults"]
    """<p>The max number of list results in a single paginated response.</p>"""
    next_token: NotRequired["capo_interconnect.types.next_token.NextToken"]
    """<p>A pagination token from a previous paginated response indicating you wish to get the next page of results.</p>"""
    provider: NotRequired["capo_interconnect.types.provider.Provider"]
    """<p>Filter results to only include <a>Environment</a> objects that connect to the <a>Provider</a>.</p>"""
    location: NotRequired["capo_interconnect.types.location.Location"]
    """<p>Filter results to only include <a>Environment</a> objects that connect to a given location distiguisher.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "provider" in value:
        import capo_interconnect.types.provider

        out["provider"] = capo_interconnect.types.provider.serialize_aws_json_1_0(
            value["provider"]
        )
    if "location" in value:
        out["location"] = value["location"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentsRequest:
    out: ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("provider") is not None:
        import capo_interconnect.types.provider

        out["provider"] = capo_interconnect.types.provider.deserialize_aws_json_1_0(
            data["provider"]
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListEnvironmentsRequest) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "provider" in value:
        import capo_interconnect.types.provider

        out["provider"] = capo_interconnect.types.provider.serialize_cbor(
            value["provider"]
        )
    if "location" in value:
        out["location"] = value["location"]
    return out


def deserialize_cbor(data: dict) -> ListEnvironmentsRequest:
    out: ListEnvironmentsRequest = {}  # type: ignore[typeddict-item]
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("provider") is not None:
        import capo_interconnect.types.provider

        out["provider"] = capo_interconnect.types.provider.deserialize_cbor(
            data["provider"]
        )
    if data.get("location") is not None:
        out["location"] = data["location"]
    return out
