"""Generated from Smithy shape ``com.amazonaws.personalize#AlgorithmImage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.docker_uri
    import capo_personalize.types.name


class AlgorithmImage(TypedDict, closed=True):
    name: NotRequired["capo_personalize.types.name.Name"]
    """<p>The name of the algorithm image.</p>"""
    docker_uri: "capo_personalize.types.docker_uri.DockerURI"
    """<p>The URI of the Docker container for the algorithm image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlgorithmImage) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    out["dockerURI"] = value["docker_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AlgorithmImage:
    out: AlgorithmImage = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("dockerURI") is not None:
        out["docker_uri"] = data["dockerURI"]
    else:
        out["docker_uri"] = ""
    return out
