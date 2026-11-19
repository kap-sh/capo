"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalReportState``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle state of an Organizational Report. The state advances through the asynchronous pipeline: <code>DISCOVERING</code> (expanding the caller-supplied scope into the full list of in-scope accounts and profiles), <code>SNAPSHOTTING</code> (materializing per-account profile and recommendation snapshots), <code>AGGREGATING</code> (merging snapshots into the final artifact), <code>COMPRESSING</code> (writing the final CSV, JSON, or Parquet artifacts to Amazon S3), <code>COMPLETED</code> (the report is ready to download), <code>FAILED</code> (terminal failure), and <code>DELETING</code> (the report is being removed).</p>"""
OrganizationalReportState: TypeAlias = Literal[
    "DISCOVERING",
    "SNAPSHOTTING",
    "AGGREGATING",
    "COMPRESSING",
    "COMPLETED",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalReportState) -> str:
    return value


def deserialize_json(data: str) -> OrganizationalReportState:
    return cast(OrganizationalReportState, data)
