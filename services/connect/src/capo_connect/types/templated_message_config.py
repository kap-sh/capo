"""Generated from Smithy shape ``com.amazonaws.connect#TemplatedMessageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.message_template_id
    import capo_connect.types.message_template_knowledge_base_id
    import capo_connect.types.template_attributes


class TemplatedMessageConfig(TypedDict, closed=True):
    knowledge_base_id: "capo_connect.types.message_template_knowledge_base_id.MessageTemplateKnowledgeBaseId"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "capo_connect.types.message_template_id.MessageTemplateId"
    """<p>The identifier of the message template Id.</p>"""
    template_attributes: "capo_connect.types.template_attributes.TemplateAttributes"
    """<p>Information about template attributes, that is, CustomAttributes or CustomerProfileAttributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplatedMessageConfig) -> dict:
    out: dict = {}
    out["KnowledgeBaseId"] = value["knowledge_base_id"]
    out["MessageTemplateId"] = value["message_template_id"]
    import capo_connect.types.template_attributes

    out["TemplateAttributes"] = capo_connect.types.template_attributes.serialize_json(
        value["template_attributes"]
    )
    return out


def deserialize_json(data: dict) -> TemplatedMessageConfig:
    out: TemplatedMessageConfig = {}  # type: ignore[typeddict-item]
    if data.get("KnowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["KnowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("MessageTemplateId") is not None:
        out["message_template_id"] = data["MessageTemplateId"]
    else:
        out["message_template_id"] = ""
    if data.get("TemplateAttributes") is not None:
        import capo_connect.types.template_attributes

        out["template_attributes"] = (
            capo_connect.types.template_attributes.deserialize_json(
                data["TemplateAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "TemplatedMessageConfig.template_attributes required"
        )
    return out
