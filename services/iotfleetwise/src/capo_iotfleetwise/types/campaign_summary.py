"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CampaignSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.campaign_arn
    import capo_iotfleetwise.types.campaign_name
    import capo_iotfleetwise.types.campaign_status
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.timestamp


class CampaignSummary(TypedDict, closed=True):
    arn: NotRequired["capo_iotfleetwise.types.campaign_arn.campaignArn"]
    """<p>The Amazon Resource Name (ARN) of a campaign.</p>"""
    name: NotRequired["capo_iotfleetwise.types.campaign_name.campaignName"]
    """<p>The name of a campaign.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>The description of the campaign.</p>"""
    signal_catalog_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the signal catalog associated with the campaign.</p>"""
    target_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of a vehicle or fleet to which the campaign is deployed.</p>"""
    status: NotRequired["capo_iotfleetwise.types.campaign_status.CampaignStatus"]
    """<p>The state of a campaign. The status can be one of the following:</p> <ul> <li> <p> <code>CREATING</code> - Amazon Web Services IoT FleetWise is processing your request to create the campaign.</p> </li> <li> <p> <code>WAITING_FOR_APPROVAL</code> - After a campaign is created, it enters the <code>WAITING_FOR_APPROVAL</code> state. To allow Amazon Web Services IoT FleetWise to deploy the campaign to the target vehicle or fleet, use the API operation to approve the campaign. </p> </li> <li> <p> <code>RUNNING</code> - The campaign is active. </p> </li> <li> <p> <code>SUSPENDED</code> - The campaign is suspended. To resume the campaign, use the API operation. </p> </li> </ul>"""
    creation_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The time the campaign was created.</p>"""
    last_modification_time: "capo_iotfleetwise.types.timestamp.timestamp"
    """<p>The last time the campaign was modified.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CampaignSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "signal_catalog_arn" in value:
        out["signalCatalogArn"] = value["signal_catalog_arn"]
    if "target_arn" in value:
        out["targetArn"] = value["target_arn"]
    if "status" in value:
        import capo_iotfleetwise.types.campaign_status

        out["status"] = capo_iotfleetwise.types.campaign_status.serialize_aws_json_1_0(
            value["status"]
        )
    import capo_iotfleetwise.types.timestamp

    out["creationTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
        value["creation_time"]
    )
    import capo_iotfleetwise.types.timestamp

    out["lastModificationTime"] = (
        capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["last_modification_time"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CampaignSummary:
    out: CampaignSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("signalCatalogArn") is not None:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    if data.get("status") is not None:
        import capo_iotfleetwise.types.campaign_status

        out["status"] = (
            capo_iotfleetwise.types.campaign_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if data.get("creationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["creation_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModificationTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["last_modification_time"] = (
            capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
                data["lastModificationTime"]
            )
        )
    else:
        import datetime

        out["last_modification_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
