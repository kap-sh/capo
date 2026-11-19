"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteAnomalyDetectorOutput``."""

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element


class DeleteAnomalyDetectorOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAnomalyDetectorOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAnomalyDetectorOutput:
    out: DeleteAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteAnomalyDetectorOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteAnomalyDetectorOutput:
    out: DeleteAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAnomalyDetectorOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAnomalyDetectorOutput:
    out: DeleteAnomalyDetectorOutput = {}  # type: ignore[typeddict-item]
    return out
