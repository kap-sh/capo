"""Generated from Smithy shape ``com.amazonaws.fms#WebACLHasIncompatibleConfigurationViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.length_bounded_string
    import capo_fms.types.resource_arn


class WebACLHasIncompatibleConfigurationViolation(TypedDict, closed=True):
    web_acl_arn: NotRequired["capo_fms.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the web ACL. </p>"""
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>Information about the problems that Firewall Manager encountered with the web ACL configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebACLHasIncompatibleConfigurationViolation) -> dict:
    out: dict = {}
    if "web_acl_arn" in value:
        out["WebACLArn"] = value["web_acl_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WebACLHasIncompatibleConfigurationViolation:
    out: WebACLHasIncompatibleConfigurationViolation = {}  # type: ignore[typeddict-item]
    if data.get("WebACLArn") is not None:
        out["web_acl_arn"] = data["WebACLArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: WebACLHasIncompatibleConfigurationViolation) -> dict:
    out: dict = {}
    if "web_acl_arn" in value:
        out["WebACLArn"] = value["web_acl_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_cbor(data: dict) -> WebACLHasIncompatibleConfigurationViolation:
    out: WebACLHasIncompatibleConfigurationViolation = {}  # type: ignore[typeddict-item]
    if data.get("WebACLArn") is not None:
        out["web_acl_arn"] = data["WebACLArn"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    return out
