"""Generated from Smithy shape ``com.amazonaws.securityhub#FindingsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.findings_export_format
    import capo_securityhub.types.findings_selected_field_list
    import capo_securityhub.types.ocsf_finding_filters


class FindingsOutput(TypedDict, closed=True):
    format: NotRequired[
        "capo_securityhub.types.findings_export_format.FindingsExportFormat"
    ]
    """<p>The output format of the export. <code>CSV</code> produces comma-separated rows that are suitable for spreadsheets and analysis tools. <code>OCSF_JSON</code> produces newline-delimited JSON records in the Open Cybersecurity Schema Framework (OCSF) format used elsewhere in Security Hub.</p>"""
    filters: NotRequired[
        "capo_securityhub.types.ocsf_finding_filters.OcsfFindingFilters"
    ]
    """<p>An optional set of OCSF finding filters that restrict which findings are exported. The filter structure is the same as the one used by <code>GetFindingsV2</code>. If you omit this member, Security Hub exports all findings available to the caller. When echoed by <code>GetExportJobV2</code>, relative date ranges are returned unresolved.</p>"""
    selected_fields: NotRequired[
        "capo_securityhub.types.findings_selected_field_list.FindingsSelectedFieldList"
    ]
    """<p>The OCSF finding fields to include in the export, specified as OCSF field paths (for example, <code>finding_info.title</code> or <code>severity</code>). You can specify from 1 to 50 fields.</p> <p>Whether this parameter is required depends on the value of <code>Format</code>:</p> <ul> <li> <p> <code>CSV</code> – Required. The field paths that you specify become the columns of the output, in the order that you provide them. If you omit this parameter, the request returns a <code>ValidationException</code>.</p> </li> <li> <p> <code>OCSF_JSON</code> – Not supported. This format includes each finding in full, so field selection doesn't apply. If you specify this parameter, the request returns a <code>ValidationException</code>.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingsOutput) -> dict:
    out: dict = {}
    if "format" in value:
        import capo_securityhub.types.findings_export_format

        out["Format"] = capo_securityhub.types.findings_export_format.serialize_json(
            value["format"]
        )
    if "filters" in value:
        import capo_securityhub.types.ocsf_finding_filters

        out["Filters"] = capo_securityhub.types.ocsf_finding_filters.serialize_json(
            value["filters"]
        )
    if "selected_fields" in value:
        import capo_securityhub.types.findings_selected_field_list

        out["SelectedFields"] = (
            capo_securityhub.types.findings_selected_field_list.serialize_json(
                value["selected_fields"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingsOutput:
    out: FindingsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Format") is not None:
        import capo_securityhub.types.findings_export_format

        out["format"] = capo_securityhub.types.findings_export_format.deserialize_json(
            data["Format"]
        )
    if data.get("Filters") is not None:
        import capo_securityhub.types.ocsf_finding_filters

        out["filters"] = capo_securityhub.types.ocsf_finding_filters.deserialize_json(
            data["Filters"]
        )
    if data.get("SelectedFields") is not None:
        import capo_securityhub.types.findings_selected_field_list

        out["selected_fields"] = (
            capo_securityhub.types.findings_selected_field_list.deserialize_json(
                data["SelectedFields"]
            )
        )
    return out
