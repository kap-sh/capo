"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Condition``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import datetime

    import capo_ssm_incidents.types.attribute_value_list


class _Condition_before(TypedDict, closed=True):
    before: "datetime.datetime"


class _Condition_after(TypedDict, closed=True):
    after: "datetime.datetime"


class _Condition_equals(TypedDict, closed=True):
    equals: "capo_ssm_incidents.types.attribute_value_list.AttributeValueList"


Condition: TypeAlias = (
    _Condition_before | _Condition_after | _Condition_equals | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: Condition) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"Condition: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "before" in value:
        import capo_ssm_incidents.types._prelude.timestamp

        return {
            "before": capo_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["before"]
            )
        }
    elif "after" in value:
        import capo_ssm_incidents.types._prelude.timestamp

        return {
            "after": capo_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["after"]
            )
        }
    elif "equals" in value:
        import capo_ssm_incidents.types.attribute_value_list

        return {
            "equals": capo_ssm_incidents.types.attribute_value_list.serialize_json(
                value["equals"]
            )
        }
    else:
        raise SerializationError("Condition: no variant present")


def deserialize_json(data: dict) -> Condition:
    if data.get("before") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        return {
            "before": capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["before"]
            )
        }
    elif data.get("after") is not None:
        import capo_ssm_incidents.types._prelude.timestamp

        return {
            "after": capo_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["after"]
            )
        }
    elif data.get("equals") is not None:
        import capo_ssm_incidents.types.attribute_value_list

        return {
            "equals": capo_ssm_incidents.types.attribute_value_list.deserialize_json(
                data["equals"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("Condition: no recognized variant key")
