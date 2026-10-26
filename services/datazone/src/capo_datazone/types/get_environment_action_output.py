"""Generated from Smithy shape ``com.amazonaws.datazone#GetEnvironmentActionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.action_parameters
    import capo_datazone.types.domain_id
    import capo_datazone.types.environment_action_id
    import capo_datazone.types.environment_id


class GetEnvironmentActionOutput(TypedDict, closed=True):
    domain_id: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the Amazon DataZone domain in which the environment action lives.</p>"""
    environment_id: "capo_datazone.types.environment_id.EnvironmentId"
    """<p>The environment ID of the environment action.</p>"""
    id: "capo_datazone.types.environment_action_id.EnvironmentActionId"
    """<p>The ID of the environment action.</p>"""
    name: "str"
    """<p>The name of the environment action.</p>"""
    parameters: "capo_datazone.types.action_parameters.ActionParameters"
    """<p>The parameters of the environment action.</p>"""
    description: NotRequired["str"]
    """<p>The description of the environment action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnvironmentActionOutput) -> dict:
    out: dict = {}
    out["domainId"] = value["domain_id"]
    out["environmentId"] = value["environment_id"]
    out["id"] = value["id"]
    out["name"] = value["name"]
    import capo_datazone.types.action_parameters

    out["parameters"] = capo_datazone.types.action_parameters.serialize_json(
        value["parameters"]
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> GetEnvironmentActionOutput:
    out: GetEnvironmentActionOutput = {}  # type: ignore[typeddict-item]
    if data.get("domainId") is not None:
        out["domain_id"] = data["domainId"]
    else:
        out["domain_id"] = ""
    if data.get("environmentId") is not None:
        out["environment_id"] = data["environmentId"]
    else:
        out["environment_id"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("parameters") is not None:
        import capo_datazone.types.action_parameters

        out["parameters"] = capo_datazone.types.action_parameters.deserialize_json(
            data["parameters"]
        )
    else:
        out["parameters"] = {"$unknown": {"name": ""}}
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
