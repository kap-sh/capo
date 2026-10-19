"""Generated from Smithy shape ``com.amazonaws.route53resolver#FirewallAdvancedContentCategoryConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.firewall_advanced_content_category_value


class FirewallAdvancedContentCategoryConfig(TypedDict, closed=True):
    category: "capo_route53resolver.types.firewall_advanced_content_category_value.FirewallAdvancedContentCategoryValue"
    """<p>The content category identifier. To retrieve the list of available content categories, call <a>ListFirewallRuleTypes</a> with <code>RuleType</code> set to <code>FirewallAdvancedContentCategory</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FirewallAdvancedContentCategoryConfig) -> dict:
    out: dict = {}
    out["Category"] = value["category"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FirewallAdvancedContentCategoryConfig:
    out: FirewallAdvancedContentCategoryConfig = {}  # type: ignore[typeddict-item]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    else:
        out["category"] = ""
    return out
