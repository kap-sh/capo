"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StopOTelEnrichmentOutput``."""

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element


class StopOTelEnrichmentOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopOTelEnrichmentOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> StopOTelEnrichmentOutput:
    out: StopOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: StopOTelEnrichmentOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> StopOTelEnrichmentOutput:
    out: StopOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StopOTelEnrichmentOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> StopOTelEnrichmentOutput:
    out: StopOTelEnrichmentOutput = {}  # type: ignore[typeddict-item]
    return out
