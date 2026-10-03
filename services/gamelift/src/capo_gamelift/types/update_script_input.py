"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateScriptInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_zero_and_max_string
    import capo_gamelift.types.s3_location
    import capo_gamelift.types.script_id_or_arn
    import capo_gamelift.types.zip_blob


class UpdateScriptInput(TypedDict, closed=True):
    script_id: NotRequired["capo_gamelift.types.script_id_or_arn.ScriptIdOrArn"]
    """<p>A unique identifier for the Realtime script to update. You can use either the script ID or ARN value.</p>"""
    name: NotRequired["capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"]
    """<p>A descriptive label that is associated with a script. Script names do not need to be unique.</p>"""
    version: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>Version information that is associated with a build or script. Version strings do not need to be unique.</p>"""
    storage_location: NotRequired["capo_gamelift.types.s3_location.S3Location"]
    """<p>The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift Servers to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift Servers uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the <code>ObjectVersion</code> parameter to specify an earlier version. </p>"""
    zip_file: NotRequired["capo_gamelift.types.zip_blob.ZipBlob"]
    """<p>A data object containing your Realtime scripts and dependencies as a zip file. The zip file can have one or multiple files. Maximum size of a zip file is 5 MB.</p> <p>When using the Amazon Web Services CLI tool to create a script, this parameter is set to the zip file name. It must be prepended with the string "fileb://" to indicate that the file data is a binary object. For example: <code>--zip-file fileb://myRealtimeScript.zip</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateScriptInput) -> dict:
    out: dict = {}
    if "script_id" in value:
        out["ScriptId"] = value["script_id"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateScriptInput:
    out: UpdateScriptInput = {}  # type: ignore[typeddict-item]
    if data.get("ScriptId") is not None:
        out["script_id"] = data["ScriptId"]
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
    return out
