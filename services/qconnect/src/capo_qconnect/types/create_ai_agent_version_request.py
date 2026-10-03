"""Generated from Smithy shape ``com.amazonaws.qconnect#CreateAIAgentVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.client_token
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class CreateAIAgentVersionRequest(TypedDict, closed=True):
    assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the Amazon Q in Connect AI Agent.</p>"""
    modified_time: NotRequired["datetime.datetime"]
    """<p>The modification time of the AI Agent should be tracked for version creation. This field should be specified to avoid version creation when simultaneous update to the underlying AI Agent are possible. The value should be the modifiedTime returned from the request to create or update an AI Agent so that version creation can fail if an update to the AI Agent post the specified modification time has been made.</p>"""
    client_token: NotRequired["capo_qconnect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAIAgentVersionRequest) -> dict:
    out: dict = {}
    if "modified_time" in value:
        import capo_qconnect.types._prelude.timestamp

        out["modifiedTime"] = capo_qconnect.types._prelude.timestamp.serialize_json(
            value["modified_time"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateAIAgentVersionRequest:
    out: CreateAIAgentVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("modifiedTime") is not None:
        import capo_qconnect.types._prelude.timestamp

        out["modified_time"] = capo_qconnect.types._prelude.timestamp.deserialize_json(
            data["modifiedTime"]
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
