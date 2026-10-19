"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#UpdateServerConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.server_id
    import capo_migrationhubstrategy.types.strategy_option


class UpdateServerConfigRequest(TypedDict, closed=True):
    server_id: "capo_migrationhubstrategy.types.server_id.ServerId"
    """<p> The ID of the server. </p>"""
    strategy_option: NotRequired[
        "capo_migrationhubstrategy.types.strategy_option.StrategyOption"
    ]
    """<p> The preferred strategy options for the application component. See the response from <a>GetServerStrategies</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServerConfigRequest) -> dict:
    out: dict = {}
    out["serverId"] = value["server_id"]
    if "strategy_option" in value:
        import capo_migrationhubstrategy.types.strategy_option

        out["strategyOption"] = (
            capo_migrationhubstrategy.types.strategy_option.serialize_json(
                value["strategy_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateServerConfigRequest:
    out: UpdateServerConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("serverId") is not None:
        out["server_id"] = data["serverId"]
    else:
        out["server_id"] = ""
    if data.get("strategyOption") is not None:
        import capo_migrationhubstrategy.types.strategy_option

        out["strategy_option"] = (
            capo_migrationhubstrategy.types.strategy_option.deserialize_json(
                data["strategyOption"]
            )
        )
    return out
