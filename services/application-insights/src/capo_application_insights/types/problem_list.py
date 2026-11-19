"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ProblemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.problem

ProblemList: TypeAlias = list["capo_application_insights.types.problem.Problem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProblemList) -> list:
    import capo_application_insights.types.problem

    out: list = []
    for item in value:
        out.append(capo_application_insights.types.problem.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ProblemList:
    import capo_application_insights.types.problem

    out: ProblemList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_insights.types.problem.deserialize_aws_json_1_1(item)
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProblemList) -> list:
    import capo_application_insights.types.problem

    out: list = []
    for item in value:
        out.append(capo_application_insights.types.problem.serialize_cbor(item))
    return out


def deserialize_cbor(data: list) -> ProblemList:
    import capo_application_insights.types.problem

    out: ProblemList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_application_insights.types.problem.deserialize_cbor(item))
    return out
