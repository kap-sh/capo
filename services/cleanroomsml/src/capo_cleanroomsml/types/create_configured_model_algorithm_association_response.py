"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateConfiguredModelAlgorithmAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn


class CreateConfiguredModelAlgorithmAssociationResponse(TypedDict, closed=True):
    configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredModelAlgorithmAssociationResponse) -> dict:
    out: dict = {}
    out["configuredModelAlgorithmAssociationArn"] = value[
        "configured_model_algorithm_association_arn"
    ]
    return out


def deserialize_json(data: dict) -> CreateConfiguredModelAlgorithmAssociationResponse:
    out: CreateConfiguredModelAlgorithmAssociationResponse = {}  # type: ignore[typeddict-item]
    if data.get("configuredModelAlgorithmAssociationArn") is not None:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    else:
        out["configured_model_algorithm_association_arn"] = ""
    return out
