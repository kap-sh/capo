"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#UpdateCampaignAssetRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.client_token
    import capo_partnercentral_marketing.types.field_value_input_list
    import capo_partnercentral_marketing.types.layout_option_value
    import capo_partnercentral_marketing.types.send_mode
    import capo_partnercentral_marketing.types.timestamp


class UpdateCampaignAssetRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The campaign identifier."""
    campaign_asset_identifier: (
        "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    )
    """The asset identifier."""
    field_values: NotRequired[
        "capo_partnercentral_marketing.types.field_value_input_list.FieldValueInputList"
    ]
    """Value-only updates to the asset's pinned template fields, keyed by FieldId. The field schema (labels, descriptions, constraints, placeholders, image defaults) is service-owned and pinned at instantiation, so clients send only the values they are changing. Fields omitted keep their stored values; send the entry with `Value` omitted to clear one. Named `FieldValues` to match the member it edits on `CampaignAsset`, which is the same concept read back. It was `templateFieldUpdates`; the two names for one concept were the defect, not the length."""
    layout: NotRequired[
        "capo_partnercentral_marketing.types.layout_option_value.LayoutOptionValue"
    ]
    """Selects a multi-layout asset's layout: one of the values in `CampaignAsset.layout.options`. PATCH: omitted leaves the selection unchanged, and there is no way to clear it. A value that is not one of the asset's options — or any value on a single-layout asset — is a plain `ValidationException`, and nothing in the call is applied. Every pinned field stays writable whichever layout is selected."""
    send_mode: NotRequired["capo_partnercentral_marketing.types.send_mode.SendMode"]
    """When a **sendable** asset (`EMAIL`, `SOCIAL_POST`) sends: on activation, or at `ScheduledSendAt`. A mode beside a value rather than a union, on purpose: `ScheduledSendAt` stays a plain `Timestamp`, and the precedent is EventBridge Scheduler's `FlexibleTimeWindow { Mode, MaximumWindowInMinutes }`. The pair is checked as one, and a request where they disagree is refused with `ValidationException` (`INVALID_VALUE`, naming the member) and applies nothing: - `SCHEDULED` requires `ScheduledSendAt`; a reschedule resends `SCHEDULED` with the new time; - `ON_ACTIVATION` forbids `ScheduledSendAt`, and drops any time already stored; - `ScheduledSendAt` without `SendMode` is refused. PATCH: omitted leaves both unchanged. Until a mode is chosen the asset reports `SEND_MODE_MISSING` and does not activate: no default, because an unchosen send mails the real audience. Rejected with `ValidationException` (`NOT_SUPPORTED_FOR_CATEGORY`) for a category that has no send (`LANDING_PAGE`, `DOCUMENT`, `BANNER_AD`). Like every other edit, it reaches the delivery platform at the asset's next activation, and a live email or social post refuses it (`ASSET_ALREADY_ACTIVE`): deactivate first."""
    scheduled_send_at: NotRequired[
        "capo_partnercentral_marketing.types.timestamp.Timestamp"
    ]
    """The send time, with `SendMode: SCHEDULED` and only then. See `SendMode`. Must be at least an hour out (`SEND_WINDOW_TOO_SOON`), unless it is the time already stored: resending the stored mode and time changes nothing and is accepted, so a form that always resubmits does not trip the window. Must also fall on or before the campaign's `EndOn` (by the end of that UTC day): refused with `ValidationException` (`INVALID_VALUE`) otherwise, so nothing is scheduled to send after the campaign completes. Was `scheduleDate`, a `YYYY-MM-DD` string. Retyped because a date alone cannot express a send *time*, which is the whole point of a schedule — and because the resource already spelled the same concept `ScheduledSendAt` on the activation responses. Two spellings of one concept on one resource was the defect."""
    client_token: NotRequired[
        "capo_partnercentral_marketing.types.client_token.ClientToken"
    ]
    """Idempotency token. Retry-safety only — this is **not** a concurrency token, and sequential edits to one field are last-writer-wins."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateCampaignAssetRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["CampaignIdentifier"] = value["campaign_identifier"]
    out["CampaignAssetIdentifier"] = value["campaign_asset_identifier"]
    if "field_values" in value:
        import capo_partnercentral_marketing.types.field_value_input_list

        out["FieldValues"] = (
            capo_partnercentral_marketing.types.field_value_input_list.serialize_cbor(
                value["field_values"]
            )
        )
    if "layout" in value:
        out["Layout"] = value["layout"]
    if "send_mode" in value:
        import capo_partnercentral_marketing.types.send_mode

        out["SendMode"] = capo_partnercentral_marketing.types.send_mode.serialize_cbor(
            value["send_mode"]
        )
    if "scheduled_send_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["ScheduledSendAt"] = (
            capo_partnercentral_marketing.types.timestamp.serialize_cbor(
                value["scheduled_send_at"]
            )
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> UpdateCampaignAssetRequest:
    out: UpdateCampaignAssetRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_marketing.types.catalog

        out["catalog"] = capo_partnercentral_marketing.types.catalog.deserialize_cbor(
            data["Catalog"]
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_marketing.types.catalog.Catalog", ""
        )
    if data.get("CampaignIdentifier") is not None:
        out["campaign_identifier"] = data["CampaignIdentifier"]
    else:
        out["campaign_identifier"] = ""
    if data.get("CampaignAssetIdentifier") is not None:
        out["campaign_asset_identifier"] = data["CampaignAssetIdentifier"]
    else:
        out["campaign_asset_identifier"] = ""
    if data.get("FieldValues") is not None:
        import capo_partnercentral_marketing.types.field_value_input_list

        out["field_values"] = (
            capo_partnercentral_marketing.types.field_value_input_list.deserialize_cbor(
                data["FieldValues"]
            )
        )
    if data.get("Layout") is not None:
        out["layout"] = data["Layout"]
    if data.get("SendMode") is not None:
        import capo_partnercentral_marketing.types.send_mode

        out["send_mode"] = (
            capo_partnercentral_marketing.types.send_mode.deserialize_cbor(
                data["SendMode"]
            )
        )
    if data.get("ScheduledSendAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["scheduled_send_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["ScheduledSendAt"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out


def redact_sensitive(value: UpdateCampaignAssetRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "field_values" in value:
        import capo_partnercentral_marketing.types.field_value_input_list

        out["field_values"] = (
            capo_partnercentral_marketing.types.field_value_input_list.redact_sensitive(
                value["field_values"]
            )
        )
    return out
