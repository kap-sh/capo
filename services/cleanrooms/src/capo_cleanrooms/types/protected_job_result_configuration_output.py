"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobResultConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_job_output_configuration_output


class ProtectedJobResultConfigurationOutput(TypedDict, closed=True):
    output_configuration: "capo_cleanrooms.types.protected_job_output_configuration_output.ProtectedJobOutputConfigurationOutput"
    """<p>The output configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedJobResultConfigurationOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_job_output_configuration_output

    out["outputConfiguration"] = (
        capo_cleanrooms.types.protected_job_output_configuration_output.serialize_json(
            value["output_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProtectedJobResultConfigurationOutput:
    out: ProtectedJobResultConfigurationOutput = {}  # type: ignore[typeddict-item]
    if data.get("outputConfiguration") is not None:
        import capo_cleanrooms.types.protected_job_output_configuration_output

        out["output_configuration"] = (
            capo_cleanrooms.types.protected_job_output_configuration_output.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        import capo_cleanrooms.types._unknown

        out["output_configuration"] = capo_cleanrooms.types._unknown.UnknownUnionMember(
            ""
        )
    return out
