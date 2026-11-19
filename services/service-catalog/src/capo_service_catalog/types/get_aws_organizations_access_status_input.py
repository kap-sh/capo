"""Generated from Smithy shape ``com.amazonaws.servicecatalog#GetAWSOrganizationsAccessStatusInput``."""

from typing_extensions import TypedDict


class GetAWSOrganizationsAccessStatusInput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAWSOrganizationsAccessStatusInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAWSOrganizationsAccessStatusInput:
    out: GetAWSOrganizationsAccessStatusInput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetAWSOrganizationsAccessStatusInput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> GetAWSOrganizationsAccessStatusInput:
    out: GetAWSOrganizationsAccessStatusInput = {}  # type: ignore[typeddict-item]
    return out
