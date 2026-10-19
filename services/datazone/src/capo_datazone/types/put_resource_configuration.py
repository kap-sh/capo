"""Generated from Smithy shape ``com.amazonaws.datazone#PutResourceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.region_name
    import capo_datazone.types.resource_configuration_parameter_map


class PutResourceConfiguration(TypedDict, closed=True):
    name: "str"
    """<p>The name of the resource configuration.</p>"""
    description: NotRequired["str"]
    """<p>The description of the resource configuration.</p>"""
    region: "capo_datazone.types.region_name.RegionName"
    """<p>The Amazon Web Services Region of the resource configuration.</p>"""
    parameters: "capo_datazone.types.resource_configuration_parameter_map.ResourceConfigurationParameterMap"
    """<p>The parameters of the resource configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutResourceConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["region"] = value["region"]
    import capo_datazone.types.resource_configuration_parameter_map

    out["parameters"] = (
        capo_datazone.types.resource_configuration_parameter_map.serialize_json(
            value["parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutResourceConfiguration:
    out: PutResourceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("region") is not None:
        out["region"] = data["region"]
    else:
        out["region"] = ""
    if data.get("parameters") is not None:
        import capo_datazone.types.resource_configuration_parameter_map

        out["parameters"] = (
            capo_datazone.types.resource_configuration_parameter_map.deserialize_json(
                data["parameters"]
            )
        )
    else:
        out["parameters"] = {}
    return out
