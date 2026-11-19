"""Generated from Smithy shape ``com.amazonaws.workspaces#IDCConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.arn


class IDCConfig(TypedDict, closed=True):
    instance_arn: NotRequired["capo_workspaces.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the identity center instance.</p>"""
    application_arn: NotRequired["capo_workspaces.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IDCConfig) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IDCConfig:
    out: IDCConfig = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: IDCConfig) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["InstanceArn"] = value["instance_arn"]
    if "application_arn" in value:
        out["ApplicationArn"] = value["application_arn"]
    return out


def deserialize_cbor(data: dict) -> IDCConfig:
    out: IDCConfig = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    if data.get("ApplicationArn") is not None:
        out["application_arn"] = data["ApplicationArn"]
    return out
