"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerConnectionDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.max_string
    import capo_gamelift.types.player_connection_endpoint_list
    import capo_gamelift.types.player_id
    import capo_gamelift.types.timestamp


class PlayerConnectionDetail(TypedDict, closed=True):
    player_id: NotRequired["capo_gamelift.types.player_id.PlayerId"]
    """<p>A unique identifier for a player associated with this connection.</p>"""
    endpoints: NotRequired[
        "capo_gamelift.types.player_connection_endpoint_list.PlayerConnectionEndpointList"
    ]
    """<p>List of connection endpoints for the game client. Your game client uses these IP address(es) and port(s) to connect to the game session.</p> <p>When player gateway is enabled, these are relay endpoints with benefits such as DDoS protection. When disabled, this is the game server endpoint.</p>"""
    player_gateway_token: NotRequired["capo_gamelift.types.max_string.MaxString"]
    """<p>Access token that your game client must prepend to all traffic sent through player gateway. Player gateway verifies identity and authorizes connection based on this token.</p> <p>This value is empty when player gateway is disabled.</p>"""
    expiration: NotRequired["capo_gamelift.types.timestamp.Timestamp"]
    """<p>When player gateway is enabled, this is the timestamp indicating when player gateway token expires. Your game backend should call <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetPlayerConnectionDetails.html">GetPlayerConnectionDetails</a> to retrieve fresh connection information for your game clients before this time. Format is a number expressed in Unix time as milliseconds (for example <code>"1469498468.057"</code>). </p> <p>This value is empty when player gateway is disabled.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerConnectionDetail) -> dict:
    out: dict = {}
    if "player_id" in value:
        out["PlayerId"] = value["player_id"]
    if "endpoints" in value:
        import capo_gamelift.types.player_connection_endpoint_list

        out["Endpoints"] = (
            capo_gamelift.types.player_connection_endpoint_list.serialize_aws_json_1_1(
                value["endpoints"]
            )
        )
    if "player_gateway_token" in value:
        out["PlayerGatewayToken"] = value["player_gateway_token"]
    if "expiration" in value:
        import capo_gamelift.types.timestamp

        out["Expiration"] = capo_gamelift.types.timestamp.serialize_aws_json_1_1(
            value["expiration"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerConnectionDetail:
    out: PlayerConnectionDetail = {}  # type: ignore[typeddict-item]
    if data.get("PlayerId") is not None:
        out["player_id"] = data["PlayerId"]
    if data.get("Endpoints") is not None:
        import capo_gamelift.types.player_connection_endpoint_list

        out["endpoints"] = (
            capo_gamelift.types.player_connection_endpoint_list.deserialize_aws_json_1_1(
                data["Endpoints"]
            )
        )
    if data.get("PlayerGatewayToken") is not None:
        out["player_gateway_token"] = data["PlayerGatewayToken"]
    if data.get("Expiration") is not None:
        import capo_gamelift.types.timestamp

        out["expiration"] = capo_gamelift.types.timestamp.deserialize_aws_json_1_1(
            data["Expiration"]
        )
    return out
