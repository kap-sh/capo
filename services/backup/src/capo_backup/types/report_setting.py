"""Generated from Smithy shape ``com.amazonaws.backup#ReportSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.integer
    import capo_backup.types.string
    import capo_backup.types.string_list


class ReportSetting(TypedDict, closed=True):
    report_template: "capo_backup.types.string.string"
    """<p>Identifies the report template for the report. Reports are built using a report template. The report templates are:</p> <p> <code>RESOURCE_COMPLIANCE_REPORT | CONTROL_COMPLIANCE_REPORT | BACKUP_JOB_REPORT | COPY_JOB_REPORT | RESTORE_JOB_REPORT | SCAN_JOB_REPORT</code> </p>"""
    framework_arns: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>The Amazon Resource Names (ARNs) of the frameworks a report covers.</p>"""
    number_of_frameworks: "capo_backup.types.integer.integer"
    """<p>The number of frameworks a report covers.</p>"""
    accounts: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>These are the accounts to be included in the report.</p> <p>Use string value of <code>ROOT</code> to include all organizational units.</p>"""
    organization_units: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>These are the Organizational Units to be included in the report.</p>"""
    regions: NotRequired["capo_backup.types.string_list.stringList"]
    """<p>These are the Regions to be included in the report.</p> <p>Use the wildcard as the string value to include all Regions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReportSetting) -> dict:
    out: dict = {}
    out["ReportTemplate"] = value["report_template"]
    if "framework_arns" in value:
        import capo_backup.types.string_list

        out["FrameworkArns"] = capo_backup.types.string_list.serialize_json(
            value["framework_arns"]
        )
    out["NumberOfFrameworks"] = value.get("number_of_frameworks", 0)
    if "accounts" in value:
        import capo_backup.types.string_list

        out["Accounts"] = capo_backup.types.string_list.serialize_json(
            value["accounts"]
        )
    if "organization_units" in value:
        import capo_backup.types.string_list

        out["OrganizationUnits"] = capo_backup.types.string_list.serialize_json(
            value["organization_units"]
        )
    if "regions" in value:
        import capo_backup.types.string_list

        out["Regions"] = capo_backup.types.string_list.serialize_json(value["regions"])
    return out


def deserialize_json(data: dict) -> ReportSetting:
    out: ReportSetting = {}  # type: ignore[typeddict-item]
    if data.get("ReportTemplate") is not None:
        out["report_template"] = data["ReportTemplate"]
    else:
        out["report_template"] = ""
    if data.get("FrameworkArns") is not None:
        import capo_backup.types.string_list

        out["framework_arns"] = capo_backup.types.string_list.deserialize_json(
            data["FrameworkArns"]
        )
    if data.get("NumberOfFrameworks") is not None:
        out["number_of_frameworks"] = data["NumberOfFrameworks"]
    else:
        out["number_of_frameworks"] = 0
    if data.get("Accounts") is not None:
        import capo_backup.types.string_list

        out["accounts"] = capo_backup.types.string_list.deserialize_json(
            data["Accounts"]
        )
    if data.get("OrganizationUnits") is not None:
        import capo_backup.types.string_list

        out["organization_units"] = capo_backup.types.string_list.deserialize_json(
            data["OrganizationUnits"]
        )
    if data.get("Regions") is not None:
        import capo_backup.types.string_list

        out["regions"] = capo_backup.types.string_list.deserialize_json(data["Regions"])
    return out
