"""Generated from Smithy shape ``com.amazonaws.sesv2#MessageInsightsFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.email_address_filter_list
    import capo_sesv2.types.email_subject_filter_list
    import capo_sesv2.types.isp_filter_list
    import capo_sesv2.types.last_delivery_event_list
    import capo_sesv2.types.last_engagement_event_list
    import capo_sesv2.types.tenant_name_filter_list


class MessageInsightsFilters(TypedDict, closed=True):
    from_email_address: NotRequired[
        "capo_sesv2.types.email_address_filter_list.EmailAddressFilterList"
    ]
    """<p>The from address used to send the message.</p>"""
    destination: NotRequired[
        "capo_sesv2.types.email_address_filter_list.EmailAddressFilterList"
    ]
    """<p>The recipient's email address.</p>"""
    subject: NotRequired[
        "capo_sesv2.types.email_subject_filter_list.EmailSubjectFilterList"
    ]
    """<p>The subject line of the message.</p>"""
    isp: NotRequired["capo_sesv2.types.isp_filter_list.IspFilterList"]
    """<p>The recipient's ISP (e.g., <code>Gmail</code>, <code>Yahoo</code>, etc.).</p>"""
    tenant_name: NotRequired[
        "capo_sesv2.types.tenant_name_filter_list.TenantNameFilterList"
    ]
    """<p>The name of the tenant used when sending the message.</p>"""
    last_delivery_event: NotRequired[
        "capo_sesv2.types.last_delivery_event_list.LastDeliveryEventList"
    ]
    """<p> The last delivery-related event for the email, where the ordering is as follows: <code>SEND</code> < <code>BOUNCE</code> < <code>DELIVERY</code> < <code>COMPLAINT</code>. </p>"""
    last_engagement_event: NotRequired[
        "capo_sesv2.types.last_engagement_event_list.LastEngagementEventList"
    ]
    """<p> The last engagement-related event for the email, where the ordering is as follows: <code>OPEN</code> < <code>CLICK</code>. </p> <p> Engagement events are only available if <a href="https://docs.aws.amazon.com/ses/latest/dg/vdm-settings.html">Engagement tracking</a> is enabled. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageInsightsFilters) -> dict:
    out: dict = {}
    if "from_email_address" in value:
        import capo_sesv2.types.email_address_filter_list

        out["FromEmailAddress"] = (
            capo_sesv2.types.email_address_filter_list.serialize_json(
                value["from_email_address"]
            )
        )
    if "destination" in value:
        import capo_sesv2.types.email_address_filter_list

        out["Destination"] = capo_sesv2.types.email_address_filter_list.serialize_json(
            value["destination"]
        )
    if "subject" in value:
        import capo_sesv2.types.email_subject_filter_list

        out["Subject"] = capo_sesv2.types.email_subject_filter_list.serialize_json(
            value["subject"]
        )
    if "isp" in value:
        import capo_sesv2.types.isp_filter_list

        out["Isp"] = capo_sesv2.types.isp_filter_list.serialize_json(value["isp"])
    if "tenant_name" in value:
        import capo_sesv2.types.tenant_name_filter_list

        out["TenantName"] = capo_sesv2.types.tenant_name_filter_list.serialize_json(
            value["tenant_name"]
        )
    if "last_delivery_event" in value:
        import capo_sesv2.types.last_delivery_event_list

        out["LastDeliveryEvent"] = (
            capo_sesv2.types.last_delivery_event_list.serialize_json(
                value["last_delivery_event"]
            )
        )
    if "last_engagement_event" in value:
        import capo_sesv2.types.last_engagement_event_list

        out["LastEngagementEvent"] = (
            capo_sesv2.types.last_engagement_event_list.serialize_json(
                value["last_engagement_event"]
            )
        )
    return out


def deserialize_json(data: dict) -> MessageInsightsFilters:
    out: MessageInsightsFilters = {}  # type: ignore[typeddict-item]
    if data.get("FromEmailAddress") is not None:
        import capo_sesv2.types.email_address_filter_list

        out["from_email_address"] = (
            capo_sesv2.types.email_address_filter_list.deserialize_json(
                data["FromEmailAddress"]
            )
        )
    if data.get("Destination") is not None:
        import capo_sesv2.types.email_address_filter_list

        out["destination"] = (
            capo_sesv2.types.email_address_filter_list.deserialize_json(
                data["Destination"]
            )
        )
    if data.get("Subject") is not None:
        import capo_sesv2.types.email_subject_filter_list

        out["subject"] = capo_sesv2.types.email_subject_filter_list.deserialize_json(
            data["Subject"]
        )
    if data.get("Isp") is not None:
        import capo_sesv2.types.isp_filter_list

        out["isp"] = capo_sesv2.types.isp_filter_list.deserialize_json(data["Isp"])
    if data.get("TenantName") is not None:
        import capo_sesv2.types.tenant_name_filter_list

        out["tenant_name"] = capo_sesv2.types.tenant_name_filter_list.deserialize_json(
            data["TenantName"]
        )
    if data.get("LastDeliveryEvent") is not None:
        import capo_sesv2.types.last_delivery_event_list

        out["last_delivery_event"] = (
            capo_sesv2.types.last_delivery_event_list.deserialize_json(
                data["LastDeliveryEvent"]
            )
        )
    if data.get("LastEngagementEvent") is not None:
        import capo_sesv2.types.last_engagement_event_list

        out["last_engagement_event"] = (
            capo_sesv2.types.last_engagement_event_list.deserialize_json(
                data["LastEngagementEvent"]
            )
        )
    return out
