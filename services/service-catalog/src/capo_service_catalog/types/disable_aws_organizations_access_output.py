"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisableAWSOrganizationsAccessOutput``."""

from typing_extensions import TypedDict


class DisableAWSOrganizationsAccessOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableAWSOrganizationsAccessOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableAWSOrganizationsAccessOutput:
    out: DisableAWSOrganizationsAccessOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableAWSOrganizationsAccessOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableAWSOrganizationsAccessOutput:
    out: DisableAWSOrganizationsAccessOutput = {}  # type: ignore[typeddict-item]
    return out
