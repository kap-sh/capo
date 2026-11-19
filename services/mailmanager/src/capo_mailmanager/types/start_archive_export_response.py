"""Generated from Smithy shape ``com.amazonaws.mailmanager#StartArchiveExportResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.export_id


class StartArchiveExportResponse(TypedDict, closed=True):
    export_id: NotRequired["capo_mailmanager.types.export_id.ExportId"]
    """<p>The unique identifier for the initiated export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartArchiveExportResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["ExportId"] = value["export_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StartArchiveExportResponse:
    out: StartArchiveExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExportId") is not None:
        out["export_id"] = data["ExportId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartArchiveExportResponse) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["ExportId"] = value["export_id"]
    return out


def deserialize_cbor(data: dict) -> StartArchiveExportResponse:
    out: StartArchiveExportResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExportId") is not None:
        out["export_id"] = data["ExportId"]
    return out
