"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationFsxOpenZfsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.ec2_security_group_arn_list
    import capo_datasync.types.fsx_filesystem_arn
    import capo_datasync.types.fsx_open_zfs_subdirectory
    import capo_datasync.types.fsx_protocol
    import capo_datasync.types.input_tag_list


class CreateLocationFsxOpenZfsRequest(TypedDict, closed=True):
    fsx_filesystem_arn: "capo_datasync.types.fsx_filesystem_arn.FsxFilesystemArn"
    """<p>The Amazon Resource Name (ARN) of the FSx for OpenZFS file system.</p>"""
    protocol: "capo_datasync.types.fsx_protocol.FsxProtocol"
    """<p>The type of protocol that DataSync uses to access your file system.</p>"""
    security_group_arns: (
        "capo_datasync.types.ec2_security_group_arn_list.Ec2SecurityGroupArnList"
    )
    """<p>The ARNs of the security groups that are used to configure the FSx for OpenZFS file system.</p>"""
    subdirectory: NotRequired[
        "capo_datasync.types.fsx_open_zfs_subdirectory.FsxOpenZfsSubdirectory"
    ]
    """<p>A subdirectory in the location's path that must begin with <code>/fsx</code>. DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).</p>"""
    tags: NotRequired["capo_datasync.types.input_tag_list.InputTagList"]
    """<p>The key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationFsxOpenZfsRequest) -> dict:
    out: dict = {}
    out["FsxFilesystemArn"] = value["fsx_filesystem_arn"]
    import capo_datasync.types.fsx_protocol

    out["Protocol"] = capo_datasync.types.fsx_protocol.serialize_aws_json_1_1(
        value["protocol"]
    )
    import capo_datasync.types.ec2_security_group_arn_list

    out["SecurityGroupArns"] = (
        capo_datasync.types.ec2_security_group_arn_list.serialize_aws_json_1_1(
            value["security_group_arns"]
        )
    )
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    if "tags" in value:
        import capo_datasync.types.input_tag_list

        out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationFsxOpenZfsRequest:
    out: CreateLocationFsxOpenZfsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FsxFilesystemArn") is not None:
        out["fsx_filesystem_arn"] = data["FsxFilesystemArn"]
    else:
        raise DeserializationError(
            "CreateLocationFsxOpenZfsRequest.fsx_filesystem_arn required"
        )
    if data.get("Protocol") is not None:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    else:
        raise DeserializationError("CreateLocationFsxOpenZfsRequest.protocol required")
    if data.get("SecurityGroupArns") is not None:
        import capo_datasync.types.ec2_security_group_arn_list

        out["security_group_arns"] = (
            capo_datasync.types.ec2_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    else:
        raise DeserializationError(
            "CreateLocationFsxOpenZfsRequest.security_group_arns required"
        )
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("Tags") is not None:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateLocationFsxOpenZfsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "protocol" in value:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.redact_sensitive(
            value["protocol"]
        )
    return out
