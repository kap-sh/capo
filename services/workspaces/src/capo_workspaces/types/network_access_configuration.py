"""Generated from Smithy shape ``com.amazonaws.workspaces#NetworkAccessConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.non_empty_string


class NetworkAccessConfiguration(TypedDict, closed=True):
    eni_private_ip_address: NotRequired[
        "capo_workspaces.types.non_empty_string.NonEmptyString"
    ]
    """<p>The private IP address of the elastic network interface that is attached to instances in your VPC.</p>"""
    eni_id: NotRequired["capo_workspaces.types.non_empty_string.NonEmptyString"]
    """<p>The resource identifier of the elastic network interface that is attached to instances in your VPC. All network interfaces have the eni-xxxxxxxx resource identifier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAccessConfiguration) -> dict:
    out: dict = {}
    if "eni_private_ip_address" in value:
        out["EniPrivateIpAddress"] = value["eni_private_ip_address"]
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAccessConfiguration:
    out: NetworkAccessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EniPrivateIpAddress") is not None:
        out["eni_private_ip_address"] = data["EniPrivateIpAddress"]
    if data.get("EniId") is not None:
        out["eni_id"] = data["EniId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkAccessConfiguration) -> dict:
    out: dict = {}
    if "eni_private_ip_address" in value:
        out["EniPrivateIpAddress"] = value["eni_private_ip_address"]
    if "eni_id" in value:
        out["EniId"] = value["eni_id"]
    return out


def deserialize_cbor(data: dict) -> NetworkAccessConfiguration:
    out: NetworkAccessConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EniPrivateIpAddress") is not None:
        out["eni_private_ip_address"] = data["EniPrivateIpAddress"]
    if data.get("EniId") is not None:
        out["eni_id"] = data["EniId"]
    return out
