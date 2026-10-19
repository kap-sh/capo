"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CreateHsmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cluster_id
    import capo_cloudhsm_v2.types.external_az
    import capo_cloudhsm_v2.types.ip_address


class CreateHsmRequest(TypedDict, closed=True):
    cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId"
    """<p>The identifier (ID) of the HSM's cluster. To find the cluster ID, use <a>DescribeClusters</a>.</p>"""
    availability_zone: "capo_cloudhsm_v2.types.external_az.ExternalAz"
    """<p>The Availability Zone where you are creating the HSM. To find the cluster's Availability Zones, use <a>DescribeClusters</a>.</p>"""
    ip_address: NotRequired["capo_cloudhsm_v2.types.ip_address.IpAddress"]
    """<p>The HSM's IP address. If you specify an IP address, use an available address from the subnet that maps to the Availability Zone where you are creating the HSM. If you don't specify an IP address, one is chosen for you from that subnet.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateHsmRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    out["AvailabilityZone"] = value["availability_zone"]
    if "ip_address" in value:
        out["IpAddress"] = value["ip_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateHsmRequest:
    out: CreateHsmRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    else:
        out["cluster_id"] = ""
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    else:
        out["availability_zone"] = ""
    if data.get("IpAddress") is not None:
        out["ip_address"] = data["IpAddress"]
    return out
