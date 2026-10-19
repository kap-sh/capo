"""Generated from Smithy shape ``com.amazonaws.sesv2#PutDeliverabilityDashboardOptionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.domain_deliverability_tracking_options
    import capo_sesv2.types.enabled


class PutDeliverabilityDashboardOptionRequest(TypedDict, closed=True):
    dashboard_enabled: "capo_sesv2.types.enabled.Enabled"
    """<p>Specifies whether to enable the Deliverability dashboard. To enable the dashboard, set this value to <code>true</code>.</p>"""
    subscribed_domains: NotRequired[
        "capo_sesv2.types.domain_deliverability_tracking_options.DomainDeliverabilityTrackingOptions"
    ]
    """<p>An array of objects, one for each verified domain that you use to send email and enabled the Deliverability dashboard for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDeliverabilityDashboardOptionRequest) -> dict:
    out: dict = {}
    out["DashboardEnabled"] = value["dashboard_enabled"]
    if "subscribed_domains" in value:
        import capo_sesv2.types.domain_deliverability_tracking_options

        out["SubscribedDomains"] = (
            capo_sesv2.types.domain_deliverability_tracking_options.serialize_json(
                value["subscribed_domains"]
            )
        )
    return out


def deserialize_json(data: dict) -> PutDeliverabilityDashboardOptionRequest:
    out: PutDeliverabilityDashboardOptionRequest = {}  # type: ignore[typeddict-item]
    if data.get("DashboardEnabled") is not None:
        out["dashboard_enabled"] = data["DashboardEnabled"]
    else:
        out["dashboard_enabled"] = False
    if data.get("SubscribedDomains") is not None:
        import capo_sesv2.types.domain_deliverability_tracking_options

        out["subscribed_domains"] = (
            capo_sesv2.types.domain_deliverability_tracking_options.deserialize_json(
                data["SubscribedDomains"]
            )
        )
    return out
