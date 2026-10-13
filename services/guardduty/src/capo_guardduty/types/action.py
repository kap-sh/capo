"""Generated from Smithy shape ``com.amazonaws.guardduty#Action``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.aws_api_call_action
    import capo_guardduty.types.dns_request_action
    import capo_guardduty.types.kubernetes_api_call_action
    import capo_guardduty.types.kubernetes_permission_checked_details
    import capo_guardduty.types.kubernetes_role_binding_details
    import capo_guardduty.types.kubernetes_role_details
    import capo_guardduty.types.network_connection_action
    import capo_guardduty.types.port_probe_action
    import capo_guardduty.types.rds_login_attempt_action
    import capo_guardduty.types.string


class Action(TypedDict, closed=True):
    action_type: NotRequired["capo_guardduty.types.string.String"]
    """<p>The GuardDuty finding activity type.</p>"""
    aws_api_call_action: NotRequired[
        "capo_guardduty.types.aws_api_call_action.AwsApiCallAction"
    ]
    """<p>Information about the AWS_API_CALL action described in this finding.</p>"""
    dns_request_action: NotRequired[
        "capo_guardduty.types.dns_request_action.DnsRequestAction"
    ]
    """<p>Information about the DNS_REQUEST action described in this finding.</p>"""
    network_connection_action: NotRequired[
        "capo_guardduty.types.network_connection_action.NetworkConnectionAction"
    ]
    """<p>Information about the NETWORK_CONNECTION action described in this finding.</p>"""
    port_probe_action: NotRequired[
        "capo_guardduty.types.port_probe_action.PortProbeAction"
    ]
    """<p>Information about the PORT_PROBE action described in this finding.</p>"""
    kubernetes_api_call_action: NotRequired[
        "capo_guardduty.types.kubernetes_api_call_action.KubernetesApiCallAction"
    ]
    """<p>Information about the Kubernetes API call action described in this finding.</p>"""
    kubernetes_permission_checked_details: NotRequired[
        "capo_guardduty.types.kubernetes_permission_checked_details.KubernetesPermissionCheckedDetails"
    ]
    """<p>Information whether the user has the permission to use a specific Kubernetes API.</p>"""
    kubernetes_role_binding_details: NotRequired[
        "capo_guardduty.types.kubernetes_role_binding_details.KubernetesRoleBindingDetails"
    ]
    """<p>Information about the role binding that grants the permission defined in a Kubernetes role.</p>"""
    kubernetes_role_details: NotRequired[
        "capo_guardduty.types.kubernetes_role_details.KubernetesRoleDetails"
    ]
    """<p>Information about the Kubernetes role name and role type.</p>"""
    rds_login_attempt_action: NotRequired[
        "capo_guardduty.types.rds_login_attempt_action.RdsLoginAttemptAction"
    ]
    """<p>Information about <code>RDS_LOGIN_ATTEMPT</code> action described in this finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    out: dict = {}
    if "action_type" in value:
        out["actionType"] = value["action_type"]
    if "aws_api_call_action" in value:
        import capo_guardduty.types.aws_api_call_action

        out["awsApiCallAction"] = (
            capo_guardduty.types.aws_api_call_action.serialize_json(
                value["aws_api_call_action"]
            )
        )
    if "dns_request_action" in value:
        import capo_guardduty.types.dns_request_action

        out["dnsRequestAction"] = (
            capo_guardduty.types.dns_request_action.serialize_json(
                value["dns_request_action"]
            )
        )
    if "network_connection_action" in value:
        import capo_guardduty.types.network_connection_action

        out["networkConnectionAction"] = (
            capo_guardduty.types.network_connection_action.serialize_json(
                value["network_connection_action"]
            )
        )
    if "port_probe_action" in value:
        import capo_guardduty.types.port_probe_action

        out["portProbeAction"] = capo_guardduty.types.port_probe_action.serialize_json(
            value["port_probe_action"]
        )
    if "kubernetes_api_call_action" in value:
        import capo_guardduty.types.kubernetes_api_call_action

        out["kubernetesApiCallAction"] = (
            capo_guardduty.types.kubernetes_api_call_action.serialize_json(
                value["kubernetes_api_call_action"]
            )
        )
    if "kubernetes_permission_checked_details" in value:
        import capo_guardduty.types.kubernetes_permission_checked_details

        out["kubernetesPermissionCheckedDetails"] = (
            capo_guardduty.types.kubernetes_permission_checked_details.serialize_json(
                value["kubernetes_permission_checked_details"]
            )
        )
    if "kubernetes_role_binding_details" in value:
        import capo_guardduty.types.kubernetes_role_binding_details

        out["kubernetesRoleBindingDetails"] = (
            capo_guardduty.types.kubernetes_role_binding_details.serialize_json(
                value["kubernetes_role_binding_details"]
            )
        )
    if "kubernetes_role_details" in value:
        import capo_guardduty.types.kubernetes_role_details

        out["kubernetesRoleDetails"] = (
            capo_guardduty.types.kubernetes_role_details.serialize_json(
                value["kubernetes_role_details"]
            )
        )
    if "rds_login_attempt_action" in value:
        import capo_guardduty.types.rds_login_attempt_action

        out["rdsLoginAttemptAction"] = (
            capo_guardduty.types.rds_login_attempt_action.serialize_json(
                value["rds_login_attempt_action"]
            )
        )
    return out


