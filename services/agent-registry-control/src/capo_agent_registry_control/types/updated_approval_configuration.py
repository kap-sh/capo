"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdatedApprovalConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_agent_registry_control.types.approval_configuration


class UpdatedApprovalConfiguration(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_agent_registry_control.types.approval_configuration.ApprovalConfiguration"
    ]
    """<p>The value to set for this field. Omit the wrapper to leave the field unchanged.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedApprovalConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_agent_registry_control.types.approval_configuration

        out["optionalValue"] = (
            capo_agent_registry_control.types.approval_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedApprovalConfiguration:
    out: UpdatedApprovalConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_agent_registry_control.types.approval_configuration

        out["optional_value"] = (
            capo_agent_registry_control.types.approval_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
