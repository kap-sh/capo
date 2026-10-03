"""Generated from Smithy shape ``com.amazonaws.ec2#SpotMarketOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.instance_interruption_behavior
    import capo_ec2.types.integer
    import capo_ec2.types.spot_instance_type
    import capo_ec2.types.string


class SpotMarketOptions(TypedDict, closed=True):
    max_price: NotRequired["capo_ec2.types.string.String"]
    """<p>The maximum hourly price that you're willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.</p> <important> <p>If you specify a maximum price, your Spot Instances will be interrupted more frequently than if you do not specify this parameter.</p> <p>If you specify a maximum price, it must be more than USD $0.001. Specifying a value below USD $0.001 will result in an <code>InvalidParameterValue</code> error message.</p> </important>"""
    spot_instance_type: NotRequired[
        "capo_ec2.types.spot_instance_type.SpotInstanceType"
    ]
    """<p>The Spot Instance request type. For <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances">RunInstances</a>, persistent Spot Instance requests are only supported when the instance interruption behavior is either <code>hibernate</code> or <code>stop</code>.</p>"""
    block_duration_minutes: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Deprecated.</p>"""
    valid_until: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The end date of the request, in UTC format (<i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z). Supported only for persistent requests.</p> <ul> <li> <p>For a persistent request, the request remains active until the <code>ValidUntil</code> date and time is reached. Otherwise, the request remains active until you cancel it.</p> </li> <li> <p>For a one-time request, <code>ValidUntil</code> is not supported. The request remains active until all instances launch or you cancel the request.</p> </li> </ul>"""
    instance_interruption_behavior: NotRequired[
        "capo_ec2.types.instance_interruption_behavior.InstanceInterruptionBehavior"
    ]
    """<p>The behavior when a Spot Instance is interrupted.</p> <p>If <code>Configured</code> (for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html"> <code>HibernationOptions</code> </a>) is set to <code>true</code>, the <code>InstanceInterruptionBehavior</code> parameter is automatically set to <code>hibernate</code>. If you set it to <code>stop</code> or <code>terminate</code>, you'll get an error.</p> <p>If <code>Configured</code> (for <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_HibernationOptionsRequest.html"> <code>HibernationOptions</code> </a>) is set to <code>false</code> or <code>null</code>, the <code>InstanceInterruptionBehavior</code> parameter is automatically set to <code>terminate</code>. You can also set it to <code>stop</code> or <code>hibernate</code>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruption-behavior.html">Interruption behavior</a> in the <i>Amazon EC2 User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SpotMarketOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "max_price" in value:
        pairs.append((f"{key_prefix}MaxPrice", str(value["max_price"])))
    if "spot_instance_type" in value:
        import capo_ec2.types.spot_instance_type

        capo_ec2.types.spot_instance_type.serialize_ec2_query(
            value["spot_instance_type"], pairs, f"{key_prefix}SpotInstanceType"
        )
    if "block_duration_minutes" in value:
        pairs.append(
            (f"{key_prefix}BlockDurationMinutes", str(value["block_duration_minutes"]))
        )
    if "valid_until" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["valid_until"], pairs, f"{key_prefix}ValidUntil"
        )
    if "instance_interruption_behavior" in value:
        import capo_ec2.types.instance_interruption_behavior

        capo_ec2.types.instance_interruption_behavior.serialize_ec2_query(
            value["instance_interruption_behavior"],
            pairs,
            f"{key_prefix}InstanceInterruptionBehavior",
        )


def deserialize_ec2_query(el: Element) -> SpotMarketOptions:
    out: SpotMarketOptions = {}  # type: ignore[typeddict-item]
    child_max_price = el.find("MaxPrice")
    if child_max_price is not None:
        out["max_price"] = str(child_max_price.text or "")
    child_spot_instance_type = el.find("SpotInstanceType")
    if child_spot_instance_type is not None:
        import capo_ec2.types.spot_instance_type

        out["spot_instance_type"] = (
            capo_ec2.types.spot_instance_type.deserialize_ec2_query(
                child_spot_instance_type
            )
        )
    child_block_duration_minutes = el.find("BlockDurationMinutes")
    if child_block_duration_minutes is not None:
        out["block_duration_minutes"] = int(child_block_duration_minutes.text or "")
    child_valid_until = el.find("ValidUntil")
    if child_valid_until is not None:
        import capo_ec2.types.date_time

        out["valid_until"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_valid_until
        )
    child_instance_interruption_behavior = el.find("InstanceInterruptionBehavior")
    if child_instance_interruption_behavior is not None:
        import capo_ec2.types.instance_interruption_behavior

        out["instance_interruption_behavior"] = (
            capo_ec2.types.instance_interruption_behavior.deserialize_ec2_query(
                child_instance_interruption_behavior
            )
        )
    return out
