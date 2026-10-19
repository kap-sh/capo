"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Hsm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cluster_id
    import capo_cloudhsm_v2.types.eni_id
    import capo_cloudhsm_v2.types.external_az
    import capo_cloudhsm_v2.types.hsm_id
    import capo_cloudhsm_v2.types.hsm_state
    import capo_cloudhsm_v2.types.hsm_type
    import capo_cloudhsm_v2.types.ip_address
    import capo_cloudhsm_v2.types.ip_v6_address
    import capo_cloudhsm_v2.types.string
    import capo_cloudhsm_v2.types.subnet_id


class Hsm(TypedDict, closed=True):
    availability_zone: NotRequired["capo_cloudhsm_v2.types.external_az.ExternalAz"]
    """<p>The Availability Zone that contains the HSM.</p>"""
    cluster_id: NotRequired["capo_cloudhsm_v2.types.cluster_id.ClusterId"]
    """<p>The identifier (ID) of the cluster that contains the HSM.</p>"""
    subnet_id: NotRequired["capo_cloudhsm_v2.types.subnet_id.SubnetId"]
    """<p>The subnet that contains the HSM's elastic network interface (ENI).</p>"""
    eni_id: NotRequired["capo_cloudhsm_v2.types.eni_id.EniId"]
    """<p>The identifier (ID) of the HSM's elastic network interface (ENI).</p>"""
    eni_ip: NotRequired["capo_cloudhsm_v2.types.ip_address.IpAddress"]
    """<p>The IP address of the HSM's elastic network interface (ENI).</p>"""
    eni_ip_v6: NotRequired["capo_cloudhsm_v2.types.ip_v6_address.IpV6Address"]
    """<p>The IPv6 address (if any) of the HSM's elastic network interface (ENI).</p>"""
    hsm_id: "capo_cloudhsm_v2.types.hsm_id.HsmId"
    """<p>The HSM's identifier (ID).</p>"""
    hsm_type: NotRequired["capo_cloudhsm_v2.types.hsm_type.HsmType"]
    """<p>The type of HSM.</p>"""
    state: NotRequired["capo_cloudhsm_v2.types.hsm_state.HsmState"]
    """<p>The HSM's state.</p>"""
    state_message: NotRequired["capo_cloudhsm_v2.types.string.String"]
    """<p>A description of the HSM's state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Hsm) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "cluster_id" in value:
        out["ClusterId"] = value["cluster_id"]
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    if "eni_ip" in value:
        out["EniIp"] = value["eni_ip"]
    if "eni_ip_v6" in value:
        out["EniIpV6"] = value["eni_ip_v6"]
    out["HsmId"] = value["hsm_id"]
    if "hsm_type" in value:
        out["HsmType"] = value["hsm_type"]
    if "state" in value:
        import capo_cloudhsm_v2.types.hsm_state

        out["State"] = capo_cloudhsm_v2.types.hsm_state.serialize_aws_json_1_1(
            value["state"]
        )
    if "state_message" in value:
        out["StateMessage"] = value["state_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Hsm:
    out: Hsm = {}  # type: ignore[typeddict-item]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    if data.get("SubnetId") is not None:
        out["subnet_id"] = data["SubnetId"]
    if data.get("EniId") is not None:
        out["eni_id"] = data["EniId"]
    if data.get("EniIp") is not None:
        out["eni_ip"] = data["EniIp"]
    if data.get("EniIpV6") is not None:
        out["eni_ip_v6"] = data["EniIpV6"]
    if data.get("HsmId") is not None:
        out["hsm_id"] = data["HsmId"]
    else:
        out["hsm_id"] = ""
    if data.get("HsmType") is not None:
        out["hsm_type"] = data["HsmType"]
    if data.get("State") is not None:
        import capo_cloudhsm_v2.types.hsm_state

        out["state"] = capo_cloudhsm_v2.types.hsm_state.deserialize_aws_json_1_1(
            data["State"]
        )
    if data.get("StateMessage") is not None:
        out["state_message"] = data["StateMessage"]
    return out
