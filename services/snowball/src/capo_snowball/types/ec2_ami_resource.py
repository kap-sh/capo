"""Generated from Smithy shape ``com.amazonaws.snowball#Ec2AmiResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.ami_id
    import capo_snowball.types.string


class Ec2AmiResource(TypedDict, closed=True):
    ami_id: "capo_snowball.types.ami_id.AmiId"
    """<p>The ID of the AMI in Amazon EC2.</p>"""
    snowball_ami_id: NotRequired["capo_snowball.types.string.String"]
    """<p>The ID of the AMI on the Snow device.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2AmiResource) -> dict:
    out: dict = {}
    out["AmiId"] = value["ami_id"]
    if "snowball_ami_id" in value:
        out["SnowballAmiId"] = value["snowball_ami_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Ec2AmiResource:
    out: Ec2AmiResource = {}  # type: ignore[typeddict-item]
    if data.get("AmiId") is not None:
        out["ami_id"] = data["AmiId"]
    else:
        out["ami_id"] = ""
    if data.get("SnowballAmiId") is not None:
        out["snowball_ami_id"] = data["SnowballAmiId"]
    return out
