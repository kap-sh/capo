"""Generated from Smithy shape ``com.amazonaws.wafv2#ManagedProductDescriptor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.boolean
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.product_description
    import capo_wafv2.types.product_id
    import capo_wafv2.types.product_link
    import capo_wafv2.types.product_title
    import capo_wafv2.types.resource_arn
    import capo_wafv2.types.vendor_name


class ManagedProductDescriptor(TypedDict, closed=True):
    vendor_name: NotRequired["capo_wafv2.types.vendor_name.VendorName"]
    """<p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>"""
    managed_rule_set_name: NotRequired["capo_wafv2.types.entity_name.EntityName"]
    """<p>The name of the managed rule group. For example, <code>AWSManagedRulesAnonymousIpList</code> or <code>AWSManagedRulesATPRuleSet</code>.</p>"""
    product_id: NotRequired["capo_wafv2.types.product_id.ProductId"]
    """<p>A unique identifier for the rule group. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.</p>"""
    product_link: NotRequired["capo_wafv2.types.product_link.ProductLink"]
    """<p>For Amazon Web Services Marketplace managed rule groups only, the link to the rule group product page. </p>"""
    product_title: NotRequired["capo_wafv2.types.product_title.ProductTitle"]
    """<p>The display name for the managed rule group. For example, <code>Anonymous IP list</code> or <code>Account takeover prevention</code>.</p>"""
    product_description: NotRequired[
        "capo_wafv2.types.product_description.ProductDescription"
    ]
    """<p>A short description of the managed rule group.</p>"""
    sns_topic_arn: NotRequired["capo_wafv2.types.resource_arn.ResourceArn"]
    """<p>The Amazon resource name (ARN) of the Amazon Simple Notification Service SNS topic that's used to provide notification of changes to the managed rule group. You can subscribe to the SNS topic to receive notifications when the managed rule group is modified, such as for new versions and for version expiration. For more information, see the <a href="https://docs.aws.amazon.com/sns/latest/dg/welcome.html">Amazon Simple Notification Service Developer Guide</a>.</p>"""
    is_versioning_supported: "capo_wafv2.types.boolean.Boolean"
    """<p>Indicates whether the rule group is versioned. </p>"""
    is_advanced_managed_rule_set: "capo_wafv2.types.boolean.Boolean"
    """<p>Indicates whether the rule group provides an advanced set of protections, such as the the Amazon Web Services Managed Rules rule groups that are used for WAF intelligent threat mitigation. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedProductDescriptor) -> dict:
    out: dict = {}
    if "vendor_name" in value:
        out["VendorName"] = value["vendor_name"]
    if "managed_rule_set_name" in value:
        out["ManagedRuleSetName"] = value["managed_rule_set_name"]
    if "product_id" in value:
        out["ProductId"] = value["product_id"]
    if "product_link" in value:
        out["ProductLink"] = value["product_link"]
    if "product_title" in value:
        out["ProductTitle"] = value["product_title"]
    if "product_description" in value:
        out["ProductDescription"] = value["product_description"]
    if "sns_topic_arn" in value:
        out["SnsTopicArn"] = value["sns_topic_arn"]
    out["IsVersioningSupported"] = value.get("is_versioning_supported", False)
    out["IsAdvancedManagedRuleSet"] = value.get("is_advanced_managed_rule_set", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedProductDescriptor:
    out: ManagedProductDescriptor = {}  # type: ignore[typeddict-item]
    if data.get("VendorName") is not None:
        out["vendor_name"] = data["VendorName"]
    if data.get("ManagedRuleSetName") is not None:
        out["managed_rule_set_name"] = data["ManagedRuleSetName"]
    if data.get("ProductId") is not None:
        out["product_id"] = data["ProductId"]
    if data.get("ProductLink") is not None:
        out["product_link"] = data["ProductLink"]
    if data.get("ProductTitle") is not None:
        out["product_title"] = data["ProductTitle"]
    if data.get("ProductDescription") is not None:
        out["product_description"] = data["ProductDescription"]
    if data.get("SnsTopicArn") is not None:
        out["sns_topic_arn"] = data["SnsTopicArn"]
    if data.get("IsVersioningSupported") is not None:
        out["is_versioning_supported"] = data["IsVersioningSupported"]
    else:
        out["is_versioning_supported"] = False
    if data.get("IsAdvancedManagedRuleSet") is not None:
        out["is_advanced_managed_rule_set"] = data["IsAdvancedManagedRuleSet"]
    else:
        out["is_advanced_managed_rule_set"] = False
    return out
