"""Generated from Smithy shape ``com.amazonaws.elementalinference#SearchFixturesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.data_source_sport
    import capo_elementalinference.types.fixture_date
    import capo_elementalinference.types.search_filter_list


class SearchFixturesRequest(TypedDict, closed=True):
    sport: "capo_elementalinference.types.data_source_sport.DataSourceSport"
    """<p>The sport to search for fixtures. Valid values: basketball (search for basketball fixtures), american-football (search for american-football fixtures). </p>"""
    start_date: "capo_elementalinference.types.fixture_date.FixtureDate"
    """<p>The first day of the search window, in UTC. The search includes fixtures that are scheduled on this day. </p> <p>Specify the date in ISO 8601 format, as <code>YYYY-MM-DD</code>. For example, 2026-03-14. </p>"""
    end_date: NotRequired["capo_elementalinference.types.fixture_date.FixtureDate"]
    """<p>The last day of the search window, in UTC. The search includes fixtures that are scheduled on this day. Specify the date in ISO 8601 format, as <code>YYYY-MM-DD</code>. </p> <p>If you omit this parameter, Elemental Inference searches only the day that you specified in startDate. The window from startDate through endDate must not exceed seven days. </p>"""
    filters: NotRequired[
        "capo_elementalinference.types.search_filter_list.SearchFilterList"
    ]
    """<p>An array of filters that narrow the results. Each filter applies to one dimension of a fixture, such as the competitor. You can specify up to 10 filters. </p> <p>A fixture must satisfy every filter in the array in order to appear in the results. Within one filter, a fixture must match at least one of the values. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of fixtures to return for each API request.</p> <p>The service might return fewer fixtures than the maxResults value. When more fixtures match the search, the response also includes a nextToken value that you can use to fetch the next batch of results. </p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the batch of results that you want to see.</p> <p>For example, you submit a SearchFixtures request with maxResults set at 5. The service returns the first batch of results (up to 5) and a nextToken value. To see the next batch of results, you submit the SearchFixtures request a second time, with the same search criteria, and specify the nextToken value. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFixturesRequest) -> dict:
    out: dict = {}
    import capo_elementalinference.types.data_source_sport

    out["sport"] = capo_elementalinference.types.data_source_sport.serialize_json(
        value["sport"]
    )
    out["startDate"] = value["start_date"]
    if "end_date" in value:
        out["endDate"] = value["end_date"]
    if "filters" in value:
        import capo_elementalinference.types.search_filter_list

        out["filters"] = (
            capo_elementalinference.types.search_filter_list.serialize_json(
                value["filters"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchFixturesRequest:
    out: SearchFixturesRequest = {}  # type: ignore[typeddict-item]
    if data.get("sport") is not None:
        import capo_elementalinference.types.data_source_sport

        out["sport"] = capo_elementalinference.types.data_source_sport.deserialize_json(
            data["sport"]
        )
    else:
        import typing

        out["sport"] = typing.cast(
            "capo_elementalinference.types.data_source_sport.DataSourceSport", ""
        )
    if data.get("startDate") is not None:
        out["start_date"] = data["startDate"]
    else:
        out["start_date"] = ""
    if data.get("endDate") is not None:
        out["end_date"] = data["endDate"]
    if data.get("filters") is not None:
        import capo_elementalinference.types.search_filter_list

        out["filters"] = (
            capo_elementalinference.types.search_filter_list.deserialize_json(
                data["filters"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
