"""Generated from Smithy shape ``com.amazonaws.glue#DevEndpointCustomLibraries``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.generic_string


class DevEndpointCustomLibraries(TypedDict, closed=True):
    extra_python_libs_s3_path: NotRequired[
        "capo_glue.types.generic_string.GenericString"
    ]
    """<p>The paths to one or more Python libraries in an Amazon Simple Storage Service (Amazon S3) bucket that should be loaded in your <code>DevEndpoint</code>. Multiple values must be complete paths separated by a comma.</p> <note> <p>You can only use pure Python libraries with a <code>DevEndpoint</code>. Libraries that rely on C extensions, such as the <a href="http://pandas.pydata.org/">pandas</a> Python data analysis library, are not currently supported.</p> </note>"""
    extra_jars_s3_path: NotRequired["capo_glue.types.generic_string.GenericString"]
    """<p>The path to one or more Java <code>.jar</code> files in an S3 bucket that should be loaded in your <code>DevEndpoint</code>.</p> <note> <p>You can only use pure Java/Scala libraries with a <code>DevEndpoint</code>.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DevEndpointCustomLibraries) -> dict:
    out: dict = {}
    if "extra_python_libs_s3_path" in value:
        out["ExtraPythonLibsS3Path"] = value["extra_python_libs_s3_path"]
    if "extra_jars_s3_path" in value:
        out["ExtraJarsS3Path"] = value["extra_jars_s3_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DevEndpointCustomLibraries:
    out: DevEndpointCustomLibraries = {}  # type: ignore[typeddict-item]
    if data.get("ExtraPythonLibsS3Path") is not None:
        out["extra_python_libs_s3_path"] = data["ExtraPythonLibsS3Path"]
    if data.get("ExtraJarsS3Path") is not None:
        out["extra_jars_s3_path"] = data["ExtraJarsS3Path"]
    return out
