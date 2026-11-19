"""Generated from Smithy shape ``com.amazonaws.mailmanager#DeleteAddonSubscriptionResponse``."""

from typing_extensions import TypedDict


class DeleteAddonSubscriptionResponse(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteAddonSubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteAddonSubscriptionResponse:
    out: DeleteAddonSubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteAddonSubscriptionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteAddonSubscriptionResponse:
    out: DeleteAddonSubscriptionResponse = {}  # type: ignore[typeddict-item]
    return out
