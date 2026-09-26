"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#RunMicrovmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_lambda_microvms.types.idle_policy
    import capo_lambda_microvms.types.microvm_identifier
    import capo_lambda_microvms.types.microvm_image_arn
    import capo_lambda_microvms.types.microvm_state
    import capo_lambda_microvms.types.network_connector_list
    import capo_lambda_microvms.types.non_blank_string
    import capo_lambda_microvms.types.role_arn
    import capo_lambda_microvms.types.version


class RunMicrovmResponse(TypedDict, closed=True):
    microvm_id: "capo_lambda_microvms.types.microvm_identifier.MicrovmIdentifier"
    """<p>The unique identifier of the MicroVM.</p>"""
    state: "capo_lambda_microvms.types.microvm_state.MicrovmState"
    """<p>The current lifecycle state of the MicroVM.</p>"""
    endpoint: "str"
    """<p>The HTTPS endpoint URL for communicating with the MicroVM. Include a valid authentication token in the X-aws-proxy-auth header when sending requests.</p>"""
    image_arn: "capo_lambda_microvms.types.microvm_image_arn.MicrovmImageArn"
    """<p>The ARN of the MicroVM image used to run this MicroVM.</p>"""
    image_version: "capo_lambda_microvms.types.version.Version"
    """<p>The version of the MicroVM image used to run this MicroVM.</p>"""
    execution_role_arn: NotRequired["capo_lambda_microvms.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM execution role assumed by the MicroVM.</p>"""
    idle_policy: NotRequired["capo_lambda_microvms.types.idle_policy.IdlePolicy"]
    """<p>The idle policy configuration of the MicroVM.</p>"""
    maximum_duration_in_seconds: "int"
    """<p>The maximum duration in seconds that the MicroVM can exist.</p>"""
    started_at: "datetime.datetime"
    """<p>The timestamp when the MicroVM first started.</p>"""
    terminated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the MicroVM terminated.</p>"""
    state_reason: NotRequired[
        "capo_lambda_microvms.types.non_blank_string.NonBlankString"
    ]
    """<p>The reason for why the MicroVM is in the current state.</p>"""
    ingress_network_connectors: NotRequired[
        "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
    ]
    """<p>The list of ingress network connectors configured for the MicroVM.</p>"""
    egress_network_connectors: NotRequired[
        "capo_lambda_microvms.types.network_connector_list.NetworkConnectorList"
    ]
    """<p>The list of egress network connectors configured for the MicroVM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RunMicrovmResponse) -> dict:
    out: dict = {}
    out["microvmId"] = value["microvm_id"]
    import capo_lambda_microvms.types.microvm_state

    out["state"] = capo_lambda_microvms.types.microvm_state.serialize_json(
        value["state"]
    )
    out["endpoint"] = value["endpoint"]
    out["imageArn"] = value["image_arn"]
    out["imageVersion"] = value["image_version"]
    if "execution_role_arn" in value:
        out["executionRoleArn"] = value["execution_role_arn"]
    if "idle_policy" in value:
        import capo_lambda_microvms.types.idle_policy

        out["idlePolicy"] = capo_lambda_microvms.types.idle_policy.serialize_json(
            value["idle_policy"]
        )
    out["maximumDurationInSeconds"] = value["maximum_duration_in_seconds"]
    import capo_lambda_microvms.types._prelude.timestamp

    out["startedAt"] = capo_lambda_microvms.types._prelude.timestamp.serialize_json(
        value["started_at"]
    )
    if "terminated_at" in value:
        import capo_lambda_microvms.types._prelude.timestamp

        out["terminatedAt"] = (
            capo_lambda_microvms.types._prelude.timestamp.serialize_json(
                value["terminated_at"]
            )
        )
    if "state_reason" in value:
        out["stateReason"] = value["state_reason"]
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
    return out


def deserialize_json(data: dict) -> RunMicrovmResponse:
    out: RunMicrovmResponse = {}  # type: ignore[typeddict-item]
    if data.get("microvmId") is not None:
        out["microvm_id"] = data["microvmId"]
    else:
        raise DeserializationError("RunMicrovmResponse.microvm_id required")
    if data.get("state") is not None:
        import capo_lambda_microvms.types.microvm_state

        out["state"] = capo_lambda_microvms.types.microvm_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("RunMicrovmResponse.state required")
    if data.get("endpoint") is not None:
        out["endpoint"] = data["endpoint"]
    else:
        raise DeserializationError("RunMicrovmResponse.endpoint required")
    if data.get("imageArn") is not None:
        out["image_arn"] = data["imageArn"]
    else:
        raise DeserializationError("RunMicrovmResponse.image_arn required")
    if data.get("imageVersion") is not None:
        out["image_version"] = data["imageVersion"]
    else:
        raise DeserializationError("RunMicrovmResponse.image_version required")
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    if data.get("idlePolicy") is not None:
        import capo_lambda_microvms.types.idle_policy

        out["idle_policy"] = capo_lambda_microvms.types.idle_policy.deserialize_json(
            data["idlePolicy"]
        )
    if data.get("maximumDurationInSeconds") is not None:
        out["maximum_duration_in_seconds"] = data["maximumDurationInSeconds"]
    else:
        raise DeserializationError(
            "RunMicrovmResponse.maximum_duration_in_seconds required"
        )
    if data.get("startedAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["started_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["startedAt"]
            )
        )
    else:
        raise DeserializationError("RunMicrovmResponse.started_at required")
    if data.get("terminatedAt") is not None:
        import capo_lambda_microvms.types._prelude.timestamp

        out["terminated_at"] = (
            capo_lambda_microvms.types._prelude.timestamp.deserialize_json(
                data["terminatedAt"]
            )
        )
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
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
    return out
