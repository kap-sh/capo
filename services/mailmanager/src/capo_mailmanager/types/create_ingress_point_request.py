"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateIngressPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.idempotency_token
    import capo_mailmanager.types.ingress_point_configuration
    import capo_mailmanager.types.ingress_point_name
    import capo_mailmanager.types.ingress_point_type
    import capo_mailmanager.types.network_configuration
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.tag_list
    import capo_mailmanager.types.tls_policy
    import capo_mailmanager.types.traffic_policy_id


class CreateIngressPointRequest(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    ingress_point_name: "capo_mailmanager.types.ingress_point_name.IngressPointName"
    """<p>A user friendly name for an ingress endpoint resource.</p>"""
    type: "capo_mailmanager.types.ingress_point_type.IngressPointType"
    """<p>The type of the ingress endpoint to create.</p>"""
    rule_set_id: "capo_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>"""
    traffic_policy_id: "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    """<p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>"""
    ingress_point_configuration: NotRequired[
        "capo_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
    ]
    """<p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>"""
    network_configuration: NotRequired[
        "capo_mailmanager.types.network_configuration.NetworkConfiguration"
    ]
    """<p>Specifies the network configuration for the ingress point. This allows you to create an IPv4-only, Dual-Stack, or PrivateLink type of ingress point. If not specified, the default network type is IPv4-only. </p>"""
    tls_policy: NotRequired["capo_mailmanager.types.tls_policy.TlsPolicy"]
    """<p>The Transport Layer Security (TLS) policy for the ingress point. The FIPS value is only valid in US and Canada regions.</p>"""
    tags: NotRequired["capo_mailmanager.types.tag_list.TagList"]
    """<p>The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIngressPointRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["IngressPointName"] = value["ingress_point_name"]
    import capo_mailmanager.types.ingress_point_type

    out["Type"] = capo_mailmanager.types.ingress_point_type.serialize_aws_json_1_0(
        value["type"]
    )
    out["RuleSetId"] = value["rule_set_id"]
    out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "ingress_point_configuration" in value:
        import capo_mailmanager.types.ingress_point_configuration

        out["IngressPointConfiguration"] = (
            capo_mailmanager.types.ingress_point_configuration.serialize_aws_json_1_0(
                value["ingress_point_configuration"]
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
    if "tags" in value:
        import capo_mailmanager.types.tag_list

        out["Tags"] = capo_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIngressPointRequest:
    out: CreateIngressPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("IngressPointName") is not None:
        out["ingress_point_name"] = data["IngressPointName"]
    else:
        raise DeserializationError(
            "CreateIngressPointRequest.ingress_point_name required"
        )
    if data.get("Type") is not None:
        import capo_mailmanager.types.ingress_point_type

        out["type"] = (
            capo_mailmanager.types.ingress_point_type.deserialize_aws_json_1_0(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("CreateIngressPointRequest.type required")
    if data.get("RuleSetId") is not None:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        raise DeserializationError("CreateIngressPointRequest.rule_set_id required")
    if data.get("TrafficPolicyId") is not None:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    else:
        raise DeserializationError(
            "CreateIngressPointRequest.traffic_policy_id required"
        )
    if data.get("IngressPointConfiguration") is not None:
        import capo_mailmanager.types.ingress_point_configuration

        out["ingress_point_configuration"] = (
            capo_mailmanager.types.ingress_point_configuration.deserialize_aws_json_1_0(
                data["IngressPointConfiguration"]
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
    if data.get("Tags") is not None:
        import capo_mailmanager.types.tag_list

        out["tags"] = capo_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
