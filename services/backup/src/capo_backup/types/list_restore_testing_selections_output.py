"""Generated from Smithy shape ``com.amazonaws.backup#ListRestoreTestingSelectionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.restore_testing_selections


class ListRestoreTestingSelectionsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the nexttoken.</p>"""
    restore_testing_selections: (
        "capo_backup.types.restore_testing_selections.RestoreTestingSelections"
    )
    """<p>The returned restore testing selections associated with the restore testing plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRestoreTestingSelectionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_backup.types.restore_testing_selections

    out["RestoreTestingSelections"] = (
        capo_backup.types.restore_testing_selections.serialize_json(
            value["restore_testing_selections"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListRestoreTestingSelectionsOutput:
    out: ListRestoreTestingSelectionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RestoreTestingSelections") is not None:
        import capo_backup.types.restore_testing_selections

        out["restore_testing_selections"] = (
            capo_backup.types.restore_testing_selections.deserialize_json(
                data["RestoreTestingSelections"]
            )
        )
    else:
        out["restore_testing_selections"] = []
    return out
