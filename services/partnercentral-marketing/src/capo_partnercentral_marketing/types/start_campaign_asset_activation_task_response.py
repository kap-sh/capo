"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#StartCampaignAssetActivationTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_activation_outcomes
    import capo_partnercentral_marketing.types.campaign_asset_activation_task_id
    import capo_partnercentral_marketing.types.campaign_asset_activation_task_status
    import capo_partnercentral_marketing.types.campaign_id
    import capo_partnercentral_marketing.types.timestamp


class StartCampaignAssetActivationTaskResponse(TypedDict, closed=True):
    campaign_id: "capo_partnercentral_marketing.types.campaign_id.CampaignId"
    """The campaign's id. Canonical: because `CampaignIdentifier` accepts an id or an ARN, echoing this tells a caller who passed an ARN what the id is. The task's own id is `TaskId`."""
    task_id: "capo_partnercentral_marketing.types.campaign_asset_activation_task_id.CampaignAssetActivationTaskId"
    """Opaque correlation value for the task. Echoed so a caller can tell the task it started from a later one that superseded it. Never an input: the campaign is what addresses a task, because a campaign has at most one."""
    task_status: "capo_partnercentral_marketing.types.campaign_asset_activation_task_status.CampaignAssetActivationTaskStatus"
    """The task's status over every asset it names, refused ones included: one refused and one succeeded is PARTIAL_FAILURE."""
    started_at: "capo_partnercentral_marketing.types.timestamp.Timestamp"
    """When the task was created."""
    ended_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """When the task reached a terminal status. Absent while IN_PROGRESS."""
    assets: "capo_partnercentral_marketing.types.campaign_asset_activation_outcomes.CampaignAssetActivationOutcomes"
    """One entry per asset the request named, in the order named. An asset refused up front is FAILED from the first response, with its reason."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartCampaignAssetActivationTaskResponse) -> dict:
    out: dict = {}
    out["CampaignId"] = value["campaign_id"]
    out["TaskId"] = value["task_id"]
    import capo_partnercentral_marketing.types.campaign_asset_activation_task_status

    out["TaskStatus"] = (
        capo_partnercentral_marketing.types.campaign_asset_activation_task_status.serialize_cbor(
            value["task_status"]
        )
    )
    import capo_partnercentral_marketing.types.timestamp

    out["StartedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
        value["started_at"]
    )
    if "ended_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["EndedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["ended_at"]
        )
    import capo_partnercentral_marketing.types.campaign_asset_activation_outcomes

    out["Assets"] = (
        capo_partnercentral_marketing.types.campaign_asset_activation_outcomes.serialize_cbor(
            value["assets"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> StartCampaignAssetActivationTaskResponse:
    out: StartCampaignAssetActivationTaskResponse = {}  # type: ignore[typeddict-item]
    if data.get("CampaignId") is not None:
        out["campaign_id"] = data["CampaignId"]
    else:
        out["campaign_id"] = ""
    if data.get("TaskId") is not None:
        out["task_id"] = data["TaskId"]
    else:
        out["task_id"] = ""
    if data.get("TaskStatus") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_activation_task_status

        out["task_status"] = (
            capo_partnercentral_marketing.types.campaign_asset_activation_task_status.deserialize_cbor(
                data["TaskStatus"]
            )
        )
    else:
        import typing

        out["task_status"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_activation_task_status.CampaignAssetActivationTaskStatus",
            "",
        )
    if data.get("StartedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["started_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["StartedAt"]
            )
        )
    else:
        import datetime

        out["started_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["ended_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["EndedAt"]
            )
        )
    if data.get("Assets") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_activation_outcomes

        out["assets"] = (
            capo_partnercentral_marketing.types.campaign_asset_activation_outcomes.deserialize_cbor(
                data["Assets"]
            )
        )
    else:
        out["assets"] = []
    return out
