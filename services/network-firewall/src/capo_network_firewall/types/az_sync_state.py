"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AZSyncState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.attachment


class AZSyncState(TypedDict, closed=True):
    attachment: NotRequired["capo_network_firewall.types.attachment.Attachment"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AZSyncState) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_network_firewall.types.attachment

        out["Attachment"] = (
            capo_network_firewall.types.attachment.serialize_aws_json_1_0(
                value["attachment"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AZSyncState:
    out: AZSyncState = {}  # type: ignore[typeddict-item]
    if data.get("Attachment") is not None:
        import capo_network_firewall.types.attachment

        out["attachment"] = (
            capo_network_firewall.types.attachment.deserialize_aws_json_1_0(
                data["Attachment"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AZSyncState) -> dict:
    out: dict = {}
    if "attachment" in value:
        import capo_network_firewall.types.attachment

        out["Attachment"] = capo_network_firewall.types.attachment.serialize_cbor(
            value["attachment"]
        )
    return out


def deserialize_cbor(data: dict) -> AZSyncState:
    out: AZSyncState = {}  # type: ignore[typeddict-item]
    if data.get("Attachment") is not None:
        import capo_network_firewall.types.attachment

        out["attachment"] = capo_network_firewall.types.attachment.deserialize_cbor(
            data["Attachment"]
        )
    return out
