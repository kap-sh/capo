"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisableAWSOrganizationsAccessInput``."""

from typing_extensions import TypedDict


class DisableAWSOrganizationsAccessInput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisableAWSOrganizationsAccessInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DisableAWSOrganizationsAccessInput:
    out: DisableAWSOrganizationsAccessInput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DisableAWSOrganizationsAccessInput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DisableAWSOrganizationsAccessInput:
    out: DisableAWSOrganizationsAccessInput = {}  # type: ignore[typeddict-item]
    return out
