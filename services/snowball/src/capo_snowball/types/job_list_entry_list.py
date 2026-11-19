"""Generated from Smithy shape ``com.amazonaws.snowball#JobListEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.job_list_entry

JobListEntryList: TypeAlias = list["capo_snowball.types.job_list_entry.JobListEntry"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobListEntryList) -> list:
    import capo_snowball.types.job_list_entry

    out: list = []
    for item in value:
        out.append(capo_snowball.types.job_list_entry.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobListEntryList:
    import capo_snowball.types.job_list_entry

    out: JobListEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.job_list_entry.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobListEntryList) -> list:
    import capo_snowball.types.job_list_entry

    out: list = []
    for item in value:
        out.append(capo_snowball.types.job_list_entry.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> JobListEntryList:
    import capo_snowball.types.job_list_entry

    out: JobListEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.job_list_entry.deserialize_cbor(item))
    return out
