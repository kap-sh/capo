"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ContextSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_wellarchitected.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_wellarchitected.types.agent_profile_arn
    import capo_wellarchitected.types.application_type
    import capo_wellarchitected.types.context_content
    import capo_wellarchitected.types.context_type
    import capo_wellarchitected.types.criticality
    import capo_wellarchitected.types.sensitive_string
    import capo_wellarchitected.types.uuid


class ContextSummary(TypedDict, closed=True):
    id: "capo_wellarchitected.types.uuid.UUID"
    """<p>The unique identifier of the context.</p>"""
    profile_arn: "capo_wellarchitected.types.agent_profile_arn.AgentProfileArn"
    """<p>The Amazon Resource Name (ARN) of the associated profile.</p>"""
    title: "capo_wellarchitected.types.sensitive_string.SensitiveString"
    """<p>The title of the context.</p>"""
    context_type: "capo_wellarchitected.types.context_type.ContextType"
    """<p>The type of the context.</p>"""
    content: "capo_wellarchitected.types.context_content.ContextContent"
    """<p>The typed content of the context, containing application-specific fields such as account IDs, Regions, services, and resource types.</p>"""
    application_type: NotRequired[
        "capo_wellarchitected.types.application_type.ApplicationType"
    ]
    """<p>The type of application described by this context.</p>"""
    criticality: NotRequired["capo_wellarchitected.types.criticality.Criticality"]
    """<p>The business criticality of the application described by this context.</p>"""
    created_by: "str"
    """<p>The identifier of the user or system that created this context.</p>"""
    created_at: "datetime.datetime"
    """<p>The timestamp when the context was created.</p>"""
    last_modified_by: NotRequired["str"]
    """<p>The identifier of the user or system that last modified this context.</p>"""
    last_modified_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the context was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContextSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["profileArn"] = value["profile_arn"]
    out["title"] = value["title"]
    import capo_wellarchitected.types.context_type

    out["contextType"] = capo_wellarchitected.types.context_type.serialize_json(
        value["context_type"]
    )
    import capo_wellarchitected.types.context_content

    out["content"] = capo_wellarchitected.types.context_content.serialize_json(
        value["content"]
    )
    if "application_type" in value:
        import capo_wellarchitected.types.application_type

        out["applicationType"] = (
            capo_wellarchitected.types.application_type.serialize_json(
                value["application_type"]
            )
        )
    if "criticality" in value:
        import capo_wellarchitected.types.criticality

        out["criticality"] = capo_wellarchitected.types.criticality.serialize_json(
            value["criticality"]
        )
    out["createdBy"] = value["created_by"]
    import capo_wellarchitected._protocol.serialize

    out["createdAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "last_modified_at" in value:
        import capo_wellarchitected._protocol.serialize

        out["lastModifiedAt"] = capo_wellarchitected._protocol.serialize.fmt_date_time(
            value["last_modified_at"]
        )
    return out


def deserialize_json(data: dict) -> ContextSummary:
    out: ContextSummary = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("profileArn") is not None:
        out["profile_arn"] = data["profileArn"]
    else:
        out["profile_arn"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("contextType") is not None:
        import capo_wellarchitected.types.context_type

        out["context_type"] = capo_wellarchitected.types.context_type.deserialize_json(
            data["contextType"]
        )
    else:
        import typing

        out["context_type"] = typing.cast(
            "capo_wellarchitected.types.context_type.ContextType", ""
        )
    if data.get("content") is not None:
        import capo_wellarchitected.types.context_content

        out["content"] = capo_wellarchitected.types.context_content.deserialize_json(
            data["content"]
        )
    else:
        raise DeserializationError("ContextSummary.content required")
    if data.get("applicationType") is not None:
        import capo_wellarchitected.types.application_type

        out["application_type"] = (
            capo_wellarchitected.types.application_type.deserialize_json(
                data["applicationType"]
            )
        )
    if data.get("criticality") is not None:
        import capo_wellarchitected.types.criticality

        out["criticality"] = capo_wellarchitected.types.criticality.deserialize_json(
            data["criticality"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("lastModifiedAt") is not None:
        import datetime

        out["last_modified_at"] = datetime.datetime.fromisoformat(
            data["lastModifiedAt"].replace("Z", "+00:00")
        )
    return out


def redact_sensitive(value: ContextSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "content" in value:
        import capo_wellarchitected.types.context_content

        out["content"] = capo_wellarchitected.types.context_content.redact_sensitive(
            value["content"]
        )
    return out
