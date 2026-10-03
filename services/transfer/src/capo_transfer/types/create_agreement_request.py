"""Generated from Smithy shape ``com.amazonaws.transfer#CreateAgreementRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_transfer.errors import DeserializationError

if TYPE_CHECKING:
    import capo_transfer.types.agreement_status_type
    import capo_transfer.types.custom_directories_type
    import capo_transfer.types.description
    import capo_transfer.types.enforce_message_signing_type
    import capo_transfer.types.home_directory
    import capo_transfer.types.preserve_filename_type
    import capo_transfer.types.profile_id
    import capo_transfer.types.role
    import capo_transfer.types.server_id
    import capo_transfer.types.tags


class CreateAgreementRequest(TypedDict, closed=True):
    description: NotRequired["capo_transfer.types.description.Description"]
    """<p>A name or short description to identify the agreement. </p>"""
    server_id: "capo_transfer.types.server_id.ServerId"
    """<p>A system-assigned unique identifier for a server instance. This is the specific server that the agreement uses.</p>"""
    local_profile_id: "capo_transfer.types.profile_id.ProfileId"
    """<p>A unique identifier for the AS2 local profile.</p>"""
    partner_profile_id: "capo_transfer.types.profile_id.ProfileId"
    """<p>A unique identifier for the partner profile used in the agreement.</p>"""
    base_directory: NotRequired["capo_transfer.types.home_directory.HomeDirectory"]
    """<p>The landing directory (folder) for files transferred by using the AS2 protocol.</p> <p>A <code>BaseDirectory</code> example is <code>/<i>amzn-s3-demo-bucket</i>/home/mydirectory</code>.</p>"""
    access_role: "capo_transfer.types.role.Role"
    """<p>Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the Identity and Access Management role to use.</p> <p> <b>For AS2 connectors</b> </p> <p>With AS2, you can send files by calling <code>StartFileTransfer</code> and specifying the file paths in the request parameter, <code>SendFilePaths</code>. We use the file’s parent directory (for example, for <code>--send-file-paths /bucket/dir/file.txt</code>, parent directory is <code>/bucket/dir/</code>) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the <code>AccessRole</code> needs to provide read and write access to the parent directory of the file location used in the <code>StartFileTransfer</code> request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with <code>StartFileTransfer</code>.</p> <p>If you are using Basic authentication for your AS2 connector, the access role requires the <code>secretsmanager:GetSecretValue</code> permission for the secret. If the secret is encrypted using a customer-managed key instead of the Amazon Web Services managed key in Secrets Manager, then the role also needs the <code>kms:Decrypt</code> permission for that key.</p> <p> <b>For SFTP connectors</b> </p> <p>Make sure that the access role provides read and write access to the parent directory of the file location that's used in the <code>StartFileTransfer</code> request. Additionally, make sure that the role provides <code>secretsmanager:GetSecretValue</code> permission to Secrets Manager.</p>"""
    status: NotRequired["capo_transfer.types.agreement_status_type.AgreementStatusType"]
    """<p>The status of the agreement. The agreement can be either <code>ACTIVE</code> or <code>INACTIVE</code>.</p>"""
    tags: NotRequired["capo_transfer.types.tags.Tags"]
    """<p>Key-value pairs that can be used to group and search for agreements.</p>"""
    preserve_filename: NotRequired[
        "capo_transfer.types.preserve_filename_type.PreserveFilenameType"
    ]
    """<p> Determines whether or not Transfer Family appends a unique string of characters to the end of the AS2 message payload filename when saving it. </p> <ul> <li> <p> <code>ENABLED</code>: the filename provided by your trading parter is preserved when the file is saved.</p> </li> <li> <p> <code>DISABLED</code> (default value): when Transfer Family saves the file, the filename is adjusted, as described in <a href="https://docs.aws.amazon.com/transfer/latest/userguide/send-as2-messages.html#file-names-as2">File names and locations</a>.</p> </li> </ul>"""
    enforce_message_signing: NotRequired[
        "capo_transfer.types.enforce_message_signing_type.EnforceMessageSigningType"
    ]
    """<p> Determines whether or not unsigned messages from your trading partners will be accepted. </p> <ul> <li> <p> <code>ENABLED</code>: Transfer Family rejects unsigned messages from your trading partner.</p> </li> <li> <p> <code>DISABLED</code> (default value): Transfer Family accepts unsigned messages from your trading partner.</p> </li> </ul>"""
    custom_directories: NotRequired[
        "capo_transfer.types.custom_directories_type.CustomDirectoriesType"
    ]
    """<p>A <code>CustomDirectoriesType</code> structure. This structure specifies custom directories for storing various AS2 message files. You can specify directories for the following types of files.</p> <ul> <li> <p>Failed files</p> </li> <li> <p>MDN files</p> </li> <li> <p>Payload files</p> </li> <li> <p>Status files</p> </li> <li> <p>Temporary files</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateAgreementRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    out["ServerId"] = value["server_id"]
    out["LocalProfileId"] = value["local_profile_id"]
    out["PartnerProfileId"] = value["partner_profile_id"]
    if "base_directory" in value:
        out["BaseDirectory"] = value["base_directory"]
    out["AccessRole"] = value["access_role"]
    if "status" in value:
        import capo_transfer.types.agreement_status_type

        out["Status"] = (
            capo_transfer.types.agreement_status_type.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "tags" in value:
        import capo_transfer.types.tags

        out["Tags"] = capo_transfer.types.tags.serialize_aws_json_1_1(value["tags"])
    if "preserve_filename" in value:
        import capo_transfer.types.preserve_filename_type

        out["PreserveFilename"] = (
            capo_transfer.types.preserve_filename_type.serialize_aws_json_1_1(
                value["preserve_filename"]
            )
        )
    if "enforce_message_signing" in value:
        import capo_transfer.types.enforce_message_signing_type

        out["EnforceMessageSigning"] = (
            capo_transfer.types.enforce_message_signing_type.serialize_aws_json_1_1(
                value["enforce_message_signing"]
            )
        )
    if "custom_directories" in value:
        import capo_transfer.types.custom_directories_type

        out["CustomDirectories"] = (
            capo_transfer.types.custom_directories_type.serialize_aws_json_1_1(
                value["custom_directories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateAgreementRequest:
    out: CreateAgreementRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("ServerId") is not None:
        out["server_id"] = data["ServerId"]
    else:
        raise DeserializationError("CreateAgreementRequest.server_id required")
    if data.get("LocalProfileId") is not None:
        out["local_profile_id"] = data["LocalProfileId"]
    else:
        raise DeserializationError("CreateAgreementRequest.local_profile_id required")
    if data.get("PartnerProfileId") is not None:
        out["partner_profile_id"] = data["PartnerProfileId"]
    else:
        raise DeserializationError("CreateAgreementRequest.partner_profile_id required")
    if data.get("BaseDirectory") is not None:
        out["base_directory"] = data["BaseDirectory"]
    if data.get("AccessRole") is not None:
        out["access_role"] = data["AccessRole"]
    else:
        raise DeserializationError("CreateAgreementRequest.access_role required")
    if data.get("Status") is not None:
        import capo_transfer.types.agreement_status_type

        out["status"] = (
            capo_transfer.types.agreement_status_type.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("Tags") is not None:
        import capo_transfer.types.tags

        out["tags"] = capo_transfer.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if data.get("PreserveFilename") is not None:
        import capo_transfer.types.preserve_filename_type

        out["preserve_filename"] = (
            capo_transfer.types.preserve_filename_type.deserialize_aws_json_1_1(
                data["PreserveFilename"]
            )
        )
    if data.get("EnforceMessageSigning") is not None:
        import capo_transfer.types.enforce_message_signing_type

        out["enforce_message_signing"] = (
            capo_transfer.types.enforce_message_signing_type.deserialize_aws_json_1_1(
                data["EnforceMessageSigning"]
            )
        )
    if data.get("CustomDirectories") is not None:
        import capo_transfer.types.custom_directories_type

        out["custom_directories"] = (
            capo_transfer.types.custom_directories_type.deserialize_aws_json_1_1(
                data["CustomDirectories"]
            )
        )
    return out
