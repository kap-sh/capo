"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationBackfillResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.replication_backfill_result

ReplicationBackfillResultList: TypeAlias = list[
    "capo_ecr.types.replication_backfill_result.ReplicationBackfillResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationBackfillResultList) -> list:
    import capo_ecr.types.replication_backfill_result

    out: list = []
    for item in value:
        out.append(
            capo_ecr.types.replication_backfill_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationBackfillResultList:
    import capo_ecr.types.replication_backfill_result

    out: ReplicationBackfillResultList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecr.types.replication_backfill_result.deserialize_aws_json_1_1(item)
        )
    return out
