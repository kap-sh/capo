"""Generated from Smithy shape ``com.amazonaws.waf#IPSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.ip_set_descriptors
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name


class IPSet(TypedDict, closed=True):
    ip_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The <code>IPSetId</code> for an <code>IPSet</code>. You use <code>IPSetId</code> to get information about an <code>IPSet</code> (see <a>GetIPSet</a>), update an <code>IPSet</code> (see <a>UpdateIPSet</a>), insert an <code>IPSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete an <code>IPSet</code> from AWS WAF (see <a>DeleteIPSet</a>).</p> <p> <code>IPSetId</code> is returned by <a>CreateIPSet</a> and by <a>ListIPSets</a>.</p>"""
    name: NotRequired["capo_waf.types.resource_name.ResourceName"]
    """<p>A friendly name or description of the <a>IPSet</a>. You can't change the name of an <code>IPSet</code> after you create it.</p>"""
    ip_set_descriptors: "capo_waf.types.ip_set_descriptors.IPSetDescriptors"
    """<p>The IP address type (<code>IPV4</code> or <code>IPV6</code>) and the IP address range (in CIDR notation) that web requests originate from. If the <code>WebACL</code> is associated with a CloudFront distribution and the viewer did not use an HTTP proxy or a load balancer to send the request, this is the value of the c-ip field in the CloudFront access logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IPSet) -> dict:
    out: dict = {}
    out["IPSetId"] = value["ip_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_waf.types.ip_set_descriptors

    out["IPSetDescriptors"] = capo_waf.types.ip_set_descriptors.serialize_aws_json_1_1(
        value["ip_set_descriptors"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> IPSet:
    out: IPSet = {}  # type: ignore[typeddict-item]
    if data.get("IPSetId") is not None:
        out["ip_set_id"] = data["IPSetId"]
    else:
        out["ip_set_id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("IPSetDescriptors") is not None:
        import capo_waf.types.ip_set_descriptors

        out["ip_set_descriptors"] = (
            capo_waf.types.ip_set_descriptors.deserialize_aws_json_1_1(
                data["IPSetDescriptors"]
            )
        )
    else:
        out["ip_set_descriptors"] = []
    return out
