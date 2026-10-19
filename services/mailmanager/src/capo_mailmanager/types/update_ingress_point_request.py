"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateIngressPointRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mailmanager.types.ingress_point_configuration
    import capo_mailmanager.types.ingress_point_id
    import capo_mailmanager.types.ingress_point_name
    import capo_mailmanager.types.ingress_point_status_to_update
    import capo_mailmanager.types.rule_set_id
    import capo_mailmanager.types.tls_policy
    import capo_mailmanager.types.traffic_policy_id


class UpdateIngressPointRequest(TypedDict, closed=True):
    ingress_point_id: "capo_mailmanager.types.ingress_point_id.IngressPointId"
    """<p>The identifier for the ingress endpoint you want to update.</p>"""
    ingress_point_name: NotRequired[
        "capo_mailmanager.types.ingress_point_name.IngressPointName"
    ]
    """<p>A user friendly name for the ingress endpoint resource.</p>"""
    status_to_update: NotRequired[
        "capo_mailmanager.types.ingress_point_status_to_update.IngressPointStatusToUpdate"
    ]
    """<p>The update status of an ingress endpoint.</p>"""
    rule_set_id: NotRequired["capo_mailmanager.types.rule_set_id.RuleSetId"]
    """<p>The identifier of an existing rule set that you attach to an ingress endpoint resource.</p>"""
    traffic_policy_id: NotRequired[
        "capo_mailmanager.types.traffic_policy_id.TrafficPolicyId"
    ]
    """<p>The identifier of an existing traffic policy that you attach to an ingress endpoint resource.</p>"""
    ingress_point_configuration: NotRequired[
        "capo_mailmanager.types.ingress_point_configuration.IngressPointConfiguration"
    ]
    """<p>If you choose an Authenticated ingress endpoint, you must configure either an SMTP password or a secret ARN.</p>"""
    tls_policy: NotRequired["capo_mailmanager.types.tls_policy.TlsPolicy"]
    """<p>The Transport Layer Security (TLS) policy for the ingress point. Valid values are REQUIRED, OPTIONAL. Only ingress endpoints using REQUIRED or OPTIONAL as TlsPolicy can be updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateIngressPointRequest) -> dict:
    out: dict = {}
    out["IngressPointId"] = value["ingress_point_id"]
    if "ingress_point_name" in value:
        out["IngressPointName"] = value["ingress_point_name"]
    if "status_to_update" in value:
        import capo_mailmanager.types.ingress_point_status_to_update

        out["StatusToUpdate"] = (
            capo_mailmanager.types.ingress_point_status_to_update.serialize_aws_json_1_0(
                value["status_to_update"]
            )
        )
    if "rule_set_id" in value:
        out["RuleSetId"] = value["rule_set_id"]
    if "traffic_policy_id" in value:
        out["TrafficPolicyId"] = value["traffic_policy_id"]
    if "ingress_point_configuration" in value:
        import capo_mailmanager.types.ingress_point_configuration

        out["IngressPointConfiguration"] = (
            capo_mailmanager.types.ingress_point_configuration.serialize_aws_json_1_0(
                value["ingress_point_configuration"]
            )
        )
    if "tls_policy" in value:
        import capo_mailmanager.types.tls_policy

        out["TlsPolicy"] = capo_mailmanager.types.tls_policy.serialize_aws_json_1_0(
            value["tls_policy"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateIngressPointRequest:
    out: UpdateIngressPointRequest = {}  # type: ignore[typeddict-item]
    if data.get("IngressPointId") is not None:
        out["ingress_point_id"] = data["IngressPointId"]
    else:
        out["ingress_point_id"] = ""
    if data.get("IngressPointName") is not None:
        out["ingress_point_name"] = data["IngressPointName"]
    if data.get("StatusToUpdate") is not None:
        import capo_mailmanager.types.ingress_point_status_to_update

        out["status_to_update"] = (
            capo_mailmanager.types.ingress_point_status_to_update.deserialize_aws_json_1_0(
                data["StatusToUpdate"]
            )
        )
    if data.get("RuleSetId") is not None:
        out["rule_set_id"] = data["RuleSetId"]
    if data.get("TrafficPolicyId") is not None:
        out["traffic_policy_id"] = data["TrafficPolicyId"]
    if data.get("IngressPointConfiguration") is not None:
        import capo_mailmanager.types.ingress_point_configuration

        out["ingress_point_configuration"] = (
            capo_mailmanager.types.ingress_point_configuration.deserialize_aws_json_1_0(
                data["IngressPointConfiguration"]
            )
        )
    if data.get("TlsPolicy") is not None:
        import capo_mailmanager.types.tls_policy

        out["tls_policy"] = capo_mailmanager.types.tls_policy.deserialize_aws_json_1_0(
            data["TlsPolicy"]
        )
    return out


def redact_sensitive(value: UpdateIngressPointRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ingress_point_configuration" in value:
        import capo_mailmanager.types.ingress_point_configuration

        out["ingress_point_configuration"] = (
            capo_mailmanager.types.ingress_point_configuration.redact_sensitive(
                value["ingress_point_configuration"]
            )
        )
    return out
