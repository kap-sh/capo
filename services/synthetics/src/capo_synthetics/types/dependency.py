"""Generated from Smithy shape ``com.amazonaws.synthetics#Dependency``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_synthetics.errors import DeserializationError

if TYPE_CHECKING:
    import capo_synthetics.types.dependency_type
    import capo_synthetics.types.string


class Dependency(TypedDict, closed=True):
    type: NotRequired["capo_synthetics.types.dependency_type.DependencyType"]
    """<p>The type of dependency. Valid value is <code>LambdaLayer</code>.</p>"""
    reference: "capo_synthetics.types.string.String"
    """<p>The dependency reference. For Lambda layers, this is the ARN of the Lambda layer. For more information about Lambda ARN format, see <a href="https://docs.aws.amazon.com/lambda/latest/api/API_Layer.html">Lambda</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dependency) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_synthetics.types.dependency_type

        out["Type"] = capo_synthetics.types.dependency_type.serialize_json(
            value["type"]
        )
    out["Reference"] = value["reference"]
    return out


def deserialize_json(data: dict) -> Dependency:
    out: Dependency = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        import capo_synthetics.types.dependency_type

        out["type"] = capo_synthetics.types.dependency_type.deserialize_json(
            data["Type"]
        )
    if data.get("Reference") is not None:
        out["reference"] = data["Reference"]
    else:
        raise DeserializationError("Dependency.reference required")
    return out
