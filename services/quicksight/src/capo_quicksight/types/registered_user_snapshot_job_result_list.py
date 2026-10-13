"""Generated from Smithy shape ``com.amazonaws.quicksight#RegisteredUserSnapshotJobResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.registered_user_snapshot_job_result

RegisteredUserSnapshotJobResultList: TypeAlias = list[
    "capo_quicksight.types.registered_user_snapshot_job_result.RegisteredUserSnapshotJobResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: RegisteredUserSnapshotJobResultList) -> list:
    import capo_quicksight.types.registered_user_snapshot_job_result

    out: list = []
    for item in value:
        out.append(
            capo_quicksight.types.registered_user_snapshot_job_result.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RegisteredUserSnapshotJobResultList:
    import capo_quicksight.types.registered_user_snapshot_job_result

    out: RegisteredUserSnapshotJobResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_quicksight.types.registered_user_snapshot_job_result.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: RegisteredUserSnapshotJobResultList) -> list[Any]:
    import capo_quicksight.types.registered_user_snapshot_job_result

    return [
        capo_quicksight.types.registered_user_snapshot_job_result.redact_sensitive(item)
        for item in value
    ]
