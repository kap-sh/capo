"""Generated from Smithy shape ``com.amazonaws.quicksight#AnonymousUserSnapshotJobResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.anonymous_user_snapshot_job_result

AnonymousUserSnapshotJobResultList: TypeAlias = list[
    "capo_quicksight.types.anonymous_user_snapshot_job_result.AnonymousUserSnapshotJobResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: AnonymousUserSnapshotJobResultList) -> list:
    import capo_quicksight.types.anonymous_user_snapshot_job_result

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.anonymous_user_snapshot_job_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AnonymousUserSnapshotJobResultList:
    import capo_quicksight.types.anonymous_user_snapshot_job_result

    out: AnonymousUserSnapshotJobResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.anonymous_user_snapshot_job_result.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: AnonymousUserSnapshotJobResultList) -> list[Any]:
    import capo_quicksight.types.anonymous_user_snapshot_job_result

    return [
        capo_quicksight.types.anonymous_user_snapshot_job_result.redact_sensitive(item)
        for item in value
    ]
