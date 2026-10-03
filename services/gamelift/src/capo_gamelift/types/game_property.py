"""Generated from Smithy shape ``com.amazonaws.gamelift#GameProperty``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_property_key
    import capo_gamelift.types.game_property_value


class GameProperty(TypedDict, closed=True):
    key: NotRequired["capo_gamelift.types.game_property_key.GamePropertyKey"]
    """<p>The game property identifier.</p> <note> <ul> <li> <p>Avoid using periods (".") in property keys if you plan to search for game sessions by properties. Property keys containing periods cannot be searched and will be filtered out from search results due to search index limitations.</p> </li> <li> <p>If you use SearchGameSessions API, there is a limit of 500 game property keys across all game sessions and all fleets per region. If the limit is exceeded, there will potentially be game session entries missing from SearchGameSessions API results.</p> </li> </ul> </note>"""
    value: NotRequired["capo_gamelift.types.game_property_value.GamePropertyValue"]
    """<p>The game property value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GameProperty) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GameProperty:
    out: GameProperty = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    return out
