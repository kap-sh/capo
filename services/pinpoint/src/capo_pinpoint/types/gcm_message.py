"""Generated from Smithy shape ``com.amazonaws.pinpoint#GCMMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.action
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.map_of_list_of__string


class GCMMessage(TypedDict, closed=True):
    action: NotRequired["capo_pinpoint.types.action.Action"]
    """<p>The action to occur if the recipient taps the push notification. Valid values are:</p> <ul><li><p>OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.</p></li> <li><p>DEEP_LINK - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.</p></li> <li><p>URL - The default mobile browser on the recipient's device opens and loads the web page at a URL that you specify.</p></li></ul>"""
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The body of the notification message.</p>"""
    collapse_key: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>An arbitrary string that identifies a group of messages that can be collapsed to ensure that only the last message is sent when delivery can resume. This helps avoid sending too many instances of the same messages when the recipient's device comes online again or becomes active.</p> <p>Amazon Pinpoint specifies this value in the Firebase Cloud Messaging (FCM) collapse_key parameter when it sends the notification message to FCM.</p>"""
    data: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<p>The JSON data payload to use for the push notification, if the notification is a silent push notification. This payload is added to the data.pinpoint.jsonBody object of the notification.</p>"""
    icon_reference: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The icon image name of the asset saved in your app.</p>"""
    image_icon_url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL of the large icon image to display in the content view of the push notification.</p>"""
    image_url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL of an image to display in the push notification.</p>"""
    preferred_authentication_method: NotRequired[
        "capo_pinpoint.types.__string.__string"
    ]
    """<p>The preferred authentication method, with valid values "KEY" or "TOKEN". If a value isn't provided then the <b>DefaultAuthenticationMethod</b> is used.</p>"""
    priority: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>para>normal – The notification might be delayed. Delivery is optimized for battery usage on the recipient's device. Use this value unless immediate delivery is required.</p>/listitem> <li><p>high – The notification is sent immediately and might wake a sleeping device.</p></li>/para> <p>Amazon Pinpoint specifies this value in the FCM priority parameter when it sends the notification message to FCM.</p> <p>The equivalent values for Apple Push Notification service (APNs) are 5, for normal, and 10, for high. If you specify an APNs value for this property, Amazon Pinpoint accepts and converts the value to the corresponding FCM value.</p>"""
    raw_content: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The raw, JSON-formatted string to use as the payload for the notification message. If specified, this value overrides all other content for the message.</p>"""
    restricted_package_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The package name of the application where registration tokens must match in order for the recipient to receive the message.</p>"""
    silent_push: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether the notification is a silent push notification, which is a push notification that doesn't display on a recipient's device. Silent push notifications can be used for cases such as updating an app's configuration or supporting phone home functionality.</p>"""
    small_image_icon_url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL of the small icon image to display in the status bar and the content view of the push notification.</p>"""
    sound: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The sound to play when the recipient receives the push notification. You can use the default stream or specify the file name of a sound resource that's bundled in your app. On an Android platform, the sound file must reside in /res/raw/.</p>"""
    substitutions: NotRequired[
        "capo_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>The default message variables to use in the notification message. You can override the default variables with individual address variables.</p>"""
    time_to_live: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The amount of time, in seconds, that FCM should store and attempt to deliver the push notification, if the service is unable to deliver the notification the first time. If you don't specify this value, FCM defaults to the maximum value, which is 2,419,200 seconds (28 days).</p> <p>Amazon Pinpoint specifies this value in the FCM time_to_live parameter when it sends the notification message to FCM.</p>"""
    title: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The title to display above the notification message on the recipient's device.</p>"""
    url: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The URL to open in the recipient's default mobile browser, if a recipient taps the push notification and the value of the Action property is URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GCMMessage) -> dict:
    out: dict = {}
    if "action" in value:
        import capo_pinpoint.types.action

        out["Action"] = capo_pinpoint.types.action.serialize_json(value["action"])
    if "body" in value:
        out["Body"] = value["body"]
    if "collapse_key" in value:
        out["CollapseKey"] = value["collapse_key"]
    if "data" in value:
        import capo_pinpoint.types.map_of__string

        out["Data"] = capo_pinpoint.types.map_of__string.serialize_json(value["data"])
    if "icon_reference" in value:
        out["IconReference"] = value["icon_reference"]
    if "image_icon_url" in value:
        out["ImageIconUrl"] = value["image_icon_url"]
    if "image_url" in value:
        out["ImageUrl"] = value["image_url"]
    if "preferred_authentication_method" in value:
        out["PreferredAuthenticationMethod"] = value["preferred_authentication_method"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    if "raw_content" in value:
        out["RawContent"] = value["raw_content"]
    if "restricted_package_name" in value:
        out["RestrictedPackageName"] = value["restricted_package_name"]
    if "silent_push" in value:
        out["SilentPush"] = value["silent_push"]
    if "small_image_icon_url" in value:
        out["SmallImageIconUrl"] = value["small_image_icon_url"]
    if "sound" in value:
        out["Sound"] = value["sound"]
    if "substitutions" in value:
        import capo_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.serialize_json(
                value["substitutions"]
            )
        )
    if "time_to_live" in value:
        out["TimeToLive"] = value["time_to_live"]
    if "title" in value:
        out["Title"] = value["title"]
    if "url" in value:
        out["Url"] = value["url"]
    return out


def deserialize_json(data: dict) -> GCMMessage:
    out: GCMMessage = {}  # type: ignore[typeddict-item]
    if data.get("Action") is not None:
        import capo_pinpoint.types.action

        out["action"] = capo_pinpoint.types.action.deserialize_json(data["Action"])
    if data.get("Body") is not None:
        out["body"] = data["Body"]
    if data.get("CollapseKey") is not None:
        out["collapse_key"] = data["CollapseKey"]
    if data.get("Data") is not None:
        import capo_pinpoint.types.map_of__string

        out["data"] = capo_pinpoint.types.map_of__string.deserialize_json(data["Data"])
    if data.get("IconReference") is not None:
        out["icon_reference"] = data["IconReference"]
    if data.get("ImageIconUrl") is not None:
        out["image_icon_url"] = data["ImageIconUrl"]
    if data.get("ImageUrl") is not None:
        out["image_url"] = data["ImageUrl"]
    if data.get("PreferredAuthenticationMethod") is not None:
        out["preferred_authentication_method"] = data["PreferredAuthenticationMethod"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    if data.get("RawContent") is not None:
        out["raw_content"] = data["RawContent"]
    if data.get("RestrictedPackageName") is not None:
        out["restricted_package_name"] = data["RestrictedPackageName"]
    if data.get("SilentPush") is not None:
        out["silent_push"] = data["SilentPush"]
    if data.get("SmallImageIconUrl") is not None:
        out["small_image_icon_url"] = data["SmallImageIconUrl"]
    if data.get("Sound") is not None:
        out["sound"] = data["Sound"]
    if data.get("Substitutions") is not None:
        import capo_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    if data.get("TimeToLive") is not None:
        out["time_to_live"] = data["TimeToLive"]
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    return out
