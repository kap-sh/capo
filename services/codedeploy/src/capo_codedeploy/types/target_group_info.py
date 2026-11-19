"""Generated from Smithy shape ``com.amazonaws.codedeploy#TargetGroupInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.target_group_name


class TargetGroupInfo(TypedDict, closed=True):
    name: NotRequired["capo_codedeploy.types.target_group_name.TargetGroupName"]
    """<p>For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment are registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetGroupInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetGroupInfo:
    out: TargetGroupInfo = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetGroupInfo) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_cbor(data: dict) -> TargetGroupInfo:
    out: TargetGroupInfo = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    return out
