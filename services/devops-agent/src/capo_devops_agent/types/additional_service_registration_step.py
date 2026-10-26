"""Generated from Smithy shape ``com.amazonaws.devopsagent#AdditionalServiceRegistrationStep``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError, SerializationError
from capo_devops_agent.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_devops_agent.types.o_auth_additional_step_details


class _AdditionalServiceRegistrationStep_oauth(TypedDict, closed=True):
    oauth: "capo_devops_agent.types.o_auth_additional_step_details.OAuthAdditionalStepDetails"


AdditionalServiceRegistrationStep: TypeAlias = (
    _AdditionalServiceRegistrationStep_oauth | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AdditionalServiceRegistrationStep) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AdditionalServiceRegistrationStep: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "oauth" in value:
        import capo_devops_agent.types.o_auth_additional_step_details

        return {
            "oauth": capo_devops_agent.types.o_auth_additional_step_details.serialize_json(
                value["oauth"]
            )
        }
    else:
        raise SerializationError(
            "AdditionalServiceRegistrationStep: no variant present"
        )


def deserialize_json(data: dict) -> AdditionalServiceRegistrationStep:
    if data.get("oauth") is not None:
        import capo_devops_agent.types.o_auth_additional_step_details

        return {
            "oauth": capo_devops_agent.types.o_auth_additional_step_details.deserialize_json(
                data["oauth"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "AdditionalServiceRegistrationStep: no recognized variant key"
        )
