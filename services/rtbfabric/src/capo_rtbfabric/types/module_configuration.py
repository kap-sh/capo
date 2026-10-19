"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ModuleConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rtbfabric.types.flow_module_name
    import capo_rtbfabric.types.flow_module_name_list
    import capo_rtbfabric.types.module_parameters
    import capo_rtbfabric.types.version


class ModuleConfiguration(TypedDict, closed=True):
    version: NotRequired["capo_rtbfabric.types.version.Version"]
    """<p>The version of the module.</p>"""
    name: "capo_rtbfabric.types.flow_module_name.FlowModuleName"
    """<p>The name of the module.</p>"""
    depends_on: NotRequired[
        "capo_rtbfabric.types.flow_module_name_list.FlowModuleNameList"
    ]
    """<p>The dependencies of the module.</p>"""
    module_parameters: NotRequired[
        "capo_rtbfabric.types.module_parameters.ModuleParameters"
    ]
    """<p>Describes the parameters of a module.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModuleConfiguration) -> dict:
    out: dict = {}
    if "version" in value:
        out["version"] = value["version"]
    out["name"] = value["name"]
    if "depends_on" in value:
        import capo_rtbfabric.types.flow_module_name_list

        out["dependsOn"] = capo_rtbfabric.types.flow_module_name_list.serialize_json(
            value["depends_on"]
        )
    if "module_parameters" in value:
        import capo_rtbfabric.types.module_parameters

        out["moduleParameters"] = capo_rtbfabric.types.module_parameters.serialize_json(
            value["module_parameters"]
        )
    return out


def deserialize_json(data: dict) -> ModuleConfiguration:
    out: ModuleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("dependsOn") is not None:
        import capo_rtbfabric.types.flow_module_name_list

        out["depends_on"] = capo_rtbfabric.types.flow_module_name_list.deserialize_json(
            data["dependsOn"]
        )
    if data.get("moduleParameters") is not None:
        import capo_rtbfabric.types.module_parameters

        out["module_parameters"] = (
            capo_rtbfabric.types.module_parameters.deserialize_json(
                data["moduleParameters"]
            )
        )
    return out
