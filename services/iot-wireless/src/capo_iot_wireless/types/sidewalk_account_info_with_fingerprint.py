"""Generated from Smithy shape ``com.amazonaws.iotwireless#SidewalkAccountInfoWithFingerprint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_wireless.types.amazon_id
    import capo_iot_wireless.types.fingerprint
    import capo_iot_wireless.types.partner_account_arn


class SidewalkAccountInfoWithFingerprint(TypedDict, closed=True):
    amazon_id: NotRequired["capo_iot_wireless.types.amazon_id.AmazonId"]
    """<p>The Sidewalk Amazon ID.</p>"""
    fingerprint: NotRequired["capo_iot_wireless.types.fingerprint.Fingerprint"]
    """<p>The fingerprint of the Sidewalk application server private key.</p>"""
    arn: NotRequired["capo_iot_wireless.types.partner_account_arn.PartnerAccountArn"]
    """<p>The Amazon Resource Name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SidewalkAccountInfoWithFingerprint) -> dict:
    out: dict = {}
    if "amazon_id" in value:
        out["AmazonId"] = value["amazon_id"]
    if "fingerprint" in value:
        out["Fingerprint"] = value["fingerprint"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> SidewalkAccountInfoWithFingerprint:
    out: SidewalkAccountInfoWithFingerprint = {}  # type: ignore[typeddict-item]
    if data.get("AmazonId") is not None:
        out["amazon_id"] = data["AmazonId"]
    if data.get("Fingerprint") is not None:
        out["fingerprint"] = data["Fingerprint"]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    return out


def redact_sensitive(value: SidewalkAccountInfoWithFingerprint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fingerprint" in value:
        out["fingerprint"] = "*** Sensitive Data Redacted ***"
    return out
