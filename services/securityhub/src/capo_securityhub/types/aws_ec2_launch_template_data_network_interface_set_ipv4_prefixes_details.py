"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string


class AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails(
    TypedDict, closed=True
):
    ipv4_prefix: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The IPv4 prefix. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-prefix-eni.html">Assigning prefixes to Amazon EC2 network interfaces</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails,
) -> dict:
    out: dict = {}
    if "ipv4_prefix" in value:
        out["Ipv4Prefix"] = value["ipv4_prefix"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails:
    out: AwsEc2LaunchTemplateDataNetworkInterfaceSetIpv4PrefixesDetails = {}  # type: ignore[typeddict-item]
    if data.get("Ipv4Prefix") is not None:
        out["ipv4_prefix"] = data["Ipv4Prefix"]
    return out
