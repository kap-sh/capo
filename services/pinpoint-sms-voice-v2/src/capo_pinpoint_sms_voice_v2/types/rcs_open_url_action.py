"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsOpenUrlAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_open_url_value
    import capo_pinpoint_sms_voice_v2.types.rcs_postback_data
    import capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text


class RcsOpenUrlAction(TypedDict, closed=True):
    text: "capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text.RcsSuggestedActionText"
    """<p>The display text of the action. Maximum 25 characters.</p>"""
    postback_data: "capo_pinpoint_sms_voice_v2.types.rcs_postback_data.RcsPostbackData"
    """<p>The postback data sent to your webhook when the user taps this action. Maximum 2048 characters.</p>"""
    url: "capo_pinpoint_sms_voice_v2.types.rcs_open_url_value.RcsOpenUrlValue"
    """<p>The URL to open. Must start with https://. Maximum 2048 characters.</p>"""
    application: NotRequired["str"]
    """<p>How to open the URL. BROWSER opens in the device's default browser. WEBVIEW opens in an in-app webview.</p>"""
    webview_view_mode: NotRequired["str"]
    """<p>The display mode of the webview. Valid values are FULL, HALF, and TALL. Only applicable when Application is WEBVIEW.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsOpenUrlAction) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    out["PostbackData"] = value["postback_data"]
    out["Url"] = value["url"]
    if "application" in value:
        out["Application"] = value["application"]
    if "webview_view_mode" in value:
        out["WebviewViewMode"] = value["webview_view_mode"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsOpenUrlAction:
    out: RcsOpenUrlAction = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    if data.get("PostbackData") is not None:
        out["postback_data"] = data["PostbackData"]
    else:
        out["postback_data"] = ""
    if data.get("Url") is not None:
        out["url"] = data["Url"]
    else:
        out["url"] = ""
    if data.get("Application") is not None:
        out["application"] = data["Application"]
    if data.get("WebviewViewMode") is not None:
        out["webview_view_mode"] = data["WebviewViewMode"]
    return out
