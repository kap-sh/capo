"""Generated from Smithy shape ``com.amazonaws.sesv2#GetAccountResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.account_details
    import capo_sesv2.types.enabled
    import capo_sesv2.types.general_enforcement_status
    import capo_sesv2.types.pricing_attributes
    import capo_sesv2.types.send_quota
    import capo_sesv2.types.suppression_attributes
    import capo_sesv2.types.vdm_attributes


class GetAccountResponse(TypedDict, closed=True):
    dedicated_ip_auto_warmup_enabled: "capo_sesv2.types.enabled.Enabled"
    """<p>Indicates whether or not the automatic warm-up feature is enabled for dedicated IP addresses that are associated with your account.</p>"""
    enforcement_status: NotRequired[
        "capo_sesv2.types.general_enforcement_status.GeneralEnforcementStatus"
    ]
    """<p>The reputation status of your Amazon SES account. The status can be one of the following:</p> <ul> <li> <p> <code>HEALTHY</code> – There are no reputation-related issues that currently impact your account.</p> </li> <li> <p> <code>PROBATION</code> – We've identified potential issues with your Amazon SES account. We're placing your account under review while you work on correcting these issues.</p> </li> <li> <p> <code>SHUTDOWN</code> – Your account's ability to send email is currently paused because of an issue with the email sent from your account. When you correct the issue, you can contact us and request that your account's ability to send email is resumed.</p> </li> </ul>"""
    production_access_enabled: "capo_sesv2.types.enabled.Enabled"
    """<p>Indicates whether or not your account has production access in the current Amazon Web Services Region.</p> <p>If the value is <code>false</code>, then your account is in the <i>sandbox</i>. When your account is in the sandbox, you can only send email to verified identities. </p> <p>If the value is <code>true</code>, then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.</p>"""
    send_quota: NotRequired["capo_sesv2.types.send_quota.SendQuota"]
    """<p>An object that contains information about the per-day and per-second sending limits for your Amazon SES account in the current Amazon Web Services Region.</p>"""
    sending_enabled: "capo_sesv2.types.enabled.Enabled"
    """<p>Indicates whether or not email sending is enabled for your Amazon SES account in the current Amazon Web Services Region.</p>"""
    suppression_attributes: NotRequired[
        "capo_sesv2.types.suppression_attributes.SuppressionAttributes"
    ]
    """<p>An object that contains information about the email address suppression preferences for your account in the current Amazon Web Services Region.</p>"""
    details: NotRequired["capo_sesv2.types.account_details.AccountDetails"]
    """<p>An object that defines your account details.</p>"""
    vdm_attributes: NotRequired["capo_sesv2.types.vdm_attributes.VdmAttributes"]
    """<p>The VDM attributes that apply to your Amazon SES account.</p>"""
    pricing_attributes: NotRequired[
        "capo_sesv2.types.pricing_attributes.PricingAttributes"
    ]
    """<p>The pricing attributes that apply to your Amazon SES account, including the currently active pricing plan and any scheduled change.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountResponse) -> dict:
    out: dict = {}
    out["DedicatedIpAutoWarmupEnabled"] = value.get(
        "dedicated_ip_auto_warmup_enabled", False
    )
    if "enforcement_status" in value:
        out["EnforcementStatus"] = value["enforcement_status"]
    out["ProductionAccessEnabled"] = value.get("production_access_enabled", False)
    if "send_quota" in value:
        import capo_sesv2.types.send_quota

        out["SendQuota"] = capo_sesv2.types.send_quota.serialize_json(
            value["send_quota"]
        )
    out["SendingEnabled"] = value.get("sending_enabled", False)
    if "suppression_attributes" in value:
        import capo_sesv2.types.suppression_attributes

        out["SuppressionAttributes"] = (
            capo_sesv2.types.suppression_attributes.serialize_json(
                value["suppression_attributes"]
            )
        )
    if "details" in value:
        import capo_sesv2.types.account_details

        out["Details"] = capo_sesv2.types.account_details.serialize_json(
            value["details"]
        )
    if "vdm_attributes" in value:
        import capo_sesv2.types.vdm_attributes

        out["VdmAttributes"] = capo_sesv2.types.vdm_attributes.serialize_json(
            value["vdm_attributes"]
        )
    if "pricing_attributes" in value:
        import capo_sesv2.types.pricing_attributes

        out["PricingAttributes"] = capo_sesv2.types.pricing_attributes.serialize_json(
            value["pricing_attributes"]
        )
    return out


def deserialize_json(data: dict) -> GetAccountResponse:
    out: GetAccountResponse = {}  # type: ignore[typeddict-item]
    if data.get("DedicatedIpAutoWarmupEnabled") is not None:
        out["dedicated_ip_auto_warmup_enabled"] = data["DedicatedIpAutoWarmupEnabled"]
    else:
        out["dedicated_ip_auto_warmup_enabled"] = False
    if data.get("EnforcementStatus") is not None:
        out["enforcement_status"] = data["EnforcementStatus"]
    if data.get("ProductionAccessEnabled") is not None:
        out["production_access_enabled"] = data["ProductionAccessEnabled"]
    else:
        out["production_access_enabled"] = False
    if data.get("SendQuota") is not None:
        import capo_sesv2.types.send_quota

        out["send_quota"] = capo_sesv2.types.send_quota.deserialize_json(
            data["SendQuota"]
        )
    if data.get("SendingEnabled") is not None:
        out["sending_enabled"] = data["SendingEnabled"]
    else:
        out["sending_enabled"] = False
    if data.get("SuppressionAttributes") is not None:
        import capo_sesv2.types.suppression_attributes

        out["suppression_attributes"] = (
            capo_sesv2.types.suppression_attributes.deserialize_json(
                data["SuppressionAttributes"]
            )
        )
    if data.get("Details") is not None:
        import capo_sesv2.types.account_details

        out["details"] = capo_sesv2.types.account_details.deserialize_json(
            data["Details"]
        )
    if data.get("VdmAttributes") is not None:
        import capo_sesv2.types.vdm_attributes

        out["vdm_attributes"] = capo_sesv2.types.vdm_attributes.deserialize_json(
            data["VdmAttributes"]
        )
    if data.get("PricingAttributes") is not None:
        import capo_sesv2.types.pricing_attributes

        out["pricing_attributes"] = (
            capo_sesv2.types.pricing_attributes.deserialize_json(
                data["PricingAttributes"]
            )
        )
    return out


def redact_sensitive(value: GetAccountResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "details" in value:
        import capo_sesv2.types.account_details

        out["details"] = capo_sesv2.types.account_details.redact_sensitive(
            value["details"]
        )
    return out
