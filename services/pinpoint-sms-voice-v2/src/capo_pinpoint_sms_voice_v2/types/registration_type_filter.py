"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#RegistrationTypeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.filter_value_list
    import capo_pinpoint_sms_voice_v2.types.registration_type_filter_name


class RegistrationTypeFilter(TypedDict, closed=True):
    name: "capo_pinpoint_sms_voice_v2.types.registration_type_filter_name.RegistrationTypeFilterName"
    """<p>The name of the attribute to filter on.</p>"""
    values: "capo_pinpoint_sms_voice_v2.types.filter_value_list.FilterValueList"
    """<p>An array of values to filter on.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationTypeFilter) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_pinpoint_sms_voice_v2.types.filter_value_list

    out["Values"] = (
        capo_pinpoint_sms_voice_v2.types.filter_value_list.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RegistrationTypeFilter:
    out: RegistrationTypeFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Values") is not None:
        import capo_pinpoint_sms_voice_v2.types.filter_value_list

        out["values"] = (
            capo_pinpoint_sms_voice_v2.types.filter_value_list.deserialize_aws_json_1_0(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
