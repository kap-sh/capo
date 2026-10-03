"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedUser``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.arn
    import capo_transfer.types.home_directory
    import capo_transfer.types.home_directory_mappings
    import capo_transfer.types.home_directory_type
    import capo_transfer.types.policy
    import capo_transfer.types.posix_profile
    import capo_transfer.types.role
    import capo_transfer.types.ssh_public_keys
    import capo_transfer.types.tags
    import capo_transfer.types.user_name


class DescribedUser(TypedDict, closed=True):
    arn: "capo_transfer.types.arn.Arn"
    """<p>Specifies the unique Amazon Resource Name (ARN) for the user that was requested to be described.</p>"""
    home_directory: NotRequired["capo_transfer.types.home_directory.HomeDirectory"]
    """<p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>"""
    home_directory_mappings: NotRequired[
        "capo_transfer.types.home_directory_mappings.HomeDirectoryMappings"
    ]
    """<p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to '/' and set <code>Target</code> to the HomeDirectory parameter value.</p>"""
    home_directory_type: NotRequired[
        "capo_transfer.types.home_directory_type.HomeDirectoryType"
    ]
    """<p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>"""
    policy: NotRequired["capo_transfer.types.policy.Policy"]
    """<p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p>"""
    posix_profile: NotRequired["capo_transfer.types.posix_profile.PosixProfile"]
    """<p>Specifies the full POSIX identity, including user ID (<code>Uid</code>), group ID (<code>Gid</code>), and any secondary groups IDs (<code>SecondaryGids</code>), that controls your users' access to your Amazon Elastic File System (Amazon EFS) file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.</p>"""
    role: NotRequired["capo_transfer.types.role.Role"]
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>"""
    ssh_public_keys: NotRequired["capo_transfer.types.ssh_public_keys.SshPublicKeys"]
    """<p>Specifies the public key portion of the Secure Shell (SSH) keys stored for the described user.</p> <note> <p>To delete the public key body, set its value to zero keys, as shown here:</p> <p> <code>SshPublicKeys: []</code> </p> </note>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Specifies the key-value pairs for the user requested. Tag can be used to search for and group users for a variety of purposes.</p>"""
    user_name: NotRequired["capo_transfer.types.user_name.UserName"]
    """<p>Specifies the name of the user that was requested to be described. User names are used for authentication purposes. This is the string that will be used by your user when they log in to your server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedUser) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "home_directory" in value:
        out["HomeDirectory"] = value["home_directory"]
    if "home_directory_mappings" in value:
        import capo_transfer.types.home_directory_mappings

        out["HomeDirectoryMappings"] = (
            capo_transfer.types.home_directory_mappings.serialize_aws_json_1_1(
                value["home_directory_mappings"]
            )
        )
    if "home_directory_type" in value:
        import capo_transfer.types.home_directory_type

        out["HomeDirectoryType"] = (
            capo_transfer.types.home_directory_type.serialize_aws_json_1_1(
                value["home_directory_type"]
            )
        )
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "posix_profile" in value:
        import capo_transfer.types.posix_profile

        out["PosixProfile"] = capo_transfer.types.posix_profile.serialize_aws_json_1_1(
            value["posix_profile"]
        )
    if "role" in value:
        out["Role"] = value["role"]
    if "ssh_public_keys" in value:
        import capo_transfer.types.ssh_public_keys

        out["SshPublicKeys"] = (
            capo_transfer.types.ssh_public_keys.serialize_aws_json_1_1(
                value["ssh_public_keys"]
            )
        )
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    if "user_name" in value:
        out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedUser:
    out: DescribedUser = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("DescribedUser.arn required")
    if data.get("HomeDirectory") is not None:
        out["home_directory"] = data["HomeDirectory"]
    if data.get("HomeDirectoryMappings") is not None:
        import capo_transfer.types.home_directory_mappings

        out["home_directory_mappings"] = (
            capo_transfer.types.home_directory_mappings.deserialize_aws_json_1_1(
                data["HomeDirectoryMappings"]
            )
        )
    if data.get("HomeDirectoryType") is not None:
        import capo_transfer.types.home_directory_type

        out["home_directory_type"] = (
            capo_transfer.types.home_directory_type.deserialize_aws_json_1_1(
                data["HomeDirectoryType"]
            )
        )
    if data.get("Policy") is not None:
        out["policy"] = data["Policy"]
    if data.get("PosixProfile") is not None:
        import capo_transfer.types.posix_profile

        out["posix_profile"] = (
            capo_transfer.types.posix_profile.deserialize_aws_json_1_1(
                data["PosixProfile"]
            )
        )
    if data.get("Role") is not None:
        out["role"] = data["Role"]
    if data.get("SshPublicKeys") is not None:
        import capo_transfer.types.ssh_public_keys

        out["ssh_public_keys"] = (
            capo_transfer.types.ssh_public_keys.deserialize_aws_json_1_1(
                data["SshPublicKeys"]
            )
        )
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    return out
