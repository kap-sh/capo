"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateGuardrailVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.guardrail_description
    import capo_bedrock.types.guardrail_identifier
    import capo_bedrock.types.idempotency_token


class CreateGuardrailVersionRequest(TypedDict, closed=True):
    guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier"
    """<p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>"""
    description: NotRequired[
        "capo_bedrock.types.guardrail_description.GuardrailDescription"
    ]
    """<p>A description of the guardrail version.</p>"""
    client_request_token: NotRequired[
        "capo_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon S3 User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateGuardrailVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateGuardrailVersionRequest:
    out: CreateGuardrailVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("clientRequestToken") is not None:
        out["client_request_token"] = data["clientRequestToken"]
    return out
