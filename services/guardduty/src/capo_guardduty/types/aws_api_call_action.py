"""Generated from Smithy shape ``com.amazonaws.guardduty#AwsApiCallAction``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.affected_resources
    import capo_guardduty.types.domain_details
    import capo_guardduty.types.remote_account_details
    import capo_guardduty.types.remote_ip_details
    import capo_guardduty.types.string


class AwsApiCallAction(TypedDict, closed=True):
    api: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services API name.</p>"""
    caller_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services API caller type.</p>"""
    domain_details: NotRequired["capo_guardduty.types.domain_details.DomainDetails"]
    """<p>The domain information for the Amazon Web Services API call.</p>"""
    error_code: NotRequired["capo_guardduty.types.string.String"]
    """<p>The error code of the failed Amazon Web Services API action.</p>"""
    user_agent: NotRequired["capo_guardduty.types.string.String"]
    """<p>The agent through which the API request was made.</p>"""
    remote_ip_details: NotRequired[
        "capo_guardduty.types.remote_ip_details.RemoteIpDetails"
    ]
    """<p>The remote IP information of the connection that initiated the Amazon Web Services API call.</p>"""
    service_name: NotRequired["capo_guardduty.types.string.String"]
    """<p>The Amazon Web Services service name whose API was invoked.</p>"""
    remote_account_details: NotRequired[
        "capo_guardduty.types.remote_account_details.RemoteAccountDetails"
    ]
    """<p>The details of the Amazon Web Services account that made the API call. This field appears if the call was made from outside your account.</p>"""
    affected_resources: NotRequired[
        "capo_guardduty.types.affected_resources.AffectedResources"
    ]
    """<p>The details of the Amazon Web Services account that made the API call. This field identifies the resources that were affected by this API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiCallAction) -> dict:
    out: dict = {}
    if "api" in value:
        out["api"] = value["api"]
    if "caller_type" in value:
        out["callerType"] = value["caller_type"]
    if "domain_details" in value:
        import capo_guardduty.types.domain_details

        out["domainDetails"] = capo_guardduty.types.domain_details.serialize_json(
            value["domain_details"]
        )
    if "error_code" in value:
        out["errorCode"] = value["error_code"]
    if "user_agent" in value:
        out["userAgent"] = value["user_agent"]
    if "remote_ip_details" in value:
        import capo_guardduty.types.remote_ip_details

        out["remoteIpDetails"] = capo_guardduty.types.remote_ip_details.serialize_json(
            value["remote_ip_details"]
        )
    if "service_name" in value:
        out["serviceName"] = value["service_name"]
    if "remote_account_details" in value:
        import capo_guardduty.types.remote_account_details

        out["remoteAccountDetails"] = (
            capo_guardduty.types.remote_account_details.serialize_json(
                value["remote_account_details"]
            )
        )
    if "affected_resources" in value:
        import capo_guardduty.types.affected_resources

        out["affectedResources"] = (
            capo_guardduty.types.affected_resources.serialize_json(
                value["affected_resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsApiCallAction:
    out: AwsApiCallAction = {}  # type: ignore[typeddict-item]
    if data.get("api") is not None:
        out["api"] = data["api"]
    if data.get("callerType") is not None:
        out["caller_type"] = data["callerType"]
    if data.get("domainDetails") is not None:
        import capo_guardduty.types.domain_details

        out["domain_details"] = capo_guardduty.types.domain_details.deserialize_json(
            data["domainDetails"]
        )
    if data.get("errorCode") is not None:
        out["error_code"] = data["errorCode"]
    if data.get("userAgent") is not None:
        out["user_agent"] = data["userAgent"]
    if data.get("remoteIpDetails") is not None:
        import capo_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            capo_guardduty.types.remote_ip_details.deserialize_json(
                data["remoteIpDetails"]
            )
        )
    if data.get("serviceName") is not None:
        out["service_name"] = data["serviceName"]
    if data.get("remoteAccountDetails") is not None:
        import capo_guardduty.types.remote_account_details

        out["remote_account_details"] = (
            capo_guardduty.types.remote_account_details.deserialize_json(
                data["remoteAccountDetails"]
            )
        )
    if data.get("affectedResources") is not None:
        import capo_guardduty.types.affected_resources

        out["affected_resources"] = (
            capo_guardduty.types.affected_resources.deserialize_json(
                data["affectedResources"]
            )
        )
    return out


def redact_sensitive(value: AwsApiCallAction) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "remote_ip_details" in value:
        import capo_guardduty.types.remote_ip_details

        out["remote_ip_details"] = (
            capo_guardduty.types.remote_ip_details.redact_sensitive(
                value["remote_ip_details"]
            )
        )
    return out
