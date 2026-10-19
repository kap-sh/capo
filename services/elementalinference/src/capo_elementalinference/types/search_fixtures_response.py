"""Generated from Smithy shape ``com.amazonaws.elementalinference#SearchFixturesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.fixture_summary_list


class SearchFixturesResponse(TypedDict, closed=True):
    fixtures: "capo_elementalinference.types.fixture_summary_list.FixtureSummaryList"
    """<p>An array of FixtureSummary objects, one for each fixture that matches the search. The array is empty if no fixtures match. </p>"""
    next_token: NotRequired["str"]
    """<p>The token that identifies the next batch of results. To see the next batch, submit the SearchFixtures request again, with the same search criteria, and specify this value in nextToken. </p> <p>This parameter is absent when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchFixturesResponse) -> dict:
    out: dict = {}
    import capo_elementalinference.types.fixture_summary_list

    out["fixtures"] = capo_elementalinference.types.fixture_summary_list.serialize_json(
        value["fixtures"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchFixturesResponse:
    out: SearchFixturesResponse = {}  # type: ignore[typeddict-item]
    if data.get("fixtures") is not None:
        import capo_elementalinference.types.fixture_summary_list

        out["fixtures"] = (
            capo_elementalinference.types.fixture_summary_list.deserialize_json(
                data["fixtures"]
            )
        )
    else:
        out["fixtures"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
