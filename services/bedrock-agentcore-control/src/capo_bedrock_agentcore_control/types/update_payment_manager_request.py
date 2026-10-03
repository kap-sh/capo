"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatePaymentManagerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.payment_manager_id
    import capo_bedrock_agentcore_control.types.payments_authorizer_type
    import capo_bedrock_agentcore_control.types.payments_description
    import capo_bedrock_agentcore_control.types.role_arn


class UpdatePaymentManagerRequest(TypedDict, closed=True):
    payment_manager_id: (
        "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId"
    )
    """<p>The unique identifier of the payment manager to update.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
    ]
    """<p>The updated description of the payment manager.</p>"""
    authorizer_type: NotRequired[
        "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
    ]
    """<p>The updated authorizer type for the payment manager.</p>"""
    authorizer_configuration: NotRequired[
        "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    """<p>The updated authorizer configuration for the payment manager.</p>"""
    role_arn: NotRequired["capo_bedrock_agentcore_control.types.role_arn.RoleArn"]
    """<p>The updated Amazon Resource Name (ARN) of the IAM role for the payment manager.</p>"""
    client_token: NotRequired[
        "capo_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>"""
    kms_key_arn: NotRequired[
        "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The updated Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt sensitive payment manager data at rest.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePaymentManagerRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "authorizer_type" in value:
        import capo_bedrock_agentcore_control.types.payments_authorizer_type

        out["authorizerType"] = (
            capo_bedrock_agentcore_control.types.payments_authorizer_type.serialize_json(
                value["authorizer_type"]
            )
        )
    if "authorizer_configuration" in value:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> UpdatePaymentManagerRequest:
    out: UpdatePaymentManagerRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("authorizerType") is not None:
        import capo_bedrock_agentcore_control.types.payments_authorizer_type

        out["authorizer_type"] = (
            capo_bedrock_agentcore_control.types.payments_authorizer_type.deserialize_json(
                data["authorizerType"]
            )
        )
    if data.get("authorizerConfiguration") is not None:
        import capo_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            capo_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
