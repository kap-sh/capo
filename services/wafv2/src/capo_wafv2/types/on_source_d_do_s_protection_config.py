"""Generated from Smithy shape ``com.amazonaws.wafv2#OnSourceDDoSProtectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.low_reputation_mode


class OnSourceDDoSProtectionConfig(TypedDict, closed=True):
    alb_low_reputation_mode: "capo_wafv2.types.low_reputation_mode.LowReputationMode"
    """<p>The level of DDoS protection that applies to web ACLs associated with Application Load Balancers. <code>ACTIVE_UNDER_DDOS</code> protection is enabled by default whenever a web ACL is associated with an Application Load Balancer. In the event that an Application Load Balancer experiences high-load conditions or suspected DDoS attacks, the <code>ACTIVE_UNDER_DDOS</code> protection automatically rate limits traffic from known low reputation sources without disrupting Application Load Balancer availability. <code>ALWAYS_ON</code> protection provides constant, always-on monitoring of known low reputation sources for suspected DDoS attacks. While this provides a higher level of protection, there may be potential impacts on legitimate traffic.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnSourceDDoSProtectionConfig) -> dict:
    out: dict = {}
    import capo_wafv2.types.low_reputation_mode

    out["ALBLowReputationMode"] = (
        capo_wafv2.types.low_reputation_mode.serialize_aws_json_1_1(
            value["alb_low_reputation_mode"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> OnSourceDDoSProtectionConfig:
    out: OnSourceDDoSProtectionConfig = {}  # type: ignore[typeddict-item]
    if data.get("ALBLowReputationMode") is not None:
        import capo_wafv2.types.low_reputation_mode

        out["alb_low_reputation_mode"] = (
            capo_wafv2.types.low_reputation_mode.deserialize_aws_json_1_1(
                data["ALBLowReputationMode"]
            )
        )
    else:
        import typing

        out["alb_low_reputation_mode"] = typing.cast(
            "capo_wafv2.types.low_reputation_mode.LowReputationMode", ""
        )
    return out
