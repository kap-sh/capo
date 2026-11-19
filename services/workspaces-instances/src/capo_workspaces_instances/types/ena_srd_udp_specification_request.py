"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EnaSrdUdpSpecificationRequest``."""

from typing_extensions import NotRequired, TypedDict


class EnaSrdUdpSpecificationRequest(TypedDict, closed=True):
    ena_srd_udp_enabled: NotRequired["bool"]
    """<p>Enables or disables ENA SRD for UDP traffic.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnaSrdUdpSpecificationRequest) -> dict:
    out: dict = {}
    if "ena_srd_udp_enabled" in value:
        out["EnaSrdUdpEnabled"] = value["ena_srd_udp_enabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EnaSrdUdpSpecificationRequest:
    out: EnaSrdUdpSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EnaSrdUdpEnabled") is not None:
        out["ena_srd_udp_enabled"] = data["EnaSrdUdpEnabled"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnaSrdUdpSpecificationRequest) -> dict:
    out: dict = {}
    if "ena_srd_udp_enabled" in value:
        out["EnaSrdUdpEnabled"] = value["ena_srd_udp_enabled"]
    return out


def deserialize_cbor(data: dict) -> EnaSrdUdpSpecificationRequest:
    out: EnaSrdUdpSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EnaSrdUdpEnabled") is not None:
        out["ena_srd_udp_enabled"] = data["EnaSrdUdpEnabled"]
    return out
