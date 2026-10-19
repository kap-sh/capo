"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryS3OutputConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.key_prefix
    import capo_cleanrooms.types.result_format


class ProtectedQueryS3OutputConfiguration(TypedDict, closed=True):
    result_format: "capo_cleanrooms.types.result_format.ResultFormat"
    """<p>Intended file format of the result.</p>"""
    bucket: "str"
    """<p>The S3 bucket to unload the protected query results.</p>"""
    key_prefix: NotRequired["capo_cleanrooms.types.key_prefix.KeyPrefix"]
    """<p>The S3 prefix to unload the protected query results.</p>"""
    single_file_output: NotRequired["bool"]
    """<p>Indicates whether files should be output as a single file (<code>TRUE</code>) or output as multiple files (<code>FALSE</code>). This parameter is only supported for analyses with the Spark analytics engine.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryS3OutputConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.result_format

    out["resultFormat"] = capo_cleanrooms.types.result_format.serialize_json(
        value["result_format"]
    )
    out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    if "single_file_output" in value:
        out["singleFileOutput"] = value["single_file_output"]
    return out


def deserialize_json(data: dict) -> ProtectedQueryS3OutputConfiguration:
    out: ProtectedQueryS3OutputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("resultFormat") is not None:
        import capo_cleanrooms.types.result_format

        out["result_format"] = capo_cleanrooms.types.result_format.deserialize_json(
            data["resultFormat"]
        )
    else:
        import typing

        out["result_format"] = typing.cast(
            "capo_cleanrooms.types.result_format.ResultFormat", ""
        )
    if data.get("bucket") is not None:
        out["bucket"] = data["bucket"]
    else:
        out["bucket"] = ""
    if data.get("keyPrefix") is not None:
        out["key_prefix"] = data["keyPrefix"]
    if data.get("singleFileOutput") is not None:
        out["single_file_output"] = data["singleFileOutput"]
    return out
