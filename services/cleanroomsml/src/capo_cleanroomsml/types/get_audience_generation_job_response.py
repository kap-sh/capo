"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetAudienceGenerationJobResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.audience_generation_job_data_source
    import capo_cleanroomsml.types.audience_generation_job_status
    import capo_cleanroomsml.types.audience_quality_metrics
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.status_details
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.uuid


class GetAudienceGenerationJobResponse(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the audience generation job was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the audience generation job was updated.</p>"""
    audience_generation_job_arn: (
        "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    )
    """<p>The Amazon Resource Name (ARN) of the audience generation job.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the audience generation job.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the audience generation job.</p>"""
    status: "capo_cleanroomsml.types.audience_generation_job_status.AudienceGenerationJobStatus"
    """<p>The status of the audience generation job.</p>"""
    status_details: NotRequired["capo_cleanroomsml.types.status_details.StatusDetails"]
    """<p>Details about the status of the audience generation job.</p>"""
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model used for this audience generation job.</p>"""
    seed_audience: NotRequired[
        "capo_cleanroomsml.types.audience_generation_job_data_source.AudienceGenerationJobDataSource"
    ]
    """<p>The seed audience that was used for this audience generation job. This field will be null if the account calling the API is the account that started this audience generation job. </p>"""
    include_seed_in_output: NotRequired["bool"]
    """<p>Configure whether the seed users are included in the output audience. By default, Clean Rooms ML removes seed users from the output audience. If you specify <code>TRUE</code>, the seed users will appear first in the output. Clean Rooms ML does not explicitly reveal whether a user was in the seed, but the recipient of the audience will know that the first <code>minimumSeedSize</code> count of users are from the seed.</p>"""
    collaboration_id: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The identifier of the collaboration that this audience generation job is associated with.</p>"""
    metrics: NotRequired[
        "capo_cleanroomsml.types.audience_quality_metrics.AudienceQualityMetrics"
    ]
    """<p>The relevance scores for different audience sizes and the recall score of the generated audience. </p>"""
    started_by: NotRequired["capo_cleanroomsml.types.account_id.AccountId"]
    """<p>The AWS account that started this audience generation job.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The tags that are associated to this audience generation job.</p>"""
    protected_query_identifier: NotRequired["str"]
    """<p>The unique identifier of the protected query for this audience generation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAudienceGenerationJobResponse) -> dict:
    out: dict = {}
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    out["audienceGenerationJobArn"] = value["audience_generation_job_arn"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanroomsml.types.audience_generation_job_status

    out["status"] = (
        capo_cleanroomsml.types.audience_generation_job_status.serialize_json(
            value["status"]
        )
    )
    if "status_details" in value:
        import capo_cleanroomsml.types.status_details

        out["statusDetails"] = capo_cleanroomsml.types.status_details.serialize_json(
            value["status_details"]
        )
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    if "seed_audience" in value:
        import capo_cleanroomsml.types.audience_generation_job_data_source

        out["seedAudience"] = (
            capo_cleanroomsml.types.audience_generation_job_data_source.serialize_json(
                value["seed_audience"]
            )
        )
    if "include_seed_in_output" in value:
        out["includeSeedInOutput"] = value["include_seed_in_output"]
    if "collaboration_id" in value:
        out["collaborationId"] = value["collaboration_id"]
    if "metrics" in value:
        import capo_cleanroomsml.types.audience_quality_metrics

        out["metrics"] = (
            capo_cleanroomsml.types.audience_quality_metrics.serialize_json(
                value["metrics"]
            )
        )
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "protected_query_identifier" in value:
        out["protectedQueryIdentifier"] = value["protected_query_identifier"]
    return out


def deserialize_json(data: dict) -> GetAudienceGenerationJobResponse:
    out: GetAudienceGenerationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("createTime") is not None:
        import datetime

        out["create_time"] = datetime.datetime.fromisoformat(
            data["createTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["create_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updateTime") is not None:
        import datetime

        out["update_time"] = datetime.datetime.fromisoformat(
            data["updateTime"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["update_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("audienceGenerationJobArn") is not None:
        out["audience_generation_job_arn"] = data["audienceGenerationJobArn"]
    else:
        out["audience_generation_job_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_cleanroomsml.types.audience_generation_job_status

        out["status"] = (
            capo_cleanroomsml.types.audience_generation_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanroomsml.types.audience_generation_job_status.AudienceGenerationJobStatus",
            "",
        )
    if data.get("statusDetails") is not None:
        import capo_cleanroomsml.types.status_details

        out["status_details"] = capo_cleanroomsml.types.status_details.deserialize_json(
            data["statusDetails"]
        )
    if data.get("configuredAudienceModelArn") is not None:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        out["configured_audience_model_arn"] = ""
    if data.get("seedAudience") is not None:
        import capo_cleanroomsml.types.audience_generation_job_data_source

        out["seed_audience"] = (
            capo_cleanroomsml.types.audience_generation_job_data_source.deserialize_json(
                data["seedAudience"]
            )
        )
    if data.get("includeSeedInOutput") is not None:
        out["include_seed_in_output"] = data["includeSeedInOutput"]
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    if data.get("metrics") is not None:
        import capo_cleanroomsml.types.audience_quality_metrics

        out["metrics"] = (
            capo_cleanroomsml.types.audience_quality_metrics.deserialize_json(
                data["metrics"]
            )
        )
    if data.get("startedBy") is not None:
        out["started_by"] = data["startedBy"]
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if data.get("protectedQueryIdentifier") is not None:
        out["protected_query_identifier"] = data["protectedQueryIdentifier"]
    return out


def redact_sensitive(value: GetAudienceGenerationJobResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "seed_audience" in value:
        import capo_cleanroomsml.types.audience_generation_job_data_source

        out["seed_audience"] = (
            capo_cleanroomsml.types.audience_generation_job_data_source.redact_sensitive(
                value["seed_audience"]
            )
        )
    return out
