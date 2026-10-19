"""Generated from Smithy shape ``com.amazonaws.athena#GetQueryRuntimeStatisticsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.query_execution_id


class GetQueryRuntimeStatisticsInput(TypedDict, closed=True):
    query_execution_id: "capo_athena.types.query_execution_id.QueryExecutionId"
    """<p>The unique ID of the query execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQueryRuntimeStatisticsInput) -> dict:
    out: dict = {}
    out["QueryExecutionId"] = value["query_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQueryRuntimeStatisticsInput:
    out: GetQueryRuntimeStatisticsInput = {}  # type: ignore[typeddict-item]
    if data.get("QueryExecutionId") is not None:
        out["query_execution_id"] = data["QueryExecutionId"]
    else:
        out["query_execution_id"] = ""
    return out
