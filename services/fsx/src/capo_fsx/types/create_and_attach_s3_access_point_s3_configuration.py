"""Generated from Smithy shape ``com.amazonaws.fsx#CreateAndAttachS3AccessPointS3Configuration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.access_point_policy
    import capo_fsx.types.s3_access_point_vpc_configuration


class CreateAndAttachS3AccessPointS3Configuration(TypedDict, closed=True):
    vpc_configuration: NotRequired[
        "capo_fsx.types.s3_access_point_vpc_configuration.S3AccessPointVpcConfiguration"
    ]
    """<p>If included, Amazon S3 restricts access to this S3 access point to requests made from the specified virtual private cloud (VPC).</p>"""
    policy: NotRequired["capo_fsx.types.access_point_policy.AccessPointPolicy"]
    """<p>Specifies an access policy to associate with the S3 access point configuration. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-points-policies.html">Configuring IAM policies for using access points</a> in the Amazon Simple Storage Service User Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAndAttachS3AccessPointS3Configuration) -> dict:
    out: dict = {}
    if "vpc_configuration" in value:
        import capo_fsx.types.s3_access_point_vpc_configuration

        out["VpcConfiguration"] = (
            capo_fsx.types.s3_access_point_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAndAttachS3AccessPointS3Configuration:
    out: CreateAndAttachS3AccessPointS3Configuration = {}  # type: ignore[typeddict-item]
    if data.get("VpcConfiguration") is not None:
        import capo_fsx.types.s3_access_point_vpc_configuration

        out["vpc_configuration"] = (
            capo_fsx.types.s3_access_point_vpc_configuration.deserialize_aws_json_1_1(
                data["VpcConfiguration"]
            )
        )
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    return out
