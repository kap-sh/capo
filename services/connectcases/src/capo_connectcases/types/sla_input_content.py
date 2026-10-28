"""Generated from Smithy shape ``com.amazonaws.connectcases#SlaInputContent``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError, SerializationError
from capo_connectcases.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connectcases.types.sla_input_configuration


class SlaInputContentSlaInputConfigurationMember(TypedDict, closed=True):
    slaInputConfiguration: (
        "capo_connectcases.types.sla_input_configuration.SlaInputConfiguration"
    )


SlaInputContent: TypeAlias = (
    SlaInputContentSlaInputConfigurationMember | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SlaInputContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SlaInputContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "slaInputConfiguration" in value:
        import capo_connectcases.types.sla_input_configuration

        return {
            "slaInputConfiguration": capo_connectcases.types.sla_input_configuration.serialize_json(
                value["slaInputConfiguration"]
            )
        }
    else:
        raise SerializationError("SlaInputContent: no variant present")


def deserialize_json(data: dict) -> SlaInputContent:
    if data.get("slaInputConfiguration") is not None:
        import capo_connectcases.types.sla_input_configuration

        return {
            "slaInputConfiguration": capo_connectcases.types.sla_input_configuration.deserialize_json(
                data["slaInputConfiguration"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SlaInputContent: no recognized variant key")


def redact_sensitive(value: SlaInputContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "slaInputConfiguration" in value:
        import capo_connectcases.types.sla_input_configuration

        out["slaInputConfiguration"] = (
            capo_connectcases.types.sla_input_configuration.redact_sensitive(
                value["slaInputConfiguration"]
            )
        )
    return out
