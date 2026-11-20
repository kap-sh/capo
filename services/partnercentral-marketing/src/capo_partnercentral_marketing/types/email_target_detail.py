"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#EmailTargetDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.scan_status
    import capo_partnercentral_marketing.types.timestamp


class EmailTargetDetail(TypedDict, closed=True):
    scan_status: NotRequired[
        "capo_partnercentral_marketing.types.scan_status.ScanStatus"
    ]
    """The scan verdict for the attached list."""
    attached_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """When the list was attached."""
    valid_count: NotRequired["int"]
    """Distinct usable addresses — the recipients an email activation sends to."""
    rejected_count: NotRequired["int"]
    """Rows skipped because their email cell is not a usable address."""
    duplicate_count: NotRequired["int"]
    """Rows repeating an address already counted. Not an error: each address is sent to once."""
    file_name: NotRequired["str"]
    """The display name of the uploaded file, as the partner named it, with no path: for example `Q4 leads.csv`. Absent for a list attached before the service kept the name. There is no link to the file: the list is never downloadable from the campaign."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EmailTargetDetail) -> dict:
    out: dict = {}
    if "scan_status" in value:
        import capo_partnercentral_marketing.types.scan_status

        out["ScanStatus"] = (
            capo_partnercentral_marketing.types.scan_status.serialize_cbor(
                value["scan_status"]
            )
        )
    if "attached_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["AttachedAt"] = (
            capo_partnercentral_marketing.types.timestamp.serialize_cbor(
                value["attached_at"]
            )
        )
    if "valid_count" in value:
        out["ValidCount"] = value["valid_count"]
    if "rejected_count" in value:
        out["RejectedCount"] = value["rejected_count"]
    if "duplicate_count" in value:
        out["DuplicateCount"] = value["duplicate_count"]
    if "file_name" in value:
        out["FileName"] = value["file_name"]
    return out


def deserialize_cbor(data: dict) -> EmailTargetDetail:
    out: EmailTargetDetail = {}  # type: ignore[typeddict-item]
    if data.get("ScanStatus") is not None:
        import capo_partnercentral_marketing.types.scan_status

        out["scan_status"] = (
            capo_partnercentral_marketing.types.scan_status.deserialize_cbor(
                data["ScanStatus"]
            )
        )
    if data.get("AttachedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["attached_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["AttachedAt"]
            )
        )
    if data.get("ValidCount") is not None:
        out["valid_count"] = data["ValidCount"]
    if data.get("RejectedCount") is not None:
        out["rejected_count"] = data["RejectedCount"]
    if data.get("DuplicateCount") is not None:
        out["duplicate_count"] = data["DuplicateCount"]
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    return out
