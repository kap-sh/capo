"""Generated from Smithy shape ``com.amazonaws.devopsagent#DynatraceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_agent.types.dynatrace_resource_list


class DynatraceConfiguration(TypedDict, closed=True):
    env_id: "str"
    """<p>Dynatrace environment id</p>"""
    resources: NotRequired[
        "capo_devops_agent.types.dynatrace_resource_list.DynatraceResourceList"
    ]
    """<p>List of Dynatrace resources to monitor</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DynatraceConfiguration) -> dict:
    out: dict = {}
    out["envId"] = value["env_id"]
    if "resources" in value:
        import capo_devops_agent.types.dynatrace_resource_list

        out["resources"] = (
            capo_devops_agent.types.dynatrace_resource_list.serialize_json(
                value["resources"]
            )
        )
    return out


def deserialize_json(data: dict) -> DynatraceConfiguration:
    out: DynatraceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("envId") is not None:
        out["env_id"] = data["envId"]
    else:
        out["env_id"] = ""
    if data.get("resources") is not None:
        import capo_devops_agent.types.dynatrace_resource_list

        out["resources"] = (
            capo_devops_agent.types.dynatrace_resource_list.deserialize_json(
                data["resources"]
            )
        )
    return out
