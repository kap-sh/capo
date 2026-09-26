"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#RunMicrovmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.idle_policy
    import capo_lambda_microvms.types.logging
    import capo_lambda_microvms.types.microvm_image_identifier
    import capo_lambda_microvms.types.network_connector_list
    import capo_lambda_microvms.types.role_arn
    import capo_lambda_microvms.types.run_hook_payload
    import capo_lambda_microvms.types.version


class RunMicrovmRequest(TypedDict, closed=True):
    ingress_network_connectors: NotRequired[
        "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
    ]
    """<p>The list of ingress network connectors to configure for the MicroVM.</p>"""
    egress_network_connectors: NotRequired[
        "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
    ]
    """<p>The list of egress network connectors to configure for the MicroVM.</p>"""
    image_identifier: (
        "capo_lambda_microvms.types.microvm_image_identifier.MicrovmImageIdentifier"
    )
    """<p>The identifier (ARN or ID) of the MicroVM image to run.</p>"""
    image_version: NotRequired["capo_lambda_microvms.types.version.Version"]
    """<p>The version of the MicroVM image to run.</p>"""
    execution_role_arn: NotRequired["capo_lambda_microvms.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role to be assumed by the MicroVM during execution.</p>"""
    idle_policy: NotRequired["capo_lambda_microvms.types.idle_policy.IdlePolicy"]
    """<p>Configuration to control auto-suspend and auto-resume behavior.</p>"""
    logging: NotRequired["capo_lambda_microvms.types.logging.Logging"]
    r"""<p>The logging configuration for this MicroVM instance. Specify {\"cloudWatch\": {\"logGroup\": \"...\"}} to stream application logs to a custom CloudWatch log group, or {\"disabled\": {}} to turn off logging.</p>"""
    run_hook_payload: NotRequired[
        "capo_lambda_microvms.types.run_hook_payload.RunHookPayload"
    ]
    """<p>Per-MicroVM initialization data delivered as the request body of the /run lifecycle hook. Use to pass tenant-specific configuration such as session IDs or secret references. Maximum: 16,384 bytes.</p>"""
    maximum_duration_in_seconds: NotRequired["int"]
    """<p>The maximum duration in seconds that the MicroVM can exist before being terminated by the platform. Valid range: 1–28,800 (8 hours).</p>"""
    client_token: NotRequired["str"]
    """<p>A unique, case-sensitive identifier you provide to ensure the idempotency of the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunMicrovmRequest) -> dict:
    out: dict = {}
    if "ingress_network_connectors" in value:
        import capo_lambda_microvms.types.network_connector_list

        out["ingressNetworkConnectors"] = (
            capo_lambda_microvms.types.network_connector_list.serialize_json(
                value["ingress_network_connectors"]
            )
        )
    if "egress_network_connectors" in value:
        import capo_lambda_microvms.types.network_connector_list

        out["egressNetworkConnectors"] = (
            capo_lambda_microvms.types.network_connector_list.serialize_json(
                value["egress_network_connectors"]
            )
        )
    out["imageIdentifier"] = value["image_identifier"]
    if "image_version" in value:
        out["imageVersion"] = value["image_version"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "idle_policy" in value:
        import capo_lambda_microvms.types.idle_policy

        out["idlePolicy"] = capo_lambda_microvms.types.idle_policy.serialize_json(
            value["idle_policy"]
        )
    if "logging" in value:
        import capo_lambda_microvms.types.logging

        out["logging"] = capo_lambda_microvms.types.logging.serialize_json(
            value["logging"]
        )
    if "run_hook_payload" in value:
        out["runHookPayload"] = value["run_hook_payload"]
    if "maximum_duration_in_seconds" in value:
        out["maximumDurationInSeconds"] = value["maximum_duration_in_seconds"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> RunMicrovmRequest:
    out: RunMicrovmRequest = {}  # type: ignore[typeddict-item]
    if data.get("ingressNetworkConnectors") is not None:
        import capo_lambda_microvms.types.network_connector_list

        out["ingress_network_connectors"] = (
            capo_lambda_microvms.types.network_connector_list.deserialize_json(
                data["ingressNetworkConnectors"]
            )
        )
    if data.get("egressNetworkConnectors") is not None:
        import capo_lambda_microvms.types.network_connector_list

        out["egress_network_connectors"] = (
            capo_lambda_microvms.types.network_connector_list.deserialize_json(
                data["egressNetworkConnectors"]
            )
        )
    if data.get("imageIdentifier") is not None:
        out["image_identifier"] = data["imageIdentifier"]
    else:
        raise DeserializationError("RunMicrovmRequest.image_identifier required")
    if data.get("imageVersion") is not None:
        out["image_version"] = data["imageVersion"]
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("idlePolicy") is not None:
        import capo_lambda_microvms.types.idle_policy

        out["idle_policy"] = capo_lambda_microvms.types.idle_policy.deserialize_json(
            data["idlePolicy"]
        )
    if data.get("logging") is not None:
        import capo_lambda_microvms.types.logging

        out["logging"] = capo_lambda_microvms.types.logging.deserialize_json(
            data["logging"]
        )
    if data.get("runHookPayload") is not None:
        out["run_hook_payload"] = data["runHookPayload"]
    if data.get("maximumDurationInSeconds") is not None:
        out["maximum_duration_in_seconds"] = data["maximumDurationInSeconds"]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
