"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ServiceLevelObjectiveBudgetReportError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_signals.types.service_level_objective_arn
    import capo_application_signals.types.service_level_objective_budget_report_error_code
    import capo_application_signals.types.service_level_objective_budget_report_error_message
    import capo_application_signals.types.service_level_objective_name


class ServiceLevelObjectiveBudgetReportError(TypedDict, closed=True):
    name: "capo_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName"
    """<p>The name of the SLO that this error is related to.</p>"""
    arn: "capo_application_signals.types.service_level_objective_arn.ServiceLevelObjectiveArn"
    """<p>The ARN of the SLO that this error is related to.</p>"""
    error_code: "capo_application_signals.types.service_level_objective_budget_report_error_code.ServiceLevelObjectiveBudgetReportErrorCode"
    """<p>The error code for this error.</p>"""
    error_message: "capo_application_signals.types.service_level_objective_budget_report_error_message.ServiceLevelObjectiveBudgetReportErrorMessage"
    """<p>The message for this error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceLevelObjectiveBudgetReportError) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    out["Arn"] = value["arn"]
    out["ErrorCode"] = value["error_code"]
    out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ServiceLevelObjectiveBudgetReportError:
    out: ServiceLevelObjectiveBudgetReportError = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("ErrorCode") is not None:
        out["error_code"] = data["ErrorCode"]
    else:
        out["error_code"] = ""
    if data.get("ErrorMessage") is not None:
        out["error_message"] = data["ErrorMessage"]
    else:
        out["error_message"] = ""
    return out
