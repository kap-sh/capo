"""Generated from Smithy shape ``com.amazonaws.transfer#ListedUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.home_directory
    import capo_transfer.types.home_directory_type
    import capo_transfer.types.role
    import capo_transfer.types.ssh_public_key_count
    import capo_transfer.types.user_name


class ListedUser(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>Provides the unique Amazon Resource Name (ARN) for the user that you want to learn about.</p>"""
    home_directory: NotRequired["capo_transfer.types.home_directory.HomeDirectory"]
    """<p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>"""
    home_directory_type: NotRequired[
        "capo_transfer.types.home_directory_type.HomeDirectoryType"
    ]
    """<p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>"""
    role: NotRequired["capo_transfer.types.role.Role"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p> <note> <p>The IAM role that controls your users' access to your Amazon S3 bucket for servers with <code>Domain=S3</code>, or your EFS file system for servers with <code>Domain=EFS</code>. </p> <p>The policies attached to this role determine the level of access you want to provide your users when transferring files into and out of your S3 buckets or EFS file systems.</p> </note>"""
    ssh_public_key_count: NotRequired[
        "capo_transfer.types.ssh_public_key_count.SshPublicKeyCount"
    ]
    """<p>Specifies the number of SSH public keys stored for the user you specified.</p>"""
    user_name: NotRequired["capo_transfer.types.user_name.UserName"]
    """<p>Specifies the name of the user whose ARN was specified. User names are used for authentication purposes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListedUser) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "home_directory" in value:
        out["HomeDirectory"] = value["home_directory"]
    if "home_directory_type" in value:
        import capo_transfer.types.home_directory_type

        out["HomeDirectoryType"] = (
            capo_transfer.types.home_directory_type.serialize_aws_json_1_1(
                value["home_directory_type"]
            )
        )
    if "role" in value:
        out["Role"] = value["role"]
    if "ssh_public_key_count" in value:
        out["SshPublicKeyCount"] = value["ssh_public_key_count"]
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListedUser:
    out: ListedUser = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("HomeDirectory") is not None:
        out["home_directory"] = data["HomeDirectory"]
    if data.get("HomeDirectoryType") is not None:
        import capo_transfer.types.home_directory_type

        out["home_directory_type"] = (
            capo_transfer.types.home_directory_type.deserialize_aws_json_1_1(
                data["HomeDirectoryType"]
            )
        )
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    if data.get("SshPublicKeyCount") is not None:
        out["ssh_public_key_count"] = data["SshPublicKeyCount"]
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    return out
