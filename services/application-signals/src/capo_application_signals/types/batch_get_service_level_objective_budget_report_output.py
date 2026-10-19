"""Generated from Smithy shape ``com.amazonaws.applicationsignals#BatchGetServiceLevelObjectiveBudgetReportOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_application_signals.types.service_level_objective_budget_report_errors
    import capo_application_signals.types.service_level_objective_budget_reports


class BatchGetServiceLevelObjectiveBudgetReportOutput(TypedDict, closed=True):
    timestamp: "datetime.datetime"
    """<p>The date and time that the report is for. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.</p>"""
    reports: "capo_application_signals.types.service_level_objective_budget_reports.ServiceLevelObjectiveBudgetReports"
    """<p>An array of structures, where each structure is one budget report.</p>"""
    errors: "capo_application_signals.types.service_level_objective_budget_report_errors.ServiceLevelObjectiveBudgetReportErrors"
    """<p>An array of structures, where each structure includes an error indicating that one of the requests in the array was not valid.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetServiceLevelObjectiveBudgetReportOutput) -> dict:
    out: dict = {}
    import capo_application_signals.types._prelude.timestamp

    out["Timestamp"] = capo_application_signals.types._prelude.timestamp.serialize_json(
        value["timestamp"]
    )
    import capo_application_signals.types.service_level_objective_budget_reports

    out["Reports"] = (
        capo_application_signals.types.service_level_objective_budget_reports.serialize_json(
            value["reports"]
        )
    )
    import capo_application_signals.types.service_level_objective_budget_report_errors

    out["Errors"] = (
        capo_application_signals.types.service_level_objective_budget_report_errors.serialize_json(
            value["errors"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetServiceLevelObjectiveBudgetReportOutput:
    out: BatchGetServiceLevelObjectiveBudgetReportOutput = {}  # type: ignore[typeddict-item]
    if data.get("Timestamp") is not None:
        import capo_application_signals.types._prelude.timestamp

        out["timestamp"] = (
            capo_application_signals.types._prelude.timestamp.deserialize_json(
                data["Timestamp"]
            )
        )
    else:
        import datetime

        out["timestamp"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Reports") is not None:
        import capo_application_signals.types.service_level_objective_budget_reports

        out["reports"] = (
            capo_application_signals.types.service_level_objective_budget_reports.deserialize_json(
                data["Reports"]
            )
        )
    else:
        out["reports"] = []
    if data.get("Errors") is not None:
        import capo_application_signals.types.service_level_objective_budget_report_errors

        out["errors"] = (
            capo_application_signals.types.service_level_objective_budget_report_errors.deserialize_json(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    return out
