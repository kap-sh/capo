"""Generated from Smithy shape ``com.amazonaws.iotwireless#GetPartnerAccountResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.account_linked
    import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint


class GetPartnerAccountResponse(TypedDict, closed=True):
    sidewalk: NotRequired[
        "capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.SidewalkAccountInfoWithFingerprint"
    ]
    """<p>The Sidewalk account credentials.</p>"""
    account_linked: "capo_iot_wireless.types.account_linked.AccountLinked"
    """<p>Whether the partner account is linked to the AWS account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPartnerAccountResponse) -> dict:
    out: dict = {}
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

        out["Sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.serialize_json(
                value["sidewalk"]
            )
        )
    out["AccountLinked"] = value.get("account_linked", False)
    return out


def deserialize_json(data: dict) -> GetPartnerAccountResponse:
    out: GetPartnerAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("Sidewalk") is not None:
        import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.deserialize_json(
                data["Sidewalk"]
            )
        )
    if data.get("AccountLinked") is not None:
        out["account_linked"] = data["AccountLinked"]
    else:
        out["account_linked"] = False
    return out


def redact_sensitive(value: GetPartnerAccountResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "sidewalk" in value:
        import capo_iot_wireless.types.sidewalk_account_info_with_fingerprint

        out["sidewalk"] = (
            capo_iot_wireless.types.sidewalk_account_info_with_fingerprint.redact_sensitive(
                value["sidewalk"]
            )
        )
    return out
