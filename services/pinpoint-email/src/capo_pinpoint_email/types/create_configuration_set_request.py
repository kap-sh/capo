"""Generated from Smithy shape ``com.amazonaws.pinpointemail#CreateConfigurationSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_email.types.configuration_set_name
    import capo_pinpoint_email.types.delivery_options
    import capo_pinpoint_email.types.reputation_options
    import capo_pinpoint_email.types.sending_options
    import capo_pinpoint_email.types.tag_list
    import capo_pinpoint_email.types.tracking_options


class CreateConfigurationSetRequest(TypedDict, closed=True):
    configuration_set_name: (
        "capo_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    )
    """<p>The name of the configuration set.</p>"""
    tracking_options: NotRequired[
        "capo_pinpoint_email.types.tracking_options.TrackingOptions"
    ]
    """<p>An object that defines the open and click tracking options for emails that you send using the configuration set.</p>"""
    delivery_options: NotRequired[
        "capo_pinpoint_email.types.delivery_options.DeliveryOptions"
    ]
    """<p>An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.</p>"""
    reputation_options: NotRequired[
        "capo_pinpoint_email.types.reputation_options.ReputationOptions"
    ]
    """<p>An object that defines whether or not Amazon Pinpoint collects reputation metrics for the emails that you send that use the configuration set.</p>"""
    sending_options: NotRequired[
        "capo_pinpoint_email.types.sending_options.SendingOptions"
    ]
    """<p>An object that defines whether or not Amazon Pinpoint can send email that you send using the configuration set.</p>"""
    tags: NotRequired["capo_pinpoint_email.types.tag_list.TagList"]
    """<p>An array of objects that define the tags (keys and values) that you want to associate with the configuration set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfigurationSetRequest) -> dict:
    out: dict = {}
    out["ConfigurationSetName"] = value["configuration_set_name"]
    if "tracking_options" in value:
        import capo_pinpoint_email.types.tracking_options

        out["TrackingOptions"] = (
            capo_pinpoint_email.types.tracking_options.serialize_json(
                value["tracking_options"]
            )
        )
    if "delivery_options" in value:
        import capo_pinpoint_email.types.delivery_options

        out["DeliveryOptions"] = (
            capo_pinpoint_email.types.delivery_options.serialize_json(
                value["delivery_options"]
            )
        )
    if "reputation_options" in value:
        import capo_pinpoint_email.types.reputation_options

        out["ReputationOptions"] = (
            capo_pinpoint_email.types.reputation_options.serialize_json(
                value["reputation_options"]
            )
        )
    if "sending_options" in value:
        import capo_pinpoint_email.types.sending_options

        out["SendingOptions"] = (
            capo_pinpoint_email.types.sending_options.serialize_json(
                value["sending_options"]
            )
        )
    if "tags" in value:
        import capo_pinpoint_email.types.tag_list

        out["Tags"] = capo_pinpoint_email.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateConfigurationSetRequest:
    out: CreateConfigurationSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationSetName") is not None:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    else:
        out["configuration_set_name"] = ""
    if data.get("TrackingOptions") is not None:
        import capo_pinpoint_email.types.tracking_options

        out["tracking_options"] = (
            capo_pinpoint_email.types.tracking_options.deserialize_json(
                data["TrackingOptions"]
            )
        )
    if data.get("DeliveryOptions") is not None:
        import capo_pinpoint_email.types.delivery_options

        out["delivery_options"] = (
            capo_pinpoint_email.types.delivery_options.deserialize_json(
                data["DeliveryOptions"]
            )
        )
    if data.get("ReputationOptions") is not None:
        import capo_pinpoint_email.types.reputation_options

        out["reputation_options"] = (
            capo_pinpoint_email.types.reputation_options.deserialize_json(
                data["ReputationOptions"]
            )
        )
    if data.get("SendingOptions") is not None:
        import capo_pinpoint_email.types.sending_options

        out["sending_options"] = (
            capo_pinpoint_email.types.sending_options.deserialize_json(
                data["SendingOptions"]
            )
        )
    if data.get("Tags") is not None:
        import capo_pinpoint_email.types.tag_list

        out["tags"] = capo_pinpoint_email.types.tag_list.deserialize_json(data["Tags"])
    return out
