"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#FileDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_benefits.types.file_type
    import capo_partnercentral_benefits.types.file_uri
    import capo_partnercentral_benefits.types.timestamp


class FileDetail(TypedDict, closed=True):
    file_uri: "capo_partnercentral_benefits.types.file_uri.FileURI"
    """<p>The URI or location where the file is stored.</p>"""
    business_use_case: NotRequired["str"]
    """<p>The business purpose or use case that this file supports in the benefit application.</p>"""
    file_name: NotRequired["str"]
    """<p>The original name of the uploaded file.</p>"""
    file_status: NotRequired["str"]
    """<p>The current processing status of the file (e.g., uploaded, processing, approved, rejected).</p>"""
    file_status_reason: NotRequired["str"]
    """<p>The reason for that particulat file status.</p>"""
    file_type: NotRequired["capo_partnercentral_benefits.types.file_type.FileType"]
    """<p>The type or category of the file (e.g., document, image, spreadsheet).</p>"""
    created_by: NotRequired["str"]
    """<p>The identifier of the user who uploaded the file.</p>"""
    created_at: NotRequired["capo_partnercentral_benefits.types.timestamp.Timestamp"]
    """<p>The timestamp when the file was uploaded.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FileDetail) -> dict:
    out: dict = {}
    out["FileURI"] = value["file_uri"]
    if "business_use_case" in value:
        out["BusinessUseCase"] = value["business_use_case"]
    if "file_name" in value:
        out["FileName"] = value["file_name"]
    if "file_status" in value:
        out["FileStatus"] = value["file_status"]
    if "file_status_reason" in value:
        out["FileStatusReason"] = value["file_status_reason"]
    if "file_type" in value:
        import capo_partnercentral_benefits.types.file_type

        out["FileType"] = (
            capo_partnercentral_benefits.types.file_type.serialize_aws_json_1_0(
                value["file_type"]
            )
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "created_at" in value:
        import capo_partnercentral_benefits.types.timestamp

        out["CreatedAt"] = (
            capo_partnercentral_benefits.types.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FileDetail:
    out: FileDetail = {}  # type: ignore[typeddict-item]
    if data.get("FileURI") is not None:
        out["file_uri"] = data["FileURI"]
    else:
        out["file_uri"] = ""
    if data.get("BusinessUseCase") is not None:
        out["business_use_case"] = data["BusinessUseCase"]
    if data.get("FileName") is not None:
        out["file_name"] = data["FileName"]
    if data.get("FileStatus") is not None:
        out["file_status"] = data["FileStatus"]
    if data.get("FileStatusReason") is not None:
        out["file_status_reason"] = data["FileStatusReason"]
    if data.get("FileType") is not None:
        import capo_partnercentral_benefits.types.file_type

        out["file_type"] = (
            capo_partnercentral_benefits.types.file_type.deserialize_aws_json_1_0(
                data["FileType"]
            )
        )
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_benefits.types.timestamp

        out["created_at"] = (
            capo_partnercentral_benefits.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    return out
