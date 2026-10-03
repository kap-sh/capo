"""Generated from Smithy shape ``com.amazonaws.pinpoint#WriteCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__boolean
    import capo_pinpoint.types.__integer
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.campaign_hook
    import capo_pinpoint.types.campaign_limits
    import capo_pinpoint.types.custom_delivery_configuration
    import capo_pinpoint.types.list_of_write_treatment_resource
    import capo_pinpoint.types.map_of__string
    import capo_pinpoint.types.message_configuration
    import capo_pinpoint.types.schedule
    import capo_pinpoint.types.template_configuration


class WriteCampaignRequest(TypedDict, closed=True):
    additional_treatments: NotRequired[
        "capo_pinpoint.types.list_of_write_treatment_resource.ListOfWriteTreatmentResource"
    ]
    """<p>An array of requests that defines additional treatments for the campaign, in addition to the default treatment for the campaign.</p>"""
    custom_delivery_configuration: NotRequired[
        "capo_pinpoint.types.custom_delivery_configuration.CustomDeliveryConfiguration"
    ]
    """<p>The delivery configuration settings for sending the campaign through a custom channel. This object is required if the MessageConfiguration object for the campaign specifies a CustomMessage object.</p>"""
    description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A custom description of the campaign.</p>"""
    holdout_percent: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The allocated percentage of users (segment members) who shouldn't receive messages from the campaign.</p>"""
    hook: NotRequired["capo_pinpoint.types.campaign_hook.CampaignHook"]
    """<p>The settings for the AWS Lambda function to invoke as a code hook for the campaign. You can use this hook to customize the segment that's used by the campaign.</p>"""
    is_paused: NotRequired["capo_pinpoint.types.__boolean.__boolean"]
    """<p>Specifies whether to pause the campaign. A paused campaign doesn't run unless you resume it by changing this value to false.</p>"""
    limits: NotRequired["capo_pinpoint.types.campaign_limits.CampaignLimits"]
    """<p>The messaging limits for the campaign.</p>"""
    message_configuration: NotRequired[
        "capo_pinpoint.types.message_configuration.MessageConfiguration"
    ]
    """<p>The message configuration settings for the campaign.</p>"""
    name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A custom name for the campaign.</p>"""
    schedule: NotRequired["capo_pinpoint.types.schedule.Schedule"]
    """<p>The schedule settings for the campaign.</p>"""
    segment_id: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the segment to associate with the campaign.</p>"""
    segment_version: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>The version of the segment to associate with the campaign.</p>"""
    tags: NotRequired["capo_pinpoint.types.map_of__string.MapOf__string"]
    """<note><p>As of <b>22-05-2023</b> tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either <a href="https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html">Tags</a> in the <i>API Reference for Amazon Pinpoint</i>, <a href="https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html">resourcegroupstaggingapi</a> commands in the <i>AWS Command Line Interface Documentation</i> or <a href="https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html">resourcegroupstaggingapi</a> in the <i>AWS SDK</i>.</p></note> <p>(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the campaign. Each tag consists of a required tag key and an associated tag value.</p>"""
    template_configuration: NotRequired[
        "capo_pinpoint.types.template_configuration.TemplateConfiguration"
    ]
    """<p>The message template to use for the campaign.</p>"""
    treatment_description: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A custom description of the default treatment for the campaign.</p>"""
    treatment_name: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>A custom name of the default treatment for the campaign, if the campaign has multiple treatments. A <i>treatment</i> is a variation of a campaign that's used for A/B testing.</p>"""
    priority: NotRequired["capo_pinpoint.types.__integer.__integer"]
    """<p>Defines the priority of the campaign, used to decide the order of messages displayed to user if there are multiple messages scheduled to be displayed at the same moment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WriteCampaignRequest) -> dict:
    out: dict = {}
    if "additional_treatments" in value:
        import capo_pinpoint.types.list_of_write_treatment_resource

        out["AdditionalTreatments"] = (
            capo_pinpoint.types.list_of_write_treatment_resource.serialize_json(
                value["additional_treatments"]
            )
        )
    if "custom_delivery_configuration" in value:
        import capo_pinpoint.types.custom_delivery_configuration

        out["CustomDeliveryConfiguration"] = (
            capo_pinpoint.types.custom_delivery_configuration.serialize_json(
                value["custom_delivery_configuration"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "holdout_percent" in value:
        out["HoldoutPercent"] = value["holdout_percent"]
    if "hook" in value:
        import capo_pinpoint.types.campaign_hook

        out["Hook"] = capo_pinpoint.types.campaign_hook.serialize_json(value["hook"])
    if "is_paused" in value:
        out["IsPaused"] = value["is_paused"]
    if "limits" in value:
        import capo_pinpoint.types.campaign_limits

        out["Limits"] = capo_pinpoint.types.campaign_limits.serialize_json(
            value["limits"]
        )
    if "message_configuration" in value:
        import capo_pinpoint.types.message_configuration

        out["MessageConfiguration"] = (
            capo_pinpoint.types.message_configuration.serialize_json(
                value["message_configuration"]
            )
        )
    if "name" in value:
        out["Name"] = value["name"]
    if "schedule" in value:
        import capo_pinpoint.types.schedule

        out["Schedule"] = capo_pinpoint.types.schedule.serialize_json(value["schedule"])
    if "segment_id" in value:
        out["SegmentId"] = value["segment_id"]
    if "segment_version" in value:
        out["SegmentVersion"] = value["segment_version"]
    if "tags" in value:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.serialize_json(value["tags"])
    if "template_configuration" in value:
        import capo_pinpoint.types.template_configuration

        out["TemplateConfiguration"] = (
            capo_pinpoint.types.template_configuration.serialize_json(
                value["template_configuration"]
            )
        )
    if "treatment_description" in value:
        out["TreatmentDescription"] = value["treatment_description"]
    if "treatment_name" in value:
        out["TreatmentName"] = value["treatment_name"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_json(data: dict) -> WriteCampaignRequest:
    out: WriteCampaignRequest = {}  # type: ignore[typeddict-item]
    if data.get("AdditionalTreatments") is not None:
        import capo_pinpoint.types.list_of_write_treatment_resource

        out["additional_treatments"] = (
            capo_pinpoint.types.list_of_write_treatment_resource.deserialize_json(
                data["AdditionalTreatments"]
            )
        )
    if data.get("CustomDeliveryConfiguration") is not None:
        import capo_pinpoint.types.custom_delivery_configuration

        out["custom_delivery_configuration"] = (
            capo_pinpoint.types.custom_delivery_configuration.deserialize_json(
                data["CustomDeliveryConfiguration"]
            )
        )
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("HoldoutPercent") is not None:
        out["holdout_percent"] = data["HoldoutPercent"]
    if data.get("Hook") is not None:
        import capo_pinpoint.types.campaign_hook

        out["hook"] = capo_pinpoint.types.campaign_hook.deserialize_json(data["Hook"])
    if data.get("IsPaused") is not None:
        out["is_paused"] = data["IsPaused"]
    if data.get("Limits") is not None:
        import capo_pinpoint.types.campaign_limits

        out["limits"] = capo_pinpoint.types.campaign_limits.deserialize_json(
            data["Limits"]
        )
    if data.get("MessageConfiguration") is not None:
        import capo_pinpoint.types.message_configuration

        out["message_configuration"] = (
            capo_pinpoint.types.message_configuration.deserialize_json(
                data["MessageConfiguration"]
            )
        )
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Schedule") is not None:
        import capo_pinpoint.types.schedule

        out["schedule"] = capo_pinpoint.types.schedule.deserialize_json(
            data["Schedule"]
        )
    if data.get("SegmentId") is not None:
        out["segment_id"] = data["SegmentId"]
    if data.get("SegmentVersion") is not None:
        out["segment_version"] = data["SegmentVersion"]
    if data.get("tags") is not None:
        import capo_pinpoint.types.map_of__string

        out["tags"] = capo_pinpoint.types.map_of__string.deserialize_json(data["tags"])
    if data.get("TemplateConfiguration") is not None:
        import capo_pinpoint.types.template_configuration

        out["template_configuration"] = (
            capo_pinpoint.types.template_configuration.deserialize_json(
                data["TemplateConfiguration"]
            )
        )
    if data.get("TreatmentDescription") is not None:
        out["treatment_description"] = data["TreatmentDescription"]
    if data.get("TreatmentName") is not None:
        out["treatment_name"] = data["TreatmentName"]
    if data.get("Priority") is not None:
        out["priority"] = data["Priority"]
    return out
