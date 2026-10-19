"""Generated from Smithy shape ``com.amazonaws.ssmincidents#Integration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_ssm_incidents.errors import DeserializationError, SerializationError
from capo_ssm_incidents.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_ssm_incidents.types.pager_duty_configuration


class _Integration_pagerDutyConfiguration(TypedDict, closed=True):
    pagerDutyConfiguration: (
        "capo_ssm_incidents.types.pager_duty_configuration.PagerDutyConfiguration"
    )


Integration: TypeAlias = _Integration_pagerDutyConfiguration | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: Integration) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"Integration: cannot serialize unknown variant {value.name!r}"
        )
    elif "pagerDutyConfiguration" in value:
        import capo_ssm_incidents.types.pager_duty_configuration

        return {
            "pagerDutyConfiguration": capo_ssm_incidents.types.pager_duty_configuration.serialize_json(
                value["pagerDutyConfiguration"]
            )
        }
    else:
        raise SerializationError("Integration: no variant present")


def deserialize_json(data: dict) -> Integration:
    if data.get("pagerDutyConfiguration") is not None:
        import capo_ssm_incidents.types.pager_duty_configuration

        return {
            "pagerDutyConfiguration": capo_ssm_incidents.types.pager_duty_configuration.deserialize_json(
                data["pagerDutyConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("Integration: no recognized variant key")
