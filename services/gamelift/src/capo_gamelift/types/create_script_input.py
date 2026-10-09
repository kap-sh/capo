"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateScriptInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.node_js_version
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.s3_location
    import capo_gamelift.types.tag_list
    import capo_gamelift.types.zip_blob


class CreateScriptInput(TypedDict, closed=True):
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a script. Script names do not need to be unique. You can use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateScript.html">UpdateScript</a> to change this value later. </p>"""
    version: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Version information that is associated with a build or script. Version strings do not need to be unique. You can use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateScript.html">UpdateScript</a> to change this value later. </p>"""
    storage_location: NotRequired["capo_gamelift.types.s3_location.S3Location"]
    """<p>The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the <code>ObjectVersion</code> parameter to specify an earlier version. </p>"""
    zip_file: NotRequired["capo_gamelift.types.zip_blob.ZipBlob"]
    """<p>A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.</p> <p>When using the Amazon Web Services CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string "fileb://" to indicate that the file data is a binary object. For example: <code>--zip-file fileb://myRealtimeScript.zip</code>.</p>"""
    tags: NotRequired["capo_gamelift.types.tag_list.TagList"]
    """<p>A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging Amazon Web Services resources is useful for resource management, access management and cost allocation. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html"> Tagging Amazon Web Services Resources</a> in the <i>Amazon Web Services General Reference</i>. Once the resource is created, you can use <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_TagResource.html">TagResource</a>, <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_UntagResource.html">UntagResource</a>, and <a href="https://docs.aws.amazon.com/gamelift/latest/apireference/API_ListTagsForResource.html">ListTagsForResource</a> to add, remove, and view tags. The maximum tag limit may be lower than stated. See the Amazon Web Services General Reference for actual tagging limits.</p>"""
    node_js_version: NotRequired["capo_gamelift.types.node_js_version.NodeJsVersion"]
    """<p>The Node.js version used for execution of your Realtime script. The valid values are <code>10.x | 24.x</code>. By default, <code>NodeJsVersion</code> is <code>10.x</code>. This value cannot be updated later. </p> <note> <p>Node.js 10 will reach end of support on September 30, 2026. See more details in the <a href="http://aws.amazon.com/gamelift/faq/nodejs10/">Node.js 10 FAQs</a>. For migration guidance, see <a href="https://docs.aws.amazon.com/gamelift/latest/realtimeguide/realtime-script.html#realtime-script-nodejs-migration"> Migrating from Node.js 10 to 24</a>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateScriptInput) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "storage_location" in value:
        import capo_gamelift.types.s3_location

        out["StorageLocation"] = capo_gamelift.types.s3_location.serialize_aws_json_1_1(
            value["storage_location"]
        )
    if "zip_file" in value:
        import capo_gamelift.types.zip_blob

        out["ZipFile"] = capo_gamelift.types.zip_blob.serialize_aws_json_1_1(
            value["zip_file"]
        )
    if "tags" in value:
        import capo_gamelift.types.tag_list

        out["Tags"] = capo_gamelift.types.tag_list.serialize_aws_json_1_1(value["tags"])
    if "node_js_version" in value:
        out["NodeJsVersion"] = value["node_js_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateScriptInput:
    out: CreateScriptInput = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Version") is not None:
        out["version"] = data["Version"]
    if data.get("StorageLocation") is not None:
        import capo_gamelift.types.s3_location

        out["storage_location"] = (
            capo_gamelift.types.s3_location.deserialize_aws_json_1_1(
                data["StorageLocation"]
            )
        )
    if data.get("ZipFile") is not None:
        import capo_gamelift.types.zip_blob

        out["zip_file"] = capo_gamelift.types.zip_blob.deserialize_aws_json_1_1(
            data["ZipFile"]
        )
    if data.get("Tags") is not None:
        import capo_gamelift.types.tag_list

        out["tags"] = capo_gamelift.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("NodeJsVersion") is not None:
        out["node_js_version"] = data["NodeJsVersion"]
    return out
