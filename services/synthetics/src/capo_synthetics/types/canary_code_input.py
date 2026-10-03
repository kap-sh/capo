"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryCodeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.blob
    import capo_synthetics.types.blueprint_types
    import capo_synthetics.types.code_handler
    import capo_synthetics.types.dependencies
    import capo_synthetics.types.string


class CanaryCodeInput(TypedDict, closed=True):
    s3_bucket: NotRequired["capo_synthetics.types.string.String"]
    """<p>If your canary script is located in Amazon S3, specify the bucket name here. Do not include <code>s3://</code> as the start of the bucket name.</p>"""
    s3_key: NotRequired["capo_synthetics.types.string.String"]
    """<p>The Amazon S3 key of your script. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingObjects.html">Working with Amazon S3 Objects</a>.</p>"""
    s3_version: NotRequired["capo_synthetics.types.string.String"]
    """<p>The Amazon S3 version ID of your script.</p>"""
    zip_file: NotRequired["capo_synthetics.types.blob.Blob"]
    """<p>If you input your canary script directly into the canary instead of referring to an Amazon S3 location, the value of this parameter is the base64-encoded contents of the .zip file that contains the script. It must be smaller than 225 Kb.</p> <p>For large canary scripts, we recommend that you use an Amazon S3 location instead of inputting it directly with this parameter.</p>"""
    handler: "capo_synthetics.types.code_handler.CodeHandler"
    """<p>The entry point to use for the source code when running the canary. For canaries that use the <code>syn-python-selenium-1.0</code> runtime or a <code>syn-nodejs.puppeteer</code> runtime earlier than <code>syn-nodejs.puppeteer-3.4</code>, the handler must be specified as <code> <i>fileName</i>.handler</code>. For <code>syn-python-selenium-1.1</code>, <code>syn-nodejs.puppeteer-3.4</code>, and later runtimes, the handler can be specified as <code> <i>fileName</i>.<i>functionName</i> </code>, or you can specify a folder where canary scripts reside as <code> <i>folder</i>/<i>fileName</i>.<i>functionName</i> </code>.</p> <p>This field is required when you don't specify <code>BlueprintTypes</code> and is not allowed when you specify <code>BlueprintTypes</code>.</p>"""
    blueprint_types: NotRequired["capo_synthetics.types.blueprint_types.BlueprintTypes"]
    """<p> <code>BlueprintTypes</code> is a list of templates that enable simplified canary creation. You can create canaries for common monitoring scenarios by providing only a JSON configuration file instead of writing custom scripts. The only supported value is <code>multi-checks</code>.</p> <p>Multi-checks monitors HTTP/DNS/SSL/TCP endpoints with built-in authentication schemes (Basic, API Key, OAuth, SigV4) and assertion capabilities. When you specify <code>BlueprintTypes</code>, the <code>Handler</code> field cannot be specified since the blueprint provides a pre-defined entry point.</p> <p> <code>BlueprintTypes</code> is supported only on canaries for syn-nodejs-3.0 runtime or later.</p>"""
    dependencies: NotRequired["capo_synthetics.types.dependencies.Dependencies"]
    """<p>A list of dependencies that should be used for running this canary. Specify the dependencies as a key-value pair, where the key is the type of dependency and the value is the dependency reference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryCodeInput) -> dict:
    out: dict = {}
    if "s3_bucket" in value:
        out["S3Bucket"] = value["s3_bucket"]
    if "s3_key" in value:
        out["S3Key"] = value["s3_key"]
    if "s3_version" in value:
        out["S3Version"] = value["s3_version"]
    if "zip_file" in value:
        import capo_synthetics.types.blob

        out["ZipFile"] = capo_synthetics.types.blob.serialize_json(value["zip_file"])
    out["Handler"] = value.get("handler", "")
    if "blueprint_types" in value:
        import capo_synthetics.types.blueprint_types

        out["BlueprintTypes"] = capo_synthetics.types.blueprint_types.serialize_json(
            value["blueprint_types"]
        )
    if "dependencies" in value:
        import capo_synthetics.types.dependencies

        out["Dependencies"] = capo_synthetics.types.dependencies.serialize_json(
            value["dependencies"]
        )
    return out


def deserialize_json(data: dict) -> CanaryCodeInput:
    out: CanaryCodeInput = {}  # type: ignore[typeddict-item]
    if data.get("S3Bucket") is not None:
        out["s3_bucket"] = data["S3Bucket"]
    if data.get("S3Key") is not None:
        out["s3_key"] = data["S3Key"]
    if data.get("S3Version") is not None:
        out["s3_version"] = data["S3Version"]
    if data.get("ZipFile") is not None:
        import capo_synthetics.types.blob

        out["zip_file"] = capo_synthetics.types.blob.deserialize_json(data["ZipFile"])
    if data.get("Handler") is not None:
        out["handler"] = data["Handler"]
    else:
        out["handler"] = ""
    if data.get("BlueprintTypes") is not None:
        import capo_synthetics.types.blueprint_types

        out["blueprint_types"] = capo_synthetics.types.blueprint_types.deserialize_json(
            data["BlueprintTypes"]
        )
    if data.get("Dependencies") is not None:
        import capo_synthetics.types.dependencies

        out["dependencies"] = capo_synthetics.types.dependencies.deserialize_json(
            data["Dependencies"]
        )
    return out
