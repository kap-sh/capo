"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobResultConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_output_configuration_input


class ProtectedJobResultConfigurationInput(TypedDict, closed=True):
    output_configuration: "capo_cleanrooms.types.protected_job_output_configuration_input.ProtectedJobOutputConfigurationInput"
    """<p> The output configuration for a protected job result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobResultConfigurationInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_job_output_configuration_input

    out["outputConfiguration"] = (
        capo_cleanrooms.types.protected_job_output_configuration_input.serialize_json(
            value["output_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProtectedJobResultConfigurationInput:
    out: ProtectedJobResultConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("outputConfiguration") is not None:
        import capo_cleanrooms.types.protected_job_output_configuration_input

        out["output_configuration"] = (
            capo_cleanrooms.types.protected_job_output_configuration_input.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        out["output_configuration"] = {"$unknown": {"name": ""}}
    return out
