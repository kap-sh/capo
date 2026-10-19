"""Generated from Smithy shape ``com.amazonaws.qconnect#AssistantAssociationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.arn
    import capo_qconnect.types.assistant_association_output_data
    import capo_qconnect.types.association_type
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid


class AssistantAssociationSummary(TypedDict, closed=True):
    assistant_association_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the assistant association.</p>"""
    assistant_association_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the assistant association.</p>"""
    assistant_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    assistant_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    association_type: "capo_qconnect.types.association_type.AssociationType"
    """<p>The type of association.</p>"""
    association_data: "capo_qconnect.types.assistant_association_output_data.AssistantAssociationOutputData"
    """<p>The association data.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssistantAssociationSummary) -> dict:
    out: dict = {}
    out["assistantAssociationId"] = value["assistant_association_id"]
    out["assistantAssociationArn"] = value["assistant_association_arn"]
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["associationType"] = value["association_type"]
    import capo_qconnect.types.assistant_association_output_data

    out["associationData"] = (
        capo_qconnect.types.assistant_association_output_data.serialize_json(
            value["association_data"]
        )
    )
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> AssistantAssociationSummary:
    out: AssistantAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("assistantAssociationId") is not None:
        out["assistant_association_id"] = data["assistantAssociationId"]
    else:
        out["assistant_association_id"] = ""
    if data.get("assistantAssociationArn") is not None:
        out["assistant_association_arn"] = data["assistantAssociationArn"]
    else:
        out["assistant_association_arn"] = ""
    if data.get("assistantId") is not None:
        out["assistant_id"] = data["assistantId"]
    else:
        out["assistant_id"] = ""
    if data.get("assistantArn") is not None:
        out["assistant_arn"] = data["assistantArn"]
    else:
        out["assistant_arn"] = ""
    if data.get("associationType") is not None:
        out["association_type"] = data["associationType"]
    else:
        out["association_type"] = ""
    if data.get("associationData") is not None:
        import capo_qconnect.types.assistant_association_output_data

        out["association_data"] = (
            capo_qconnect.types.assistant_association_output_data.deserialize_json(
                data["associationData"]
            )
        )
    else:
        import capo_qconnect.types._unknown

        out["association_data"] = capo_qconnect.types._unknown.UnknownUnionMember("")
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out
