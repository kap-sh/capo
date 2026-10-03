"""Generated from Smithy shape ``com.amazonaws.pinpoint#PushNotificationTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.android_push_notification_template
    import capo_pinpoint.types.apns_push_notification_template
    import capo_pinpoint.types.default_push_notification_template
    import capo_pinpoint.types.map_of__string


class PushNotificationTemplateRequest(TypedDict, closed=True):
    adm: NotRequired[
        "capo_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template to use for the ADM (Amazon Device Messaging) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    apns: NotRequired[
        "capo_pinpoint.types.apns_push_notification_template.APNSPushNotificationTemplate"
    ]
    """<p>The message template to use for the APNs (Apple Push Notification service) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    baidu: NotRequired[
        "capo_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template to use for the Baidu (Baidu Cloud Push) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    default: NotRequired[
        "capo_pinpoint.types.default_push_notification_template.DefaultPushNotificationTemplate"
    ]
    """<p>The default message template to use for push notification channels.</p>"""
    default_substitutions: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message that's based on the template, you can override these defaults with message-specific and address-specific variables and values.</p>"""
    gcm: NotRequired[
        "capo_pinpoint.types.android_push_notification_template.AndroidPushNotificationTemplate"
    ]
    """<p>The message template to use for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).</p>"""
    recommender_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the recommender model to use for the message template. Amazon Pinpoint uses this value to determine how to retrieve and process data from a recommender model when it sends messages that use the template, if the template contains message variables for recommendation data.</p>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<note><p>As of <b>22-05-2023</b> tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html">Tags</a> in the <i>API Reference for Amazon Pinpoint</i>, <a href="https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html">resourcegroupstaggingapi</a> commands in the <i>AWS Command Line Interface Documentation</i> or <a href="https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html">resourcegroupstaggingapi</a> in the <i>AWS SDK</i>.</p></note> <p>(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A custom description of the message template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PushNotificationTemplateRequest) -> dict:
    out: dict = {}
    if "adm" in value:
        import capo_pinpoint.types.android_push_notification_template

        out["ADM"] = (
            capo_pinpoint.types.android_push_notification_template.serialize_json(
                value["adm"]
            )
        )
    if "apns" in value:
        import capo_pinpoint.types.apns_push_notification_template

        out["APNS"] = (
            capo_pinpoint.types.apns_push_notification_template.serialize_json(
                value["apns"]
            )
        )
    if "baidu" in value:
        import capo_pinpoint.types.android_push_notification_template

        out["Baidu"] = (
            capo_pinpoint.types.android_push_notification_template.serialize_json(
                value["baidu"]
            )
        )
    if "default" in value:
        import capo_pinpoint.types.default_push_notification_template

        out["Default"] = (
            capo_pinpoint.types.default_push_notification_template.serialize_json(
                value["default"]
            )
        )
    if "default_substitutions" in value:
        out["DefaultSubstitutions"] = value["default_substitutions"]
    if "gcm" in value:
        import capo_pinpoint.types.android_push_notification_template

        out["GCM"] = (
            capo_pinpoint.types.android_push_notification_template.serialize_json(
                value["gcm"]
            )
        )
    if "recommender_id" in value:
        out["RecommenderId"] = value["recommender_id"]
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    if "template_description" in value:
        out["TemplateDescription"] = value["template_description"]
    return out


def deserialize_json(data: dict) -> PushNotificationTemplateRequest:
    out: PushNotificationTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("ADM") is not None:
        import capo_pinpoint.types.android_push_notification_template

        out["adm"] = (
            capo_pinpoint.types.android_push_notification_template.deserialize_json(
                data["ADM"]
            )
        )
    if data.get("APNS") is not None:
        import capo_pinpoint.types.apns_push_notification_template

        out["apns"] = (
            capo_pinpoint.types.apns_push_notification_template.deserialize_json(
                data["APNS"]
            )
        )
    if data.get("Baidu") is not None:
        import capo_pinpoint.types.android_push_notification_template

        out["baidu"] = (
            capo_pinpoint.types.android_push_notification_template.deserialize_json(
                data["Baidu"]
            )
        )
    if data.get("Default") is not None:
        import capo_pinpoint.types.default_push_notification_template

        out["default"] = (
            capo_pinpoint.types.default_push_notification_template.deserialize_json(
                data["Default"]
            )
        )
    if data.get("DefaultSubstitutions") is not None:
        out["default_substitutions"] = data["DefaultSubstitutions"]
    if data.get("GCM") is not None:
        import capo_pinpoint.types.android_push_notification_template

        out["gcm"] = (
            capo_pinpoint.types.android_push_notification_template.deserialize_json(
                data["GCM"]
            )
        )
    if data.get("RecommenderId") is not None:
        out["recommender_id"] = data["RecommenderId"]
    if data.get("tags") is not None:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    if data.get("TemplateDescription") is not None:
        out["template_description"] = data["TemplateDescription"]
    return out
