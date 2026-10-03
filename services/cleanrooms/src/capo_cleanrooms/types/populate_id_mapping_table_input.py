"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulateIdMappingTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.job_type
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.uuid


class PopulateIdMappingTableInput(TypedDict, closed=True):
    id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the ID mapping table that you want to populate.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID mapping table that you want to populate.</p>"""
    job_type: NotRequired["capo_cleanrooms.types.job_type.JobType"]
    """<p>The job type of the rule-based ID mapping job. Valid values include:</p> <p> <code>INCREMENTAL</code>: Processes only new or changed data since the last job run. This is the default job type if the ID mapping workflow was created in Entity Resolution with <code>incrementalRunConfig</code> specified.</p> <p> <code>BATCH</code>: Processes all data from the input source, regardless of previous job runs. This is the default job type if the ID mapping workflow was created in Entity Resolution but <code>incrementalRunConfig</code> wasn't specified.</p> <p> <code>DELETE_ONLY</code>: Processes only deletion requests from <code>BatchDeleteUniqueId</code>, which is set in Entity Resolution.</p> <p>For more information about <code>incrementalRunConfig</code> and <code>BatchDeleteUniqueId</code>, see the <a href="https://docs.aws.amazon.com/entityresolution/latest/apireference/Welcome.html">Entity Resolution API Reference</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PopulateIdMappingTableInput) -> dict:
    out: dict = {}
    if "job_type" in value:
        import capo_cleanrooms.types.job_type

        out["jobType"] = capo_cleanrooms.types.job_type.serialize_json(
            value["job_type"]
        )
    return out


def deserialize_json(data: dict) -> PopulateIdMappingTableInput:
    out: PopulateIdMappingTableInput = {}  # type: ignore[typeddict-item]
    if data.get("jobType") is not None:
        import capo_cleanrooms.types.job_type

        out["job_type"] = capo_cleanrooms.types.job_type.deserialize_json(
            data["jobType"]
        )
    return out
