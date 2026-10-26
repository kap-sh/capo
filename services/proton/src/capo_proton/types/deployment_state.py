"""Generated from Smithy shape ``com.amazonaws.proton#DeploymentState``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError, SerializationError
from capo_proton.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_proton.types.component_state
    import capo_proton.types.environment_state
    import capo_proton.types.service_instance_state
    import capo_proton.types.service_pipeline_state


class _DeploymentState_serviceInstance(TypedDict, closed=True):
    serviceInstance: "capo_proton.types.service_instance_state.ServiceInstanceState"


class _DeploymentState_environment(TypedDict, closed=True):
    environment: "capo_proton.types.environment_state.EnvironmentState"


class _DeploymentState_servicePipeline(TypedDict, closed=True):
    servicePipeline: "capo_proton.types.service_pipeline_state.ServicePipelineState"


class _DeploymentState_component(TypedDict, closed=True):
    component: "capo_proton.types.component_state.ComponentState"


DeploymentState: TypeAlias = (
    _DeploymentState_serviceInstance
    | _DeploymentState_environment
    | _DeploymentState_servicePipeline
    | _DeploymentState_component
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeploymentState) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DeploymentState: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "serviceInstance" in value:
        import capo_proton.types.service_instance_state

        return {
            "serviceInstance": capo_proton.types.service_instance_state.serialize_aws_json_1_0(
                value["serviceInstance"]
            )
        }
    elif "environment" in value:
        import capo_proton.types.environment_state

        return {
            "environment": capo_proton.types.environment_state.serialize_aws_json_1_0(
                value["environment"]
            )
        }
    elif "servicePipeline" in value:
        import capo_proton.types.service_pipeline_state

        return {
            "servicePipeline": capo_proton.types.service_pipeline_state.serialize_aws_json_1_0(
                value["servicePipeline"]
            )
        }
    elif "component" in value:
        import capo_proton.types.component_state

        return {
            "component": capo_proton.types.component_state.serialize_aws_json_1_0(
                value["component"]
            )
        }
    else:
        raise SerializationError("DeploymentState: no variant present")


def deserialize_aws_json_1_0(data: dict) -> DeploymentState:
    if data.get("serviceInstance") is not None:
        import capo_proton.types.service_instance_state

        return {
            "serviceInstance": capo_proton.types.service_instance_state.deserialize_aws_json_1_0(
                data["serviceInstance"]
            )
        }
    elif data.get("environment") is not None:
        import capo_proton.types.environment_state

        return {
            "environment": capo_proton.types.environment_state.deserialize_aws_json_1_0(
                data["environment"]
            )
        }
    elif data.get("servicePipeline") is not None:
        import capo_proton.types.service_pipeline_state

        return {
            "servicePipeline": capo_proton.types.service_pipeline_state.deserialize_aws_json_1_0(
                data["servicePipeline"]
            )
        }
    elif data.get("component") is not None:
        import capo_proton.types.component_state

        return {
            "component": capo_proton.types.component_state.deserialize_aws_json_1_0(
                data["component"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DeploymentState: no recognized variant key")


def redact_sensitive(value: DeploymentState) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "serviceInstance" in value:
        import capo_proton.types.service_instance_state

        out["serviceInstance"] = (
            capo_proton.types.service_instance_state.redact_sensitive(
                value["serviceInstance"]
            )
        )
    if "environment" in value:
        import capo_proton.types.environment_state

        out["environment"] = capo_proton.types.environment_state.redact_sensitive(
            value["environment"]
        )
    if "servicePipeline" in value:
        import capo_proton.types.service_pipeline_state

        out["servicePipeline"] = (
            capo_proton.types.service_pipeline_state.redact_sensitive(
                value["servicePipeline"]
            )
        )
    if "component" in value:
        import capo_proton.types.component_state

        out["component"] = capo_proton.types.component_state.redact_sensitive(
            value["component"]
        )
    return out
