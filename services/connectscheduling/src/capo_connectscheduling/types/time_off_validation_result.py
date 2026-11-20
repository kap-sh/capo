"""Generated from Smithy shape ``com.amazonaws.connectscheduling#TimeOffValidationResult``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectscheduling.types.time_off_validation_code
    import capo_connectscheduling.types.time_off_validation_severity


class TimeOffValidationResult(TypedDict, closed=True):
    severity: "capo_connectscheduling.types.time_off_validation_severity.TimeOffValidationSeverity"
    """<p>The severity of the validation result. <code>WARNING</code> is a breach of the configured rules that is not enough to reject the request, either because of the rules configuration or because the caller sent <code>RuleFailureAction</code> <code>OVERRIDE</code>. <code>ERROR</code> is a reason the request was rejected.</p>"""
    code: "capo_connectscheduling.types.time_off_validation_code.TimeOffValidationCode"
    """<p>The specific reason for the validation result. New values may be added, so treat an unrecognized value as a generic failure of the reported severity.</p> <ul> <li> <p> <code>INSUFFICIENT_USER_TIME_OFF_BALANCE</code>: the user's time off balance for the activity is less than the time this request deducts. Connect Customer deducts only working time in the window. For details, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/upload-timeoff-balance.html#how-system-calculates-time-off-deductions">How the system calculates time off deductions</a> in the <i>Connect Customer Administrator Guide</i>.</p> </li> <li> <p> <code>INSUFFICIENT_GROUP_TIME_OFF_ALLOWANCE</code>: the time off allowance of the user's forecast group or demand group for the activity is too low for this request.</p> </li> <li> <p> <code>INSUFFICIENT_STAFFING_GROUP_TIME_OFF_ALLOWANCE</code>: the daily time off allowance of the user's staffing group for the activity is too low for this request.</p> </li> <li> <p> <code>CONFLICTING_TIME_OFF_REQUEST</code>: the request overlaps another time off request for the user that is <code>APPROVED</code> or being approved. Requests in <code>AWAITING_APPROVAL</code> don't count. For <code>CreateTimeOff</code> with <code>AUTOMATIC</code>, overlapping overtime and voluntary time off also count.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeOffValidationResult) -> dict:
    out: dict = {}
    import capo_connectscheduling.types.time_off_validation_severity

    out["Severity"] = (
        capo_connectscheduling.types.time_off_validation_severity.serialize_json(
            value["severity"]
        )
    )
    import capo_connectscheduling.types.time_off_validation_code

    out["Code"] = capo_connectscheduling.types.time_off_validation_code.serialize_json(
        value["code"]
    )
    return out


def deserialize_json(data: dict) -> TimeOffValidationResult:
    out: TimeOffValidationResult = {}  # type: ignore[typeddict-item]
    if data.get("Severity") is not None:
        import capo_connectscheduling.types.time_off_validation_severity

        out["severity"] = (
            capo_connectscheduling.types.time_off_validation_severity.deserialize_json(
                data["Severity"]
            )
        )
    else:
        import typing

        out["severity"] = typing.cast(
            "capo_connectscheduling.types.time_off_validation_severity.TimeOffValidationSeverity",
            "",
        )
    if data.get("Code") is not None:
        import capo_connectscheduling.types.time_off_validation_code

        out["code"] = (
            capo_connectscheduling.types.time_off_validation_code.deserialize_json(
                data["Code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_connectscheduling.types.time_off_validation_code.TimeOffValidationCode",
            "",
        )
    return out
