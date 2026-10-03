"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsApiCallAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.action_remote_ip_details
    import capo_securityhub.types.aws_api_call_action_domain_details
    import capo_securityhub.types.field_map
    import capo_securityhub.types.non_empty_string


class AwsApiCallAction(TypedDict, closed=True):
    api: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the API method that was issued.</p> <p>Length Constraints: 128.</p>"""
    service_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the Amazon Web Services service that the API method belongs to.</p> <p>Length Constraints: 128.</p>"""
    caller_type: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Indicates whether the API call originated from a remote IP address (<code>remoteip</code>) or from a DNS domain (<code>domain</code>).</p>"""
    remote_ip_details: NotRequired[
        "capo_securityhub.types.action_remote_ip_details.ActionRemoteIpDetails"
    ]
    """<p>Provided if <code>CallerType</code> is <code>remoteip</code>. Provides information about the remote IP address that the API call originated from.</p>"""
    domain_details: NotRequired[
        "capo_securityhub.types.aws_api_call_action_domain_details.AwsApiCallActionDomainDetails"
    ]
    """<p>Provided if <code>CallerType</code> is <code>domain</code>. Provides information about the DNS domain that the API call originated from.</p>"""
    affected_resources: NotRequired["capo_securityhub.types.field_map.FieldMap"]
    """<p>Identifies the resources that were affected by the API call.</p>"""
    first_seen: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A timestamp that indicates when the API call was first observed.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""
    last_seen: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>A timestamp that indicates when the API call was most recently observed.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href="https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps">Timestamps</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsApiCallAction) -> dict:
    out: dict = {}
    if "api" in value:
        out["Api"] = value["api"]
    if "service_name" in value:
        out["ServiceName"] = value["service_name"]
    if "caller_type" in value:
        out["CallerType"] = value["caller_type"]
    if "remote_ip_details" in value:
        import capo_securityhub.types.action_remote_ip_details

        out["RemoteIpDetails"] = (
            capo_securityhub.types.action_remote_ip_details.serialize_json(
                value["remote_ip_details"]
            )
        )
    if "domain_details" in value:
        import capo_securityhub.types.aws_api_call_action_domain_details

        out["DomainDetails"] = (
            capo_securityhub.types.aws_api_call_action_domain_details.serialize_json(
                value["domain_details"]
            )
        )
    if "affected_resources" in value:
        import capo_securityhub.types.field_map

        out["AffectedResources"] = capo_securityhub.types.field_map.serialize_json(
            value["affected_resources"]
        )
    if "first_seen" in value:
        out["FirstSeen"] = value["first_seen"]
    if "last_seen" in value:
        out["LastSeen"] = value["last_seen"]
    return out


def deserialize_json(data: dict) -> AwsApiCallAction:
    out: AwsApiCallAction = {}  # type: ignore[typeddict-item]
    if data.get("Api") is not None:
        out["api"] = data["Api"]
    if data.get("ServiceName") is not None:
        out["service_name"] = data["ServiceName"]
    if data.get("CallerType") is not None:
        out["caller_type"] = data["CallerType"]
    if data.get("RemoteIpDetails") is not None:
        import capo_securityhub.types.action_remote_ip_details

        out["remote_ip_details"] = (
            capo_securityhub.types.action_remote_ip_details.deserialize_json(
                data["RemoteIpDetails"]
            )
        )
    if data.get("DomainDetails") is not None:
        import capo_securityhub.types.aws_api_call_action_domain_details

        out["domain_details"] = (
            capo_securityhub.types.aws_api_call_action_domain_details.deserialize_json(
                data["DomainDetails"]
            )
        )
    if data.get("AffectedResources") is not None:
        import capo_securityhub.types.field_map

        out["affected_resources"] = capo_securityhub.types.field_map.deserialize_json(
            data["AffectedResources"]
        )
    if data.get("FirstSeen") is not None:
        out["first_seen"] = data["FirstSeen"]
    if data.get("LastSeen") is not None:
        out["last_seen"] = data["LastSeen"]
    return out
