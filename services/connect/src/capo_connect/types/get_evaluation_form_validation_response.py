"""Generated from Smithy shape ``com.amazonaws.connect#GetEvaluationFormValidationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_validation_failure_reason
    import capo_connect.types.evaluation_form_validation_finding_list
    import capo_connect.types.evaluation_form_validation_status
    import capo_connect.types.resource_id
    import capo_connect.types.timestamp
    import capo_connect.types.version_number


class GetEvaluationFormValidationResponse(TypedDict, closed=True):
    status: "capo_connect.types.evaluation_form_validation_status.EvaluationFormValidationStatus"
    """<p>The current status of the validation process. Valid values: <code>IN_PROGRESS</code>, <code>COMPLETED</code>, <code>FAILED</code>.</p>"""
    failure_reason: NotRequired[
        "capo_connect.types.evaluation_form_validation_failure_reason.EvaluationFormValidationFailureReason"
    ]
    """<p>The reason the validation failed. This field is populated only when the status is <code>FAILED</code>.</p>"""
    evaluation_form_id: "capo_connect.types.resource_id.ResourceId"
    """<p>The unique identifier for the evaluation form.</p>"""
    evaluation_form_version: "capo_connect.types.version_number.VersionNumber"
    """<p>A version of the evaluation form.</p>"""
    started_time: "capo_connect.types.timestamp.Timestamp"
    """<p>The timestamp when the validation process was started.</p>"""
    findings: NotRequired[
        "capo_connect.types.evaluation_form_validation_finding_list.EvaluationFormValidationFindingList"
    ]
    """<p>A list of findings from the validation process. Each finding identifies a structural issue or quality improvement for the evaluation form, and may include a suggested fix. This field is populated when the status is <code>COMPLETED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEvaluationFormValidationResponse) -> dict:
    out: dict = {}
    import capo_connect.types.evaluation_form_validation_status

    out["Status"] = capo_connect.types.evaluation_form_validation_status.serialize_json(
        value["status"]
    )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    out["EvaluationFormId"] = value["evaluation_form_id"]
    out["EvaluationFormVersion"] = value.get("evaluation_form_version", 0)
    import capo_connect.types.timestamp

    out["StartedTime"] = capo_connect.types.timestamp.serialize_json(
        value["started_time"]
    )
    if "findings" in value:
        import capo_connect.types.evaluation_form_validation_finding_list

        out["Findings"] = (
            capo_connect.types.evaluation_form_validation_finding_list.serialize_json(
                value["findings"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEvaluationFormValidationResponse:
    out: GetEvaluationFormValidationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_connect.types.evaluation_form_validation_status

        out["status"] = (
            capo_connect.types.evaluation_form_validation_status.deserialize_json(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connect.types.evaluation_form_validation_status.EvaluationFormValidationStatus",
            "",
        )
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    if data.get("EvaluationFormId") is not None:
        out["evaluation_form_id"] = data["EvaluationFormId"]
    else:
        out["evaluation_form_id"] = ""
    if data.get("EvaluationFormVersion") is not None:
        out["evaluation_form_version"] = data["EvaluationFormVersion"]
    else:
        out["evaluation_form_version"] = 0
    if data.get("StartedTime") is not None:
        import capo_connect.types.timestamp

        out["started_time"] = capo_connect.types.timestamp.deserialize_json(
            data["StartedTime"]
        )
    else:
        import datetime

        out["started_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("Findings") is not None:
        import capo_connect.types.evaluation_form_validation_finding_list

        out["findings"] = (
            capo_connect.types.evaluation_form_validation_finding_list.deserialize_json(
                data["Findings"]
            )
        )
    return out
