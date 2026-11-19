"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Entitlement``."""

from typing_extensions import NotRequired, TypedDict


class Entitlement(TypedDict, closed=True):
    license_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the AWS License Manager license associated with the entitlement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Entitlement) -> dict:
    out: dict = {}
    if "license_arn" in value:
        out["licenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Entitlement:
    out: Entitlement = {}  # type: ignore[typeddict-item]
    if data.get("licenseArn") is not None:
        out["license_arn"] = data["licenseArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Entitlement) -> dict:
    out: dict = {}
    if "license_arn" in value:
        out["licenseArn"] = value["license_arn"]
    return out


def deserialize_cbor(data: dict) -> Entitlement:
    out: Entitlement = {}  # type: ignore[typeddict-item]
    if data.get("licenseArn") is not None:
        out["license_arn"] = data["licenseArn"]
    return out
