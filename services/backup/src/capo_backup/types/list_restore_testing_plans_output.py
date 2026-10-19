"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreTestingPlansOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_plans


class ListRestoreTestingPlansOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the nexttoken.</p>"""
    restore_testing_plans: "capo_backup.types.restore_testing_plans.RestoreTestingPlans"
    """<p>This is a returned list of restore testing plans.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreTestingPlansOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_backup.types.restore_testing_plans

    out["RestoreTestingPlans"] = capo_backup.types.restore_testing_plans.serialize_json(
        value["restore_testing_plans"]
    )
    return out


def deserialize_json(data: dict) -> ListRestoreTestingPlansOutput:
    out: ListRestoreTestingPlansOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RestoreTestingPlans") is not None:
        import capo_backup.types.restore_testing_plans

        out["restore_testing_plans"] = (
            capo_backup.types.restore_testing_plans.deserialize_json(
                data["RestoreTestingPlans"]
            )
        )
    else:
        out["restore_testing_plans"] = []
    return out
