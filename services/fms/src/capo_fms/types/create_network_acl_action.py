"""Generated from Smithy shape ``com.amazonaws.fms#CreateNetworkAclAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.action_target
    import capo_fms.types.boolean
    import capo_fms.types.length_bounded_string


class CreateNetworkAclAction(TypedDict, closed=True):
    description: NotRequired["capo_fms.types.length_bounded_string.LengthBoundedString"]
    """<p>Brief description of this remediation action. </p>"""
    vpc: NotRequired["capo_fms.types.action_target.ActionTarget"]
    """<p>The VPC that's associated with the remediation action.</p>"""
    fms_can_remediate: "capo_fms.types.boolean.Boolean"
    """<p>Indicates whether it is possible for Firewall Manager to perform this remediation action. A false value indicates that auto remediation is disabled or Firewall Manager is unable to perform the action due to a conflict of some kind.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNetworkAclAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc" in value:
        import capo_fms.types.action_target

        out["Vpc"] = capo_fms.types.action_target.serialize_aws_json_1_1(value["vpc"])
    out["FMSCanRemediate"] = value.get("fms_can_remediate", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNetworkAclAction:
    out: CreateNetworkAclAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Vpc") is not None:
        import capo_fms.types.action_target

        out["vpc"] = capo_fms.types.action_target.deserialize_aws_json_1_1(data["Vpc"])
    if data.get("FMSCanRemediate") is not None:
        out["fms_can_remediate"] = data["FMSCanRemediate"]
    else:
        out["fms_can_remediate"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateNetworkAclAction) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc" in value:
        import capo_fms.types.action_target

        out["Vpc"] = capo_fms.types.action_target.serialize_cbor(value["vpc"])
    out["FMSCanRemediate"] = value.get("fms_can_remediate", False)
    return out


def deserialize_cbor(data: dict) -> CreateNetworkAclAction:
    out: CreateNetworkAclAction = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Vpc") is not None:
        import capo_fms.types.action_target

        out["vpc"] = capo_fms.types.action_target.deserialize_cbor(data["Vpc"])
    if data.get("FMSCanRemediate") is not None:
        out["fms_can_remediate"] = data["FMSCanRemediate"]
    else:
        out["fms_can_remediate"] = False
    return out
