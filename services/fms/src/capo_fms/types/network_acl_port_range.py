"""Generated from Smithy shape ``com.amazonaws.fms#NetworkAclPortRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.ip_port_number_integer

NetworkAclPortRange = TypedDict(
    "NetworkAclPortRange",
    {
        "from": NotRequired[
            "capo_fms.types.ip_port_number_integer.IPPortNumberInteger"
        ],
        "to": NotRequired["capo_fms.types.ip_port_number_integer.IPPortNumberInteger"],
    },
    closed=True,
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkAclPortRange) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = value["from"]
    if "to" in value:
        out["To"] = value["to"]
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkAclPortRange:
    out: NetworkAclPortRange = {}  # type: ignore[typeddict-item]
    if data.get("From") is not None:
        out["from"] = data["From"]
    if data.get("To") is not None:
        out["to"] = data["To"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkAclPortRange) -> dict:
    out: dict = {}
    if "from" in value:
        out["From"] = value["from"]
    if "to" in value:
        out["To"] = value["to"]
    return out


def deserialize_cbor(data: dict) -> NetworkAclPortRange:
    out: NetworkAclPortRange = {}  # type: ignore[typeddict-item]
    if data.get("From") is not None:
        out["from"] = data["From"]
    if data.get("To") is not None:
        out["to"] = data["To"]
    return out
