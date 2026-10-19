"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateConfiguredModelAlgorithmResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_arn


class CreateConfiguredModelAlgorithmResponse(TypedDict, closed=True):
    configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredModelAlgorithmResponse) -> dict:
    out: dict = {}
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    return out


def deserialize_json(data: dict) -> CreateConfiguredModelAlgorithmResponse:
    out: CreateConfiguredModelAlgorithmResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuredModelAlgorithmArn") is not None:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        out["configured_model_algorithm_arn"] = ""
    return out
