"""Generated from Smithy shape ``com.amazonaws.codepipeline#RegisterWebhookWithThirdPartyOutput``."""

from typing_extensions import TypedDict


class RegisterWebhookWithThirdPartyOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegisterWebhookWithThirdPartyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> RegisterWebhookWithThirdPartyOutput:
    out: RegisterWebhookWithThirdPartyOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RegisterWebhookWithThirdPartyOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> RegisterWebhookWithThirdPartyOutput:
    out: RegisterWebhookWithThirdPartyOutput = {}  # type: ignore[typeddict-item]
    return out
