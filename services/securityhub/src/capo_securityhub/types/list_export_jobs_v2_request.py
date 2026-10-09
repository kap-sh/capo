"""Generated from Smithy shape ``com.amazonaws.securityhub#ListExportJobsV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.export_data_type
    import capo_securityhub.types.export_max_results
    import capo_securityhub.types.export_status
    import capo_securityhub.types.next_token


class ListExportJobsV2Request(TypedDict, closed=True):
    status: NotRequired["capo_securityhub.types.export_status.ExportStatus"]
    """<p>Filters the results to export jobs that have the specified status.</p>"""
    data_type: NotRequired["capo_securityhub.types.export_data_type.ExportDataType"]
    """<p>Filters the results to export jobs that produce the specified data type.</p>"""
    max_results: NotRequired[
        "capo_securityhub.types.export_max_results.ExportMaxResults"
    ]
    """<p>The maximum number of results to return in a single call. Valid range is 1–20.</p>"""
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token required for pagination. On your first call, set the value of this parameter to <code>NULL</code>. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportJobsV2Request) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListExportJobsV2Request:
    out: ListExportJobsV2Request = {}  # type: ignore[typeddict-item]
    return out
