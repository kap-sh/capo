"""Generated from Smithy shape ``com.amazonaws.appstream#ScriptDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.integer
    import capo_appstream.types.s3_location
    import capo_appstream.types.string


class ScriptDetails(TypedDict, closed=True):
    script_s3_location: NotRequired["capo_appstream.types.s3_location.S3Location"]
    """<p>The S3 object location for the script.</p>"""
    executable_path: NotRequired["capo_appstream.types.string.String"]
    """<p>The run path for the script.</p>"""
    executable_parameters: NotRequired["capo_appstream.types.string.String"]
    """<p>The runtime parameters passed to the run path for the script.</p>"""
    timeout_in_seconds: NotRequired["capo_appstream.types.integer.Integer"]
    """<p>The run timeout, in seconds, for the script.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScriptDetails) -> dict:
    out: dict = {}
    if "script_s3_location" in value:
        import capo_appstream.types.s3_location

        out["ScriptS3Location"] = (
            capo_appstream.types.s3_location.serialize_aws_json_1_1(
                value["script_s3_location"]
            )
        )
    if "executable_path" in value:
        out["ExecutablePath"] = value["executable_path"]
    if "executable_parameters" in value:
        out["ExecutableParameters"] = value["executable_parameters"]
    if "timeout_in_seconds" in value:
        out["TimeoutInSeconds"] = value["timeout_in_seconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ScriptDetails:
    out: ScriptDetails = {}  # type: ignore[typeddict-item]
    if data.get("ScriptS3Location") is not None:
        import capo_appstream.types.s3_location

        out["script_s3_location"] = (
            capo_appstream.types.s3_location.deserialize_aws_json_1_1(
                data["ScriptS3Location"]
            )
        )
    if data.get("ExecutablePath") is not None:
        out["executable_path"] = data["ExecutablePath"]
    if data.get("ExecutableParameters") is not None:
        out["executable_parameters"] = data["ExecutableParameters"]
    if data.get("TimeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["TimeoutInSeconds"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScriptDetails) -> dict:
    out: dict = {}
    if "script_s3_location" in value:
        import capo_appstream.types.s3_location

        out["ScriptS3Location"] = capo_appstream.types.s3_location.serialize_cbor(
            value["script_s3_location"]
        )
    if "executable_path" in value:
        out["ExecutablePath"] = value["executable_path"]
    if "executable_parameters" in value:
        out["ExecutableParameters"] = value["executable_parameters"]
    if "timeout_in_seconds" in value:
        out["TimeoutInSeconds"] = value["timeout_in_seconds"]
    return out


def deserialize_cbor(data: dict) -> ScriptDetails:
    out: ScriptDetails = {}  # type: ignore[typeddict-item]
    if data.get("ScriptS3Location") is not None:
        import capo_appstream.types.s3_location

        out["script_s3_location"] = capo_appstream.types.s3_location.deserialize_cbor(
            data["ScriptS3Location"]
        )
    if data.get("ExecutablePath") is not None:
        out["executable_path"] = data["ExecutablePath"]
    if data.get("ExecutableParameters") is not None:
        out["executable_parameters"] = data["ExecutableParameters"]
    if data.get("TimeoutInSeconds") is not None:
        out["timeout_in_seconds"] = data["TimeoutInSeconds"]
    return out
