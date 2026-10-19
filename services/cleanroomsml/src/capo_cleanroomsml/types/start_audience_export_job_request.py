"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StartAudienceExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.audience_size
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description


class StartAudienceExportJobRequest(TypedDict, closed=True):
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience export job.</p>"""
    audience_generation_job_arn: (
        "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    )
    """<p>The Amazon Resource Name (ARN) of the audience generation job that you want to export.</p>"""
    audience_size: "capo_cleanroomsml.types.audience_size.AudienceSize"
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAudienceExportJobRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["audienceGenerationJobArn"] = value["audience_generation_job_arn"]
    import capo_cleanroomsml.types.audience_size

    out["audienceSize"] = capo_cleanroomsml.types.audience_size.serialize_json(
        value["audience_size"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StartAudienceExportJobRequest:
    out: StartAudienceExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("audienceGenerationJobArn") is not None:
        out["audience_generation_job_arn"] = data["audienceGenerationJobArn"]
    else:
        out["audience_generation_job_arn"] = ""
    if data.get("audienceSize") is not None:
        import capo_cleanroomsml.types.audience_size

        out["audience_size"] = capo_cleanroomsml.types.audience_size.deserialize_json(
            data["audienceSize"]
        )
    else:
        raise DeserializationError(
            "StartAudienceExportJobRequest.audience_size required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
