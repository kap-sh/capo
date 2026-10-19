"""Generated from Smithy shape ``com.amazonaws.storagegateway#CancelCacheReportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.cache_report_arn


class CancelCacheReportInput(TypedDict, closed=True):
    cache_report_arn: "capo_storage_gateway.types.cache_report_arn.CacheReportARN"
    """<p>The Amazon Resource Name (ARN) of the cache report you want to cancel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelCacheReportInput) -> dict:
    out: dict = {}
    out["CacheReportARN"] = value["cache_report_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelCacheReportInput:
    out: CancelCacheReportInput = {}  # type: ignore[typeddict-item]
    if data.get("CacheReportARN") is not None:
        out["cache_report_arn"] = data["CacheReportARN"]
    else:
        out["cache_report_arn"] = ""
    return out
