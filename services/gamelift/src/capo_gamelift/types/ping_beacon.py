"""Generated from Smithy shape ``com.amazonaws.gamelift#PingBeacon``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.udp_endpoint


class PingBeacon(TypedDict, closed=True):
    udp_endpoint: NotRequired["capo_gamelift.types.udp_endpoint.UDPEndpoint"]
    """<p>The domain name and port of the UDP ping beacon. Your game client can send UDP messages to this endpoint and receive responses to measure network latency.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PingBeacon) -> dict:
    out: dict = {}
    if "udp_endpoint" in value:
        import capo_gamelift.types.udp_endpoint

        out["UDPEndpoint"] = capo_gamelift.types.udp_endpoint.serialize_aws_json_1_1(
            value["udp_endpoint"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PingBeacon:
    out: PingBeacon = {}  # type: ignore[typeddict-item]
    if data.get("UDPEndpoint") is not None:
        import capo_gamelift.types.udp_endpoint

        out["udp_endpoint"] = capo_gamelift.types.udp_endpoint.deserialize_aws_json_1_1(
            data["UDPEndpoint"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PingBeacon) -> dict:
    out: dict = {}
    if "udp_endpoint" in value:
        import capo_gamelift.types.udp_endpoint

        out["UDPEndpoint"] = capo_gamelift.types.udp_endpoint.serialize_cbor(
            value["udp_endpoint"]
        )
    return out


def deserialize_cbor(data: dict) -> PingBeacon:
    out: PingBeacon = {}  # type: ignore[typeddict-item]
    if data.get("UDPEndpoint") is not None:
        import capo_gamelift.types.udp_endpoint

        out["udp_endpoint"] = capo_gamelift.types.udp_endpoint.deserialize_cbor(
            data["UDPEndpoint"]
        )
    return out
