"""Generated from Smithy shape ``com.amazonaws.ec2#IpamDiscoveryFailureReason``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipam_discovery_failure_code
    import capo_ec2.types.string


class IpamDiscoveryFailureReason(TypedDict, closed=True):
    code: NotRequired[
        "capo_ec2.types.ipam_discovery_failure_code.IpamDiscoveryFailureCode"
    ]
    """<p>The discovery failure code.</p> <ul> <li> <p> <code>assume-role-failure</code> - IPAM could not assume the Amazon Web Services IAM service-linked role. This could be because of any of the following:</p> <ul> <li> <p>SLR has not been created yet and IPAM is still creating it.</p> </li> <li> <p>You have opted-out of the IPAM home Region.</p> </li> <li> <p>Account you are using as your IPAM account has been suspended.</p> </li> </ul> </li> <li> <p> <code>throttling-failure</code> - IPAM account is already using the allotted transactions per second and IPAM is receiving a throttling error when assuming the Amazon Web Services IAM SLR.</p> </li> <li> <p> <code>unauthorized-failure</code> - Amazon Web Services account making the request is not authorized. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/errors-overview.html">AuthFailure</a> in the <i>Amazon Elastic Compute Cloud API Reference</i>.</p> </li> </ul>"""
    message: NotRequired["capo_ec2.types.string.String"]
    """<p>The discovery failure message.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: IpamDiscoveryFailureReason, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "code" in value:
        import capo_ec2.types.ipam_discovery_failure_code

        capo_ec2.types.ipam_discovery_failure_code.serialize_ec2_query(
            value["code"], pairs, f"{key_prefix}Code"
        )
    if "message" in value:
        pairs.append((f"{key_prefix}Message", str(value["message"])))


def deserialize_ec2_query(el: Element) -> IpamDiscoveryFailureReason:
    out: IpamDiscoveryFailureReason = {}  # type: ignore[typeddict-item]
    child_code = el.find("code")
    if child_code is not None:
        import capo_ec2.types.ipam_discovery_failure_code

        out["code"] = capo_ec2.types.ipam_discovery_failure_code.deserialize_ec2_query(
            child_code
        )
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out
