"""Generated from Smithy shape ``com.amazonaws.evs#DisassociateEipFromVlanRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_evs.types.association_id
    import capo_evs.types.client_token
    import capo_evs.types.environment_id


class DisassociateEipFromVlanRequest(TypedDict, closed=True):
    client_token: NotRequired["capo_evs.types.client_token.ClientToken"]
    """<note> <p>This parameter is not used in Amazon EVS currently. If you supply input for this parameter, it will have no effect.</p> </note> <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the environment creation request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""
    environment_id: "capo_evs.types.environment_id.EnvironmentId"
    """<p>A unique ID for the environment containing the VLAN that the Elastic IP address disassociates from.</p>"""
    vlan_name: "str"
    """<p>The name of the VLAN. <code>hcx</code> is the only accepted VLAN name at this time.</p>"""
    association_id: "capo_evs.types.association_id.AssociationId"
    """<p> A unique ID for the Elastic IP address association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateEipFromVlanRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["environmentId"] = value["environment_id"]
    out["vlanName"] = value["vlan_name"]
    out["associationId"] = value["association_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateEipFromVlanRequest:
    out: DisassociateEipFromVlanRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("vlanName") is not None:
        out["vlan_name"] = data["vlanName"]
    else:
        out["vlan_name"] = ""
    if data.get("associationId") is not None:
        out["association_id"] = data["associationId"]
    else:
        out["association_id"] = ""
    return out
