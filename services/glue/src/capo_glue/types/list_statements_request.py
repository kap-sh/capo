"""Generated from Smithy shape ``com.amazonaws.glue#ListStatementsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.orchestration_name_string
    import capo_glue.types.orchestration_token


class ListStatementsRequest(TypedDict, closed=True):
    session_id: "capo_glue.types.name_string.NameString"
    """<p>The Session ID of the statements.</p>"""
    request_origin: NotRequired[
        "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request to list statements.</p>"""
    next_token: NotRequired["capo_glue.types.orchestration_token.OrchestrationToken"]
    """<p>A continuation token, if this is a continuation call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStatementsRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStatementsRequest:
    out: ListStatementsRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    if data.get("RequestOrigin") is not None:
        out["request_origin"] = data["RequestOrigin"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
