"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EnaSrdSpecificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.ena_srd_udp_specification_request


class EnaSrdSpecificationRequest(TypedDict, closed=True):
    ena_srd_enabled: NotRequired["bool"]
    """<p>Enables or disables ENA SRD for network performance.</p>"""
    ena_srd_udp_specification: NotRequired[
        "capo_workspaces_instances.types.ena_srd_udp_specification_request.EnaSrdUdpSpecificationRequest"
    ]
    """<p>Configures UDP-specific ENA SRD settings.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnaSrdSpecificationRequest) -> dict:
    out: dict = {}
    if "ena_srd_enabled" in value:
        out["EnaSrdEnabled"] = value["ena_srd_enabled"]
    if "ena_srd_udp_specification" in value:
        import capo_workspaces_instances.types.ena_srd_udp_specification_request

        out["EnaSrdUdpSpecification"] = (
            capo_workspaces_instances.types.ena_srd_udp_specification_request.serialize_aws_json_1_0(
                value["ena_srd_udp_specification"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EnaSrdSpecificationRequest:
    out: EnaSrdSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EnaSrdEnabled") is not None:
        out["ena_srd_enabled"] = data["EnaSrdEnabled"]
    if data.get("EnaSrdUdpSpecification") is not None:
        import capo_workspaces_instances.types.ena_srd_udp_specification_request

        out["ena_srd_udp_specification"] = (
            capo_workspaces_instances.types.ena_srd_udp_specification_request.deserialize_aws_json_1_0(
                data["EnaSrdUdpSpecification"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnaSrdSpecificationRequest) -> dict:
    out: dict = {}
    if "ena_srd_enabled" in value:
        out["EnaSrdEnabled"] = value["ena_srd_enabled"]
    if "ena_srd_udp_specification" in value:
        import capo_workspaces_instances.types.ena_srd_udp_specification_request

        out["EnaSrdUdpSpecification"] = (
            capo_workspaces_instances.types.ena_srd_udp_specification_request.serialize_cbor(
                value["ena_srd_udp_specification"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> EnaSrdSpecificationRequest:
    out: EnaSrdSpecificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EnaSrdEnabled") is not None:
        out["ena_srd_enabled"] = data["EnaSrdEnabled"]
    if data.get("EnaSrdUdpSpecification") is not None:
        import capo_workspaces_instances.types.ena_srd_udp_specification_request

        out["ena_srd_udp_specification"] = (
            capo_workspaces_instances.types.ena_srd_udp_specification_request.deserialize_cbor(
                data["EnaSrdUdpSpecification"]
            )
        )
    return out
