"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#CustomizableMetricParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer.types.customizable_metric_headroom
    import capo_compute_optimizer.types.customizable_metric_threshold


class CustomizableMetricParameters(TypedDict, closed=True):
    threshold: NotRequired[
        "capo_compute_optimizer.types.customizable_metric_threshold.CustomizableMetricThreshold"
    ]
    """<p> The threshold value used for the specified metric parameter. </p> <note> <p>You can only specify the threshold value for CPU utilization.</p> </note>"""
    headroom: NotRequired[
        "capo_compute_optimizer.types.customizable_metric_headroom.CustomizableMetricHeadroom"
    ]
    """<p> The headroom value in percentage used for the specified metric parameter. </p> <p>The following lists the valid values for CPU and memory utilization.</p> <ul> <li> <p>CPU utilization: <code>PERCENT_30 | PERCENT_20 | PERCENT_0</code> </p> </li> <li> <p>Memory utilization: <code>PERCENT_30 | PERCENT_20 | PERCENT_10</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CustomizableMetricParameters) -> dict:
    out: dict = {}
    if "threshold" in value:
        import capo_compute_optimizer.types.customizable_metric_threshold

        out["threshold"] = (
            capo_compute_optimizer.types.customizable_metric_threshold.serialize_aws_json_1_0(
                value["threshold"]
            )
        )
    if "headroom" in value:
        import capo_compute_optimizer.types.customizable_metric_headroom

        out["headroom"] = (
            capo_compute_optimizer.types.customizable_metric_headroom.serialize_aws_json_1_0(
                value["headroom"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CustomizableMetricParameters:
    out: CustomizableMetricParameters = {}  # type: ignore[typeddict-item]
    if data.get("threshold") is not None:
        import capo_compute_optimizer.types.customizable_metric_threshold

        out["threshold"] = (
            capo_compute_optimizer.types.customizable_metric_threshold.deserialize_aws_json_1_0(
                data["threshold"]
            )
        )
    if data.get("headroom") is not None:
        import capo_compute_optimizer.types.customizable_metric_headroom

        out["headroom"] = (
            capo_compute_optimizer.types.customizable_metric_headroom.deserialize_aws_json_1_0(
                data["headroom"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CustomizableMetricParameters) -> dict:
    out: dict = {}
    if "threshold" in value:
        import capo_compute_optimizer.types.customizable_metric_threshold

        out["threshold"] = (
            capo_compute_optimizer.types.customizable_metric_threshold.serialize_cbor(
                value["threshold"]
            )
        )
    if "headroom" in value:
        import capo_compute_optimizer.types.customizable_metric_headroom

        out["headroom"] = (
            capo_compute_optimizer.types.customizable_metric_headroom.serialize_cbor(
                value["headroom"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CustomizableMetricParameters:
    out: CustomizableMetricParameters = {}  # type: ignore[typeddict-item]
    if data.get("threshold") is not None:
        import capo_compute_optimizer.types.customizable_metric_threshold

        out["threshold"] = (
            capo_compute_optimizer.types.customizable_metric_threshold.deserialize_cbor(
                data["threshold"]
            )
        )
    if data.get("headroom") is not None:
        import capo_compute_optimizer.types.customizable_metric_headroom

        out["headroom"] = (
            capo_compute_optimizer.types.customizable_metric_headroom.deserialize_cbor(
                data["headroom"]
            )
        )
    return out
