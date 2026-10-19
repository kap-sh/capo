"""Generated from Smithy shape ``com.amazonaws.route53resolver#DnsThreatProtectionRuleTypeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.confidence_threshold
    import capo_route53resolver.types.dns_threat_protection_rule_type_value


class DnsThreatProtectionRuleTypeConfig(TypedDict, closed=True):
    value: "capo_route53resolver.types.dns_threat_protection_rule_type_value.DnsThreatProtectionRuleTypeValue"
    """<p>The type of DNS threat protection. Valid values are:</p> <ul> <li> <p> <code>DGA</code>: Domain generation algorithms detection. DGAs are used by attackers to generate a large number of domains to launch malware attacks.</p> </li> <li> <p> <code>DNS_TUNNELING</code>: DNS tunneling detection. DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.</p> </li> <li> <p> <code>DICTIONARY_DGA</code>: Dictionary-based domain generation algorithms detection. Dictionary DGAs use wordlists to generate domains that appear more legitimate, making them harder to detect than traditional DGAs.</p> </li> </ul>"""
    confidence_threshold: (
        "capo_route53resolver.types.confidence_threshold.ConfidenceThreshold"
    )
    """<p>The confidence threshold for DNS Firewall Advanced. You must provide this value when you create or update a DNS Firewall Advanced rule. The confidence level values mean:</p> <ul> <li> <p> <code>LOW</code>: Provides the highest detection rate for threats, but also increases false positives.</p> </li> <li> <p> <code>MEDIUM</code>: Provides a balance between detecting threats and false positives.</p> </li> <li> <p> <code>HIGH</code>: Detects only the most well corroborated threats with a low rate of false positives.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsThreatProtectionRuleTypeConfig) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_route53resolver.types.confidence_threshold

    out["ConfidenceThreshold"] = (
        capo_route53resolver.types.confidence_threshold.serialize_aws_json_1_1(
            value["confidence_threshold"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsThreatProtectionRuleTypeConfig:
    out: DnsThreatProtectionRuleTypeConfig = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    if data.get("ConfidenceThreshold") is not None:
        import capo_route53resolver.types.confidence_threshold

        out["confidence_threshold"] = (
            capo_route53resolver.types.confidence_threshold.deserialize_aws_json_1_1(
                data["ConfidenceThreshold"]
            )
        )
    else:
        import typing

        out["confidence_threshold"] = typing.cast(
            "capo_route53resolver.types.confidence_threshold.ConfidenceThreshold", ""
        )
    return out
