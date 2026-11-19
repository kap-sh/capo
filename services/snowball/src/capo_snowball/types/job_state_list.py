"""Generated from Smithy shape ``com.amazonaws.snowball#JobStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.job_state

JobStateList: TypeAlias = list["capo_snowball.types.job_state.JobState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JobStateList) -> list:
    import capo_snowball.types.job_state

    out: list = []
    for item in value:
        out.append(capo_snowball.types.job_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> JobStateList:
    import capo_snowball.types.job_state

    out: JobStateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.job_state.deserialize_aws_json_1_1(item))
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: JobStateList) -> list:
    import capo_snowball.types.job_state

    out: list = []
    for item in value:
        out.append(capo_snowball.types.job_state.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> JobStateList:
    import capo_snowball.types.job_state

    out: JobStateList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_snowball.types.job_state.deserialize_cbor(item))
    return out
