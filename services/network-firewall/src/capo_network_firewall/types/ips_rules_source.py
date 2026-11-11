"""Generated from Smithy shape ``com.amazonaws.networkfirewall#IpsRulesSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.rules_string


class IpsRulesSource(TypedDict, closed=True):
    rules_string: NotRequired["capo_network_firewall.types.rules_string.RulesString"]
    """<p>IPS engine rules, provided as a single Suricata-compatible rule string. For the rule format, see <a href="https://suricata.readthedocs.io/en/suricata-8.0.3/rules/intro.html">Rules Format</a> on the Suricata website.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IpsRulesSource) -> dict:
    out: dict = {}
    if "rules_string" in value:
        out["RulesString"] = value["rules_string"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IpsRulesSource:
    out: IpsRulesSource = {}  # type: ignore[typeddict-item]
    if data.get("RulesString") is not None:
        out["rules_string"] = data["RulesString"]
    return out
