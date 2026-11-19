"""Generated from Smithy shape ``com.amazonaws.servicecatalog#EnableAWSOrganizationsAccessInput``."""

from typing_extensions import TypedDict


class EnableAWSOrganizationsAccessInput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnableAWSOrganizationsAccessInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> EnableAWSOrganizationsAccessInput:
    out: EnableAWSOrganizationsAccessInput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EnableAWSOrganizationsAccessInput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> EnableAWSOrganizationsAccessInput:
    out: EnableAWSOrganizationsAccessInput = {}  # type: ignore[typeddict-item]
    return out
