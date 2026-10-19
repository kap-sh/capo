"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AvailabilityZoneMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.availability_zone_mapping_string


class AvailabilityZoneMapping(TypedDict, closed=True):
    availability_zone: "capo_network_firewall.types.availability_zone_mapping_string.AvailabilityZoneMappingString"
    """<p>The ID of the Availability Zone where the firewall endpoint is located. For example, <code>us-east-2a</code>. The Availability Zone must be in the same Region as the transit gateway.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AvailabilityZoneMapping) -> dict:
    out: dict = {}
    out["AvailabilityZone"] = value["availability_zone"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AvailabilityZoneMapping:
    out: AvailabilityZoneMapping = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    else:
        out["availability_zone"] = ""
    return out
