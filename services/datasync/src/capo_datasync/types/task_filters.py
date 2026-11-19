"""Generated from Smithy shape ``com.amazonaws.datasync#TaskFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_datasync.types.task_filter

TaskFilters: TypeAlias = list["capo_datasync.types.task_filter.TaskFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskFilters) -> list:
    import capo_datasync.types.task_filter

    out: list = []
    for item in value:
        out.append(capo_datasync.types.task_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TaskFilters:
    import capo_datasync.types.task_filter

    out: TaskFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.task_filter.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TaskFilters) -> list:
    import capo_datasync.types.task_filter

    out: list = []
    for item in value:
        out.append(capo_datasync.types.task_filter.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> TaskFilters:
    import capo_datasync.types.task_filter

    out: TaskFilters = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datasync.types.task_filter.deserialize_cbor(item))
    return out
