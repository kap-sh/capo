"""Generated from Smithy shape ``com.amazonaws.pinpointemail#PutDeliverabilityDashboardOptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import capo_pinpoint_email.types.domain_deliverability_tracking_options
    import capo_pinpoint_email.types.enabled


class PutDeliverabilityDashboardOptionRequest(TypedDict, closed=True):
    dashboard_enabled: "capo_pinpoint_email.types.enabled.Enabled"
    """<p>Specifies whether to enable the Deliverability dashboard for your Amazon Pinpoint account. To enable the dashboard, set this value to <code>true</code>.</p>"""
    subscribed_domains: NotRequired[
        "capo_pinpoint_email.types.domain_deliverability_tracking_options.DomainDeliverabilityTrackingOptions"
    ]
    """<p>An array of objects, one for each verified domain that you use to send email and enabled the Deliverability dashboard for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDeliverabilityDashboardOptionRequest) -> dict:
    out: dict = {}
    out["DashboardEnabled"] = value["dashboard_enabled"]
    if "subscribed_domains" in value:
        import capo_pinpoint_email.types.domain_deliverability_tracking_options

        out["SubscribedDomains"] = (
            capo_pinpoint_email.types.domain_deliverability_tracking_options.serialize_json(
                value["subscribed_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutDeliverabilityDashboardOptionRequest:
    out: PutDeliverabilityDashboardOptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DashboardEnabled") is not None:
        out["dashboard_enabled"] = data["DashboardEnabled"]
    else:
        raise DeserializationError(
            "PutDeliverabilityDashboardOptionRequest.dashboard_enabled required"
        )
    if data.get("SubscribedDomains") is not None:
        import capo_pinpoint_email.types.domain_deliverability_tracking_options

        out["subscribed_domains"] = (
            capo_pinpoint_email.types.domain_deliverability_tracking_options.deserialize_json(
                data["SubscribedDomains"]
            )
        )
    return out
