"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceGenerationJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.account_id
    import capo_cleanroomsml.types.audience_generation_job_arn
    import capo_cleanroomsml.types.audience_generation_job_status
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.uuid


class AudienceGenerationJobSummary(TypedDict, closed=True):
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
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that was used for this audience generation job.</p>"""
    collaboration_id: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The identifier of the collaboration that contains this audience generation job.</p>"""
    started_by: NotRequired["capo_cleanroomsml.types.account_id.AccountId"]
    """<p>The AWS Account that submitted the job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudienceGenerationJobSummary) -> dict:
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
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    if "collaboration_id" in value:
        out["collaborationId"] = value["collaboration_id"]
    if "started_by" in value:
        out["startedBy"] = value["started_by"]
    return out


def deserialize_json(data: dict) -> AudienceGenerationJobSummary:
    out: AudienceGenerationJobSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("configuredAudienceModelArn") is not None:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        out["configured_audience_model_arn"] = ""
    if data.get("collaborationId") is not None:
        out["collaboration_id"] = data["collaborationId"]
    if data.get("startedBy") is not None:
        out["started_by"] = data["startedBy"]
    return out
