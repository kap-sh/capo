"""Generated from Smithy shape ``com.amazonaws.storagegateway#CacheReportFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.cache_report_filter_name
    import capo_storage_gateway.types.cache_report_filter_values


class CacheReportFilter(TypedDict, closed=True):
    name: "capo_storage_gateway.types.cache_report_filter_name.CacheReportFilterName"
    """<p>The parameter name for a filter that determines which files are included or excluded from a cache report.</p> <p> <b>Valid Names:</b> </p> <p>UploadFailureReason | UploadState</p>"""
    values: (
        "capo_storage_gateway.types.cache_report_filter_values.CacheReportFilterValues"
    )
    """<p>The parameter value for a filter that determines which files are included or excluded from a cache report.</p> <p> <b>Valid <code>UploadFailureReason</code> Values:</b> </p> <p> <code>InaccessibleStorageClass</code> | <code>InvalidObjectState</code> | <code>ObjectMissing</code> | <code>S3AccessDenied</code> </p> <p> <b>Valid <code>UploadState</code> Values:</b> </p> <p> <code>FailingUpload</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CacheReportFilter) -> dict:
    out: dict = {}
    import capo_storage_gateway.types.cache_report_filter_name

    out["Name"] = (
        capo_storage_gateway.types.cache_report_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import capo_storage_gateway.types.cache_report_filter_values

    out["Values"] = (
        capo_storage_gateway.types.cache_report_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CacheReportFilter:
    out: CacheReportFilter = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        import capo_storage_gateway.types.cache_report_filter_name

        out["name"] = (
            capo_storage_gateway.types.cache_report_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        import typing

        out["name"] = typing.cast(
            "capo_storage_gateway.types.cache_report_filter_name.CacheReportFilterName",
            "",
        )
    if data.get("Values") is not None:
        import capo_storage_gateway.types.cache_report_filter_values

        out["values"] = (
            capo_storage_gateway.types.cache_report_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        out["values"] = []
    return out
