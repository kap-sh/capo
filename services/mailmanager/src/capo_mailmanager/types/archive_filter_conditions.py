"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveFilterConditions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mailmanager.types.archive_filter_condition

ArchiveFilterConditions: TypeAlias = list[
    "capo_mailmanager.types.archive_filter_condition.ArchiveFilterCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ArchiveFilterConditions) -> list:
    import capo_mailmanager.types.archive_filter_condition

    out: list = []
    for item in value:
        out.append(
            capo_mailmanager.types.archive_filter_condition.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ArchiveFilterConditions:
    import capo_mailmanager.types.archive_filter_condition

    out: ArchiveFilterConditions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mailmanager.types.archive_filter_condition.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ArchiveFilterConditions) -> list:
    import capo_mailmanager.types.archive_filter_condition

    out: list = []
    for item in value:
        out.append(capo_mailmanager.types.archive_filter_condition.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ArchiveFilterConditions:
    import capo_mailmanager.types.archive_filter_condition

    out: ArchiveFilterConditions = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_mailmanager.types.archive_filter_condition.deserialize_cbor(item)
        )
    return out
