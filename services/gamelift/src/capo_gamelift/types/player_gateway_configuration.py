"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerGatewayConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.game_server_ip_protocol_supported


class PlayerGatewayConfiguration(TypedDict, closed=True):
    game_server_ip_protocol_supported: NotRequired[
        "capo_gamelift.types.game_server_ip_protocol_supported.GameServerIpProtocolSupported"
    ]
    """<p>The IP protocol that your game servers support for player connections through player gateway. If the value is set to <code>IPv4</code>, GameLift will install and execute a lightweight IP translation software on fleet instances to receive and transform incoming IPv6 traffic to IPv4. If the value is set to <code>DUAL_STACK</code>, the lightweight IP translation software will not be installed on fleet instances. <code>DUAL_STACK</code> provides slightly better performance than <code>IPv4</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerGatewayConfiguration) -> dict:
    out: dict = {}
    if "game_server_ip_protocol_supported" in value:
        import capo_gamelift.types.game_server_ip_protocol_supported

        out["GameServerIpProtocolSupported"] = (
            capo_gamelift.types.game_server_ip_protocol_supported.serialize_aws_json_1_1(
                value["game_server_ip_protocol_supported"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerGatewayConfiguration:
    out: PlayerGatewayConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("GameServerIpProtocolSupported") is not None:
        import capo_gamelift.types.game_server_ip_protocol_supported

        out["game_server_ip_protocol_supported"] = (
            capo_gamelift.types.game_server_ip_protocol_supported.deserialize_aws_json_1_1(
                data["GameServerIpProtocolSupported"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PlayerGatewayConfiguration) -> dict:
    out: dict = {}
    if "game_server_ip_protocol_supported" in value:
        import capo_gamelift.types.game_server_ip_protocol_supported

        out["GameServerIpProtocolSupported"] = (
            capo_gamelift.types.game_server_ip_protocol_supported.serialize_cbor(
                value["game_server_ip_protocol_supported"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> PlayerGatewayConfiguration:
    out: PlayerGatewayConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("GameServerIpProtocolSupported") is not None:
        import capo_gamelift.types.game_server_ip_protocol_supported

        out["game_server_ip_protocol_supported"] = (
            capo_gamelift.types.game_server_ip_protocol_supported.deserialize_cbor(
                data["GameServerIpProtocolSupported"]
            )
        )
    return out
