"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RcsShowLocationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.rcs_location_label
    import capo_pinpoint_sms_voice_v2.types.rcs_postback_data
    import capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text


class RcsShowLocationAction(TypedDict, closed=True):
    text: "capo_pinpoint_sms_voice_v2.types.rcs_suggested_action_text.RcsSuggestedActionText"
    """<p>The display text of the action. Maximum 25 characters.</p>"""
    postback_data: "capo_pinpoint_sms_voice_v2.types.rcs_postback_data.RcsPostbackData"
    """<p>The postback data sent to your webhook when the user taps this action. Maximum 2048 characters.</p>"""
    latitude: "float"
    """<p>The latitude of the location. Valid values are -90 to 90.</p>"""
    longitude: "float"
    """<p>The longitude of the location. Valid values are -180 to 180.</p>"""
    label: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.rcs_location_label.RcsLocationLabel"
    ]
    """<p>An optional label for the location pin. Maximum 100 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RcsShowLocationAction) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    out["PostbackData"] = value["postback_data"]
    out["Latitude"] = (
        "NaN"
        if value["latitude"] != value["latitude"]
        else "Infinity"
        if value["latitude"] == float("inf")
        else "-Infinity"
        if value["latitude"] == float("-inf")
        else value["latitude"]
    )
    out["Longitude"] = (
        "NaN"
        if value["longitude"] != value["longitude"]
        else "Infinity"
        if value["longitude"] == float("inf")
        else "-Infinity"
        if value["longitude"] == float("-inf")
        else value["longitude"]
    )
    if "label" in value:
        out["Label"] = value["label"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RcsShowLocationAction:
    out: RcsShowLocationAction = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        out["text"] = ""
    if data.get("PostbackData") is not None:
        out["postback_data"] = data["PostbackData"]
    else:
        out["postback_data"] = ""
    if data.get("Latitude") is not None:
        out["latitude"] = float(data["Latitude"])
    else:
        out["latitude"] = 0.0
    if data.get("Longitude") is not None:
        out["longitude"] = float(data["Longitude"])
    else:
        out["longitude"] = 0.0
    if data.get("Label") is not None:
        out["label"] = data["Label"]
    return out
