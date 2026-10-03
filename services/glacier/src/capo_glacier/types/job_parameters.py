"""Generated from Smithy shape ``com.amazonaws.glacier#JobParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glacier.types.inventory_retrieval_job_input
    import capo_glacier.types.output_location
    import capo_glacier.types.select_parameters
    import capo_glacier.types.string


class JobParameters(TypedDict, closed=True):
    format: NotRequired["capo_glacier.types.string.string"]
    """<p>When initiating a job to retrieve a vault inventory, you can optionally add this parameter to your request to specify the output format. If you are initiating an inventory job and do not specify a Format field, JSON is the default format. Valid values are "CSV" and "JSON".</p>"""
    type: NotRequired["capo_glacier.types.string.string"]
    """<p>The job type. You can initiate a job to perform a select query on an archive, retrieve an archive, or get an inventory of a vault. Valid values are "select", "archive-retrieval" and "inventory-retrieval".</p>"""
    archive_id: NotRequired["capo_glacier.types.string.string"]
    """<p>The ID of the archive that you want to retrieve. This field is required only if <code>Type</code> is set to <code>select</code> or <code>archive-retrieval</code>code>. An error occurs if you specify this request parameter for an inventory retrieval job request. </p>"""
    description: NotRequired["capo_glacier.types.string.string"]
    """<p>The optional description for the job. The description must be less than or equal to 1,024 bytes. The allowable characters are 7-bit ASCII without control codes-specifically, ASCII values 32-126 decimal or 0x20-0x7E hexadecimal.</p>"""
    sns_topic: NotRequired["capo_glacier.types.string.string"]
    """<p>The Amazon SNS topic ARN to which Amazon Glacier sends a notification when the job is completed and the output is ready for you to download. The specified topic publishes the notification to its subscribers. The SNS topic must exist.</p>"""
    retrieval_byte_range: NotRequired["capo_glacier.types.string.string"]
    """<p>The byte range to retrieve for an archive retrieval. in the form "<i>StartByteValue</i>-<i>EndByteValue</i>" If not specified, the whole archive is retrieved. If specified, the byte range must be megabyte (1024*1024) aligned which means that <i>StartByteValue</i> must be divisible by 1 MB and <i>EndByteValue</i> plus 1 must be divisible by 1 MB or be the end of the archive specified as the archive byte size value minus 1. If RetrievalByteRange is not megabyte aligned, this operation returns a 400 response. </p> <p>An error occurs if you specify this field for an inventory retrieval job request.</p>"""
    tier: NotRequired["capo_glacier.types.string.string"]
    """<p>The tier to use for a select or an archive retrieval job. Valid values are <code>Expedited</code>, <code>Standard</code>, or <code>Bulk</code>. <code>Standard</code> is the default.</p>"""
    inventory_retrieval_parameters: NotRequired[
        "capo_glacier.types.inventory_retrieval_job_input.InventoryRetrievalJobInput"
    ]
    """<p>Input parameters used for range inventory retrieval.</p>"""
    select_parameters: NotRequired[
        "capo_glacier.types.select_parameters.SelectParameters"
    ]
    """<p>Contains the parameters that define a job.</p>"""
    output_location: NotRequired["capo_glacier.types.output_location.OutputLocation"]
    """<p>Contains information about the location where the select job results are stored.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobParameters) -> dict:
    out: dict = {}
    if "format" in value:
        out["Format"] = value["format"]
    if "type" in value:
        out["Type"] = value["type"]
    if "archive_id" in value:
        out["ArchiveId"] = value["archive_id"]
    if "description" in value:
        out["Description"] = value["description"]
    if "sns_topic" in value:
        out["SNSTopic"] = value["sns_topic"]
    if "retrieval_byte_range" in value:
        out["RetrievalByteRange"] = value["retrieval_byte_range"]
    if "tier" in value:
        out["Tier"] = value["tier"]
    if "inventory_retrieval_parameters" in value:
        import capo_glacier.types.inventory_retrieval_job_input

        out["InventoryRetrievalParameters"] = (
            capo_glacier.types.inventory_retrieval_job_input.serialize_json(
                value["inventory_retrieval_parameters"]
            )
        )
    if "select_parameters" in value:
        import capo_glacier.types.select_parameters

        out["SelectParameters"] = capo_glacier.types.select_parameters.serialize_json(
            value["select_parameters"]
        )
    if "output_location" in value:
        import capo_glacier.types.output_location

        out["OutputLocation"] = capo_glacier.types.output_location.serialize_json(
            value["output_location"]
        )
    return out


def deserialize_json(data: dict) -> JobParameters:
    out: JobParameters = {}  # type: ignore[typeddict-item]
    if data.get("Format") is not None:
        out["format"] = data["Format"]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    if data.get("ArchiveId") is not None:
        out["archive_id"] = data["ArchiveId"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SNSTopic") is not None:
        out["sns_topic"] = data["SNSTopic"]
    if data.get("RetrievalByteRange") is not None:
        out["retrieval_byte_range"] = data["RetrievalByteRange"]
    if data.get("Tier") is not None:
        out["tier"] = data["Tier"]
    if data.get("InventoryRetrievalParameters") is not None:
        import capo_glacier.types.inventory_retrieval_job_input

        out["inventory_retrieval_parameters"] = (
            capo_glacier.types.inventory_retrieval_job_input.deserialize_json(
                data["InventoryRetrievalParameters"]
            )
        )
    if data.get("SelectParameters") is not None:
        import capo_glacier.types.select_parameters

        out["select_parameters"] = (
            capo_glacier.types.select_parameters.deserialize_json(
                data["SelectParameters"]
            )
        )
    if data.get("OutputLocation") is not None:
        import capo_glacier.types.output_location

        out["output_location"] = capo_glacier.types.output_location.deserialize_json(
            data["OutputLocation"]
        )
    return out
