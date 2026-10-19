"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StopResourceSnapshotJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.resource_snapshot_job_identifier


class StopResourceSnapshotJobRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Stops the request from the production AWS environment.</p> </li> <li> <p>Sandbox: Stops the request from a sandbox environment used for testing or development purposes.</p> </li> </ul>"""
    resource_snapshot_job_identifier: "capo_partnercentral_selling.types.resource_snapshot_job_identifier.ResourceSnapshotJobIdentifier"
    """<p>The identifier of the job to stop.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StopResourceSnapshotJobRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ResourceSnapshotJobIdentifier"] = value["resource_snapshot_job_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> StopResourceSnapshotJobRequest:
    out: StopResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ResourceSnapshotJobIdentifier") is not None:
        out["resource_snapshot_job_identifier"] = data["ResourceSnapshotJobIdentifier"]
    else:
        out["resource_snapshot_job_identifier"] = ""
    return out
