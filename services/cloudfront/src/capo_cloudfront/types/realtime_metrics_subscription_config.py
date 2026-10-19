"""Generated from Smithy shape ``com.amazonaws.cloudfront#RealtimeMetricsSubscriptionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudfront._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_cloudfront.types.realtime_metrics_subscription_status


class RealtimeMetricsSubscriptionConfig(TypedDict, closed=True):
    realtime_metrics_subscription_status: "capo_cloudfront.types.realtime_metrics_subscription_status.RealtimeMetricsSubscriptionStatus"
    """<p>A flag that indicates whether additional CloudWatch metrics are enabled for a given CloudFront distribution.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: RealtimeMetricsSubscriptionConfig, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_cloudfront.types.realtime_metrics_subscription_status

    capo_cloudfront.types.realtime_metrics_subscription_status.serialize_xml(
        value["realtime_metrics_subscription_status"],
        el,
        "RealtimeMetricsSubscriptionStatus",
    )


def deserialize_xml(el: Element) -> RealtimeMetricsSubscriptionConfig:
    out: RealtimeMetricsSubscriptionConfig = {}  # type: ignore[typeddict-item]
    child_realtime_metrics_subscription_status = el.find(
        "RealtimeMetricsSubscriptionStatus"
    )
    if child_realtime_metrics_subscription_status is not None:
        import capo_cloudfront.types.realtime_metrics_subscription_status

        out["realtime_metrics_subscription_status"] = (
            capo_cloudfront.types.realtime_metrics_subscription_status.deserialize_xml(
                child_realtime_metrics_subscription_status
            )
        )
    else:
        import typing

        out["realtime_metrics_subscription_status"] = typing.cast(
            "capo_cloudfront.types.realtime_metrics_subscription_status.RealtimeMetricsSubscriptionStatus",
            "",
        )
    return out
