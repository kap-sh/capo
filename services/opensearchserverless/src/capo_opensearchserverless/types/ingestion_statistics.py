"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IngestionStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.s3_statistics


class IngestionStatistics(TypedDict, closed=True):
    s3: NotRequired["capo_opensearchserverless.types.s3_statistics.S3Statistics"]
    """<p>Processing statistics for the Amazon S3 source.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IngestionStatistics) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_opensearchserverless.types.s3_statistics

        out["s3"] = (
            capo_opensearchserverless.types.s3_statistics.serialize_aws_json_1_0(
                value["s3"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IngestionStatistics:
    out: IngestionStatistics = {}  # type: ignore[typeddict-item]
    if data.get("s3") is not None:
        import capo_opensearchserverless.types.s3_statistics

        out["s3"] = (
            capo_opensearchserverless.types.s3_statistics.deserialize_aws_json_1_0(
                data["s3"]
            )
        )
    return out
