"""Generated from Smithy shape ``com.amazonaws.shield#DescribeProtectionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protection_id
    import capo_shield.types.resource_arn


class DescribeProtectionRequest(TypedDict, closed=True):
    protection_id: NotRequired["capo_shield.types.protection_id.ProtectionId"]
    """<p>The unique identifier (ID) for the <a>Protection</a> object to describe. You must provide either the <code>ResourceArn</code> of the protected resource or the <code>ProtectionID</code> of the protection, but not both.</p>"""
    resource_arn: NotRequired["capo_shield.types.resource_arn.ResourceArn"]
    """<p>The ARN (Amazon Resource Name) of the protected Amazon Web Services resource. You must provide either the <code>ResourceArn</code> of the protected resource or the <code>ProtectionID</code> of the protection, but not both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProtectionRequest) -> dict:
    out: dict = {}
    if "protection_id" in value:
        out["ProtectionId"] = value["protection_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProtectionRequest:
    out: DescribeProtectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionId") is not None:
        out["protection_id"] = data["ProtectionId"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProtectionRequest) -> dict:
    out: dict = {}
    if "protection_id" in value:
        out["ProtectionId"] = value["protection_id"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_cbor(data: dict) -> DescribeProtectionRequest:
    out: DescribeProtectionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionId") is not None:
        out["protection_id"] = data["ProtectionId"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    return out
