"""Generated from Smithy shape ``com.amazonaws.qconnect#UpdateMessageTemplateMetadataRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.description
    import capo_qconnect.types.grouping_configuration
    import capo_qconnect.types.name
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier


class UpdateMessageTemplateMetadataRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
    """<p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>"""
    name: NotRequired["capo_qconnect.types.name.Name"]
    """<p>The name of the message template.</p>"""
    description: NotRequired["capo_qconnect.types.description.Description"]
    """<p>The description of the message template.</p>"""
    grouping_configuration: NotRequired[
        "capo_qconnect.types.grouping_configuration.GroupingConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateMessageTemplateMetadataRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "grouping_configuration" in value:
        import capo_qconnect.types.grouping_configuration

        out["groupingConfiguration"] = (
            capo_qconnect.types.grouping_configuration.serialize_json(
                value["grouping_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateMessageTemplateMetadataRequest:
    out: UpdateMessageTemplateMetadataRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("groupingConfiguration") is not None:
        import capo_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_qconnect.types.grouping_configuration.deserialize_json(
                data["groupingConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateMessageTemplateMetadataRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "grouping_configuration" in value:
        import capo_qconnect.types.grouping_configuration

        out["grouping_configuration"] = (
            capo_qconnect.types.grouping_configuration.redact_sensitive(
                value["grouping_configuration"]
            )
        )
    return out
