"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsExportFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The output format of an export. <code>CSV</code> produces comma-separated rows. <code>OCSF_JSON</code> produces newline-delimited JSON records in the Open Cybersecurity Schema Framework (OCSF) format.</p>"""
FindingsExportFormat: TypeAlias = Literal[
    "CSV",
    "OCSF_JSON",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingsExportFormat) -> str:
    return value


def deserialize_json(data: str) -> FindingsExportFormat:
    return cast(FindingsExportFormat, data)
