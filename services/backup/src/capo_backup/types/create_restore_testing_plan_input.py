"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreTestingPlanInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_plan_for_create
    import capo_backup.types.sensitive_string_map


class CreateRestoreTestingPlanInput(TypedDict, closed=True):
    creator_request_id: NotRequired["str"]
    """<p>This is a unique string that identifies the request and allows failed requests to be retriedwithout the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    restore_testing_plan: (
        "capo_backup.types.restore_testing_plan_for_create.RestoreTestingPlanForCreate"
    )
    """<p>A restore testing plan must contain a unique <code>RestoreTestingPlanName</code> string you create and must contain a <code>ScheduleExpression</code> cron. You may optionally include a <code>StartWindowHours</code> integer and a <code>CreatorRequestId</code> string.</p> <p>The <code>RestoreTestingPlanName</code> is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>"""
    tags: NotRequired["capo_backup.types.sensitive_string_map.SensitiveStringMap"]
    """<p>The tags to assign to the restore testing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreTestingPlanInput) -> dict:
    out: dict = {}
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    import capo_backup.types.restore_testing_plan_for_create

    out["RestoreTestingPlan"] = (
        capo_backup.types.restore_testing_plan_for_create.serialize_json(
            value["restore_testing_plan"]
        )
    )
    if "tags" in value:
        import capo_backup.types.sensitive_string_map

        out["Tags"] = capo_backup.types.sensitive_string_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRestoreTestingPlanInput:
    out: CreateRestoreTestingPlanInput = {}  # type: ignore[typeddict-item]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("RestoreTestingPlan") is not None:
        import capo_backup.types.restore_testing_plan_for_create

        out["restore_testing_plan"] = (
            capo_backup.types.restore_testing_plan_for_create.deserialize_json(
                data["RestoreTestingPlan"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRestoreTestingPlanInput.restore_testing_plan required"
        )
    if data.get("Tags") is not None:
        import capo_backup.types.sensitive_string_map

        out["tags"] = capo_backup.types.sensitive_string_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateRestoreTestingPlanInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
