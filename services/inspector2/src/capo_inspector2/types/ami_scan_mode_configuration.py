"""Generated from Smithy shape ``com.amazonaws.inspector2#AmiScanModeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ami_scan_mode
    import capo_inspector2.types.ami_tag_filter_list


class AmiScanModeConfiguration(TypedDict, closed=True):
    scan_mode: "capo_inspector2.types.ami_scan_mode.AmiScanMode"
    """<p>The scan mode that determines whether all AMIs are scanned or only those matching the specified tags.</p>"""
    tags: NotRequired["capo_inspector2.types.ami_tag_filter_list.AmiTagFilterList"]
    """<p>The tag filters used to select which AMIs are scanned when using targeted scanning.</p>"""
    exclude_copied_amis: NotRequired["bool"]
    """<p>Whether to exclude AMIs that are copies of other AMIs from scanning.</p>"""
    exclude_backup_dlm_amis: NotRequired["bool"]
    """<p>Whether to exclude AMIs created by Amazon Data Lifecycle Manager (DLM) backups from scanning.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AmiScanModeConfiguration) -> dict:
    out: dict = {}
    out["scanMode"] = value["scan_mode"]
    if "tags" in value:
        import capo_inspector2.types.ami_tag_filter_list

        out["tags"] = capo_inspector2.types.ami_tag_filter_list.serialize_json(
            value["tags"]
        )
    if "exclude_copied_amis" in value:
        out["excludeCopiedAmis"] = value["exclude_copied_amis"]
    if "exclude_backup_dlm_amis" in value:
        out["excludeBackupDlmAmis"] = value["exclude_backup_dlm_amis"]
    return out


def deserialize_json(data: dict) -> AmiScanModeConfiguration:
    out: AmiScanModeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scanMode") is not None:
        out["scan_mode"] = data["scanMode"]
    else:
        out["scan_mode"] = ""
    if data.get("tags") is not None:
        import capo_inspector2.types.ami_tag_filter_list

        out["tags"] = capo_inspector2.types.ami_tag_filter_list.deserialize_json(
            data["tags"]
        )
    if data.get("excludeCopiedAmis") is not None:
        out["exclude_copied_amis"] = data["excludeCopiedAmis"]
    if data.get("excludeBackupDlmAmis") is not None:
        out["exclude_backup_dlm_amis"] = data["excludeBackupDlmAmis"]
    return out
