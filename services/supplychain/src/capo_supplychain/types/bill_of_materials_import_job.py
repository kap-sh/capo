"""Generated from Smithy shape ``com.amazonaws.supplychain#BillOfMaterialsImportJob``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.configuration_job_status
    import capo_supplychain.types.configuration_s3_uri
    import capo_supplychain.types.uuid


class BillOfMaterialsImportJob(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The BillOfMaterialsImportJob instanceId.</p>"""
    job_id: "capo_supplychain.types.uuid.UUID"
    """<p>The BillOfMaterialsImportJob jobId.</p>"""
    status: "capo_supplychain.types.configuration_job_status.ConfigurationJobStatus"
    """<p>The BillOfMaterialsImportJob ConfigurationJobStatus.</p>"""
    s3uri: "capo_supplychain.types.configuration_s3_uri.ConfigurationS3Uri"
    """<p>The S3 URI from which the CSV is read.</p>"""
    message: NotRequired["str"]
    """<p>When the BillOfMaterialsImportJob has reached a terminal state, there will be a message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BillOfMaterialsImportJob) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["jobId"] = value["job_id"]
    import capo_supplychain.types.configuration_job_status

    out["status"] = capo_supplychain.types.configuration_job_status.serialize_json(
        value["status"]
    )
    out["s3uri"] = value["s3uri"]
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> BillOfMaterialsImportJob:
    out: BillOfMaterialsImportJob = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    if data.get("status") is not None:
        import capo_supplychain.types.configuration_job_status

        out["status"] = (
            capo_supplychain.types.configuration_job_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_supplychain.types.configuration_job_status.ConfigurationJobStatus", ""
        )
    if data.get("s3uri") is not None:
        out["s3uri"] = data["s3uri"]
    else:
        out["s3uri"] = ""
    if data.get("message") is not None:
        out["message"] = data["message"]
    return out
