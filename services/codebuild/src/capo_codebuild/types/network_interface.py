"""Generated from Smithy shape ``com.amazonaws.codebuild#NetworkInterface``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.non_empty_string


class NetworkInterface(TypedDict, closed=True):
    subnet_id: NotRequired["capo_codebuild.types.non_empty_string.NonEmptyString"]
    """<p>The ID of the subnet.</p>"""
    network_interface_id: NotRequired[
        "capo_codebuild.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of the network interface.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkInterface) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    if data.get("networkInterfaceId") is not None:
        out["network_interface_id"] = data["networkInterfaceId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkInterface) -> dict:
    out: dict = {}
    if "subnet_id" in value:
        out["subnetId"] = value["subnet_id"]
    if "network_interface_id" in value:
        out["networkInterfaceId"] = value["network_interface_id"]
    return out


def deserialize_cbor(data: dict) -> NetworkInterface:
    out: NetworkInterface = {}  # type: ignore[typeddict-item]
    if data.get("subnetId") is not None:
        out["subnet_id"] = data["subnetId"]
    if data.get("networkInterfaceId") is not None:
        out["network_interface_id"] = data["networkInterfaceId"]
    return out
