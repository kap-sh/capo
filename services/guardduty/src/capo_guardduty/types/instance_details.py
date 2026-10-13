"""Generated from Smithy shape ``com.amazonaws.guardduty#InstanceDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.iam_instance_profile
    import capo_guardduty.types.network_interfaces
    import capo_guardduty.types.product_codes
    import capo_guardduty.types.string
    import capo_guardduty.types.tags


class InstanceDetails(TypedDict, closed=True):
    availability_zone: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Availability Zone of the EC2 instance.</p>"""
    iam_instance_profile: NotRequired[
        "capo_guardduty.types.iam_instance_profile.IamInstanceProfile"
    ]
    """<p>The profile information of the EC2 instance.</p>"""
    image_description: NotRequired["capo_guardduty.types.string.String"]
    """<p>The image description of the EC2 instance.</p>"""
    image_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The image ID of the EC2 instance.</p>"""
    instance_id: NotRequired["capo_guardduty.types.string.String"]
    """<p>The ID of the EC2 instance.</p>"""
    instance_state: NotRequired["capo_guardduty.types.string.String"]
    """<p>The state of the EC2 instance.</p>"""
    instance_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The type of the EC2 instance.</p>"""
    outpost_arn: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Outpost. Only applicable to Amazon Web Services Outposts instances.</p>"""
    launch_time: NotRequired["capo_guardduty.types.string.String"]
    """<p>The launch time of the EC2 instance.</p>"""
    network_interfaces: NotRequired[
        "capo_guardduty.types.network_interfaces.NetworkInterfaces"
    ]
    """<p>The elastic network interface information of the EC2 instance.</p>"""
    platform: NotRequired["capo_guardduty.types.string.String"]
    """<p>The platform of the EC2 instance.</p>"""
    product_codes: NotRequired["capo_guardduty.types.product_codes.ProductCodes"]
    """<p>The product code of the EC2 instance.</p>"""
    tags: NotRequired["capo_guardduty.types.tags.Tags"]
    """<p>The tags of the EC2 instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InstanceDetails) -> dict:
    out: dict = {}
    if "availability_zone" in value:
        out["availabilityZone"] = value["availability_zone"]
    if "iam_instance_profile" in value:
        import capo_guardduty.types.iam_instance_profile

        out["iamInstanceProfile"] = (
            capo_guardduty.types.iam_instance_profile.serialize_json(
                value["iam_instance_profile"]
            )
        )
    if "image_description" in value:
        out["imageDescription"] = value["image_description"]
    if "image_id" in value:
        out["imageId"] = value["image_id"]
    if "instance_id" in value:
        out["instanceId"] = value["instance_id"]
    if "instance_state" in value:
        out["instanceState"] = value["instance_state"]
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "outpost_arn" in value:
        out["outpostArn"] = value["outpost_arn"]
    if "launch_time" in value:
        out["launchTime"] = value["launch_time"]
    if "network_interfaces" in value:
        import capo_guardduty.types.network_interfaces

        out["networkInterfaces"] = (
            capo_guardduty.types.network_interfaces.serialize_json(
                value["network_interfaces"]
            )
        )
    if "platform" in value:
        out["platform"] = value["platform"]
    if "product_codes" in value:
        import capo_guardduty.types.product_codes

        out["productCodes"] = capo_guardduty.types.product_codes.serialize_json(
            value["product_codes"]
        )
    if "tags" in value:
        import capo_guardduty.types.tags

        out["tags"] = capo_guardduty.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> InstanceDetails:
    out: InstanceDetails = {}  # type: ignore[typeddict-item]
    if data.get("availabilityZone") is not None:
        out["availability_zone"] = data["availabilityZone"]
    if data.get("iamInstanceProfile") is not None:
        import capo_guardduty.types.iam_instance_profile

        out["iam_instance_profile"] = (
            capo_guardduty.types.iam_instance_profile.deserialize_json(
                data["iamInstanceProfile"]
            )
        )
    if data.get("imageDescription") is not None:
        out["image_description"] = data["imageDescription"]
    if data.get("imageId") is not None:
        out["image_id"] = data["imageId"]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    if data.get("instanceState") is not None:
        out["instance_state"] = data["instanceState"]
    if data.get("instanceType") is not None:
        out["instance_type"] = data["instanceType"]
    if data.get("outpostArn") is not None:
        out["outpost_arn"] = data["outpostArn"]
    if data.get("launchTime") is not None:
        out["launch_time"] = data["launchTime"]
    if data.get("networkInterfaces") is not None:
        import capo_guardduty.types.network_interfaces

        out["network_interfaces"] = (
            capo_guardduty.types.network_interfaces.deserialize_json(
                data["networkInterfaces"]
            )
        )
    if data.get("platform") is not None:
        out["platform"] = data["platform"]
    if data.get("productCodes") is not None:
        import capo_guardduty.types.product_codes

        out["product_codes"] = capo_guardduty.types.product_codes.deserialize_json(
            data["productCodes"]
        )
    if data.get("tags") is not None:
        import capo_guardduty.types.tags

        out["tags"] = capo_guardduty.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: InstanceDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "network_interfaces" in value:
        import capo_guardduty.types.network_interfaces

        out["network_interfaces"] = (
            capo_guardduty.types.network_interfaces.redact_sensitive(
                value["network_interfaces"]
            )
        )
    return out
