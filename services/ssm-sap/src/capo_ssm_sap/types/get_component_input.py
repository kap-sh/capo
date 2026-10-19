"""Generated from Smithy shape ``com.amazonaws.ssmsap#GetComponentInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm_sap.types.application_id
    import capo_ssm_sap.types.component_id


class GetComponentInput(TypedDict, closed=True):
    application_id: "capo_ssm_sap.types.application_id.ApplicationId"
    """<p>The ID of the application.</p>"""
    component_id: "capo_ssm_sap.types.component_id.ComponentId"
    """<p>The ID of the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetComponentInput) -> dict:
    out: dict = {}
    out["ApplicationId"] = value["application_id"]
    out["ComponentId"] = value["component_id"]
    return out


def deserialize_json(data: dict) -> GetComponentInput:
    out: GetComponentInput = {}  # type: ignore[typeddict-item]
    if data.get("ApplicationId") is not None:
        out["application_id"] = data["ApplicationId"]
    else:
        out["application_id"] = ""
    if data.get("ComponentId") is not None:
        out["component_id"] = data["ComponentId"]
    else:
        out["component_id"] = ""
    return out
