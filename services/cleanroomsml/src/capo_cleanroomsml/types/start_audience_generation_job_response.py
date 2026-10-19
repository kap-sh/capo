"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StartAudienceGenerationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_generation_job_arn


class StartAudienceGenerationJobResponse(TypedDict, closed=True):
    audience_generation_job_arn: (
        "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    )
    """<p>The Amazon Resource Name (ARN) of the audience generation job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAudienceGenerationJobResponse) -> dict:
    out: dict = {}
    out["audienceGenerationJobArn"] = value["audience_generation_job_arn"]
    return out


def deserialize_json(data: dict) -> StartAudienceGenerationJobResponse:
    out: StartAudienceGenerationJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("audienceGenerationJobArn") is not None:
        out["audience_generation_job_arn"] = data["audienceGenerationJobArn"]
    else:
        out["audience_generation_job_arn"] = ""
    return out
