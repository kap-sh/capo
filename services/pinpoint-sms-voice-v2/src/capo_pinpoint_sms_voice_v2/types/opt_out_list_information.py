"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#OptOutListInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name


class OptOutListInformation(TypedDict, closed=True):
    opt_out_list_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the OptOutList.</p>"""
    opt_out_list_name: (
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name.OptOutListName"
    )
    """<p>The name of the OptOutList.</p>"""
    created_timestamp: "datetime.datetime"
    """<p>The time when the OutOutList was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OptOutListInformation) -> dict:
    out: dict = {}
    out["OptOutListArn"] = value["opt_out_list_arn"]
    out["OptOutListName"] = value["opt_out_list_name"]
    import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        capo_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OptOutListInformation:
    out: OptOutListInformation = {}  # type: ignore[typeddict-item]
    if data.get("OptOutListArn") is not None:
        out["opt_out_list_arn"] = data["OptOutListArn"]
    else:
        raise DeserializationError("OptOutListInformation.opt_out_list_arn required")
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    else:
        raise DeserializationError("OptOutListInformation.opt_out_list_name required")
    if data.get("CreatedTimestamp") is not None:
        import capo_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError("OptOutListInformation.created_timestamp required")
    return out
