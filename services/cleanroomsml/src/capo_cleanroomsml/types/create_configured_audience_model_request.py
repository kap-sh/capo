"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateConfiguredAudienceModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_model_arn
    import capo_cleanroomsml.types.audience_size_config
    import capo_cleanroomsml.types.configured_audience_model_output_config
    import capo_cleanroomsml.types.metrics_list
    import capo_cleanroomsml.types.min_matching_seed_size
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.tag_on_create_policy


class CreateConfiguredAudienceModelRequest(TypedDict, closed=True):
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured audience model.</p>"""
    audience_model_arn: "capo_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model to use for the configured audience model.</p>"""
    output_config: "capo_cleanroomsml.types.configured_audience_model_output_config.ConfiguredAudienceModelOutputConfig"
    """<p>Configure the Amazon S3 location and IAM Role for audiences created using this configured audience model. Each audience will have a unique location. The IAM Role must have <code>s3:PutObject</code> permission on the destination Amazon S3 location. If the destination is protected with Amazon S3 KMS-SSE, then the Role must also have the required KMS permissions.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured audience model.</p>"""
    shared_audience_metrics: "capo_cleanroomsml.types.metrics_list.MetricsList"
    """<p>Whether audience metrics are shared.</p>"""
    min_matching_seed_size: NotRequired[
        "capo_cleanroomsml.types.min_matching_seed_size.MinMatchingSeedSize"
    ]
    """<p>The minimum number of users from the seed audience that must match with users in the training data of the audience model. The default value is 500.</p>"""
    audience_size_config: NotRequired[
        "capo_cleanroomsml.types.audience_size_config.AudienceSizeConfig"
    ]
    """<p>Configure the list of output sizes of audiences that can be created using this configured audience model. A request to <a>StartAudienceGenerationJob</a> that uses this configured audience model must have an <code>audienceSize</code> selected from this list. You can use the <code>ABSOLUTE</code> <a>AudienceSize</a> to configure out audience sizes using the count of identifiers in the output. You can use the <code>Percentage</code> <a>AudienceSize</a> to configure sizes in the range 1-100 percent.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    child_resource_tag_on_create_policy: NotRequired[
        "capo_cleanroomsml.types.tag_on_create_policy.TagOnCreatePolicy"
    ]
    """<p>Configure how the service tags audience generation jobs created using this configured audience model. If you specify <code>NONE</code>, the tags from the <a>StartAudienceGenerationJob</a> request determine the tags of the audience generation job. If you specify <code>FROM_PARENT_RESOURCE</code>, the audience generation job inherits the tags from the configured audience model, by default. Tags in the <a>StartAudienceGenerationJob</a> will override the default.</p> <p>When the client is in a different account than the configured audience model, the tags from the client are never applied to a resource in the caller's account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredAudienceModelRequest) -> dict:
    out: dict = {}
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


def deserialize_json(data: dict) -> CreateConfiguredAudienceModelRequest:
    out: CreateConfiguredAudienceModelRequest = {}  # type: ignore[typeddict-item]
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
            "CreateConfiguredAudienceModelRequest.output_config required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
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
