"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#AcceptChannelHandshakeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.catalog
    import capo_partnercentral_channel.types.channel_handshake_identifier


class AcceptChannelHandshakeRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_channel.types.catalog.Catalog"
    """<p>The catalog identifier for the handshake request.</p>"""
    identifier: "capo_partnercentral_channel.types.channel_handshake_identifier.ChannelHandshakeIdentifier"
    """<p>The unique identifier of the channel handshake to accept.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptChannelHandshakeRequest) -> dict:
    out: dict = {}
    out["catalog"] = value["catalog"]
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptChannelHandshakeRequest:
    out: AcceptChannelHandshakeRequest = {}  # type: ignore[typeddict-item]
    if data.get("catalog") is not None:
        out["catalog"] = data["catalog"]
    else:
        out["catalog"] = ""
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
