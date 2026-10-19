"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#StateTemplateUpdateStrategy``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError
from capo_iotfleetwise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotfleetwise.types.on_change_state_template_update_strategy
    import capo_iotfleetwise.types.periodic_state_template_update_strategy


class _StateTemplateUpdateStrategy_periodic(TypedDict, closed=True):
    periodic: "capo_iotfleetwise.types.periodic_state_template_update_strategy.PeriodicStateTemplateUpdateStrategy"


class _StateTemplateUpdateStrategy_onChange(TypedDict, closed=True):
    onChange: "capo_iotfleetwise.types.on_change_state_template_update_strategy.OnChangeStateTemplateUpdateStrategy"


StateTemplateUpdateStrategy: TypeAlias = (
    _StateTemplateUpdateStrategy_periodic
    | _StateTemplateUpdateStrategy_onChange
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StateTemplateUpdateStrategy) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"StateTemplateUpdateStrategy: cannot serialize unknown variant {value.name!r}"
        )
    elif "periodic" in value:
        import capo_iotfleetwise.types.periodic_state_template_update_strategy

        return {
            "periodic": capo_iotfleetwise.types.periodic_state_template_update_strategy.serialize_aws_json_1_0(
                value["periodic"]
            )
        }
    elif "onChange" in value:
        import capo_iotfleetwise.types.on_change_state_template_update_strategy

        return {
            "onChange": capo_iotfleetwise.types.on_change_state_template_update_strategy.serialize_aws_json_1_0(
                value["onChange"]
            )
        }
    else:
        raise SerializationError("StateTemplateUpdateStrategy: no variant present")


def deserialize_aws_json_1_0(data: dict) -> StateTemplateUpdateStrategy:
    if data.get("periodic") is not None:
        import capo_iotfleetwise.types.periodic_state_template_update_strategy

        return {
            "periodic": capo_iotfleetwise.types.periodic_state_template_update_strategy.deserialize_aws_json_1_0(
                data["periodic"]
            )
        }
    elif data.get("onChange") is not None:
        import capo_iotfleetwise.types.on_change_state_template_update_strategy

        return {
            "onChange": capo_iotfleetwise.types.on_change_state_template_update_strategy.deserialize_aws_json_1_0(
                data["onChange"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "StateTemplateUpdateStrategy: no recognized variant key"
        )
