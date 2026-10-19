"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#VpcTransitConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_gameliftstreams.types.ipv4_cidr_block_list
    import capo_gameliftstreams.types.vpc_id


class VpcTransitConfiguration(TypedDict, closed=True):
    vpc_id: "capo_gameliftstreams.types.vpc_id.VpcId"
    """<p>The ID of the Amazon VPC that you want to connect to the stream group. The VPC must be in the same Amazon Web Services account as the stream group. This value cannot be changed after the stream group is created.</p>"""
    ipv4_cidr_blocks: (
        "capo_gameliftstreams.types.ipv4_cidr_block_list.Ipv4CidrBlockList"
    )
    """<p>A list of IPv4 CIDR blocks in your VPC that you want the stream group to be able to access. You can specify up to 5 CIDR blocks. The CIDR blocks must be valid subsets of the VPC's CIDR blocks and cannot overlap with the service VPC CIDR block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcTransitConfiguration) -> dict:
    out: dict = {}
    out["VpcId"] = value["vpc_id"]
    import capo_gameliftstreams.types.ipv4_cidr_block_list

    out["Ipv4CidrBlocks"] = (
        capo_gameliftstreams.types.ipv4_cidr_block_list.serialize_json(
            value["ipv4_cidr_blocks"]
        )
    )
    return out


def deserialize_json(data: dict) -> VpcTransitConfiguration:
    out: VpcTransitConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("VpcId") is not None:
        out["vpc_id"] = data["VpcId"]
    else:
        out["vpc_id"] = ""
    if data.get("Ipv4CidrBlocks") is not None:
        import capo_gameliftstreams.types.ipv4_cidr_block_list

        out["ipv4_cidr_blocks"] = (
            capo_gameliftstreams.types.ipv4_cidr_block_list.deserialize_json(
                data["Ipv4CidrBlocks"]
            )
        )
    else:
        out["ipv4_cidr_blocks"] = []
    return out
