"""Generated from Smithy shape ``com.amazonaws.sagemaker#AthenaStepMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.string256
    import capo_sagemaker.types.string1024


class AthenaStepMetadata(TypedDict, closed=True):
    query_execution_id: NotRequired["capo_sagemaker.types.string256.String256"]
    """<p>The unique identifier of the Amazon Athena query execution that was run by this step execution.</p>"""
    s3_output_location: NotRequired["capo_sagemaker.types.string1024.String1024"]
    """<p>The Amazon S3 location of the Amazon Athena query results. This is the effective output location reported by <code>GetQueryExecution</code> for the query. This value can be absent when the query uses Athena managed query results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AthenaStepMetadata) -> dict:
    out: dict = {}
    if "query_execution_id" in value:
        out["QueryExecutionId"] = value["query_execution_id"]
    if "s3_output_location" in value:
        out["S3OutputLocation"] = value["s3_output_location"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AthenaStepMetadata:
    out: AthenaStepMetadata = {}  # type: ignore[typeddict-item]
    if data.get("QueryExecutionId") is not None:
        out["query_execution_id"] = data["QueryExecutionId"]
    if data.get("S3OutputLocation") is not None:
        out["s3_output_location"] = data["S3OutputLocation"]
    return out
