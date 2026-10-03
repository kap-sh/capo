"""Generated from Smithy shape ``com.amazonaws.lambda#PublishLayerVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda.types.compatible_architectures
    import capo_lambda.types.compatible_runtimes
    import capo_lambda.types.description
    import capo_lambda.types.layer_name
    import capo_lambda.types.layer_version_content_input
    import capo_lambda.types.license_info


class PublishLayerVersionRequest(TypedDict, closed=True):
    layer_name: "capo_lambda.types.layer_name.LayerName"
    """<p>The name or Amazon Resource Name (ARN) of the layer.</p>"""
    description: NotRequired["capo_lambda.types.description.Description"]
    """<p>The description of the version.</p>"""
    content: "capo_lambda.types.layer_version_content_input.LayerVersionContentInput"
    """<p>The function layer archive.</p>"""
    compatible_architectures: NotRequired[
        "capo_lambda.types.compatible_architectures.CompatibleArchitectures"
    ]
    """<p>A list of compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html">instruction set architectures</a>.</p>"""
    compatible_runtimes: NotRequired[
        "capo_lambda.types.compatible_runtimes.CompatibleRuntimes"
    ]
    """<p>A list of compatible <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html">function runtimes</a>. Used for filtering with <a>ListLayers</a> and <a>ListLayerVersions</a>.</p> <p>The following list includes deprecated runtimes. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy">Runtime deprecation policy</a>.</p>"""
    license_info: NotRequired["capo_lambda.types.license_info.LicenseInfo"]
    """<p>The layer's software license. It can be any of the following:</p> <ul> <li> <p>An <a href="https://spdx.org/licenses/">SPDX license identifier</a>. For example, <code>MIT</code>.</p> </li> <li> <p>The URL of a license hosted on the internet. For example, <code>https://opensource.org/licenses/MIT</code>.</p> </li> <li> <p>The full text of the license.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PublishLayerVersionRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    import capo_lambda.types.layer_version_content_input

    out["Content"] = capo_lambda.types.layer_version_content_input.serialize_json(
        value["content"]
    )
    if "compatible_architectures" in value:
        import capo_lambda.types.compatible_architectures

        out["CompatibleArchitectures"] = (
            capo_lambda.types.compatible_architectures.serialize_json(
                value["compatible_architectures"]
            )
        )
    if "compatible_runtimes" in value:
        import capo_lambda.types.compatible_runtimes

        out["CompatibleRuntimes"] = (
            capo_lambda.types.compatible_runtimes.serialize_json(
                value["compatible_runtimes"]
            )
        )
    if "license_info" in value:
        out["LicenseInfo"] = value["license_info"]
    return out


def deserialize_json(data: dict) -> PublishLayerVersionRequest:
    out: PublishLayerVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Content") is not None:
        import capo_lambda.types.layer_version_content_input

        out["content"] = capo_lambda.types.layer_version_content_input.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("PublishLayerVersionRequest.content required")
    if data.get("CompatibleArchitectures") is not None:
        import capo_lambda.types.compatible_architectures

        out["compatible_architectures"] = (
            capo_lambda.types.compatible_architectures.deserialize_json(
                data["CompatibleArchitectures"]
            )
        )
    if data.get("CompatibleRuntimes") is not None:
        import capo_lambda.types.compatible_runtimes

        out["compatible_runtimes"] = (
            capo_lambda.types.compatible_runtimes.deserialize_json(
                data["CompatibleRuntimes"]
            )
        )
    if data.get("LicenseInfo") is not None:
        out["license_info"] = data["LicenseInfo"]
    return out
