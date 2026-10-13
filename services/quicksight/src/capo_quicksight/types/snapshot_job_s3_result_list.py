"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobS3ResultList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.snapshot_job_s3_result

SnapshotJobS3ResultList: TypeAlias = list[
    "capo_quicksight.types.snapshot_job_s3_result.SnapshotJobS3Result"
]


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobS3ResultList) -> list:
    import capo_quicksight.types.snapshot_job_s3_result

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.snapshot_job_s3_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> SnapshotJobS3ResultList:
    import capo_quicksight.types.snapshot_job_s3_result

    out: SnapshotJobS3ResultList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_quicksight.types.snapshot_job_s3_result.deserialize_json(item))
    return out


def redact_sensitive(value: SnapshotJobS3ResultList) -> list[Any]:
    import capo_quicksight.types.snapshot_job_s3_result

    return [
        capo_quicksight.types.snapshot_job_s3_result.redact_sensitive(item)
        for item in value
    ]
