"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsOutputSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.findings_export_format


class FindingsOutputSummary(TypedDict, closed=True):
    format: NotRequired[
        "capo_securityhub.types.findings_export_format.FindingsExportFormat"
    ]
    """<p>The output format of the export. <code>CSV</code> produces comma-separated rows that are suitable for spreadsheets and analysis tools. <code>OCSF_JSON</code> produces newline-delimited JSON records in the Open Cybersecurity Schema Framework (OCSF) format used elsewhere in Security Hub.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingsOutputSummary) -> dict:
    out: dict = {}
    if "format" in value:
        import capo_securityhub.types.findings_export_format

        out["Format"] = capo_securityhub.types.findings_export_format.serialize_json(
            value["format"]
        )
    return out


def deserialize_json(data: dict) -> FindingsOutputSummary:
    out: FindingsOutputSummary = {}  # type: ignore[typeddict-item]
    if data.get("Format") is not None:
        import capo_securityhub.types.findings_export_format

        out["format"] = capo_securityhub.types.findings_export_format.deserialize_json(
            data["Format"]
        )
    return out
