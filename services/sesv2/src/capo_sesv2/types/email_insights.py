"""Generated from Smithy shape ``com.amazonaws.sesv2#EmailInsights``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.insights_email_address
    import capo_sesv2.types.insights_events
    import capo_sesv2.types.isp


class EmailInsights(TypedDict, closed=True):
    destination: NotRequired[
        "capo_sesv2.types.insights_email_address.InsightsEmailAddress"
    ]
    """<p>The recipient of the email.</p>"""
    isp: NotRequired["capo_sesv2.types.isp.Isp"]
    """<p>The recipient's ISP (e.g., <code>Gmail</code>, <code>Yahoo</code>, etc.).</p>"""
    events: NotRequired["capo_sesv2.types.insights_events.InsightsEvents"]
    """<p>A list of events associated with the sent email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailInsights) -> dict:
    out: dict = {}
    if "destination" in value:
        out["Destination"] = value["destination"]
    if "isp" in value:
        out["Isp"] = value["isp"]
    if "events" in value:
        import capo_sesv2.types.insights_events

        out["Events"] = capo_sesv2.types.insights_events.serialize_json(value["events"])
    return out


def deserialize_json(data: dict) -> EmailInsights:
    out: EmailInsights = {}  # type: ignore[typeddict-item]
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    if data.get("Isp") is not None:
        out["isp"] = data["Isp"]
    if data.get("Events") is not None:
        import capo_sesv2.types.insights_events

        out["events"] = capo_sesv2.types.insights_events.deserialize_json(
            data["Events"]
        )
    return out


def redact_sensitive(value: EmailInsights) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "destination" in value:
        out["destination"] = "*** Sensitive Data Redacted ***"
    return out
