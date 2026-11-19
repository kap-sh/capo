"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Asg``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.asg_arn
    import capo_arc_region_switch.types.iam_role_arn


class Asg(TypedDict, closed=True):
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    arn: NotRequired["capo_arc_region_switch.types.asg_arn.AsgArn"]
    """<p>The Amazon Resource Name (ARN) of the EC2 Auto Scaling group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Asg) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Asg:
    out: Asg = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Asg) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> Asg:
    out: Asg = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out
