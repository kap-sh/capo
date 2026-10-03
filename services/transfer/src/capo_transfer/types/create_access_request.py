"""Generated from Smithy shape ``com.amazonaws.transfer#CreateAccessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.external_id
    import capo_transfer.types.home_directory
    import capo_transfer.types.home_directory_mappings
    import capo_transfer.types.home_directory_type
    import capo_transfer.types.policy
    import capo_transfer.types.posix_profile
    import capo_transfer.types.role
    import capo_transfer.types.server_id


class CreateAccessRequest(TypedDict, closed=True):
    home_directory: NotRequired["capo_transfer.types.home_directory.HomeDirectory"]
    """<p>The landing directory (folder) for a user when they log in to the server using the client.</p> <p>A <code>HomeDirectory</code> example is <code>/bucket_name/home/mydirectory</code>.</p> <note> <p>You can use the <code>HomeDirectory</code> parameter for <code>HomeDirectoryType</code> when it is set to either <code>PATH</code> or <code>LOGICAL</code>.</p> </note>"""
    home_directory_type: NotRequired[
        "capo_transfer.types.home_directory_type.HomeDirectoryType"
    ]
    """<p>The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to <code>PATH</code>, the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to <code>LOGICAL</code>, you need to provide mappings in the <code>HomeDirectoryMappings</code> for how you want to make Amazon S3 or Amazon EFS paths visible to your users.</p> <note> <p>If <code>HomeDirectoryType</code> is <code>LOGICAL</code>, you must provide mappings, using the <code>HomeDirectoryMappings</code> parameter. If, on the other hand, <code>HomeDirectoryType</code> is <code>PATH</code>, you provide an absolute path using the <code>HomeDirectory</code> parameter. You cannot have both <code>HomeDirectory</code> and <code>HomeDirectoryMappings</code> in your template.</p> </note>"""
    home_directory_mappings: NotRequired[
        "capo_transfer.types.home_directory_mappings.HomeDirectoryMappings"
    ]
    """<p>Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the <code>Entry</code> and <code>Target</code> pair, where <code>Entry</code> shows how the path is made visible and <code>Target</code> is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your Identity and Access Management (IAM) role provides access to paths in <code>Target</code>. This value can be set only when <code>HomeDirectoryType</code> is set to <i>LOGICAL</i>.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example.</p> <p> <code>[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]</code> </p> <p>In most cases, you can use this value instead of the session policy to lock down your user to the designated home directory ("<code>chroot</code>"). To do this, you can set <code>Entry</code> to <code>/</code> and set <code>Target</code> to the <code>HomeDirectory</code> parameter value.</p> <p>The following is an <code>Entry</code> and <code>Target</code> pair example for <code>chroot</code>.</p> <p> <code>[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]</code> </p>"""
    policy: NotRequired["capo_transfer.types.policy.Policy"]
    """<p>A session policy for your user so that you can use the same Identity and Access Management (IAM) role across multiple users. This policy scopes down a user's access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include <code>${Transfer:UserName}</code>, <code>${Transfer:HomeDirectory}</code>, and <code>${Transfer:HomeBucket}</code>.</p> <note> <p>This policy applies only when the domain of <code>ServerId</code> is Amazon S3. Amazon EFS does not use session policies.</p> <p>For session policies, Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the <code>Policy</code> argument.</p> <p>For an example of a session policy, see <a href="https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html">Example session policy</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html">AssumeRole</a> in the <i>Security Token Service API Reference</i>.</p> </note>"""
    posix_profile: NotRequired["capo_transfer.types.posix_profile.PosixProfile"]
    role: "capo_transfer.types.role.Role"
    """<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.</p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.</p>"""
    external_id: "capo_transfer.types.external_id.ExternalId"
    """<p>A unique identifier that is required to identify specific groups within your directory. The users of the group that you associate have access to your Amazon S3 or Amazon EFS resources over the enabled protocols using Transfer Family. If you know the group name, you can view the SID values by running the following command using Windows PowerShell.</p> <p> <code>Get-ADGroup -Filter {samAccountName -like "<i>YourGroupName</i>*"} -Properties * | Select SamAccountName,ObjectSid</code> </p> <p>In that command, replace <i>YourGroupName</i> with the name of your Active Directory group.</p> <p>The regular expression used to validate this parameter is a string of characters consisting of uppercase and lowercase alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@:/-</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAccessRequest) -> dict:
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
    out["ExternalId"] = value["external_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAccessRequest:
    out: CreateAccessRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("CreateAccessRequest.role required")
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("CreateAccessRequest.server_id required")
    if data.get("ExternalId") is not None:
        out["external_id"] = data["ExternalId"]
    else:
        raise DeserializationError("CreateAccessRequest.external_id required")
    return out
