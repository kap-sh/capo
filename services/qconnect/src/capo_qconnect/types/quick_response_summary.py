"""Generated from Smithy shape ``com.amazonaws.qconnect#QuickResponseSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_qconnect.types.arn
    import capo_qconnect.types.channels
    import capo_qconnect.types.generic_arn
    import capo_qconnect.types.quick_response_description
    import capo_qconnect.types.quick_response_name
    import capo_qconnect.types.quick_response_status
    import capo_qconnect.types.quick_response_type
    import capo_qconnect.types.tags
    import capo_qconnect.types.uuid


class QuickResponseSummary(TypedDict, closed=True):
    quick_response_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the quick response.</p>"""
    quick_response_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the quick response.</p>"""
    knowledge_base_arn: "capo_qconnect.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the knowledge base.</p>"""
    knowledge_base_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the knowledge base.</p>"""
    name: "capo_qconnect.types.quick_response_name.QuickResponseName"
    """<p>The name of the quick response.</p>"""
    content_type: "capo_qconnect.types.quick_response_type.QuickResponseType"
    """<p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>"""
    status: "capo_qconnect.types.quick_response_status.QuickResponseStatus"
    """<p>The resource status of the quick response.</p>"""
    created_time: "datetime.datetime"
    """<p>The timestamp when the quick response was created.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp when the quick response summary was last modified.</p>"""
    description: NotRequired[
        "capo_qconnect.types.quick_response_description.QuickResponseDescription"
    ]
    """<p>The description of the quick response.</p>"""
    last_modified_by: NotRequired["capo_qconnect.types.generic_arn.GenericArn"]
    """<p>The Amazon Resource Name (ARN) of the user who last updated the quick response data.</p>"""
    is_active: NotRequired["bool"]
    """<p>Whether the quick response is active.</p>"""
    channels: NotRequired["capo_qconnect.types.channels.Channels"]
    """<p>The Connect Customer contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>"""
    tags: NotRequired["capo_qconnect.types.tags.Tags"]
    """<p>The tags used to organize, track, or control access for this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickResponseSummary) -> dict:
    out: dict = {}
    out["quickResponseArn"] = value["quick_response_arn"]
    out["quickResponseId"] = value["quick_response_id"]
    out["knowledgeBaseArn"] = value["knowledge_base_arn"]
    out["knowledgeBaseId"] = value["knowledge_base_id"]
    out["name"] = value["name"]
    out["contentType"] = value["content_type"]
    out["status"] = value["status"]
    out["createdTime"] = value["created_time"].timestamp()
    out["lastModifiedTime"] = value["last_modified_time"].timestamp()
    if "description" in value:
        out["description"] = value["description"]
    if "last_modified_by" in value:
        out["lastModifiedBy"] = value["last_modified_by"]
    if "is_active" in value:
        out["isActive"] = value["is_active"]
    if "channels" in value:
        import capo_qconnect.types.channels

        out["channels"] = capo_qconnect.types.channels.serialize_json(value["channels"])
    if "tags" in value:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> QuickResponseSummary:
    out: QuickResponseSummary = {}  # type: ignore[typeddict-item]
    if data.get("quickResponseArn") is not None:
        out["quick_response_arn"] = data["quickResponseArn"]
    else:
        out["quick_response_arn"] = ""
    if data.get("quickResponseId") is not None:
        out["quick_response_id"] = data["quickResponseId"]
    else:
        out["quick_response_id"] = ""
    if data.get("knowledgeBaseArn") is not None:
        out["knowledge_base_arn"] = data["knowledgeBaseArn"]
    else:
        out["knowledge_base_arn"] = ""
    if data.get("knowledgeBaseId") is not None:
        out["knowledge_base_id"] = data["knowledgeBaseId"]
    else:
        out["knowledge_base_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("contentType") is not None:
        out["content_type"] = data["contentType"]
    else:
        out["content_type"] = ""
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("createdTime") is not None:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            float(data["createdTime"]), tz=datetime.timezone.utc
        )
    else:
        import datetime

        out["created_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedTime") is not None:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            float(data["lastModifiedTime"]), tz=datetime.timezone.utc
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("lastModifiedBy") is not None:
        out["last_modified_by"] = data["lastModifiedBy"]
    if data.get("isActive") is not None:
        out["is_active"] = data["isActive"]
    if data.get("channels") is not None:
        import capo_qconnect.types.channels

        out["channels"] = capo_qconnect.types.channels.deserialize_json(
            data["channels"]
        )
    if data.get("tags") is not None:
        import capo_qconnect.types.tags

        out["tags"] = capo_qconnect.types.tags.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: QuickResponseSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "channels" in value:
        import capo_qconnect.types.channels

        out["channels"] = capo_qconnect.types.channels.redact_sensitive(
            value["channels"]
        )
    return out
