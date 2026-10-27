"""Generated from Smithy shape ``com.amazonaws.ecr#ReplicationBackfillSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.replication_backfill_summary

ReplicationBackfillSummaryList: TypeAlias = list[
    "capo_ecr.types.replication_backfill_summary.ReplicationBackfillSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplicationBackfillSummaryList) -> list:
    import capo_ecr.types.replication_backfill_summary

    out: list = []
    for item in value:
        out.append(
            capo_ecr.types.replication_backfill_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ReplicationBackfillSummaryList:
    import capo_ecr.types.replication_backfill_summary

    out: ReplicationBackfillSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecr.types.replication_backfill_summary.deserialize_aws_json_1_1(item)
        )
    return out
