"""Generated from Smithy shape ``com.amazonaws.ssmincidents#FindingDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.cloud_formation_stack_update
    import capo_ssm_incidents.types.code_deploy_deployment


class _FindingDetails_codeDeployDeployment(TypedDict, closed=True):
    codeDeployDeployment: (
        "capo_ssm_incidents.types.code_deploy_deployment.CodeDeployDeployment"
    )


class _FindingDetails_cloudFormationStackUpdate(TypedDict, closed=True):
    cloudFormationStackUpdate: "capo_ssm_incidents.types.cloud_formation_stack_update.CloudFormationStackUpdate"


FindingDetails: TypeAlias = (
    _FindingDetails_codeDeployDeployment
    | _FindingDetails_cloudFormationStackUpdate
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FindingDetails) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"FindingDetails: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "codeDeployDeployment" in value:
        import capo_ssm_incidents.types.code_deploy_deployment

        return {
            "codeDeployDeployment": capo_ssm_incidents.types.code_deploy_deployment.serialize_json(
                value["codeDeployDeployment"]
            )
        }
    elif "cloudFormationStackUpdate" in value:
        import capo_ssm_incidents.types.cloud_formation_stack_update

        return {
            "cloudFormationStackUpdate": capo_ssm_incidents.types.cloud_formation_stack_update.serialize_json(
                value["cloudFormationStackUpdate"]
            )
        }
    else:
        raise SerializationError("FindingDetails: no variant present")


def deserialize_json(data: dict) -> FindingDetails:
    if data.get("codeDeployDeployment") is not None:
        import capo_ssm_incidents.types.code_deploy_deployment

        return {
            "codeDeployDeployment": capo_ssm_incidents.types.code_deploy_deployment.deserialize_json(
                data["codeDeployDeployment"]
            )
        }
    elif data.get("cloudFormationStackUpdate") is not None:
        import capo_ssm_incidents.types.cloud_formation_stack_update

        return {
            "cloudFormationStackUpdate": capo_ssm_incidents.types.cloud_formation_stack_update.deserialize_json(
                data["cloudFormationStackUpdate"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("FindingDetails: no recognized variant key")
