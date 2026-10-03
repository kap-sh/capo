"""Generated from Smithy shape ``com.amazonaws.wisdom#CreateAssistantAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.assistant_association_input_data
    import capo_wisdom.types.association_type
    import capo_wisdom.types.client_token
    import capo_wisdom.types.tags
    import capo_wisdom.types.uuid_or_arn


class CreateAssistantAssociationRequest(TypedDict, closed=True):
    assistant_id: "capo_wisdom.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Wisdom assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    association_type: "capo_wisdom.types.association_type.AssociationType"
    """<p>The type of association.</p>"""
    association: "capo_wisdom.types.assistant_association_input_data.AssistantAssociationInputData"
    """<p>The identifier of the associated resource.</p>"""
    client_token: NotRequired["capo_wisdom.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""
    tags: NotRequired["capo_wisdom.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAssistantAssociationRequest) -> dict:
    out: dict = {}
    out["associationType"] = value["association_type"]
    import capo_wisdom.types.assistant_association_input_data

    out["association"] = (
        capo_wisdom.types.assistant_association_input_data.serialize_json(
            value["association"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAssistantAssociationRequest:
    out: CreateAssistantAssociationRequest = {}  # type: ignore[typeddict-item]
    if data.get("associationType") is not None:
        out["association_type"] = data["associationType"]
    else:
        raise DeserializationError(
            "CreateAssistantAssociationRequest.association_type required"
        )
    if data.get("association") is not None:
        import capo_wisdom.types.assistant_association_input_data

        out["association"] = (
            capo_wisdom.types.assistant_association_input_data.deserialize_json(
                data["association"]
            )
        )
    else:
        raise DeserializationError(
            "CreateAssistantAssociationRequest.association required"
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_wisdom.types.tags

        out["tags"] = capo_wisdom.types.tags.deserialize_json(data["tags"])
    return out
