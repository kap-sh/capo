"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveExportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.export_id


class GetArchiveExportRequest(TypedDict, closed=True):
    export_id: "capo_mailmanager.types.export_id.ExportId"
    """<p>The identifier of the export job to get details for.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveExportRequest) -> dict:
    out: dict = {}
    out["ExportId"] = value["export_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveExportRequest:
    out: GetArchiveExportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExportId") is not None:
        out["export_id"] = data["ExportId"]
    else:
        out["export_id"] = ""
    return out