def deserialize_json(data: dict) -> Action:
    out: Action = {}  # type: ignore[typeddict-item]
    if data.get("actionType") is not None:
        out["action_type"] = data["actionType"]
    if data.get("awsApiCallAction") is not None:
        import capo_guardduty.types.aws_api_call_action

        out["aws_api_call_action"] = (
            capo_guardduty.types.aws_api_call_action.deserialize_json(
                data["awsApiCallAction"]
            )
        )
    if data.get("dnsRequestAction") is not None:
        import capo_guardduty.types.dns_request_action

        out["dns_request_action"] = (
            capo_guardduty.types.dns_request_action.deserialize_json(
                data["dnsRequestAction"]
            )
        )
    if data.get("networkConnectionAction") is not None:
        import capo_guardduty.types.network_connection_action

        out["network_connection_action"] = (
            capo_guardduty.types.network_connection_action.deserialize_json(
                data["networkConnectionAction"]
            )
        )
    if data.get("portProbeAction") is not None:
        import capo_guardduty.types.port_probe_action

        out["port_probe_action"] = (
            capo_guardduty.types.port_probe_action.deserialize_json(
                data["portProbeAction"]
            )
        )
    if data.get("kubernetesApiCallAction") is not None:
        import capo_guardduty.types.kubernetes_api_call_action

        out["kubernetes_api_call_action"] = (
            capo_guardduty.types.kubernetes_api_call_action.deserialize_json(
                data["kubernetesApiCallAction"]
            )
        )
    if data.get("kubernetesPermissionCheckedDetails") is not None:
        import capo_guardduty.types.kubernetes_permission_checked_details

        out["kubernetes_permission_checked_details"] = (
            capo_guardduty.types.kubernetes_permission_checked_details.deserialize_json(
                data["kubernetesPermissionCheckedDetails"]
            )
        )
    if data.get("kubernetesRoleBindingDetails") is not None:
        import capo_guardduty.types.kubernetes_role_binding_details

        out["kubernetes_role_binding_details"] = (
            capo_guardduty.types.kubernetes_role_binding_details.deserialize_json(
                data["kubernetesRoleBindingDetails"]
            )
        )
    if data.get("kubernetesRoleDetails") is not None:
        import capo_guardduty.types.kubernetes_role_details

        out["kubernetes_role_details"] = (
            capo_guardduty.types.kubernetes_role_details.deserialize_json(
                data["kubernetesRoleDetails"]
            )
        )
    if data.get("rdsLoginAttemptAction") is not None:
        import capo_guardduty.types.rds_login_attempt_action

        out["rds_login_attempt_action"] = (
            capo_guardduty.types.rds_login_attempt_action.deserialize_json(
                data["rdsLoginAttemptAction"]
            )
        )
    return out


def redact_sensitive(value: Action) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "aws_api_call_action" in value:
        import capo_guardduty.types.aws_api_call_action

        out["aws_api_call_action"] = (
            capo_guardduty.types.aws_api_call_action.redact_sensitive(
                value["aws_api_call_action"]
            )
        )
    if "network_connection_action" in value:
        import capo_guardduty.types.network_connection_action

        out["network_connection_action"] = (
            capo_guardduty.types.network_connection_action.redact_sensitive(
                value["network_connection_action"]
            )
        )
    if "port_probe_action" in value:
        import capo_guardduty.types.port_probe_action

        out["port_probe_action"] = (
            capo_guardduty.types.port_probe_action.redact_sensitive(
                value["port_probe_action"]
            )
        )
    if "kubernetes_api_call_action" in value:
        import capo_guardduty.types.kubernetes_api_call_action

        out["kubernetes_api_call_action"] = (
            capo_guardduty.types.kubernetes_api_call_action.redact_sensitive(
                value["kubernetes_api_call_action"]
            )
        )
    if "rds_login_attempt_action" in value:
        import capo_guardduty.types.rds_login_attempt_action

        out["rds_login_attempt_action"] = (
            capo_guardduty.types.rds_login_attempt_action.redact_sensitive(
                value["rds_login_attempt_action"]
            )
        )
    return out
