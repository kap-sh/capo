"""Generated from Smithy shape ``com.amazonaws.proton#CancelServicePipelineDeploymentOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.service_pipeline


class CancelServicePipelineDeploymentOutput(TypedDict, closed=True):
    pipeline: "capo_proton.types.service_pipeline.ServicePipeline"
    """<p>The service pipeline detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelServicePipelineDeploymentOutput) -> dict:
    out: dict = {}
    import capo_proton.types.service_pipeline

    out["pipeline"] = capo_proton.types.service_pipeline.serialize_aws_json_1_0(
        value["pipeline"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelServicePipelineDeploymentOutput:
    out: CancelServicePipelineDeploymentOutput = {}  # type: ignore[typeddict-item]
    if data.get("pipeline") is not None:
        import capo_proton.types.service_pipeline

        out["pipeline"] = capo_proton.types.service_pipeline.deserialize_aws_json_1_0(
            data["pipeline"]
        )
    else:
        raise DeserializationError(
            "CancelServicePipelineDeploymentOutput.pipeline required"
        )
    return out


def redact_sensitive(value: CancelServicePipelineDeploymentOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "pipeline" in value:
        import capo_proton.types.service_pipeline

        out["pipeline"] = capo_proton.types.service_pipeline.redact_sensitive(
            value["pipeline"]
        )
    return out
