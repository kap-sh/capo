"""Generated from Smithy shape ``com.amazonaws.backup#CreateRestoreTestingSelectionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_selection_for_create


class CreateRestoreTestingSelectionInput(TypedDict, closed=True):
    creator_request_id: NotRequired["str"]
    """<p>This is an optional unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice. If used, this parameter must contain 1 to 50 alphanumeric or '-_.' characters.</p>"""
    restore_testing_plan_name: "str"
    """<p>Input the restore testing plan name that was returned from the related CreateRestoreTestingPlan request.</p>"""
    restore_testing_selection: "capo_backup.types.restore_testing_selection_for_create.RestoreTestingSelectionForCreate"
    """<p>This consists of <code>RestoreTestingSelectionName</code>, <code>ProtectedResourceType</code>, and one of the following:</p> <ul> <li> <p> <code>ProtectedResourceArns</code> </p> </li> <li> <p> <code>ProtectedResourceConditions</code> </p> </li> </ul> <p>Each protected resource type can have one single value.</p> <p>A restore testing selection can include a wildcard value ("*") for <code>ProtectedResourceArns</code> along with <code>ProtectedResourceConditions</code>. Alternatively, you can include up to 30 specific protected resource ARNs in <code>ProtectedResourceArns</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRestoreTestingSelectionInput) -> dict:
    out: dict = {}
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
    import capo_backup.types.restore_testing_selection_for_create

    out["RestoreTestingSelection"] = (
        capo_backup.types.restore_testing_selection_for_create.serialize_json(
            value["restore_testing_selection"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateRestoreTestingSelectionInput:
    out: CreateRestoreTestingSelectionInput = {}  # type: ignore[typeddict-item]
    if data.get("CreatorRequestId") is not None:
        out["creator_request_id"] = data["CreatorRequestId"]
    if data.get("RestoreTestingSelection") is not None:
        import capo_backup.types.restore_testing_selection_for_create

        out["restore_testing_selection"] = (
            capo_backup.types.restore_testing_selection_for_create.deserialize_json(
                data["RestoreTestingSelection"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRestoreTestingSelectionInput.restore_testing_selection required"
        )
    return out
