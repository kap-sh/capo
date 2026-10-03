"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ListSourceRepositoriesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecatalyst.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecatalyst.types.source_repository_description_string
    import capo_codecatalyst.types.source_repository_id_string
    import capo_codecatalyst.types.source_repository_name_string
    import capo_codecatalyst.types.timestamp


class ListSourceRepositoriesItem(TypedDict, closed=True):
    id: "capo_codecatalyst.types.source_repository_id_string.SourceRepositoryIdString"
    """<p>The system-generated unique ID of the source repository.</p>"""
    name: "capo_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the source repository.</p>"""
    description: NotRequired[
        "capo_codecatalyst.types.source_repository_description_string.SourceRepositoryDescriptionString"
    ]
    """<p>The description of the repository, if any.</p>"""
    last_updated_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The time the source repository was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""
    created_time: "capo_codecatalyst.types.timestamp.Timestamp"
    """<p>The time the source repository was created, in coordinated universal time (UTC) timestamp format as specified in <a href="https://www.rfc-editor.org/rfc/rfc3339#section-5.6">RFC 3339</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSourceRepositoriesItem) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_codecatalyst.types.timestamp

    out["lastUpdatedTime"] = capo_codecatalyst.types.timestamp.serialize_json(
        value["last_updated_time"]
    )
    import capo_codecatalyst.types.timestamp

    out["createdTime"] = capo_codecatalyst.types.timestamp.serialize_json(
        value["created_time"]
    )
    return out


def deserialize_json(data: dict) -> ListSourceRepositoriesItem:
    out: ListSourceRepositoriesItem = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        raise DeserializationError("ListSourceRepositoriesItem.id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("ListSourceRepositoriesItem.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("lastUpdatedTime") is not None:
        import capo_codecatalyst.types.timestamp

        out["last_updated_time"] = capo_codecatalyst.types.timestamp.deserialize_json(
            data["lastUpdatedTime"]
        )
    else:
        raise DeserializationError(
            "ListSourceRepositoriesItem.last_updated_time required"
        )
    if data.get("createdTime") is not None:
        import capo_codecatalyst.types.timestamp

        out["created_time"] = capo_codecatalyst.types.timestamp.deserialize_json(
            data["createdTime"]
        )
    else:
        raise DeserializationError("ListSourceRepositoriesItem.created_time required")
    return out
