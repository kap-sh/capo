"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#ConflictException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_marketing.errors import ServiceError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.conflict_reason
    import capo_partnercentral_marketing.types.error_message


class ConflictException_(TypedDict, closed=True):
    message: "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    """Error message."""
    resource_id: NotRequired["str"]
    """The affected resource identifier. For a uniqueness conflict this is the identifier of the *existing* resource, so the caller can act on it without a separate lookup."""
    resource_type: NotRequired["str"]
    """The affected resource type."""
    reason: NotRequired[
        "capo_partnercentral_marketing.types.conflict_reason.ConflictReason"
    ]
    """Machine-readable cause, for clients that branch on it. An open set of `SCREAMING_SNAKE_CASE` tokens, deliberately typed as a string rather than an enum. `ConflictException` is shared by every resource in this service, so an enum here would accumulate values that are meaningful for one resource and inapplicable to the rest — the cohesiveness problem the Backward Compatibility standard describes under "Sharing enums" — and each new value would force an SDK regeneration on callers who can never encounter it. Clients MUST treat an unrecognised value as an unspecified conflict and fall back to `Message`. Values in use today: From the campaign asset activation path. Every one of these is decided before the operation returns, so a caller that receives one knows nothing was started. These two are thrown by `DeactivateCampaignAsset`, which refuses one asset outright. `StartCampaignAssetActivationTask` reports the same two causes **per asset** as a FAILED task entry instead of throwing, because one bad identifier must not refuse the twenty-four good ones beside it — so the spellings are deliberately identical to `CampaignAssetStateReason`'s, letting a client match one string whichever way the refusal arrived. The two types evolve independently on purpose: this is an open string shared by every resource, that is a closed enum owned by one operation. - `ASSET_START_IN_PROGRESS` — the asset is already being started, or another caller changed it during this request. Retryable once the outcome is visible. - `PREREQUISITE_ASSET_NOT_ACTIVE` — this asset embeds output from another asset that is not live. `ResourceId` carries that asset's identifier. From the prerequisite edges between a campaign's assets — an email that embeds its landing page's URL. Both refuse the whole request and write nothing. - `PREREQUISITE_ASSET_MISSING` — from `BatchCreateCampaignAsset`: an entry's blueprint embeds another blueprint's output, and that blueprint is neither named in the same request nor already an asset on the campaign. Retry with it in the request. `ResourceId` carries the missing blueprint's identifier. - `ASSET_HAS_DEPENDENTS` — from `DeleteCampaignAsset`: another asset on the campaign embeds this asset's output, so deleting it would leave that asset unactivatable. Delete the dependents first. The message names them. `CAMPAIGN_COMPLETED` — the campaign is complete (the UTC date is after its `EndOn`), so it and its assets are read-only. Refuses `UpdateCampaign`, `BatchCreateCampaignAsset`, `UpdateCampaignAsset`, `DeleteCampaignAsset` and `StartCampaignAssetActivationTask`; never `DeactivateCampaignAsset`. **Not retryable, and not fixable** — `EndOn` cannot be moved once it has passed, so nothing the caller does will make the write succeed. `ResourceId` carries the campaign identifier. ⚠️ This is the one conflict reason whose condition **never clears**, which sits awkwardly with `ConflictException` promising a state that may change. It is a conflict rather than a validation failure because the request is well formed and would have succeeded a moment earlier — the resource's state is what refuses it, which is what this exception is for. Contrast `ASSET_NOT_STARTABLE`, which moved to `ValidationException` precisely because it is a property of the asset's *type* rather than of its state. ⚠️ **`COMPLETED` also exists as a `CampaignAssetExportTaskStatus` value, on a different axis.** That one means an export archive finished assembling. The two are unrelated and must not be unified. `CAMPAIGN_HAS_ACTIVE_ASSETS` — from `DeleteCampaign`: at least one of the campaign's assets is live, and deleting the campaign would orphan what the delivery platform still serves or sends. Deactivate those assets with `DeactivateCampaignAsset`, then retry. The message names them. `ResourceId` carries the campaign identifier. `CAMPAIGN_ACTIVATION_IN_PROGRESS` — from `StartCampaignAssetActivationTask` and `DeleteCampaign`, refusing the whole request: one activation task runs on a campaign at a time. `ResourceId` carries the **holding task's id**, so a caller can poll `GetCampaignAssetActivationTask` rather than guess. Retryable once that task reaches a terminal status. `SERVICE_LINKED_ROLE_DELETION_IN_PROGRESS` — from `StartCampaignAssetActivationTask`, refusing the whole request: this service's service-linked role is being deleted, so no asset may go live. Not a lease conflict: `ResourceId` is unset and there is no task to poll. Retryable after a short wait; if the role was deleted, the next activation recreates it. `LAYOUT_LOCKED_AFTER_ACTIVATION` — from `UpdateCampaignAsset`, refusing a `Layout` change on a multi-layout asset that has activated successfully at least once (DG-044). The published object is that layout's, so switching would leave the asset describing a layout that is not the one live. **Not fixable**: the asset keeps its layout for life. A failed activation does not lock it. Re-sending the layout already selected is not a change and is accepted. `ResourceId` carries the asset identifier. `ASSET_START_IN_PROGRESS` — also from `UpdateCampaignAsset`, refusing any edit to an asset the campaign's running activation task has accepted and not yet finished: the run publishes the content it read, so an edit accepted mid-run would either be published unvalidated or never published. Nothing is written. Retryable once the asset's outcome on the task (`GetCampaignAssetActivationTask`) is terminal; the asset's siblings may still be running. `ResourceId` carries the asset identifier. `ASSET_ALREADY_ACTIVE` — from `UpdateCampaignAsset`, refusing any change to a live email or social post, content or schedule. Deactivate it first; the next activation sends everything current. Landing pages and documents are edited live and converge by re-activation. `ResourceId` carries the asset identifier. `ASSET_NOT_DEACTIVATABLE` — from `DeactivateCampaignAsset`, for an asset that can't be stopped: a document, banner or landing page until the campaign has completed, when it becomes removable. Until then, update it and activate it again. `ResourceId` carries the asset identifier. `ASSET_HAS_LOCKED_SENDS` — from `DeactivateCampaignAsset`, within an hour of the asset's send (a social post's publish), when it can no longer be withdrawn. `ASSET_ALREADY_DELIVERED` — the same, once that time has passed: a sent email or a published post cannot be recalled. Neither is retryable. Three values were removed with the campaign lifecycle and the singular activate, and none should be re-added here: - `CAMPAIGN_NOT_STARTED` — a campaign has no state to be started out of. - `ASSET_NOT_STARTABLE` — moved to `ValidationException`, with no reason. The value's own documentation said it was "not retryable and not fixable: it is a property of the asset's type", and `ConflictException` promises a state that may change. The gate itself stays — deleting it lets a download-only asset into a task with no dispatch arm, which would succeed and do nothing. - `ASSET_START_UNCONFIRMED` — described a state that no longer occurs. DG cannot be more idempotent than a platform whose social create has no idempotency key, so an ambiguous hand-over is now an ordinary failure carrying `INTERNAL_ERROR`. Holding the asset in a distinct state bought a guarantee that was never real, and had no exit."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ConflictException_) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_cbor(data: dict) -> ConflictException_:
    out: ConflictException_ = {}  # type: ignore[typeddict-item]
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    return out


class ConflictException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.partnercentralmarketing#ConflictException``."""

    code: str | None = "ConflictException"

    def __init__(
        self,
        data: ConflictException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ConflictException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_cbor(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ConflictException":
        return cls(deserialize_cbor(data), message, response=response)
