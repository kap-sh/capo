"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_quicksight.types.integer
    import capo_quicksight.types.long
    import capo_quicksight.types.public_space_arn
    import capo_quicksight.types.public_space_id
    import capo_quicksight.types.space_description
    import capo_quicksight.types.space_name


class SpaceSummary(TypedDict, closed=True):
    space_id: "capo_quicksight.types.public_space_id.PublicSpaceId"
    """<p>The ID of the space.</p>"""
    space_arn: NotRequired["capo_quicksight.types.public_space_arn.PublicSpaceArn"]
    """<p>The ARN of the space.</p>"""
    name: NotRequired["capo_quicksight.types.space_name.SpaceName"]
    """<p>The display name of the space.</p>"""
    description: NotRequired["capo_quicksight.types.space_description.SpaceDescription"]
    """<p>The description of the space.</p>"""
    updated_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the space was last updated.</p>"""
    consumed_source_size: NotRequired["capo_quicksight.types.long.Long"]
    """<p>The total consumed source size in bytes.</p>"""
    consumed_source_doc_count: NotRequired["capo_quicksight.types.integer.Integer"]
    """<p>The number of consumed source documents.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The date and time that the space was created.</p>"""
    created_by: NotRequired["str"]
    """<p>The user who created the space.</p>"""
    created_by_arn: NotRequired["str"]
    """<p>The ARN of the user who created the space.</p>"""
    resources_count: NotRequired["capo_quicksight.types.integer.Integer"]
    """<p>The number of resources in the space.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceSummary) -> dict:
    out: dict = {}
    out["spaceId"] = value["space_id"]
    if "space_arn" in value:
        out["spaceArn"] = value["space_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "updated_at" in value:
        import capo_quicksight.types._prelude.timestamp

        out["updatedAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["updated_at"]
        )
    if "consumed_source_size" in value:
        out["consumedSourceSize"] = value["consumed_source_size"]
    if "consumed_source_doc_count" in value:
        out["consumedSourceDocCount"] = value["consumed_source_doc_count"]
    if "created_at" in value:
        import capo_quicksight.types._prelude.timestamp

        out["createdAt"] = capo_quicksight.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    if "created_by_arn" in value:
        out["createdByArn"] = value["created_by_arn"]
    if "resources_count" in value:
        out["resourcesCount"] = value["resources_count"]
    return out


def deserialize_json(data: dict) -> SpaceSummary:
    out: SpaceSummary = {}  # type: ignore[typeddict-item]
    if data.get("spaceId") is not None:
        out["space_id"] = data["spaceId"]
    else:
        raise DeserializationError("SpaceSummary.space_id required")
    if data.get("spaceArn") is not None:
        out["space_arn"] = data["spaceArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("updatedAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["updated_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["updatedAt"]
        )
    if data.get("consumedSourceSize") is not None:
        out["consumed_source_size"] = data["consumedSourceSize"]
    if data.get("consumedSourceDocCount") is not None:
        out["consumed_source_doc_count"] = data["consumedSourceDocCount"]
    if data.get("createdAt") is not None:
        import capo_quicksight.types._prelude.timestamp

        out["created_at"] = capo_quicksight.types._prelude.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    if data.get("createdByArn") is not None:
        out["created_by_arn"] = data["createdByArn"]
    if data.get("resourcesCount") is not None:
        out["resources_count"] = data["resourcesCount"]
    return out


def redact_sensitive(value: SpaceSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
