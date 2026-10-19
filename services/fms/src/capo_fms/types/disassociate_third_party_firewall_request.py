"""Generated from Smithy shape ``com.amazonaws.fms#DisassociateThirdPartyFirewallRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fms.types.third_party_firewall


class DisassociateThirdPartyFirewallRequest(TypedDict, closed=True):
    third_party_firewall: "capo_fms.types.third_party_firewall.ThirdPartyFirewall"
    """<p>The name of the third-party firewall vendor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateThirdPartyFirewallRequest) -> dict:
    out: dict = {}
    import capo_fms.types.third_party_firewall

    out["ThirdPartyFirewall"] = (
        capo_fms.types.third_party_firewall.serialize_aws_json_1_1(
            value["third_party_firewall"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateThirdPartyFirewallRequest:
    out: DisassociateThirdPartyFirewallRequest = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewall") is not None:
        import capo_fms.types.third_party_firewall

        out["third_party_firewall"] = (
            capo_fms.types.third_party_firewall.deserialize_aws_json_1_1(
                data["ThirdPartyFirewall"]
            )
        )
    else:
        import typing

        out["third_party_firewall"] = typing.cast(
            "capo_fms.types.third_party_firewall.ThirdPartyFirewall", ""
        )
    return out
