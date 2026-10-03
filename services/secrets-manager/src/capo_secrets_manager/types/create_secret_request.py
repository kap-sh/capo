"""Generated from Smithy shape ``com.amazonaws.secretsmanager#CreateSecretRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.add_replica_region_list_type
    import capo_secrets_manager.types.boolean_type
    import capo_secrets_manager.types.client_request_token_type
    import capo_secrets_manager.types.description_type
    import capo_secrets_manager.types.kms_key_id_type
    import capo_secrets_manager.types.medea_type_type
    import capo_secrets_manager.types.name_type
    import capo_secrets_manager.types.secret_binary_type
    import capo_secrets_manager.types.secret_string_type
    import capo_secrets_manager.types.tag_list_type


class CreateSecretRequest(TypedDict, closed=True):
    name: "capo_secrets_manager.types.name_type.NameType"
    """<p>The name of the new secret.</p> <p>The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@-</p> <p>Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.</p>"""
    client_request_token: NotRequired[
        "capo_secrets_manager.types.client_request_token_type.ClientRequestTokenType"
    ]
    """<p>If you include <code>SecretString</code> or <code>SecretBinary</code>, then Secrets Manager creates an initial version for the secret, and this parameter specifies the unique identifier for the new version. </p> <note> <p>If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. </p> </note> <p>If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a <code>ClientRequestToken</code> and include it in the request.</p> <p>This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value to ensure uniqueness of your versions within the specified secret. </p> <ul> <li> <p>If the <code>ClientRequestToken</code> value isn't already associated with a version of the secret then a new version of the secret is created. </p> </li> <li> <p>If a version with this value already exists and the version <code>SecretString</code> and <code>SecretBinary</code> values are the same as those in the request, then the request is ignored.</p> </li> <li> <p>If a version with this value already exists and that version's <code>SecretString</code> and <code>SecretBinary</code> values are different from those in the request, then the request fails because you cannot modify an existing version. Instead, use <a>PutSecretValue</a> to create a new version.</p> </li> </ul> <p>This value becomes the <code>VersionId</code> of the new version.</p>"""
    description: NotRequired[
        "capo_secrets_manager.types.description_type.DescriptionType"
    ]
    """<p>The description of the secret.</p>"""
    kms_key_id: NotRequired["capo_secrets_manager.types.kms_key_id_type.KmsKeyIdType"]
    """<p>The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by <code>alias/</code>, for example <code>alias/aws/secretsmanager</code>. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html">About aliases</a>.</p> <p>To use a KMS key in a different account, use the key ARN or the alias ARN.</p> <p>If you don't specify this value, then Secrets Manager uses the key <code>aws/secretsmanager</code>. If that key doesn't yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.</p> <p>If the secret is in a different Amazon Web Services account from the credentials calling the API, then you can't use <code>aws/secretsmanager</code> to encrypt the secret, and you must create and use a customer managed KMS key. </p>"""
    secret_binary: NotRequired[
        "capo_secrets_manager.types.secret_binary_type.SecretBinaryType"
    ]
    """<p>The binary data to encrypt and store in the new version of the secret. We recommend that you store your binary data in a file and then pass the contents of the file as a parameter.</p> <p>Either <code>SecretString</code> or <code>SecretBinary</code> must have a value, but not both.</p> <p>This parameter is not available in the Secrets Manager console.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""
    secret_string: NotRequired[
        "capo_secrets_manager.types.secret_string_type.SecretStringType"
    ]
    """<p>The text data to encrypt and store in this new version of the secret. We recommend you use a JSON structure of key/value pairs for your secret value.</p> <p>Either <code>SecretString</code> or <code>SecretBinary</code> must have a value, but not both.</p> <p>If you create a secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the <code>SecretString</code> parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that a Lambda rotation function can parse.</p> <p>Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.</p>"""
    tags: NotRequired["capo_secrets_manager.types.tag_list_type.TagListType"]
    """<p>A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:</p> <p> <code>[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]</code> </p> <p>Secrets Manager tag key names are case sensitive. A tag with the key "ABC" is a different tag from one with key "abc".</p> <p>If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an <code>Access Denied</code> error. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac">Control access to secrets using tags</a> and <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2">Limit access to identities with tags that match secrets' tags</a>.</p> <p>For information about how to format a JSON parameter for the various command line tool environments, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json">Using JSON for Parameters</a>. If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.</p> <p>For tag quotas and naming restrictions, see <a href="https://docs.aws.amazon.com/general/latest/gr/arg.html#taged-reference-quotas">Service quotas for Tagging</a> in the <i>Amazon Web Services General Reference guide</i>.</p>"""
    add_replica_regions: NotRequired[
        "capo_secrets_manager.types.add_replica_region_list_type.AddReplicaRegionListType"
    ]
    """<p>A list of Regions and KMS keys to replicate secrets.</p>"""
    force_overwrite_replica_secret: (
        "capo_secrets_manager.types.boolean_type.BooleanType"
    )
    """<p>Specifies whether to overwrite a secret with the same name in the destination Region. By default, secrets aren't overwritten.</p>"""
    type: NotRequired["capo_secrets_manager.types.medea_type_type.MedeaTypeType"]
    """<p>The exact string that identifies the partner that holds the external secret. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html">Using Secrets Manager managed external secrets</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSecretRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "description" in value:
        out["Description"] = value["description"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "secret_binary" in value:
        import capo_secrets_manager.types.secret_binary_type

        out["SecretBinary"] = (
            capo_secrets_manager.types.secret_binary_type.serialize_aws_json_1_1(
                value["secret_binary"]
            )
        )
    if "secret_string" in value:
        out["SecretString"] = value["secret_string"]
    if "tags" in value:
        import capo_secrets_manager.types.tag_list_type

        out["Tags"] = capo_secrets_manager.types.tag_list_type.serialize_aws_json_1_1(
            value["tags"]
        )
    if "add_replica_regions" in value:
        import capo_secrets_manager.types.add_replica_region_list_type

        out["AddReplicaRegions"] = (
            capo_secrets_manager.types.add_replica_region_list_type.serialize_aws_json_1_1(
                value["add_replica_regions"]
            )
        )
    out["ForceOverwriteReplicaSecret"] = value.get(
        "force_overwrite_replica_secret", False
    )
    if "type" in value:
        out["Type"] = value["type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSecretRequest:
    out: CreateSecretRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateSecretRequest.name required")
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("SecretBinary") is not None:
        import capo_secrets_manager.types.secret_binary_type

        out["secret_binary"] = (
            capo_secrets_manager.types.secret_binary_type.deserialize_aws_json_1_1(
                data["SecretBinary"]
            )
        )
    if data.get("SecretString") is not None:
        out["secret_string"] = data["SecretString"]
    if data.get("Tags") is not None:
        import capo_secrets_manager.types.tag_list_type

        out["tags"] = capo_secrets_manager.types.tag_list_type.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("AddReplicaRegions") is not None:
        import capo_secrets_manager.types.add_replica_region_list_type

        out["add_replica_regions"] = (
            capo_secrets_manager.types.add_replica_region_list_type.deserialize_aws_json_1_1(
                data["AddReplicaRegions"]
            )
        )
    if data.get("ForceOverwriteReplicaSecret") is not None:
        out["force_overwrite_replica_secret"] = data["ForceOverwriteReplicaSecret"]
    else:
        out["force_overwrite_replica_secret"] = False
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    return out
