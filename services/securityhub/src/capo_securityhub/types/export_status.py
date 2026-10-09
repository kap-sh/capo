"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The state of an export job. Valid values are as follows:</p> <ul> <li> <p> <code>RUNNING</code> – The job is queued or in progress.</p> </li> <li> <p> <code>SUCCEEDED</code> – The job completed and the output is available in the destination bucket.</p> </li> <li> <p> <code>FAILED</code> – The job didn't complete. See <code>FailureCode</code> and <code>FailureMessage</code>.</p> </li> <li> <p> <code>CANCELLED</code> – The job was canceled with <code>CancelExportJobV2</code>.</p> </li> </ul>"""
ExportStatus: TypeAlias = Literal[
    "RUNNING",
    "SUCCEEDED",
    "FAILED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportStatus) -> str:
    return value


def deserialize_json(data: str) -> ExportStatus:
    return cast(ExportStatus, data)
