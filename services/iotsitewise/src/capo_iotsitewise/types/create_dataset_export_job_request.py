"""Generated from Smithy shape ``com.amazonaws.iotsitewise#CreateDatasetExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.export_error_report_location
    import capo_iotsitewise.types.processing_input
    import capo_iotsitewise.types.s3_uri
    import capo_iotsitewise.types.workspace_name


class CreateDatasetExportJobRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace in which to create the dataset export job.</p>"""
    client_token: NotRequired["capo_iotsitewise.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. The AWS SDKs and CLI populate this automatically.</p>"""
    destination_s3_uri: "capo_iotsitewise.types.s3_uri.S3Uri"
    """<p>The S3 URI where output clips will be written.</p>"""
    input: "capo_iotsitewise.types.processing_input.ProcessingInput"
    """<p>The processing input source.</p>"""
    error_report_location: (
        "capo_iotsitewise.types.export_error_report_location.ExportErrorReportLocation"
    )
    """<p>The location where the error report will be written on failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetExportJobRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["destinationS3Uri"] = value["destination_s3_uri"]
    import capo_iotsitewise.types.processing_input

    out["input"] = capo_iotsitewise.types.processing_input.serialize_json(
        value["input"]
    )
    import capo_iotsitewise.types.export_error_report_location

    out["errorReportLocation"] = (
        capo_iotsitewise.types.export_error_report_location.serialize_json(
            value["error_report_location"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateDatasetExportJobRequest:
    out: CreateDatasetExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("destinationS3Uri") is not None:
        out["destination_s3_uri"] = data["destinationS3Uri"]
    else:
        out["destination_s3_uri"] = ""
    if data.get("input") is not None:
        import capo_iotsitewise.types.processing_input

        out["input"] = capo_iotsitewise.types.processing_input.deserialize_json(
            data["input"]
        )
    else:
        import capo_iotsitewise.types._unknown

        out["input"] = capo_iotsitewise.types._unknown.UnknownUnionMember("")
    if data.get("errorReportLocation") is not None:
        import capo_iotsitewise.types.export_error_report_location

        out["error_report_location"] = (
            capo_iotsitewise.types.export_error_report_location.deserialize_json(
                data["errorReportLocation"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDatasetExportJobRequest.error_report_location required"
        )
    return out
