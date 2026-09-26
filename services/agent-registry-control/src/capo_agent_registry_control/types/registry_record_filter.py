"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#RegistryRecordFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.filter_values
    import capo_agent_registry_control.types.registry_record_filter_name


class RegistryRecordFilter(TypedDict, closed=True):
    name: "capo_agent_registry_control.types.registry_record_filter_name.RegistryRecordFilterName"
    """<p>The attribute to filter on</p>"""
    values: "capo_agent_registry_control.types.filter_values.FilterValues"
    """<p>The values to match for the attribute</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordFilter) -> dict:
    out: dict = {}
    import capo_agent_registry_control.types.registry_record_filter_name

    out["name"] = (
        capo_agent_registry_control.types.registry_record_filter_name.serialize_json(
            value["name"]
        )
    )
    import capo_agent_registry_control.types.filter_values

    out["values"] = capo_agent_registry_control.types.filter_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> RegistryRecordFilter:
    out: RegistryRecordFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_agent_registry_control.types.registry_record_filter_name

        out["name"] = (
            capo_agent_registry_control.types.registry_record_filter_name.deserialize_json(
                data["name"]
            )
        )
    else:
        raise DeserializationError("RegistryRecordFilter.name required")
    if data.get("values") is not None:
        import capo_agent_registry_control.types.filter_values

        out["values"] = (
            capo_agent_registry_control.types.filter_values.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("RegistryRecordFilter.values required")
    return out
