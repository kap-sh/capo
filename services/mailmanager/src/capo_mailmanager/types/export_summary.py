"""Generated from Smithy shape ``com.amazonaws.mailmanager#ExportSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.export_id
    import capo_mailmanager.types.export_status


class ExportSummary(TypedDict, closed=True):
    export_id: NotRequired["capo_mailmanager.types.export_id.ExportId"]
    """<p>The unique identifier of the export job.</p>"""
    status: NotRequired["capo_mailmanager.types.export_status.ExportStatus"]
    """<p>The current status of the export job.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportSummary) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["ExportId"] = value["export_id"]
    if "status" in value:
        import capo_mailmanager.types.export_status

        out["Status"] = capo_mailmanager.types.export_status.serialize_aws_json_1_0(
            value["status"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportSummary:
    out: ExportSummary = {}  # type: ignore[typeddict-item]
    if data.get("ExportId") is not None:
        out["export_id"] = data["ExportId"]
    if data.get("Status") is not None:
        import capo_mailmanager.types.export_status

        out["status"] = capo_mailmanager.types.export_status.deserialize_aws_json_1_0(
            data["Status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExportSummary) -> dict:
    out: dict = {}
    if "export_id" in value:
        out["ExportId"] = value["export_id"]
    if "status" in value:
        import capo_mailmanager.types.export_status

        out["Status"] = capo_mailmanager.types.export_status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> ExportSummary:
    out: ExportSummary = {}  # type: ignore[typeddict-item]
    if data.get("ExportId") is not None:
        out["export_id"] = data["ExportId"]
    if data.get("Status") is not None:
        import capo_mailmanager.types.export_status

        out["status"] = capo_mailmanager.types.export_status.deserialize_cbor(
            data["Status"]
        )
    return out
