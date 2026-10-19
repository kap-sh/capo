"""Generated from Smithy shape ``com.amazonaws.wafv2#DescribeManagedRuleGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.entity_name
    import capo_wafv2.types.scope
    import capo_wafv2.types.vendor_name
    import capo_wafv2.types.version_key_string


class DescribeManagedRuleGroupRequest(TypedDict, closed=True):
    vendor_name: "capo_wafv2.types.vendor_name.VendorName"
    """<p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>"""
    name: "capo_wafv2.types.entity_name.EntityName"
    """<p>The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""
    version_name: NotRequired["capo_wafv2.types.version_key_string.VersionKeyString"]
    """<p>The version of the rule group. You can only use a version that is not scheduled for expiration. If you don't provide this, WAF uses the vendor's default version. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeManagedRuleGroupRequest) -> dict:
    out: dict = {}
    out["VendorName"] = value["vendor_name"]
    out["Name"] = value["name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    if "version_name" in value:
        out["VersionName"] = value["version_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeManagedRuleGroupRequest:
    out: DescribeManagedRuleGroupRequest = {}  # type: ignore[typeddict-item]
    if data.get("VendorName") is not None:
        out["vendor_name"] = data["VendorName"]
    else:
        out["vendor_name"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_wafv2.types.scope.Scope", "")
    if data.get("VersionName") is not None:
        out["version_name"] = data["VersionName"]
    return out
