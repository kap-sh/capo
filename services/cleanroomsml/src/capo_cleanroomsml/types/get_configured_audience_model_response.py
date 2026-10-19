"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetConfiguredAudienceModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.audience_model_arn
    import capo_cleanroomsml.types.audience_size_config
    import capo_cleanroomsml.types.configured_audience_model_arn
    import capo_cleanroomsml.types.configured_audience_model_output_config
    import capo_cleanroomsml.types.configured_audience_model_status
    import capo_cleanroomsml.types.metrics_list
    import capo_cleanroomsml.types.min_matching_seed_size
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.tag_on_create_policy


class GetConfiguredAudienceModelResponse(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the configured audience model was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured audience model was updated.</p>"""
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured audience model.</p>"""
    audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model used for this configured audience model.</p>"""
    output_config: "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig"
    """<p>The output configuration of the configured audience model</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model.</p>"""
    status: "capo_cleanroomsml.types.configured_audience_model_status.ConfiguredAudienceModelStatus"
    """<p>The status of the configured audience model.</p>"""
    shared_audience_metrics: "capo_cleanroomsml.types.metrics_list.MetricsList"
    """<p>Whether audience metrics are shared.</p>"""
    min_matching_seed_size: NotRequired[
        "capo_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
    ]
    """<p>The minimum number of users from the seed audience that must match with users in the training data of the audience model.</p>"""
    audience_size_config: NotRequired[
        "capo_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
    ]
    """<p>The list of output sizes of audiences that can be created using this configured audience model. A request to <a>StartAudienceGenerationJob</a> that uses this configured audience model must have an <code>audienceSize</code> selected from this list. You can use the <code>ABSOLUTE</code> <a>AudienceSize</a> to configure out audience sizes using the count of identifiers in the output. You can use the <code>Percentage</code> <a>AudienceSize</a> to configure sizes in the range 1-100 percent.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The tags that are associated to this configured audience model.</p>"""
    child_resource_tag_on_create_policy: NotRequired[
        "capo_cleanroomsml.types.tag_on_create_policy.TagOnCreatePolicy"
    ]
    """<p>Provides the <code>childResourceTagOnCreatePolicy</code> that was used for this configured audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredAudienceModelResponse) -> dict:
    out: dict = {}
    import capo_cleanroomsml._protocol.serialize

    out["createTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["create_time"]
    )
    import capo_cleanroomsml._protocol.serialize

    out["updateTime"] = capo_cleanroomsml._protocol.serialize.fmt_date_time(
        value["update_time"]
    )
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    out["name"] = value["name"]
    out["audienceModelArn"] = value["audience_model_arn"]
    import capo_cleanroomsml.types.configured_audience_model_output_config

    out["outputConfig"] = (
        capo_cleanroomsml.types.configured_audience_model_output_config.serialize_json(
            value["output_config"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanroomsml.types.configured_audience_model_status

    out["status"] = (
        capo_cleanroomsml.types.configured_audience_model_status.serialize_json(
            value["status"]
        )
    )
    import capo_cleanroomsml.types.metrics_list

    out["sharedAudienceMetrics"] = capo_cleanroomsml.types.metrics_list.serialize_json(
        value["shared_audience_metrics"]
    )
    if "min_matching_seed_size" in value:
        out["minMatchingSeedSize"] = value["min_matching_seed_size"]
    if "audience_size_config" in value:
        import capo_cleanroomsml.types.audience_size_config

        out["audienceSizeConfig"] = (
            capo_cleanroomsml.types.audience_size_config.serialize_json(
                value["audience_size_config"]
            )
        )
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "child_resource_tag_on_create_policy" in value:
        import capo_cleanroomsml.types.tag_on_create_policy

        out["childResourceTagOnCreatePolicy"] = (
            capo_cleanroomsml.types.tag_on_create_policy.serialize_json(
                value["child_resource_tag_on_create_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfiguredAudienceModelResponse:
    out: GetConfiguredAudienceModelResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("configuredAudienceModelArn") is not None:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        out["configured_audience_model_arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("audienceModelArn") is not None:
        out["audience_model_arn"] = data["audienceModelArn"]
    else:
        out["audience_model_arn"] = ""
    if data.get("outputConfig") is not None:
        import capo_cleanroomsml.types.configured_audience_model_output_config

        out["output_config"] = (
            capo_cleanroomsml.types.configured_audience_model_output_config.deserialize_json(
                data["outputConfig"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredAudienceModelResponse.output_config required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("status") is not None:
        import capo_cleanroomsml.types.configured_audience_model_status

        out["status"] = (
            capo_cleanroomsml.types.configured_audience_model_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_cleanroomsml.types.configured_audience_model_status.ConfiguredAudienceModelStatus",
            "",
        )
    if data.get("sharedAudienceMetrics") is not None:
        import capo_cleanroomsml.types.metrics_list

        out["shared_audience_metrics"] = (
            capo_cleanroomsml.types.metrics_list.deserialize_json(
                data["sharedAudienceMetrics"]
            )
        )
    else:
        out["shared_audience_metrics"] = []
    if data.get("minMatchingSeedSize") is not None:
        out["min_matching_seed_size"] = data["minMatchingSeedSize"]
    if data.get("audienceSizeConfig") is not None:
        import capo_cleanroomsml.types.audience_size_config

        out["audience_size_config"] = (
            capo_cleanroomsml.types.audience_size_config.deserialize_json(
                data["audienceSizeConfig"]
            )
        )
    if data.get("tags") is not None:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if data.get("childResourceTagOnCreatePolicy") is not None:
        import capo_cleanroomsml.types.tag_on_create_policy

        out["child_resource_tag_on_create_policy"] = (
            capo_cleanroomsml.types.tag_on_create_policy.deserialize_json(
                data["childResourceTagOnCreatePolicy"]
            )
        )
    return out
