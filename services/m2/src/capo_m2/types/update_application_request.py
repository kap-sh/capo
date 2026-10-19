"""Generated from Smithy shape ``com.amazonaws.m2#UpdateApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.definition
    import capo_m2.types.entity_description
    import capo_m2.types.identifier
    import capo_m2.types.version


class UpdateApplicationRequest(TypedDict, closed=True):
    application_id: "capo_m2.types.identifier.Identifier"
    """<p>The unique identifier of the application you want to update.</p>"""
    description: NotRequired["capo_m2.types.entity_description.EntityDescription"]
    """<p>The description of the application to update.</p>"""
    current_application_version: "capo_m2.types.version.Version"
    """<p>The current version of the application to update.</p>"""
    definition: NotRequired["capo_m2.types.definition.Definition"]
    """<p>The application definition for this application. You can specify either inline JSON or an S3 bucket location.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApplicationRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    out["currentApplicationVersion"] = value["current_application_version"]
    if "definition" in value:
        import capo_m2.types.definition

        out["definition"] = capo_m2.types.definition.serialize_json(value["definition"])
    return out


def deserialize_json(data: dict) -> UpdateApplicationRequest:
    out: UpdateApplicationRequest = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("currentApplicationVersion") is not None:
        out["current_application_version"] = data["currentApplicationVersion"]
    else:
        out["current_application_version"] = 0
    if data.get("definition") is not None:
        import capo_m2.types.definition

        out["definition"] = capo_m2.types.definition.deserialize_json(
            data["definition"]
        )
    return out
