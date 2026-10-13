"""Generated from Smithy shape ``com.amazonaws.iotwireless#UpdatePartnerAccountRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_iot_wireless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_wireless.types.partner_account_id
    import capo_iot_wireless.types.partner_type
    import capo_iot_wireless.types.sidewalk_update_account


class UpdatePartnerAccountRequest(TypedDict, closed=True):
    sidewalk: "capo_iot_wireless.types.sidewalk_update_account.SidewalkUpdateAccount"
    """<p>The Sidewalk account credentials.</p>"""
    partner_account_id: "capo_iot_wireless.types.partner_account_id.PartnerAccountId"
    """<p>The ID of the partner account to update.</p>"""
    partner_type: "capo_iot_wireless.types.partner_type.PartnerType"
    """<p>The partner type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePartnerAccountRequest) -> dict:
    out: dict = {}
    import capo_iot_wireless.types.sidewalk_update_account

    out["Sidewalk"] = capo_iot_wireless.types.sidewalk_update_account.serialize_json(
        value["sidewalk"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePartnerAccountRequest:
    out: UpdatePartnerAccountRequest = {}  # type: ignore[typeddict-item]
    if data.get("Sidewalk") is not None:
        import capo_iot_wireless.types.sidewalk_update_account

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_update_account.deserialize_json(
                data["Sidewalk"]
            )
        )
    else:
        raise DeserializationError("UpdatePartnerAccountRequest.sidewalk required")
    return out


def redact_sensitive(value: UpdatePartnerAccountRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_update_account

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_update_account.redact_sensitive(
                value["sidewalk"]
            )
        )
    return out
