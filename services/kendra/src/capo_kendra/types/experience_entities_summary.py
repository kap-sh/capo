"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceEntitiesSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.entity_display_data
    import capo_kendra.types.entity_id
    import capo_kendra.types.entity_type


class ExperienceEntitiesSummary(TypedDict, closed=True):
    entity_id: NotRequired["capo_kendra.types.entity_id.EntityId"]
    """<p>The identifier of a user or group in your IAM Identity Center identity source. For example, a user ID could be an email.</p>"""
    entity_type: NotRequired["capo_kendra.types.entity_type.EntityType"]
    """<p>Shows the type as <code>User</code> or <code>Group</code>.</p>"""
    display_data: NotRequired["capo_kendra.types.entity_display_data.EntityDisplayData"]
    """<p>Information about the user entity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperienceEntitiesSummary) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "entity_type" in value:
        import capo_kendra.types.entity_type

        out["EntityType"] = capo_kendra.types.entity_type.serialize_aws_json_1_1(
            value["entity_type"]
        )
    if "display_data" in value:
        import capo_kendra.types.entity_display_data

        out["DisplayData"] = (
            capo_kendra.types.entity_display_data.serialize_aws_json_1_1(
                value["display_data"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExperienceEntitiesSummary:
    out: ExperienceEntitiesSummary = {}  # type: ignore[typeddict-item]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("EntityType") is not None:
        import capo_kendra.types.entity_type

        out["entity_type"] = capo_kendra.types.entity_type.deserialize_aws_json_1_1(
            data["EntityType"]
        )
    if data.get("DisplayData") is not None:
        import capo_kendra.types.entity_display_data

        out["display_data"] = (
            capo_kendra.types.entity_display_data.deserialize_aws_json_1_1(
                data["DisplayData"]
            )
        )
    return out


def redact_sensitive(value: ExperienceEntitiesSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_data" in value:
        import capo_kendra.types.entity_display_data

        out["display_data"] = capo_kendra.types.entity_display_data.redact_sensitive(
            value["display_data"]
        )
    return out
