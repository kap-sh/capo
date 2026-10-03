"""Generated from Smithy shape ``com.amazonaws.pinpoint#APNSMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.action
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.map_of_list_of__string


class APNSMessage(TypedDict, closed=True):
    apns_push_type: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The type of push notification to send. Valid values are:</p> <ul><li><p>alert - For a standard notification that's displayed on recipients' devices and prompts a recipient to interact with the notification.</p></li> <li><p>background - For a silent notification that delivers content in the background and isn't displayed on recipients' devices.</p></li> <li><p>complication - For a notification that contains update information for an app’s complication timeline.</p></li> <li><p>fileprovider - For a notification that signals changes to a File Provider extension.</p></li> <li><p>mdm - For a notification that tells managed devices to contact the MDM server.</p></li> <li><p>voip - For a notification that provides information about an incoming VoIP call.</p></li></ul> <p>Amazon Pinpoint specifies this value in the apns-push-type request header when it sends the notification message to APNs. If you don't specify a value for this property, Amazon Pinpoint sets the value to alert or background automatically, based on the value that you specify for the SilentPush or RawContent property of the message.</p> <p>For more information about the apns-push-type request header, see <a href="https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns">Sending Notification Requests to APNs</a> on the Apple Developer website.</p>"""
    action: NotRequired["capo_pinpoint.types.action.Action"]
    """<p>The action to occur if the recipient taps the push notification. Valid values are:</p> <ul><li><p>OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p></li> <li><p>DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS platform.</p></li> <li><p>URL - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p></li></ul>"""
    badge: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The key that indicates whether and how to modify the badge of your app's icon when the recipient receives the push notification. If this key isn't included in the dictionary, the badge doesn't change. To remove the badge, set this value to 0.</p>"""
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The body of the notification message.</p>"""
    category: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The key that indicates the notification type for the push notification. This key is a value that's defined by the identifier property of one of your app's registered categories.</p>"""
    collapse_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>An arbitrary identifier that, if assigned to multiple messages, APNs uses to coalesce the messages into a single push notification instead of delivering each message individually. This value can't exceed 64 bytes.</p> <p>Amazon Pinpoint specifies this value in the apns-collapse-id request header when it sends the notification message to APNs.</p>"""
    data: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>The JSON payload to use for a silent push notification. This payload is added to the data.pinpoint.jsonBody object of the notification.</p>"""
    media_url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL of an image or video to display in the push notification.</p>"""
    preferred_authentication_method: NotRequired[
        "capo_pinpoint.types.__string.__string"
    ]
    """<p>The authentication method that you want Amazon Pinpoint to use when authenticating with APNs, CERTIFICATE or TOKEN.</p>"""
    priority: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>para>5 - Low priority, the notification might be delayed, delivered as part of a group, or throttled.</p>/listitem> <li><p>10 - High priority, the notification is sent immediately. This is the default value. A high priority notification should trigger an alert, play a sound, or badge your app's icon on the recipient's device.</p></li>/para> <p>Amazon Pinpoint specifies this value in the apns-priority request header when it sends the notification message to APNs.</p> <p>The equivalent values for Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), are normal, for 5, and high, for 10. If you specify an FCM value for this property, Amazon Pinpoint accepts and converts the value to the corresponding APNs value.</p>"""
    raw_content: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.</p> <note><p>If you specify the raw content of an APNs push notification, the message payload has to include the content-available key. The value of the content-available key has to be an integer, and can only be 0 or 1. If you're sending a standard notification, set the value of content-available to 0. If you're sending a silent (background) notification, set the value of content-available to 1. Additionally, silent notification payloads can't include the alert, badge, or sound keys. For more information, see <a href="https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification">Generating a Remote Notification</a> and <a href="https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app">Pushing Background Updates to Your App</a> on the Apple Developer website.</p></note>"""
    silent_push: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the notification is a silent push notification. A silent (or background) push notification isn't displayed on recipients' devices. You can use silent push notifications to make small updates to your app, or to display messages in an in-app message center.</p> <p>Amazon Pinpoint uses this property to determine the correct value for the apns-push-type request header when it sends the notification message to APNs. If you specify a value of true for this property, Amazon Pinpoint sets the value for the apns-push-type header field to background.</p> <note><p>If you specify the raw content of an APNs push notification, the message payload has to include the content-available key. For silent (background) notifications, set the value of content-available to 1. Additionally, the message payload for a silent notification can't include the alert, badge, or sound keys. For more information, see <a href="https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification">Generating a Remote Notification</a> and <a href="https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/pushing_background_updates_to_your_app">Pushing Background Updates to Your App</a> on the Apple Developer website.</p> <p>Apple has indicated that they will throttle "excessive" background notifications based on current traffic volumes. To prevent your notifications being throttled, Apple recommends that you send no more than 3 silent push notifications to each recipient per hour.</p></note>"""
    sound: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The key for the sound to play when the recipient receives the push notification. The value for this key is the name of a sound file in your app's main bundle or the Library/Sounds folder in your app's data container. If the sound file can't be found or you specify default for the value, the system plays the default alert sound.</p>"""
    substitutions: NotRequired[
        "capo_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>The default message variables to use in the notification message. You can override these default variables with individual address variables.</p>"""
    thread_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The key that represents your app-specific identifier for grouping notifications. If you provide a Notification Content app extension, you can use this value to group your notifications together.</p>"""
    time_to_live: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The amount of time, in seconds, that APNs should store and attempt to deliver the push notification, if the service is unable to deliver the notification the first time. If this value is 0, APNs treats the notification as if it expires immediately and the service doesn't store or try to deliver the notification again.</p> <p>Amazon Pinpoint specifies this value in the apns-expiration request header when it sends the notification message to APNs.</p>"""
    title: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The title to display above the notification message on the recipient's device.</p>"""
    url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL to open in the recipient's default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: APNSMessage) -> dict:
    out: dict = {}
    if "apns_push_type" in value:
        out["APNSPushType"] = value["apns_push_type"]
    if "action" in value:
        import capo_pinpoint.types.action

        out["Action"] = capo_pinpoint.types.action.serialize_json(value["action"])
    if "badge" in value:
        out["Badge"] = value["badge"]
    if "body" in value:
        out["Body"] = value["body"]
    if "category" in value:
        out["Category"] = value["category"]
    if "collapse_id" in value:
        out["CollapseId"] = value["collapse_id"]
    if "data" in value:
        import capo_pinpoint.types.map_of__string

        out["Data"] = capo_pinpoint.types.map_of__string.serialize_json(value["data"])
    if "media_url" in value:
        out["MediaUrl"] = value["media_url"]
    if "preferred_authentication_method" in value:
        out["PreferredAuthenticationMethod"] = value["preferred_authentication_method"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "raw_content" in value:
        out["RawContent"] = value["raw_content"]
    if "silent_push" in value:
        out["SilentPush"] = value["silent_push"]
    if "sound" in value:
        out["Sound"] = value["sound"]
    if "substitutions" in value:
        import capo_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.serialize_json(
                value["substitutions"]
            )
        )
    if "thread_id" in value:
        out["ThreadId"] = value["thread_id"]
    if "time_to_live" in value:
        out["TimeToLive"] = value["time_to_live"]
    if "title" in value:
        out["Title"] = value["title"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> APNSMessage:
    out: APNSMessage = {}  # type: ignore[typeddict-item]
    if data.get("APNSPushType") is not None:
        out["apns_push_type"] = data["APNSPushType"]
    if data.get("Action") is not None:
        import capo_pinpoint.types.action

        out["action"] = capo_pinpoint.types.action.deserialize_json(data["Action"])
    if data.get("Badge") is not None:
        out["badge"] = data["Badge"]
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    if data.get("CollapseId") is not None:
        out["collapse_id"] = data["CollapseId"]
    if data.get("Data") is not None:
        import capo_pinpoint.types.map_of__string

        out["data"] = capo_pinpoint.types.map_of__string.deserialize_json(data["Data"])
    if data.get("MediaUrl") is not None:
        out["media_url"] = data["MediaUrl"]
    if data.get("PreferredAuthenticationMethod") is not None:
        out["preferred_authentication_method"] = data["PreferredAuthenticationMethod"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("RawContent") is not None:
        out["raw_content"] = data["RawContent"]
    if data.get("SilentPush") is not None:
        out["silent_push"] = data["SilentPush"]
    if data.get("Sound") is not None:
        out["sound"] = data["Sound"]
    if data.get("Substitutions") is not None:
        import capo_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    if data.get("ThreadId") is not None:
        out["thread_id"] = data["ThreadId"]
    if data.get("TimeToLive") is not None:
        out["time_to_live"] = data["TimeToLive"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
