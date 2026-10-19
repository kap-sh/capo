"""Generated from Smithy shape ``com.amazonaws.glue#RunStatementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.name_string
    import capo_glue.types.orchestration_name_string
    import capo_glue.types.orchestration_statement_code_string


class RunStatementRequest(TypedDict, closed=True):
    session_id: "capo_glue.types.name_string.NameString"
    """<p>The Session Id of the statement to be run.</p>"""
    code: "capo_glue.types.orchestration_statement_code_string.OrchestrationStatementCodeString"
    """<p>The statement code to be run.</p>"""
    request_origin: NotRequired[
        "capo_glue.types.orchestration_name_string.OrchestrationNameString"
    ]
    """<p>The origin of the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunStatementRequest) -> dict:
    out: dict = {}
    out["SessionId"] = value["session_id"]
    out["Code"] = value["code"]
    if "request_origin" in value:
        out["RequestOrigin"] = value["request_origin"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RunStatementRequest:
    out: RunStatementRequest = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    if data.get("RequestOrigin") is not None:
        out["request_origin"] = data["RequestOrigin"]
    return out
