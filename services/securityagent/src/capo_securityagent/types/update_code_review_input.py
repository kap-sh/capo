"""Generated from Smithy shape ``com.amazonaws.securityagent#UpdateCodeReviewInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_securityagent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_securityagent.types.assets
    import capo_securityagent.types.cloud_watch_log
    import capo_securityagent.types.code_remediation_strategy
    import capo_securityagent.types.report_destination
    import capo_securityagent.types.report_filters
    import capo_securityagent.types.service_role
    import capo_securityagent.types.validation_mode


class UpdateCodeReviewInput(TypedDict, closed=True):
    code_review_id: "str"
    """<p>The unique identifier of the code review to update.</p>"""
    agent_space_id: "str"
    """<p>The unique identifier of the agent space that contains the code review.</p>"""
    title: NotRequired["str"]
    """<p>The updated title of the code review.</p>"""
    assets: NotRequired["capo_securityagent.types.assets.Assets"]
    """<p>The updated assets for the code review.</p>"""
    service_role: NotRequired["capo_securityagent.types.service_role.ServiceRole"]
    """<p>The updated IAM service role for the code review.</p>"""
    log_config: NotRequired["capo_securityagent.types.cloud_watch_log.CloudWatchLog"]
    """<p>The updated CloudWatch Logs configuration for the code review.</p>"""
    code_remediation_strategy: NotRequired[
        "capo_securityagent.types.code_remediation_strategy.CodeRemediationStrategy"
    ]
    """<p>The updated code remediation strategy for the code review.</p>"""
    validation_mode: NotRequired[
        "capo_securityagent.types.validation_mode.ValidationMode"
    ]
    """<p>The updated validation mode for the code review. Valid values are SIMULATED and DISABLED.</p>"""
    max_task_hours: NotRequired["float"]
    """<p>The updated maximum number of billable task hours allowed for jobs started from this code review.</p>"""
    report_destination: NotRequired[
        "capo_securityagent.types.report_destination.ReportDestination"
    ]
    """<p>The destination for publishing scan reports to an integrated document provider.</p>"""
    report_filters: NotRequired["capo_securityagent.types.report_filters.ReportFilters"]
    """<p>The report-generation filters applied when the report is exported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeReviewInput) -> dict:
    out: dict = {}
    out["codeReviewId"] = value["code_review_id"]
    out["agentSpaceId"] = value["agent_space_id"]
    if "title" in value:
        out["title"] = value["title"]
    if "assets" in value:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.serialize_json(value["assets"])
    if "service_role" in value:
        out["serviceRole"] = value["service_role"]
    if "log_config" in value:
        import capo_securityagent.types.cloud_watch_log

        out["logConfig"] = capo_securityagent.types.cloud_watch_log.serialize_json(
            value["log_config"]
        )
    if "code_remediation_strategy" in value:
        import capo_securityagent.types.code_remediation_strategy

        out["codeRemediationStrategy"] = (
            capo_securityagent.types.code_remediation_strategy.serialize_json(
                value["code_remediation_strategy"]
            )
        )
    if "validation_mode" in value:
        import capo_securityagent.types.validation_mode

        out["validationMode"] = capo_securityagent.types.validation_mode.serialize_json(
            value["validation_mode"]
        )
    if "max_task_hours" in value:
        out["maxTaskHours"] = (
            "NaN"
            if value["max_task_hours"] != value["max_task_hours"]
            else "Infinity"
            if value["max_task_hours"] == float("inf")
            else "-Infinity"
            if value["max_task_hours"] == float("-inf")
            else value["max_task_hours"]
        )
    if "report_destination" in value:
        import capo_securityagent.types.report_destination

        out["reportDestination"] = (
            capo_securityagent.types.report_destination.serialize_json(
                value["report_destination"]
            )
        )
    if "report_filters" in value:
        import capo_securityagent.types.report_filters

        out["reportFilters"] = capo_securityagent.types.report_filters.serialize_json(
            value["report_filters"]
        )
    return out


def deserialize_json(data: dict) -> UpdateCodeReviewInput:
    out: UpdateCodeReviewInput = {}  # type: ignore[typeddict-item]
    if data.get("codeReviewId") is not None:
        out["code_review_id"] = data["codeReviewId"]
    else:
        raise DeserializationError("UpdateCodeReviewInput.code_review_id required")
    if data.get("agentSpaceId") is not None:
        out["agent_space_id"] = data["agentSpaceId"]
    else:
        raise DeserializationError("UpdateCodeReviewInput.agent_space_id required")
    if data.get("title") is not None:
        out["title"] = data["title"]
    if data.get("assets") is not None:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.deserialize_json(data["assets"])
    if data.get("serviceRole") is not None:
        out["service_role"] = data["serviceRole"]
    if data.get("logConfig") is not None:
        import capo_securityagent.types.cloud_watch_log

        out["log_config"] = capo_securityagent.types.cloud_watch_log.deserialize_json(
            data["logConfig"]
        )
    if data.get("codeRemediationStrategy") is not None:
        import capo_securityagent.types.code_remediation_strategy

        out["code_remediation_strategy"] = (
            capo_securityagent.types.code_remediation_strategy.deserialize_json(
                data["codeRemediationStrategy"]
            )
        )
    if data.get("validationMode") is not None:
        import capo_securityagent.types.validation_mode

        out["validation_mode"] = (
            capo_securityagent.types.validation_mode.deserialize_json(
                data["validationMode"]
            )
        )
    if data.get("maxTaskHours") is not None:
        out["max_task_hours"] = float(data["maxTaskHours"])
    if data.get("reportDestination") is not None:
        import capo_securityagent.types.report_destination

        out["report_destination"] = (
            capo_securityagent.types.report_destination.deserialize_json(
                data["reportDestination"]
            )
        )
    if data.get("reportFilters") is not None:
        import capo_securityagent.types.report_filters

        out["report_filters"] = (
            capo_securityagent.types.report_filters.deserialize_json(
                data["reportFilters"]
            )
        )
    return out


def redact_sensitive(value: UpdateCodeReviewInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "assets" in value:
        import capo_securityagent.types.assets

        out["assets"] = capo_securityagent.types.assets.redact_sensitive(
            value["assets"]
        )
    return out
