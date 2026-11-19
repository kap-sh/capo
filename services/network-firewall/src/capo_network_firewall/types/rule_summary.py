"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.collection_member_string


class RuleSummary(TypedDict, closed=True):
    sid: NotRequired[
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    ]
    """<p>The unique identifier (Signature ID) of the Suricata rule.</p>"""
    msg: NotRequired[
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    ]
    """<p>The contents taken from the rule's msg field.</p>"""
    metadata: NotRequired[
        "capo_network_firewall.types.collection_member_string.CollectionMember_String"
    ]
    """<p>The contents of the rule's metadata.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleSummary) -> dict:
    out: dict = {}
    if "sid" in value:
        out["SID"] = value["sid"]
    if "msg" in value:
        out["Msg"] = value["msg"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    if data.get("Msg") is not None:
        out["msg"] = data["Msg"]
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleSummary) -> dict:
    out: dict = {}
    if "sid" in value:
        out["SID"] = value["sid"]
    if "msg" in value:
        out["Msg"] = value["msg"]
    if "metadata" in value:
        out["Metadata"] = value["metadata"]
    return out


def deserialize_cbor(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("SID") is not None:
        out["sid"] = data["SID"]
    if data.get("Msg") is not None:
        out["msg"] = data["Msg"]
    if data.get("Metadata") is not None:
        out["metadata"] = data["Metadata"]
    return out
