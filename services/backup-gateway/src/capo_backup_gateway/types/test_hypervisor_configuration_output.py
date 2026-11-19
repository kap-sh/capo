"""Generated from Smithy shape ``com.amazonaws.backupgateway#TestHypervisorConfigurationOutput``."""

from typing_extensions import TypedDict


class TestHypervisorConfigurationOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestHypervisorConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> TestHypervisorConfigurationOutput:
    out: TestHypervisorConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TestHypervisorConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> TestHypervisorConfigurationOutput:
    out: TestHypervisorConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out
