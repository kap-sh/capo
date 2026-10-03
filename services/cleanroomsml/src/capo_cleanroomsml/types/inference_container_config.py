"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InferenceContainerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.algorithm_image


class InferenceContainerConfig(TypedDict, closed=True):
    image_uri: "capo_cleanroomsml.types.algorithm_image.AlgorithmImage"
    """<p>The registry path of the docker image that contains the inference algorithm. Clean Rooms ML currently only supports the <code>registry/repository[:tag]</code> image path format. For more information about using images in Clean Rooms ML, see the <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AlgorithmSpecification.html#sagemaker-Type-AlgorithmSpecification-TrainingImage">Sagemaker API reference</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InferenceContainerConfig) -> dict:
    out: dict = {}
    out["imageUri"] = value["image_uri"]
    return out


def deserialize_json(data: dict) -> InferenceContainerConfig:
    out: InferenceContainerConfig = {}  # type: ignore[typeddict-item]
    if data.get("imageUri") is not None:
        out["image_uri"] = data["imageUri"]
    else:
        raise DeserializationError("InferenceContainerConfig.image_uri required")
    return out
