"""Generated from Smithy shape ``com.amazonaws.transfer#CreateUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.home_directory
    import capo_transfer.types.home_directory_mappings
    import capo_transfer.types.home_directory_type
    import capo_transfer.types.policy
    import capo_transfer.types.posix_profile
    import capo_transfer.types.role
    import capo_transfer.types.server_id
    import capo_transfer.types.ssh_public_key_body
    import capo_transfer.types.tags
    import capo_transfer.types.user_name


class CreateUserRequest(TypedDict, closed=True):
    home_directory: NotRequired["capo_transfer.types.home_directory.HomeDirectory"]
    """<p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>"""
    home_directory_type: NotRequired[
        "capo_transfer.types.home_directory_type.HomeDirectoryType"
    ]
    """<p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>"""
    home_directory_mappings: NotRequired[
        "capo_transfer.types.home_directory_mappings.HomeDirectoryMappings"
    ]
    """<p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to <code>/</code> and set <code>Target</code> to the value the user should see for their home directory when they log in.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]</code> </p>"""
    policy: NotRequired["capo_transfer.types.policy.Policy"]
    """<p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html">Example session policy</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">AssumeRole</a> in the <i>Amazon Web Services Security Token Service API Reference</i>.</p> </note>"""
    posix_profile: NotRequired["capo_transfer.types.posix_profile.PosixProfile"]
    """<p>Specifies the full POSIX identity, including user ID (<code>Uid</code>), group ID (<code>Gid</code>), and any secondary groups IDs (<code>SecondaryGids</code>), that controls your users' access to your Amazon EFS file systems. The POSIX permissions that are set on files and directories in Amazon EFS determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.</p>"""
    role: "capo_transfer.types.role.Role"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.</p>"""
    ssh_public_key_body: NotRequired[
        "capo_transfer.types.ssh_public_key_body.SshPublicKeyBody"
    ]
    """<p>The public portion of the Secure Shell (SSH) key used to authenticate the user to the server.</p> <p>The three standard SSH public key format elements are <code>&lt;key type&gt;</code>, <code>&lt;body base64&gt;</code>, and an optional <code>&lt;comment&gt;</code>, with spaces between each element.</p> <p>Transfer Family accepts RSA, ECDSA, and ED25519 keys.</p> <ul> <li> <p>For RSA keys, the key type is <code>ssh-rsa</code>.</p> </li> <li> <p>For ED25519 keys, the key type is <code>ssh-ed25519</code>.</p> </li> <li> <p>For ECDSA keys, the key type is either <code>ecdsa-sha2-nistp256</code>, <code>ecdsa-sha2-nistp384</code>, or <code>ecdsa-sha2-nistp521</code>, depending on the size of the key you generated.</p> </li> </ul>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for users. Tags are metadata attached to users for any purpose.</p>"""
    user_name: "capo_transfer.types.user_name.UserName"
    """<p>A unique string that identifies a user and is associated with a <code>ServerId</code>. This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore '_', hyphen '-', period '.', and at sign '@'. The user name can't start with a hyphen, period, or at sign.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserRequest) -> dict:
    out: dict = {}
    if "home_directory" in value:
        out["HomeDirectory"] = value["home_directory"]
    if "home_directory_type" in value:
        import capo_transfer.types.home_directory_type

        out["HomeDirectoryType"] = (
            capo_transfer.types.home_directory_type.serialize_aws_json_1_1(
                value["home_directory_type"]
            )
        )
    if "home_directory_mappings" in value:
        import capo_transfer.types.home_directory_mappings

        out["HomeDirectoryMappings"] = (
            capo_transfer.types.home_directory_mappings.serialize_aws_json_1_1(
                value["home_directory_mappings"]
            )
        )
    if "policy" in value:
        out["Policy"] = value["policy"]
    if "posix_profile" in value:
        import capo_transfer.types.posix_profile

        out["PosixProfile"] = capo_transfer.types.posix_profile.serialize_aws_json_1_1(
            value["posix_profile"]
        )
    out["Role"] = value["role"]
    out["ServerId"] = value["server_id"]
    if "ssh_public_key_body" in value:
        out["SshPublicKeyBody"] = value["ssh_public_key_body"]
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    out["UserName"] = value["user_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserRequest:
    out: CreateUserRequest = {}  # type: ignore[typeddict-item]
    if data.get("HomeDirectory") is not None:
        out["home_directory"] = data["HomeDirectory"]
    if data.get("HomeDirectoryType") is not None:
        import capo_transfer.types.home_directory_type

        out["home_directory_type"] = (
            capo_transfer.types.home_directory_type.deserialize_aws_json_1_1(
                data["HomeDirectoryType"]
            )
        )
    if data.get("HomeDirectoryMappings") is not None:
        import capo_transfer.types.home_directory_mappings

        out["home_directory_mappings"] = (
            capo_transfer.types.home_directory_mappings.deserialize_aws_json_1_1(
                data["HomeDirectoryMappings"]
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
    else:
        raise DeserializationError("CreateUserRequest.role required")
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("CreateUserRequest.server_id required")
    if data.get("SshPublicKeyBody") is not None:
        out["ssh_public_key_body"] = data["SshPublicKeyBody"]
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("UserName") is not None:
        out["user_name"] = data["UserName"]
    else:
        raise DeserializationError("CreateUserRequest.user_name required")
    return out
