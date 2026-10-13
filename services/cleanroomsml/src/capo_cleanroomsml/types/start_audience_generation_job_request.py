"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StartAudienceGenerationJobRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_generation_job_data_source
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.uuid


class StartAudienceGenerationJobRequest(TypedDict, closed=True):
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience generation job.</p>"""
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that is used for this audience generation job.</p>"""
    seed_audience: "capo_cleanroomsml.types.audience_generation_job_data_source.AudienceGenerationJobDataSource"
    """<p>The seed audience that is used to generate the audience.</p>"""
    include_seed_in_output: "bool"
    """<p>Whether the seed audience is included in the audience generation output.</p>"""
    collaboration_id: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The identifier of the collaboration that contains the audience generation job.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience generation job.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAudienceGenerationJobRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    import capo_cleanroomsml.types.audience_generation_job_data_source

    out["seedAudience"] = (
        capo_cleanroomsml.types.audience_generation_job_data_source.serialize_json(
            value["seed_audience"]
        )
    )
    out["includeSeedInOutput"] = value.get("include_seed_in_output", False)
    if "collaboration_id" in value:
        out["collaborationId"] = value["collaboration_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> StartAudienceGenerationJobRequest:
    out: StartAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("StartAudienceGenerationJobRequest.name required")
    if data.get("configuredAudienceModelArn") is not None:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "StartAudienceGenerationJobRequest.configured_audience_model_arn required"
        )
    if data.get("seedAudience") is not None:
        import capo_cleanroomsml.types.audience_generation_job_data_source

        out["seed_audience"] = (
            capo_cleanroomsml.types.audience_generation_job_data_source.deserialize_json(
                data["seedAudience"]
            )
        )
    else:
        raise DeserializationError(
            "StartAudienceGenerationJobRequest.seed_audience required"
        )
    if data.get("includeSeedInOutput") is not None:
        out["include_seed_in_output"] = data["includeSeedInOutput"]
    else:
        out["include_seed_in_output"] = False
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: StartAudienceGenerationJobRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "seed_audience" in value:
        import capo_cleanroomsml.types.audience_generation_job_data_source

        out["seed_audience"] = (
            capo_cleanroomsml.types.audience_generation_job_data_source.redact_sensitive(
                value["seed_audience"]
            )
        )
    return out
