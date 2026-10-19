"""Generated from Smithy shape ``com.amazonaws.wafv2#DescribeManagedProductsByVendorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.scope
    import capo_wafv2.types.vendor_name


class DescribeManagedProductsByVendorRequest(TypedDict, closed=True):
    vendor_name: "capo_wafv2.types.vendor_name.VendorName"
    """<p>The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.</p>"""
    scope: "capo_wafv2.types.scope.Scope"
    """<p>Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use <code>CLOUDFRONT</code>.</p> <p>To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows: </p> <ul> <li> <p>CLI - Specify the Region when you use the CloudFront scope: <code>--scope=CLOUDFRONT --region=us-east-1</code>. </p> </li> <li> <p>API and SDKs - For all calls, use the Region endpoint us-east-1. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeManagedProductsByVendorRequest) -> dict:
    out: dict = {}
    out["VendorName"] = value["vendor_name"]
    import capo_wafv2.types.scope

    out["Scope"] = capo_wafv2.types.scope.serialize_aws_json_1_1(value["scope"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeManagedProductsByVendorRequest:
    out: DescribeManagedProductsByVendorRequest = {}  # type: ignore[typeddict-item]
    if data.get("VendorName") is not None:
        out["vendor_name"] = data["VendorName"]
    else:
        out["vendor_name"] = ""
    if data.get("Scope") is not None:
        import capo_wafv2.types.scope

        out["scope"] = capo_wafv2.types.scope.deserialize_aws_json_1_1(data["Scope"])
    else:
        import typing

        out["scope"] = typing.cast("capo_wafv2.types.scope.Scope", "")
    return out
