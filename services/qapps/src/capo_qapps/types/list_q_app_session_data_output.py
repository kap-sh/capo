"""Generated from Smithy shape ``com.amazonaws.qapps#ListQAppSessionDataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.q_app_session_data_list
    import capo_qapps.types.uuid


class ListQAppSessionDataOutput(TypedDict, closed=True):
    session_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App data collection session.</p>"""
    session_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Q App data collection session.</p>"""
    session_data: NotRequired[
        "capo_qapps.types.q_app_session_data_list.QAppSessionDataList"
    ]
    """<p>The collected responses of a Q App session.</p>"""
    next_token: NotRequired["str"]
    """<p> The pagination token that indicates the next set of results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListQAppSessionDataOutput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    if "session_data" in value:
        import capo_qapps.types.q_app_session_data_list

        out["sessionData"] = capo_qapps.types.q_app_session_data_list.serialize_json(
            value["session_data"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListQAppSessionDataOutput:
    out: ListQAppSessionDataOutput = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("sessionData") is not None:
        import capo_qapps.types.q_app_session_data_list

        out["session_data"] = capo_qapps.types.q_app_session_data_list.deserialize_json(
            data["sessionData"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
