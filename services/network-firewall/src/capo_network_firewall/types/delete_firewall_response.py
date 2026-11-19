"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteFirewallResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall
    import capo_network_firewall.types.firewall_status


class DeleteFirewallResponse(TypedDict, closed=True):
    firewall: NotRequired["capo_network_firewall.types.firewall.Firewall"]
    firewall_status: NotRequired[
        "capo_network_firewall.types.firewall_status.FirewallStatus"
    ]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFirewallResponse) -> dict:
    out: dict = {}
    if "firewall" in value:
        import capo_network_firewall.types.firewall

        out["Firewall"] = capo_network_firewall.types.firewall.serialize_aws_json_1_0(
            value["firewall"]
        )
    if "firewall_status" in value:
        import capo_network_firewall.types.firewall_status

        out["FirewallStatus"] = (
            capo_network_firewall.types.firewall_status.serialize_aws_json_1_0(
                value["firewall_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFirewallResponse:
    out: DeleteFirewallResponse = {}  # type: ignore[typeddict-item]
    if data.get("Firewall") is not None:
        import capo_network_firewall.types.firewall

        out["firewall"] = capo_network_firewall.types.firewall.deserialize_aws_json_1_0(
            data["Firewall"]
        )
    if data.get("FirewallStatus") is not None:
        import capo_network_firewall.types.firewall_status

        out["firewall_status"] = (
            capo_network_firewall.types.firewall_status.deserialize_aws_json_1_0(
                data["FirewallStatus"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteFirewallResponse) -> dict:
    out: dict = {}
    if "firewall" in value:
        import capo_network_firewall.types.firewall

        out["Firewall"] = capo_network_firewall.types.firewall.serialize_cbor(
            value["firewall"]
        )
    if "firewall_status" in value:
        import capo_network_firewall.types.firewall_status

        out["FirewallStatus"] = (
            capo_network_firewall.types.firewall_status.serialize_cbor(
                value["firewall_status"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeleteFirewallResponse:
    out: DeleteFirewallResponse = {}  # type: ignore[typeddict-item]
    if data.get("Firewall") is not None:
        import capo_network_firewall.types.firewall

        out["firewall"] = capo_network_firewall.types.firewall.deserialize_cbor(
            data["Firewall"]
        )
    if data.get("FirewallStatus") is not None:
        import capo_network_firewall.types.firewall_status

        out["firewall_status"] = (
            capo_network_firewall.types.firewall_status.deserialize_cbor(
                data["FirewallStatus"]
            )
        )
    return out
