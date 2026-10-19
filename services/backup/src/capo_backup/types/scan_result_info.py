"""Generated from Smithy shape ``com.amazonaws.backup#ScanResultInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.scan_result_status


class ScanResultInfo(TypedDict, closed=True):
    scan_result_status: "capo_backup.types.scan_result_status.ScanResultStatus"
    """<p>The status of the scan results.</p> <p>Valid values: <code>THREATS_FOUND</code> | <code>NO_THREATS_FOUND</code> | <code>UNKNOWN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanResultInfo) -> dict:
    out: dict = {}
    import capo_backup.types.scan_result_status

    out["ScanResultStatus"] = capo_backup.types.scan_result_status.serialize_json(
        value["scan_result_status"]
    )
    return out


def deserialize_json(data: dict) -> ScanResultInfo:
    out: ScanResultInfo = {}  # type: ignore[typeddict-item]
    if data.get("ScanResultStatus") is not None:
        import capo_backup.types.scan_result_status

        out["scan_result_status"] = (
            capo_backup.types.scan_result_status.deserialize_json(
                data["ScanResultStatus"]
            )
        )
    else:
        import typing

        out["scan_result_status"] = typing.cast(
            "capo_backup.types.scan_result_status.ScanResultStatus", ""
        )
    return out
