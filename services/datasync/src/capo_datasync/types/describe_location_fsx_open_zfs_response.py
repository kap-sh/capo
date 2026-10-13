"""Generated from Smithy shape ``com.amazonaws.datasync#DescribeLocationFsxOpenZfsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.ec2_security_group_arn_list
    import capo_datasync.types.fsx_protocol
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri
    import capo_datasync.types.time


class DescribeLocationFsxOpenZfsResponse(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The ARN of the FSx for OpenZFS location that was described.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>The uniform resource identifier (URI) of the FSx for OpenZFS location that was described.</p> <p>Example: <code>fsxz://us-west-2.fs-1234567890abcdef02/fsx/folderA/folder</code> </p>"""
    security_group_arns: NotRequired[
        "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    ]
    """<p>The ARNs of the security groups that are configured for the FSx for OpenZFS file system.</p>"""
    protocol: NotRequired["capo_datasync.types.fsx_protocol.FsxProtocol"]
    """<p>The type of protocol that DataSync uses to access your file system.</p>"""
    creation_time: NotRequired["capo_datasync.types.time.Time"]
    """<p>The time that the FSx for OpenZFS location was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeLocationFsxOpenZfsResponse) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "security_group_arns" in value:
        import capo_datasync.types.ec2_security_group_arn_list

        out["SecurityGroupArns"] = (
            capo_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
                value["security_group_arns"]
            )
        )
    if "protocol" in value:
        import capo_datasync.types.fsx_protocol

        out["Protocol"] = capo_datasync.types.fsx_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "creation_time" in value:
        import capo_datasync.types.time

        out["CreationTime"] = capo_datasync.types.time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeLocationFsxOpenZfsResponse:
    out: DescribeLocationFsxOpenZfsResponse = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    if data.get("Protocol") is not None:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    if data.get("CreationTime") is not None:
        import capo_datasync.types.time

        out["creation_time"] = capo_datasync.types.time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    return out


def redact_sensitive(value: DescribeLocationFsxOpenZfsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "protocol" in value:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.redact_sensitive(
            value["protocol"]
        )
    return out
