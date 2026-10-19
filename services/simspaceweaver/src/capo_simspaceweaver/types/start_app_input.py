"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#StartAppInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.client_token
    import capo_simspaceweaver.types.description
    import capo_simspaceweaver.types.launch_overrides
    import capo_simspaceweaver.types.sim_space_weaver_resource_name


class StartAppInput(TypedDict, closed=True):
    client_token: NotRequired["capo_simspaceweaver.types.client_token.ClientToken"]
    """<p>A value that you provide to ensure that repeated calls to this API operation using the same parameters complete only once. A <code>ClientToken</code> is also known as an <i>idempotency token</i>. A <code>ClientToken</code> expires after 24 hours.</p>"""
    simulation: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the simulation of the app.</p>"""
    domain: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the domain of the app.</p>"""
    name: "capo_simspaceweaver.types.sim_space_weaver_resource_name.SimSpaceWeaverResourceName"
    """<p>The name of the app.</p>"""
    description: NotRequired["capo_simspaceweaver.types.description.Description"]
    """<p>The description of the app.</p>"""
    launch_overrides: NotRequired[
        "capo_simspaceweaver.types.launch_overrides.LaunchOverrides"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: StartAppInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["Simulation"] = value["simulation"]
    out["Domain"] = value["domain"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "launch_overrides" in value:
        import capo_simspaceweaver.types.launch_overrides

        out["LaunchOverrides"] = (
            capo_simspaceweaver.types.launch_overrides.serialize_json(
                value["launch_overrides"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartAppInput:
    out: StartAppInput = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Simulation") is not None:
        out["simulation"] = data["Simulation"]
    else:
        out["simulation"] = ""
    if data.get("Domain") is not None:
        out["domain"] = data["Domain"]
    else:
        out["domain"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("LaunchOverrides") is not None:
        import capo_simspaceweaver.types.launch_overrides

        out["launch_overrides"] = (
            capo_simspaceweaver.types.launch_overrides.deserialize_json(
                data["LaunchOverrides"]
            )
        )
    return out


def redact_sensitive(value: StartAppInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "client_token" in value:
        out["client_token"] = "*** Sensitive Data Redacted ***"
    return out
