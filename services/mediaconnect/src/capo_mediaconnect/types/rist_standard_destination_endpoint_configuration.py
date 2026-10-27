"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RistStandardDestinationEndpointConfiguration``."""

from typing_extensions import TypedDict


class RistStandardDestinationEndpointConfiguration(TypedDict, closed=True):
    destination_address: "str"
    """<p>The IP address on which the destination endpoint receives content.</p>"""
    destination_ingest_port: "int"
    """<p>The port on which the destination endpoint receives content. The valid range is 1024 to 65531.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RistStandardDestinationEndpointConfiguration) -> dict:
    out: dict = {}
    out["destinationAddress"] = value["destination_address"]
    out["destinationIngestPort"] = value["destination_ingest_port"]
    return out


def deserialize_json(data: dict) -> RistStandardDestinationEndpointConfiguration:
    out: RistStandardDestinationEndpointConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("destinationAddress") is not None:
        out["destination_address"] = data["destinationAddress"]
    else:
        out["destination_address"] = ""
    if data.get("destinationIngestPort") is not None:
        out["destination_ingest_port"] = data["destinationIngestPort"]
    else:
        out["destination_ingest_port"] = 0
    return out
