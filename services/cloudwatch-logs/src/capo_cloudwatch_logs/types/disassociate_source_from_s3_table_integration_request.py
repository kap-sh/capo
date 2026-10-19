"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DisassociateSourceFromS3TableIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.s3_table_integration_source_identifier


class DisassociateSourceFromS3TableIntegrationRequest(TypedDict, closed=True):
    identifier: "capo_cloudwatch_logs.types.s3_table_integration_source_identifier.S3TableIntegrationSourceIdentifier"
    """<p>The unique identifier of the association to remove between the data source and S3 Table Integration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateSourceFromS3TableIntegrationRequest,
) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateSourceFromS3TableIntegrationRequest:
    out: DisassociateSourceFromS3TableIntegrationRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        out["identifier"] = ""
    return out
