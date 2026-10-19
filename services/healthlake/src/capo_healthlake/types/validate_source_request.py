"""Generated from Smithy shape ``com.amazon.awshealthlakedatatransformationfrontendservice#ValidateSourceRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.source_file_blob
    import capo_healthlake.types.source_format


class ValidateSourceRequest(TypedDict, closed=True):
    source_format: "capo_healthlake.types.source_format.SourceFormat"
    """<p>The format of the source file to validate.</p>"""
    source_file: "capo_healthlake.types.source_file_blob.SourceFileBlob"
    """<p>The raw source file content to validate.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ValidateSourceRequest) -> dict:
    out: dict = {}
    import capo_healthlake.types.source_format

    out["SourceFormat"] = capo_healthlake.types.source_format.serialize_aws_json_1_0(
        value["source_format"]
    )
    import capo_healthlake.types.source_file_blob

    out["SourceFile"] = capo_healthlake.types.source_file_blob.serialize_aws_json_1_0(
        value["source_file"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ValidateSourceRequest:
    out: ValidateSourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("SourceFormat") is not None:
        import capo_healthlake.types.source_format

        out["source_format"] = (
            capo_healthlake.types.source_format.deserialize_aws_json_1_0(
                data["SourceFormat"]
            )
        )
    else:
        import typing

        out["source_format"] = typing.cast(
            "capo_healthlake.types.source_format.SourceFormat", ""
        )
    if data.get("SourceFile") is not None:
        import capo_healthlake.types.source_file_blob

        out["source_file"] = (
            capo_healthlake.types.source_file_blob.deserialize_aws_json_1_0(
                data["SourceFile"]
            )
        )
    else:
        out["source_file"] = b""
    return out


def redact_sensitive(value: ValidateSourceRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source_file" in value:
        out["source_file"] = "*** Sensitive Data Redacted ***"
    return out
