"""Generated from Smithy shape ``com.amazonaws.codebuild#ProjectFleet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codebuild.types.string


class ProjectFleet(TypedDict, closed=True):
    fleet_arn: NotRequired["capo_codebuild.types.string.String"]
    """<p>Specifies the compute fleet ARN for the build project.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProjectFleet) -> dict:
    out: dict = {}
    if "fleet_arn" in value:
        out["fleetArn"] = value["fleet_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProjectFleet:
    out: ProjectFleet = {}  # type: ignore[typeddict-item]
    if data.get("fleetArn") is not None:
        out["fleet_arn"] = data["fleetArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProjectFleet) -> dict:
    out: dict = {}
    if "fleet_arn" in value:
        out["fleetArn"] = value["fleet_arn"]
    return out


def deserialize_cbor(data: dict) -> ProjectFleet:
    out: ProjectFleet = {}  # type: ignore[typeddict-item]
    if data.get("fleetArn") is not None:
        out["fleet_arn"] = data["fleetArn"]
    return out
