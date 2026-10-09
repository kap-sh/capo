"""Generated from Smithy shape ``com.amazonaws.securityhub#ExportFailureCode``."""

from typing import Literal, TypeAlias, cast

"""<p>Classifies why a terminal-state export job failed. Present only when <code>Status</code> is <code>FAILED</code>. Valid values are as follows:</p> <ul> <li> <p> <code>ACCESS_DENIED</code> – Security Hub couldn't read a required resource or write to the destination. Verify the bucket policy and key policy.</p> </li> <li> <p> <code>RESOURCE_NOT_FOUND</code> – A referenced destination bucket or Amazon Web Services KMS key no longer exists.</p> </li> <li> <p> <code>INTERNAL_ERROR</code> – An unclassified service-side error occurred. Retry the export, and if the failure persists, contact Amazon Web Services Support.</p> </li> </ul>"""
ExportFailureCode: TypeAlias = Literal[
    "ACCESS_DENIED",
    "RESOURCE_NOT_FOUND",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ExportFailureCode) -> str:
    return value


def deserialize_json(data: str) -> ExportFailureCode:
    return cast(ExportFailureCode, data)
