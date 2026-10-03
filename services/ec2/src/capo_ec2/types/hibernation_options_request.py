"""Generated from Smithy shape ``com.amazonaws.ec2#HibernationOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class HibernationOptionsRequest(TypedDict, closed=True):
    configured: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Set to <code>true</code> to enable your instance for hibernation.</p> <p>For Spot Instances, if you set <code>Configured</code> to <code>true</code>, either omit the <code>InstanceInterruptionBehavior</code> parameter (for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotMarketOptions.html"> <code>SpotMarketOptions</code> </a>), or set it to <code>hibernate</code>. When <code>Configured</code> is true:</p> <ul> <li> <p>If you omit <code>InstanceInterruptionBehavior</code>, it defaults to <code>hibernate</code>.</p> </li> <li> <p>If you set <code>InstanceInterruptionBehavior</code> to a value other than <code>hibernate</code>, you'll get an error.</p> </li> </ul> <p>Default: <code>false</code> </p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: HibernationOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "configured" in value:
        pairs.append(
            (f"{key_prefix}Configured", "true" if value["configured"] else "false")
        )


def deserialize_ec2_query(el: Element) -> HibernationOptionsRequest:
    out: HibernationOptionsRequest = {}  # type: ignore[typeddict-item]
    child_configured = el.find("Configured")
    if child_configured is not None:
        out["configured"] = (child_configured.text or "").lower() == "true"
    return out
