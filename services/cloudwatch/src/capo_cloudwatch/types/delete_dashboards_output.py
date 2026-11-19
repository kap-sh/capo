"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DeleteDashboardsOutput``."""

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element


class DeleteDashboardsOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteDashboardsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteDashboardsOutput:
    out: DeleteDashboardsOutput = {}  # type: ignore[typeddict-item]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDashboardsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pass


def deserialize_query(el: Element) -> DeleteDashboardsOutput:
    out: DeleteDashboardsOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteDashboardsOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteDashboardsOutput:
    out: DeleteDashboardsOutput = {}  # type: ignore[typeddict-item]
    return out
