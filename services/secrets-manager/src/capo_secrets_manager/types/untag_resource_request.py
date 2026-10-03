"""Generated from Smithy shape ``com.amazonaws.secretsmanager#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.secret_id_type
    import capo_secrets_manager.types.tag_key_list_type


class UntagResourceRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    tag_keys: "capo_secrets_manager.types.tag_key_list_type.TagKeyListType"
    """<p>A list of tag key names to remove from the secret. You don't specify the value. Both the key and its associated value are removed.</p> <p>This parameter requires a JSON text string argument.</p> <p>For storing multiple values, we recommend that you use a JSON text string argument and specify key/value pairs. For more information, see <a href="https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters.html">Specifying parameter values for the Amazon Web Services CLI</a> in the Amazon Web Services CLI User Guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UntagResourceRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    import capo_secrets_manager.types.tag_key_list_type

    out["TagKeys"] = (
        capo_secrets_manager.types.tag_key_list_type.serialize_aws_json_1_1(
            value["tag_keys"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("UntagResourceRequest.secret_id required")
    if data.get("TagKeys") is not None:
        import capo_secrets_manager.types.tag_key_list_type

        out["tag_keys"] = (
            capo_secrets_manager.types.tag_key_list_type.deserialize_aws_json_1_1(
                data["TagKeys"]
            )
        )
    else:
        raise DeserializationError("UntagResourceRequest.tag_keys required")
    return out
