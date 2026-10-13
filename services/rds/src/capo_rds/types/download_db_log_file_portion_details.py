"""Generated from Smithy shape ``com.amazonaws.rds#DownloadDBLogFilePortionDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.boolean
    import capo_rds.types.sensitive_string
    import capo_rds.types.string


class DownloadDBLogFilePortionDetails(TypedDict, closed=True):
    log_file_data: NotRequired["capo_rds.types.sensitive_string.SensitiveString"]
    """<p>Entries from the specified log file.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>A pagination token that can be used in a later <code>DownloadDBLogFilePortion</code> request.</p>"""
    additional_data_pending: NotRequired["capo_rds.types.boolean.Boolean"]
    """<p>A Boolean value that, if true, indicates there is more data to be downloaded.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DownloadDBLogFilePortionDetails, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "log_file_data" in value:
        pairs.append((f"{key_prefix}LogFileData", str(value["log_file_data"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "additional_data_pending" in value:
        pairs.append(
            (
                f"{key_prefix}AdditionalDataPending",
                "true" if value["additional_data_pending"] else "false",
            )
        )


def deserialize_query(el: Element) -> DownloadDBLogFilePortionDetails:
    out: DownloadDBLogFilePortionDetails = {}  # type: ignore[typeddict-item]
    child_log_file_data = el.find("LogFileData")
    if child_log_file_data is not None:
        out["log_file_data"] = str(child_log_file_data.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_additional_data_pending = el.find("AdditionalDataPending")
    if child_additional_data_pending is not None:
        out["additional_data_pending"] = (
            child_additional_data_pending.text or ""
        ).lower() == "true"
    return out


def redact_sensitive(value: DownloadDBLogFilePortionDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "log_file_data" in value:
        out["log_file_data"] = "*** Sensitive Data Redacted ***"
    return out
