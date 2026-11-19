"""Generated from Smithy shape ``com.amazonaws.wellarchitected#OrganizationalReportFormat``."""

from typing import Literal, TypeAlias, cast

"""<p>The output format for an Organizational Report artifact retrieved through GetAgentOrganizationalReportData or delivered through SendAgentOrganizationalReportDataToS3.</p>"""
OrganizationalReportFormat: TypeAlias = Literal[
    "CSV",
    "JSON",
    "PARQUET",
]


# --- restJson1 ser/de ---
def serialize_json(value: OrganizationalReportFormat) -> str:
    return value


def deserialize_json(data: str) -> OrganizationalReportFormat:
    return cast(OrganizationalReportFormat, data)
