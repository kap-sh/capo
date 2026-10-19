"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetIngressPointResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_mailmanager.types.ingress_point_a_record
    import capo_mailmanager.types.ingress_point_arn
    import capo_mailmanager.types.ingress_point_auth_configuration
    import capo_mailmanager.types.ingress_point_id
    import capo_mailmanager.types.ingress_point_name
    import capo_mailmanager.types.ingress_point_status
    import capo_mailmanager.types.ingress_point_type
    import capo_mailmanager.types.network_configuration
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.tls_policy
    import capo_mailmanager.types.traffic_policy_id


class GetIngressPointResponse(TypedDict, closed=True):
    ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId"
    """<p>The identifier of an ingress endpoint resource.</p>"""
    ingress_point_name: "capo_mailmanager.types.ingress_point_name.IngressPointName"
    """<p>A user friendly name for the ingress endpoint.</p>"""
    ingress_point_arn: NotRequired[
        "capo_mailmanager.types.ingress_point_arn.IngressPointArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the ingress endpoint resource.</p>"""
    status: NotRequired[
        "capo_mailmanager.types.ingress_point_status.IngressPointStatus"
    ]
    """<p>The status of the ingress endpoint resource.</p>"""
    type: NotRequired["capo_mailmanager.types.ingress_point_type.IngressPointType"]
    """<p>The type of ingress endpoint.</p>"""
    a_record: NotRequired[
        "capo_mailmanager.types.ingress_point_a_record.IngressPointARecord"
    ]
    """<p> The DNS A Record that identifies your ingress endpoint. Configure your DNS Mail Exchange (MX) record with this value to route emails to Mail Manager. </p>"""
    rule_set_id: NotRequired["capo_mailmanager.types.rule_set_id.RuleSetId"]
    """<p>The identifier of a rule set resource associated with the ingress endpoint.</p>"""
    traffic_policy_id: NotRequired[
        "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    ]
    """<p>The identifier of the traffic policy resource associated with the ingress endpoint.</p>"""
    ingress_point_auth_configuration: NotRequired[
        "capo_mailmanager.types.ingress_point_auth_configuration.IngressPointAuthConfiguration"
    ]
    """<p>The authentication configuration of the ingress endpoint resource.</p>"""
    network_configuration: NotRequired[
        "capo_mailmanager.types.network_configuration.NetworkConfiguration"
    ]
    """<p>The network configuration for the ingress point.</p>"""
    tls_policy: NotRequired["capo_mailmanager.types.tls_policy.TlsPolicy"]
    """<p>The selected Transport Layer Security (TLS) policy of the ingress point.</p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the ingress endpoint was created.</p>"""
    last_updated_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the ingress endpoint was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetIngressPointResponse) -> dict:
    out: dict = {}
    out["IngressPointId"] = value["ingress_point_id"]
    out["IngressPointName"] = value["ingress_point_name"]
    if "ingress_point_arn" in value:
        out["IngressPointArn"] = value["ingress_point_arn"]
    if "status" in value:
        import capo_mailmanager.types.ingress_point_status

        out["Status"] = (
            capo_mailmanager.types.ingress_point_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "type" in value:
        import capo_mailmanager.types.ingress_point_type

        out["Type"] = capo_mailmanager.types.ingress_point_type.serialize_aws_json_1_0(
            value["type"]
        )
    if "a_record" in value:
        out["ARecord"] = value["a_record"]
    if "rule_set_id" in value:
        out["RuleSetId"] = value["rule_set_id"]
    if "traffic_policy_id" in value:
        out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "ingress_point_auth_configuration" in value:
        import capo_mailmanager.types.ingress_point_auth_configuration

        out["IngressPointAuthConfiguration"] = (
            capo_mailmanager.types.ingress_point_auth_configuration.serialize_aws_json_1_0(
                value["ingress_point_auth_configuration"]
            )
        )
    if "network_configuration" in value:
        import capo_mailmanager.types.network_configuration

        out["NetworkConfiguration"] = (
            capo_mailmanager.types.network_configuration.serialize_aws_json_1_0(
                value["network_configuration"]
            )
        )
    if "tls_policy" in value:
        import capo_mailmanager.types.tls_policy

        out["TlsPolicy"] = capo_mailmanager.types.tls_policy.serialize_aws_json_1_0(
            value["tls_policy"]
        )
    if "created_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "last_updated_timestamp" in value:
        import capo_mailmanager.types._prelude.timestamp

        out["LastUpdatedTimestamp"] = (
            capo_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetIngressPointResponse:
    out: GetIngressPointResponse = {}  # type: ignore[typeddict-item]
    if data.get("IngressPointId") is not None:
        out["ingress_point_id"] = data["IngressPointId"]
    else:
        out["ingress_point_id"] = ""
    if data.get("IngressPointName") is not None:
        out["ingress_point_name"] = data["IngressPointName"]
    else:
        out["ingress_point_name"] = ""
    if data.get("IngressPointArn") is not None:
        out["ingress_point_arn"] = data["IngressPointArn"]
    if data.get("Status") is not None:
        import capo_mailmanager.types.ingress_point_status

        out["status"] = (
            capo_mailmanager.types.ingress_point_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if data.get("Type") is not None:
        import capo_mailmanager.types.ingress_point_type

        out["type"] = (
            capo_mailmanager.types.ingress_point_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    if data.get("ARecord") is not None:
        out["a_record"] = data["ARecord"]
    if data.get("RuleSetId") is not None:
        out["rule_set_id"] = data["RuleSetId"]
    if data.get("TrafficPolicyId") is not None:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    if data.get("IngressPointAuthConfiguration") is not None:
        import capo_mailmanager.types.ingress_point_auth_configuration

        out["ingress_point_auth_configuration"] = (
            capo_mailmanager.types.ingress_point_auth_configuration.deserialize_aws_json_1_0(
                data["IngressPointAuthConfiguration"]
            )
        )
    if data.get("NetworkConfiguration") is not None:
        import capo_mailmanager.types.network_configuration

        out["network_configuration"] = (
            capo_mailmanager.types.network_configuration.deserialize_aws_json_1_0(
                data["NetworkConfiguration"]
            )
        )
    if data.get("TlsPolicy") is not None:
        import capo_mailmanager.types.tls_policy

        out["tls_policy"] = capo_mailmanager.types.tls_policy.deserialize_aws_json_1_0(
            data["TlsPolicy"]
        )
    if data.get("CreatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    if data.get("LastUpdatedTimestamp") is not None:
        import capo_mailmanager.types._prelude.timestamp

        out["last_updated_timestamp"] = (
            capo_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedTimestamp"]
            )
        )
    return out


def redact_sensitive(value: GetIngressPointResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ingress_point_auth_configuration" in value:
        import capo_mailmanager.types.ingress_point_auth_configuration

        out["ingress_point_auth_configuration"] = (
            capo_mailmanager.types.ingress_point_auth_configuration.redact_sensitive(
                value["ingress_point_auth_configuration"]
            )
        )
    return out
