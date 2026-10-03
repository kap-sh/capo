"""Generated from Smithy shape ``com.amazonaws.secretsmanager#RotateSecretRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_secrets_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_secrets_manager.types.boolean_type
    import capo_secrets_manager.types.client_request_token_type
    import capo_secrets_manager.types.external_secret_rotation_metadata_type
    import capo_secrets_manager.types.role_arn_type
    import capo_secrets_manager.types.rotation_lambda_arn_type
    import capo_secrets_manager.types.rotation_rules_type
    import capo_secrets_manager.types.secret_id_type


class RotateSecretRequest(TypedDict, closed=True):
    secret_id: "capo_secrets_manager.types.secret_id_type.SecretIdType"
    """<p>The ARN or name of the secret to rotate.</p> <p>For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen">Finding a secret from a partial ARN</a>.</p>"""
    client_request_token: NotRequired[
        "capo_secrets_manager.types.client_request_token_type.ClientRequestTokenType"
    ]
    """<p>A unique identifier for the new version of the secret. You only need to specify this value if you implement your own retry logic and you want to ensure that Secrets Manager doesn't attempt to create a secret version twice.</p> <note> <p>If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request. </p> </note> <p>If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a <code>ClientRequestToken</code> and include it in the request.</p> <p>This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID-type</a> value to ensure uniqueness of your versions within the specified secret. </p>"""
    rotation_lambda_arn: NotRequired[
        "capo_secrets_manager.types.rotation_lambda_arn_type.RotationLambdaARNType"
    ]
    """<p>For secrets that use a Lambda rotation function to rotate, the ARN of the Lambda rotation function. </p> <p>For secrets that use <i>managed rotation</i>, omit this field. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_managed.html">Managed rotation</a> in the <i>Secrets Manager User Guide</i>.</p>"""
    rotation_rules: NotRequired[
        "capo_secrets_manager.types.rotation_rules_type.RotationRulesType"
    ]
    """<p>A structure that defines the rotation configuration for this secret.</p> <important> <p>When changing an existing rotation schedule and setting <code>RotateImmediately</code> to <code>false</code>:</p> <ul> <li> <p>If using <code>AutomaticallyAfterDays</code> or a <code>ScheduleExpression</code> with <code>rate()</code>, the previously scheduled rotation might still occur.</p> </li> <li> <p>To prevent unintended rotations, use a <code>ScheduleExpression</code> with <code>cron()</code> for granular control over rotation windows.</p> </li> </ul> </important>"""
    external_secret_rotation_metadata: NotRequired[
        "capo_secrets_manager.types.external_secret_rotation_metadata_type.ExternalSecretRotationMetadataType"
    ]
    """<p>The metadata needed to successfully rotate a managed external secret. A list of key value pairs in JSON format specified by the partner. For more information about the required information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/managed-external-secrets.html">Using Secrets Manager managed external secrets</a> </p>"""
    external_secret_rotation_role_arn: NotRequired[
        "capo_secrets_manager.types.role_arn_type.RoleARNType"
    ]
    """<p>The Amazon Resource Name (ARN) of the role that allows Secrets Manager to rotate a secret held by a third-party partner. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/mes-security.html">Security and permissions</a>.</p>"""
    rotate_immediately: NotRequired[
        "capo_secrets_manager.types.boolean_type.BooleanType"
    ]
    """<p>Specifies whether to rotate the secret immediately or wait until the next scheduled rotation window. The rotation schedule is defined in <a>RotateSecretRequest$RotationRules</a>.</p> <p>The default for <code>RotateImmediately</code> is <code>true</code>. If you don't specify this value, Secrets Manager rotates the secret immediately.</p> <p>If you set <code>RotateImmediately</code> to <code>false</code>, Secrets Manager tests the rotation configuration by running the <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html"> <code>testSecret</code> step</a> of the Lambda rotation function. This test creates an <code>AWSPENDING</code> version of the secret and then removes it.</p> <p>When changing an existing rotation schedule and setting <code>RotateImmediately</code> to <code>false</code>:</p> <ul> <li> <p>If using <code>AutomaticallyAfterDays</code> or a <code>ScheduleExpression</code> with <code>rate()</code>, the previously scheduled rotation might still occur.</p> </li> <li> <p>To prevent unintended rotations, use a <code>ScheduleExpression</code> with <code>cron()</code> for granular control over rotation windows.</p> </li> </ul> <p>Rotation is an asynchronous process. For more information, see <a href="https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotate-secrets_how.html">How rotation works</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotateSecretRequest) -> dict:
    out: dict = {}
    out["SecretId"] = value["secret_id"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "rotation_lambda_arn" in value:
        out["RotationLambdaARN"] = value["rotation_lambda_arn"]
    if "rotation_rules" in value:
        import capo_secrets_manager.types.rotation_rules_type

        out["RotationRules"] = (
            capo_secrets_manager.types.rotation_rules_type.serialize_aws_json_1_1(
                value["rotation_rules"]
            )
        )
    if "external_secret_rotation_metadata" in value:
        import capo_secrets_manager.types.external_secret_rotation_metadata_type

        out["ExternalSecretRotationMetadata"] = (
            capo_secrets_manager.types.external_secret_rotation_metadata_type.serialize_aws_json_1_1(
                value["external_secret_rotation_metadata"]
            )
        )
    if "external_secret_rotation_role_arn" in value:
        out["ExternalSecretRotationRoleArn"] = value[
            "external_secret_rotation_role_arn"
        ]
    if "rotate_immediately" in value:
        out["RotateImmediately"] = value["rotate_immediately"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RotateSecretRequest:
    out: RotateSecretRequest = {}  # type: ignore[typeddict-item]
    if data.get("SecretId") is not None:
        out["secret_id"] = data["SecretId"]
    else:
        raise DeserializationError("RotateSecretRequest.secret_id required")
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    if data.get("RotationLambdaARN") is not None:
        out["rotation_lambda_arn"] = data["RotationLambdaARN"]
    if data.get("RotationRules") is not None:
        import capo_secrets_manager.types.rotation_rules_type

        out["rotation_rules"] = (
            capo_secrets_manager.types.rotation_rules_type.deserialize_aws_json_1_1(
                data["RotationRules"]
            )
        )
    if data.get("ExternalSecretRotationMetadata") is not None:
        import capo_secrets_manager.types.external_secret_rotation_metadata_type

        out["external_secret_rotation_metadata"] = (
            capo_secrets_manager.types.external_secret_rotation_metadata_type.deserialize_aws_json_1_1(
                data["ExternalSecretRotationMetadata"]
            )
        )
    if data.get("ExternalSecretRotationRoleArn") is not None:
        out["external_secret_rotation_role_arn"] = data["ExternalSecretRotationRoleArn"]
    if data.get("RotateImmediately") is not None:
        out["rotate_immediately"] = data["RotateImmediately"]
    return out
