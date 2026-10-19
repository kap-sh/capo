"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#DeleteHsmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudhsm_v2.types.cluster_id
    import capo_cloudhsm_v2.types.eni_id
    import capo_cloudhsm_v2.types.hsm_id
    import capo_cloudhsm_v2.types.ip_address


class DeleteHsmRequest(TypedDict, closed=True):
    cluster_id: "capo_cloudhsm_v2.types.cluster_id.ClusterId"
    """<p>The identifier (ID) of the cluster that contains the HSM that you are deleting.</p>"""
    hsm_id: NotRequired["capo_cloudhsm_v2.types.hsm_id.HsmId"]
    """<p>The identifier (ID) of the HSM that you are deleting.</p>"""
    eni_id: NotRequired["capo_cloudhsm_v2.types.eni_id.EniId"]
    """<p>The identifier (ID) of the elastic network interface (ENI) of the HSM that you are deleting.</p>"""
    eni_ip: NotRequired["capo_cloudhsm_v2.types.ip_address.IpAddress"]
    """<p>The IP address of the elastic network interface (ENI) of the HSM that you are deleting.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteHsmRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    if "hsm_id" in value:
        out["HsmId"] = value["hsm_id"]
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    if "eni_ip" in value:
        out["EniIp"] = value["eni_ip"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteHsmRequest:
    out: DeleteHsmRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClusterId") is not None:
        out["cluster_id"] = data["ClusterId"]
    else:
        out["cluster_id"] = ""
    if data.get("HsmId") is not None:
        out["hsm_id"] = data["HsmId"]
    if data.get("EniId") is not None:
        out["eni_id"] = data["EniId"]
    if data.get("EniIp") is not None:
        out["eni_ip"] = data["EniIp"]
    return out
