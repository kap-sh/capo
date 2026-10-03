"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementContextDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.engagement_context_identifier
    import capo_partnercentral_selling.types.engagement_context_payload
    import capo_partnercentral_selling.types.engagement_context_type


class EngagementContextDetails(TypedDict, closed=True):
    id: NotRequired[
        "capo_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier"
    ]
    """<p>The unique identifier of the engagement context. This ID is used to reference and manage the specific context within the engagement.</p>"""
    type: "capo_partnercentral_selling.types.engagement_context_type.EngagementContextType"
    """<p>Specifies the type of Engagement context. Valid values are "CustomerProject" or "Document", indicating whether the context relates to a customer project or a document respectively. </p>"""
    payload: NotRequired[
        "capo_partnercentral_selling.types.engagement_context_payload.EngagementContextPayload"
    ]
    """<p>Contains the specific details of the Engagement context. The structure of this payload varies depending on the Type field. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementContextDetails) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    import capo_partnercentral_selling.types.engagement_context_type

    out["Type"] = (
        capo_partnercentral_selling.types.engagement_context_type.serialize_aws_json_1_0(
            value["type"]
        )
    )
    if "payload" in value:
        import capo_partnercentral_selling.types.engagement_context_payload

        out["Payload"] = (
            capo_partnercentral_selling.types.engagement_context_payload.serialize_aws_json_1_0(
                value["payload"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementContextDetails:
    out: EngagementContextDetails = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Type") is not None:
        import capo_partnercentral_selling.types.engagement_context_type

        out["type"] = (
            capo_partnercentral_selling.types.engagement_context_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("EngagementContextDetails.type required")
    if data.get("Payload") is not None:
        import capo_partnercentral_selling.types.engagement_context_payload

        out["payload"] = (
            capo_partnercentral_selling.types.engagement_context_payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    return out
