"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCisScanReportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_report_format
    import capo_inspector2.types.cis_scan_arn
    import capo_inspector2.types.report_target_accounts


class GetCisScanReportRequest(TypedDict, closed=True):
    scan_arn: "capo_inspector2.types.cis_scan_arn.CisScanArn"
    """<p>The scan ARN.</p>"""
    target_accounts: NotRequired[
        "capo_inspector2.types.report_target_accounts.ReportTargetAccounts"
    ]
    """<p>The target accounts.</p>"""
    report_format: NotRequired[
        "capo_inspector2.types.cis_report_format.CisReportFormat"
    ]
    """<p> The format of the report. Valid values are <code>PDF</code> and <code>CSV</code>. If no value is specified, the report format defaults to <code>PDF</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCisScanReportRequest) -> dict:
    out: dict = {}
    out["scanArn"] = value["scan_arn"]
    if "target_accounts" in value:
        import capo_inspector2.types.report_target_accounts

        out["targetAccounts"] = (
            capo_inspector2.types.report_target_accounts.serialize_json(
                value["target_accounts"]
            )
        )
    if "report_format" in value:
        import capo_inspector2.types.cis_report_format

        out["reportFormat"] = capo_inspector2.types.cis_report_format.serialize_json(
            value["report_format"]
        )
    return out


def deserialize_json(data: dict) -> GetCisScanReportRequest:
    out: GetCisScanReportRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanArn") is not None:
        out["scan_arn"] = data["scanArn"]
    else:
        out["scan_arn"] = ""
    if data.get("targetAccounts") is not None:
        import capo_inspector2.types.report_target_accounts

        out["target_accounts"] = (
            capo_inspector2.types.report_target_accounts.deserialize_json(
                data["targetAccounts"]
            )
        )
    if data.get("reportFormat") is not None:
        import capo_inspector2.types.cis_report_format

        out["report_format"] = capo_inspector2.types.cis_report_format.deserialize_json(
            data["reportFormat"]
        )
    return out
