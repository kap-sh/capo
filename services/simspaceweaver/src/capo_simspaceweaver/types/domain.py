"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#Domain``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.lifecycle_management_strategy
    import capo_simspaceweaver.types.sim_space_weaver_resource_name


class Domain(TypedDict, closed=True):
    name: NotRequired[
        "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    ]
    """<p>The name of the domain.</p>"""
    lifecycle: NotRequired[
        "capo_simspaceweaver.types.lifecycle_management_strategy.LifecycleManagementStrategy"
    ]
    """<p>The type of lifecycle management for apps in the domain. Indicates whether apps in this domain are <i>managed</i> (SimSpace Weaver starts and stops the apps) or <i>unmanaged</i> (you must start and stop the apps).</p> <p class="title"> <b>Lifecycle types</b> </p> <ul> <li> <p> <code>PerWorker</code> – Managed: SimSpace Weaver starts one app on each worker.</p> </li> <li> <p> <code>BySpatialSubdivision</code> – Managed: SimSpace Weaver starts one app for each spatial partition.</p> </li> <li> <p> <code>ByRequest</code> – Unmanaged: You use the <code>StartApp</code> API to start the apps and use the <code>StopApp</code> API to stop the apps.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: Domain) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "lifecycle" in value:
        out["Lifecycle"] = value["lifecycle"]
    return out


def deserialize_json(data: dict) -> Domain:
    out: Domain = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Lifecycle") is not None:
        out["lifecycle"] = data["Lifecycle"]
    return out
