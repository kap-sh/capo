"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetSimilarProfilesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.match_type
    import capo_customer_profiles.types.max_size100
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.string1_to255
    import capo_customer_profiles.types.token


class GetSimilarProfilesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_customer_profiles.types.token.token"]
    """<p>The pagination token from the previous <code>GetSimilarProfiles</code> API call.</p>"""
    max_results: NotRequired["capo_customer_profiles.types.max_size100.maxSize100"]
    """<p>The maximum number of objects returned per page.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    match_type: "capo_customer_profiles.types.match_type.MatchType"
    """<p>Specify the type of matching to get similar profiles for.</p>"""
    search_key: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The string indicating the search key to be used.</p>"""
    search_value: "capo_customer_profiles.types.string1_to255.string1To255"
    """<p>The string based on <code>SearchKey</code> to be searched for similar profiles.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSimilarProfilesRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.match_type

    out["MatchType"] = capo_customer_profiles.types.match_type.serialize_json(
        value["match_type"]
    )
    out["SearchKey"] = value["search_key"]
    out["SearchValue"] = value["search_value"]
    return out


def deserialize_json(data: dict) -> GetSimilarProfilesRequest:
    out: GetSimilarProfilesRequest = {}  # type: ignore[typeddict-item]
    if data.get("MatchType") is not None:
        import capo_customer_profiles.types.match_type

        out["match_type"] = capo_customer_profiles.types.match_type.deserialize_json(
            data["MatchType"]
        )
    else:
        import typing

        out["match_type"] = typing.cast(
            "capo_customer_profiles.types.match_type.MatchType", ""
        )
    if data.get("SearchKey") is not None:
        out["search_key"] = data["SearchKey"]
    else:
        out["search_key"] = ""
    if data.get("SearchValue") is not None:
        out["search_value"] = data["SearchValue"]
    else:
        out["search_value"] = ""
    return out
