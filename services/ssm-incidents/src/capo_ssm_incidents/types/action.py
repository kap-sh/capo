"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Action``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.ssm_automation


class _Action_ssmAutomation(TypedDict, closed=True):
    ssmAutomation: "capo_ssm_incidents.types.ssm_automation.SsmAutomation"


Action: TypeAlias = _Action_ssmAutomation | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Action) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Action: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "ssmAutomation" in value:
        import capo_ssm_incidents.types.ssm_automation

        return {
            "ssmAutomation": capo_ssm_incidents.types.ssm_automation.serialize_json(
                value["ssmAutomation"]
            )
        }
    else:
        raise SerializationError("Action: no variant present")


def deserialize_json(data: dict) -> Action:
    if data.get("ssmAutomation") is not None:
        import capo_ssm_incidents.types.ssm_automation

        return {
            "ssmAutomation": capo_ssm_incidents.types.ssm_automation.deserialize_json(
                data["ssmAutomation"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Action: no recognized variant key")
