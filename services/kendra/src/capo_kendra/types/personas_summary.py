"""Generated from Smithy shape ``com.amazonaws.kendra#PersonasSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.entity_id
    import capo_kendra.types.persona
    import capo_kendra.types.timestamp


class PersonasSummary(TypedDict, closed=True):
    entity_id: NotRequired["capo_kendra.types.entity_id.EntityId"]
    """<p>The identifier of a user or group in your IAM Identity Center identity source. For example, a user ID could be an email.</p>"""
    persona: NotRequired["capo_kendra.types.persona.Persona"]
    """<p>The persona that defines the specific permissions of the user or group in your IAM Identity Center identity source. The available personas or access roles are <code>Owner</code> and <code>Viewer</code>. For more information on these personas, see <a href="https://docs.aws.amazon.com/kendra/latest/dg/deploying-search-experience-no-code.html#access-search-experience">Providing access to your search page</a>.</p>"""
    created_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the summary information was created.</p>"""
    updated_at: NotRequired["capo_kendra.types.timestamp.Timestamp"]
    """<p>The Unix timestamp when the summary information was last updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PersonasSummary) -> dict:
    out: dict = {}
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    if "persona" in value:
        import capo_kendra.types.persona

        out["Persona"] = capo_kendra.types.persona.serialize_aws_json_1_1(
            value["persona"]
        )
    if "created_at" in value:
        import capo_kendra.types.timestamp

        out["CreatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_kendra.types.timestamp

        out["UpdatedAt"] = capo_kendra.types.timestamp.serialize_aws_json_1_1(
            value["updated_at"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PersonasSummary:
    out: PersonasSummary = {}  # type: ignore[typeddict-item]
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    if data.get("Persona") is not None:
        import capo_kendra.types.persona

        out["persona"] = capo_kendra.types.persona.deserialize_aws_json_1_1(
            data["Persona"]
        )
    if data.get("CreatedAt") is not None:
        import capo_kendra.types.timestamp

        out["created_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["CreatedAt"]
        )
    if data.get("UpdatedAt") is not None:
        import capo_kendra.types.timestamp

        out["updated_at"] = capo_kendra.types.timestamp.deserialize_aws_json_1_1(
            data["UpdatedAt"]
        )
    return out
