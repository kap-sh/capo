"""Generated from Smithy shape ``com.amazonaws.elementalinference#DataSourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.fixture_id


class DataSourceConfiguration(TypedDict, closed=True):
    fixture_id: "capo_elementalinference.types.fixture_id.FixtureId"
    """<p>The ID of the fixture whose event data you want Elemental Inference to map onto this clipping output. The fixture should be the sports event in the source media that the feed is processing. </p> <p>To obtain this ID, use the SearchFixtures operation to find the fixture, then use the fixtureId from the matching FixtureSummary. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSourceConfiguration) -> dict:
    out: dict = {}
    out["fixtureId"] = value["fixture_id"]
    return out


def deserialize_json(data: dict) -> DataSourceConfiguration:
    out: DataSourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fixtureId") is not None:
        out["fixture_id"] = data["fixtureId"]
    else:
        out["fixture_id"] = ""
    return out
