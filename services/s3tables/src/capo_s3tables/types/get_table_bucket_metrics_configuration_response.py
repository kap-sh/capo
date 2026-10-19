"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketMetricsConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_s3tables.types.table_bucket_arn


class GetTableBucketMetricsConfigurationResponse(TypedDict, closed=True):
    table_bucket_arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    id: NotRequired["str"]
    """<p>The unique identifier of the metrics configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketMetricsConfigurationResponse) -> dict:
    out: dict = {}
    out["tableBucketARN"] = value["table_bucket_arn"]
    if "id" in value:
        out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> GetTableBucketMetricsConfigurationResponse:
    out: GetTableBucketMetricsConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("tableBucketARN") is not None:
        out["table_bucket_arn"] = data["tableBucketARN"]
    else:
        out["table_bucket_arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    return out
