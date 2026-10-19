"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteOptOutListRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn


class DeleteOptOutListRequest(TypedDict, closed=True):
    opt_out_list_name: (
        "capo_pinpoint_sms_voice_v2.types.opt_out_list_name_or_arn.OptOutListNameOrArn"
    )
    """<p>The OptOutListName or OptOutListArn of the OptOutList to delete. You can use <a>DescribeOptOutLists</a> to find the values for OptOutListName and OptOutListArn.</p> <important> <p>If you are using a shared End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).</p> </important>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteOptOutListRequest) -> dict:
    out: dict = {}
    out["OptOutListName"] = value["opt_out_list_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteOptOutListRequest:
    out: DeleteOptOutListRequest = {}  # type: ignore[typeddict-item]
    if data.get("OptOutListName") is not None:
        out["opt_out_list_name"] = data["OptOutListName"]
    else:
        out["opt_out_list_name"] = ""
    return out
