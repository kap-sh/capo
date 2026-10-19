"""Generated from Smithy shape ``com.amazonaws.route53resolver#PartnerThreatProtectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.partner_value


class PartnerThreatProtectionConfig(TypedDict, closed=True):
    partner: "capo_route53resolver.types.partner_value.PartnerValue"
    """<p>The identifier of the partner threat-protection product, exactly as returned in the <code>Value</code> field of a <a>FirewallRuleTypeDefinition</a> with <code>RuleType</code> set to <code>PartnerThreatProtection</code>. The calling account must hold an active Amazon Web Services Marketplace subscription to this product.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PartnerThreatProtectionConfig) -> dict:
    out: dict = {}
    out["Partner"] = value["partner"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PartnerThreatProtectionConfig:
    out: PartnerThreatProtectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("Partner") is not None:
        out["partner"] = data["Partner"]
    else:
        out["partner"] = ""
    return out
