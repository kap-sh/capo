"""Generated from Smithy shape ``com.amazonaws.guardduty#Ec2Instance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.ec2_network_interface_uids
    import capo_guardduty.types.iam_instance_profile
    import capo_guardduty.types.product_codes
    import capo_guardduty.types.string


class Ec2Instance(TypedDict, closed=True):
    availability_zone: NotRequired["capo_guardduty.types.string.String"]
    """<p>The availability zone of the Amazon EC2 instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones">Availability zones</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    image_description: NotRequired["capo_guardduty.types.string.String"]
    """<p>The image description of the Amazon EC2 instance.</p>"""
    instance_state: NotRequired["capo_guardduty.types.string.String"]
    """<p>The state of the Amazon EC2 instance. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html">Amazon EC2 instance state changes</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    iam_instance_profile: NotRequired[
        "capo_guardduty.types.iam_instance_profile.IamInstanceProfile"
    ]
    instance_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>Type of the Amazon EC2 instance.</p>"""
    outpost_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost. This shows applicable Amazon Web Services Outposts instances.</p>"""
    platform: NotRequired["capo_guardduty.types.string.String"]
    """<p>The platform of the Amazon EC2 instance.</p>"""
    product_codes: NotRequired["capo_guardduty.types.product_codes.ProductCodes"]
    """<p>The product code of the Amazon EC2 instance.</p>"""
    ec2_network_interface_uids: NotRequired[
        "capo_guardduty.types.ec2_network_interface_uids.Ec2NetworkInterfaceUids"
    ]
    """<p>The ID of the network interface.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ec2Instance) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "image_description" in value:
        out["imageDescription"] = value["image_description"]
    if "instance_state" in value:
        out["instanceState"] = value["instance_state"]
    if "iam_instance_profile" in value:
        import capo_guardduty.types.iam_instance_profile

        out["IamInstanceProfile"] = (
            capo_guardduty.types.iam_instance_profile.serialize_json(
                value["iam_instance_profile"]
            )
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "outpost_arn" in value:
        out["outpostArn"] = value["outpost_arn"]
    if "platform" in value:
        out["platform"] = value["platform"]
    if "product_codes" in value:
        import capo_guardduty.types.product_codes

        out["productCodes"] = capo_guardduty.types.product_codes.serialize_json(
            value["product_codes"]
        )
    if "ec2_network_interface_uids" in value:
        import capo_guardduty.types.ec2_network_interface_uids

        out["ec2NetworkInterfaceUids"] = (
            capo_guardduty.types.ec2_network_interface_uids.serialize_json(
                value["ec2_network_interface_uids"]
            )
        )
    return out


def deserialize_json(data: dict) -> Ec2Instance:
    out: Ec2Instance = {}  # type: ignore[typeddict-item]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("imageDescription") is not None:
        out["image_description"] = data["imageDescription"]
    if data.get("instanceState") is not None:
        out["instance_state"] = data["instanceState"]
    if data.get("IamInstanceProfile") is not None:
        import capo_guardduty.types.iam_instance_profile

        out["iam_instance_profile"] = (
            capo_guardduty.types.iam_instance_profile.deserialize_json(
                data["IamInstanceProfile"]
            )
        )
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("outpostArn") is not None:
        out["outpost_arn"] = data["outpostArn"]
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("productCodes") is not None:
        import capo_guardduty.types.product_codes

        out["product_codes"] = capo_guardduty.types.product_codes.deserialize_json(
            data["productCodes"]
        )
    if data.get("ec2NetworkInterfaceUids") is not None:
        import capo_guardduty.types.ec2_network_interface_uids

        out["ec2_network_interface_uids"] = (
            capo_guardduty.types.ec2_network_interface_uids.deserialize_json(
                data["ec2NetworkInterfaceUids"]
            )
        )
    return out
