"""Generated from Smithy shape ``com.amazonaws.ssoadmin#AddRegionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sso_admin.types.instance_arn
    import capo_sso_admin.types.region_name


class AddRegionRequest(TypedDict, closed=True):
    instance_arn: "capo_sso_admin.types.instance_arn.InstanceArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center instance to replicate to the target Region.</p>"""
    region_name: "capo_sso_admin.types.region_name.RegionName"
    """<p>The name of the Amazon Web Services Region to add to the IAM Identity Center instance. The Region name must be 1-32 characters long and follow the pattern of Amazon Web Services Region names (for example, us-east-1).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddRegionRequest) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["RegionName"] = value["region_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AddRegionRequest:
    out: AddRegionRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("RegionName") is not None:
        out["region_name"] = data["RegionName"]
    else:
        out["region_name"] = ""
    return out
