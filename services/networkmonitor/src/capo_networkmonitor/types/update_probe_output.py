"""Generated from Smithy shape ``com.amazonaws.networkmonitor#UpdateProbeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmonitor.types.address_family
    import capo_networkmonitor.types.arn
    import capo_networkmonitor.types.destination
    import capo_networkmonitor.types.iso8601_timestamp
    import capo_networkmonitor.types.packet_size
    import capo_networkmonitor.types.port
    import capo_networkmonitor.types.probe_id
    import capo_networkmonitor.types.probe_state
    import capo_networkmonitor.types.protocol
    import capo_networkmonitor.types.tag_map
    import capo_networkmonitor.types.vpc_id


class UpdateProbeOutput(TypedDict, closed=True):
    probe_id: NotRequired["capo_networkmonitor.types.probe_id.ProbeId"]
    """<p>The updated ID of the probe.</p>"""
    probe_arn: NotRequired["capo_networkmonitor.types.arn.Arn"]
    """<p>The updated ARN of the probe.</p>"""
    source_arn: "capo_networkmonitor.types.arn.Arn"
    """<p>The updated ARN of the source subnet.</p>"""
    destination: "capo_networkmonitor.types.destination.Destination"
    """<p>The updated destination IP address for the probe.</p>"""
    destination_port: NotRequired["capo_networkmonitor.types.port.Port"]
    """<p>The updated destination port. This must be a number between <code>1</code> and <code>65536</code>.</p>"""
    protocol: "capo_networkmonitor.types.protocol.Protocol"
    """<p>The updated protocol for the probe.</p>"""
    packet_size: NotRequired["capo_networkmonitor.types.packet_size.PacketSize"]
    """<p>The updated packet size for the probe. </p>"""
    address_family: NotRequired[
        "capo_networkmonitor.types.address_family.AddressFamily"
    ]
    """<p>The updated IP address family. This must be either <code>IPV4</code> or <code>IPV6</code>.</p>"""
    vpc_id: NotRequired["capo_networkmonitor.types.vpc_id.VpcId"]
    """<p>The updated ID of the source VPC subnet ID.</p>"""
    state: NotRequired["capo_networkmonitor.types.probe_state.ProbeState"]
    """<p>The state of the updated probe.</p>"""
    created_at: NotRequired[
        "capo_networkmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time and date that the probe was created.</p>"""
    modified_at: NotRequired[
        "capo_networkmonitor.types.iso8601_timestamp.Iso8601Timestamp"
    ]
    """<p>The time and date that the probe was last updated.</p>"""
    tags: NotRequired["capo_networkmonitor.types.tag_map.TagMap"]
    """<p>Update tags for a probe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProbeOutput) -> dict:
    out: dict = {}
    if "probe_id" in value:
        out["probeId"] = value["probe_id"]
    if "probe_arn" in value:
        out["probeArn"] = value["probe_arn"]
    out["sourceArn"] = value["source_arn"]
    out["destination"] = value["destination"]
    if "destination_port" in value:
        out["destinationPort"] = value["destination_port"]
    import capo_networkmonitor.types.protocol

    out["protocol"] = capo_networkmonitor.types.protocol.serialize_json(
        value["protocol"]
    )
    if "packet_size" in value:
        out["packetSize"] = value["packet_size"]
    if "address_family" in value:
        import capo_networkmonitor.types.address_family

        out["addressFamily"] = capo_networkmonitor.types.address_family.serialize_json(
            value["address_family"]
        )
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "state" in value:
        import capo_networkmonitor.types.probe_state

        out["state"] = capo_networkmonitor.types.probe_state.serialize_json(
            value["state"]
        )
    if "created_at" in value:
        import capo_networkmonitor.types.iso8601_timestamp

        out["createdAt"] = capo_networkmonitor.types.iso8601_timestamp.serialize_json(
            value["created_at"]
        )
    if "modified_at" in value:
        import capo_networkmonitor.types.iso8601_timestamp

        out["modifiedAt"] = capo_networkmonitor.types.iso8601_timestamp.serialize_json(
            value["modified_at"]
        )
    if "tags" in value:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateProbeOutput:
    out: UpdateProbeOutput = {}  # type: ignore[typeddict-item]
    if data.get("probeId") is not None:
        out["probe_id"] = data["probeId"]
    if data.get("probeArn") is not None:
        out["probe_arn"] = data["probeArn"]
    if data.get("sourceArn") is not None:
        out["source_arn"] = data["sourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    else:
        out["destination"] = ""
    if data.get("destinationPort") is not None:
        out["destination_port"] = data["destinationPort"]
    if data.get("protocol") is not None:
        import capo_networkmonitor.types.protocol

        out["protocol"] = capo_networkmonitor.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        import typing

        out["protocol"] = typing.cast("capo_networkmonitor.types.protocol.Protocol", "")
    if data.get("packetSize") is not None:
        out["packet_size"] = data["packetSize"]
    if data.get("addressFamily") is not None:
        import capo_networkmonitor.types.address_family

        out["address_family"] = (
            capo_networkmonitor.types.address_family.deserialize_json(
                data["addressFamily"]
            )
        )
    if data.get("vpcId") is not None:
        out["vpc_id"] = data["vpcId"]
    if data.get("state") is not None:
        import capo_networkmonitor.types.probe_state

        out["state"] = capo_networkmonitor.types.probe_state.deserialize_json(
            data["state"]
        )
    if data.get("createdAt") is not None:
        import capo_networkmonitor.types.iso8601_timestamp

        out["created_at"] = (
            capo_networkmonitor.types.iso8601_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if data.get("modifiedAt") is not None:
        import capo_networkmonitor.types.iso8601_timestamp

        out["modified_at"] = (
            capo_networkmonitor.types.iso8601_timestamp.deserialize_json(
                data["modifiedAt"]
            )
        )
    if data.get("tags") is not None:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.deserialize_json(data["tags"])
    return out
