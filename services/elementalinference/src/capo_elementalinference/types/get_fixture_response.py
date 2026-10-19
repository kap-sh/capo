"""Generated from Smithy shape ``com.amazonaws.elementalinference#GetFixtureResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_elementalinference.types.competitor_list
    import capo_elementalinference.types.fixture_id


class GetFixtureResponse(TypedDict, closed=True):
    fixture_id: "capo_elementalinference.types.fixture_id.FixtureId"
    """<p>The ID that you specified in the request.</p>"""
    name: "str"
    """<p>The name of the fixture, as provided by the data source. For example, the names of the two competing teams. </p>"""
    fixture_group: NotRequired["str"]
    """<p>The group that the fixture belongs to, such as the competition, league, or tournament. The data source doesn't provide this information for every fixture. </p>"""
    scheduled_start: NotRequired["datetime.datetime"]
    """<p>The scheduled start time of the fixture, as provided by the data source. The actual start time might differ. </p>"""
    status: "str"
    """<p>The status of the fixture in its lifecycle, as provided by the data source. For example, Scheduled or Completed. </p>"""
    competitors: "capo_elementalinference.types.competitor_list.CompetitorList"
    """<p>An array of the competitors (the teams or individuals) in the fixture.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFixtureResponse) -> dict:
    out: dict = {}
    out["fixtureId"] = value["fixture_id"]
    out["name"] = value["name"]
    if "fixture_group" in value:
        out["fixtureGroup"] = value["fixture_group"]
    if "scheduled_start" in value:
        import capo_elementalinference._protocol.serialize

        out["scheduledStart"] = (
            capo_elementalinference._protocol.serialize.fmt_date_time(
                value["scheduled_start"]
            )
        )
    out["status"] = value["status"]
    import capo_elementalinference.types.competitor_list

    out["competitors"] = capo_elementalinference.types.competitor_list.serialize_json(
        value["competitors"]
    )
    return out


def deserialize_json(data: dict) -> GetFixtureResponse:
    out: GetFixtureResponse = {}  # type: ignore[typeddict-item]
    if data.get("fixtureId") is not None:
        out["fixture_id"] = data["fixtureId"]
    else:
        out["fixture_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("fixtureGroup") is not None:
        out["fixture_group"] = data["fixtureGroup"]
    if data.get("scheduledStart") is not None:
        import datetime

        out["scheduled_start"] = datetime.datetime.fromisoformat(
            data["scheduledStart"].replace("Z", "+00:00")
        )
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("competitors") is not None:
        import capo_elementalinference.types.competitor_list

        out["competitors"] = (
            capo_elementalinference.types.competitor_list.deserialize_json(
                data["competitors"]
            )
        )
    else:
        out["competitors"] = []
    return out
