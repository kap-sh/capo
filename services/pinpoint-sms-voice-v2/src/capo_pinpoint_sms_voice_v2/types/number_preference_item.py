"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#NumberPreferenceItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.number_filter_list
    import capo_pinpoint_sms_voice_v2.types.preference_type_list


class NumberPreferenceItem(TypedDict, closed=True):
    preference_type: (
        "capo_pinpoint_sms_voice_v2.types.preference_type_list.PreferenceTypeList"
    )
    """<p>The type of match to apply to the filter values.</p> <ul> <li> <p> <code>StartsWith</code>: Returns numbers that begin with the filter value.</p> </li> <li> <p> <code>EndsWith</code>: Returns numbers that end with the filter value.</p> </li> <li> <p> <code>Contains</code>: Returns numbers that contain the filter value.</p> </li> <li> <p> <code>ExactMatch</code>: Returns the number that exactly matches the filter value.</p> </li> </ul>"""
    filter: "capo_pinpoint_sms_voice_v2.types.number_filter_list.NumberFilterList"
    """<p>The digit pattern values to match against available phone numbers, using the specified preference type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NumberPreferenceItem) -> dict:
    out: dict = {}
    import capo_pinpoint_sms_voice_v2.types.preference_type_list

    out["PreferenceType"] = (
        capo_pinpoint_sms_voice_v2.types.preference_type_list.serialize_aws_json_1_0(
            value["preference_type"]
        )
    )
    import capo_pinpoint_sms_voice_v2.types.number_filter_list

    out["Filter"] = (
        capo_pinpoint_sms_voice_v2.types.number_filter_list.serialize_aws_json_1_0(
            value["filter"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> NumberPreferenceItem:
    out: NumberPreferenceItem = {}  # type: ignore[typeddict-item]
    if data.get("PreferenceType") is not None:
        import capo_pinpoint_sms_voice_v2.types.preference_type_list

        out["preference_type"] = (
            capo_pinpoint_sms_voice_v2.types.preference_type_list.deserialize_aws_json_1_0(
                data["PreferenceType"]
            )
        )
    else:
        out["preference_type"] = []
    if data.get("Filter") is not None:
        import capo_pinpoint_sms_voice_v2.types.number_filter_list

        out["filter"] = (
            capo_pinpoint_sms_voice_v2.types.number_filter_list.deserialize_aws_json_1_0(
                data["Filter"]
            )
        )
    else:
        out["filter"] = []
    return out
