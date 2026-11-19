"""Generated from Smithy shape ``com.amazonaws.lambdacore#Compatibility``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda_core.types.compatibility_policy
    import capo_lambda_core.types.integration_model_list
    import capo_lambda_core.types.runtime_architecture_list


class Compatibility(TypedDict, closed=True):
    integration_models: NotRequired[
        "capo_lambda_core.types.integration_model_list.IntegrationModelList"
    ]
    """Supported integration models for the runtime version."""
    architectures: NotRequired[
        "capo_lambda_core.types.runtime_architecture_list.RuntimeArchitectureList"
    ]
    """Supported architectures for the runtime version."""
    managed_instances: NotRequired[
        "capo_lambda_core.types.compatibility_policy.CompatibilityPolicy"
    ]
    """Whether the runtime version is compatible with managed instances."""


# --- restJson1 ser/de ---
def serialize_json(value: Compatibility) -> dict:
    out: dict = {}
    if "integration_models" in value:
        import capo_lambda_core.types.integration_model_list

        out["IntegrationModels"] = (
            capo_lambda_core.types.integration_model_list.serialize_json(
                value["integration_models"]
            )
        )
    if "architectures" in value:
        import capo_lambda_core.types.runtime_architecture_list

        out["Architectures"] = (
            capo_lambda_core.types.runtime_architecture_list.serialize_json(
                value["architectures"]
            )
        )
    if "managed_instances" in value:
        import capo_lambda_core.types.compatibility_policy

        out["ManagedInstances"] = (
            capo_lambda_core.types.compatibility_policy.serialize_json(
                value["managed_instances"]
            )
        )
    return out


def deserialize_json(data: dict) -> Compatibility:
    out: Compatibility = {}  # type: ignore[typeddict-item]
    if data.get("IntegrationModels") is not None:
        import capo_lambda_core.types.integration_model_list

        out["integration_models"] = (
            capo_lambda_core.types.integration_model_list.deserialize_json(
                data["IntegrationModels"]
            )
        )
    if data.get("Architectures") is not None:
        import capo_lambda_core.types.runtime_architecture_list

        out["architectures"] = (
            capo_lambda_core.types.runtime_architecture_list.deserialize_json(
                data["Architectures"]
            )
        )
    if data.get("ManagedInstances") is not None:
        import capo_lambda_core.types.compatibility_policy

        out["managed_instances"] = (
            capo_lambda_core.types.compatibility_policy.deserialize_json(
                data["ManagedInstances"]
            )
        )
    return out
