"""Generated from Smithy shape ``com.amazonaws.codepipeline#ThirdPartyJobList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.third_party_job

ThirdPartyJobList: TypeAlias = list[
    "capo_codepipeline.types.third_party_job.ThirdPartyJob"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyJobList) -> list:
    import capo_codepipeline.types.third_party_job

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.third_party_job.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ThirdPartyJobList:
    import capo_codepipeline.types.third_party_job

    out: ThirdPartyJobList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_codepipeline.types.third_party_job.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThirdPartyJobList) -> list:
    import capo_codepipeline.types.third_party_job

    out: list = []
    for item in value:
        out.append(capo_codepipeline.types.third_party_job.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ThirdPartyJobList:
    import capo_codepipeline.types.third_party_job

    out: ThirdPartyJobList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codepipeline.types.third_party_job.deserialize_cbor(item))
    return out
