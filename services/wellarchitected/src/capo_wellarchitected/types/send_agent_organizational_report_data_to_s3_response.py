"""Generated from Smithy shape ``com.amazonaws.wellarchitected#SendAgentOrganizationalReportDataToS3Response``."""

from typing_extensions import TypedDict


class SendAgentOrganizationalReportDataToS3Response(TypedDict, closed=True):
    delivered_to: "str"
    """<p>S3 URI (format s3://bucket/key) where the artifact was written.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendAgentOrganizationalReportDataToS3Response) -> dict:
    out: dict = {}
    out["deliveredTo"] = value["delivered_to"]
    return out


def deserialize_json(data: dict) -> SendAgentOrganizationalReportDataToS3Response:
    out: SendAgentOrganizationalReportDataToS3Response = {}  # type: ignore[typeddict-item]
    if data.get("deliveredTo") is not None:
        out["delivered_to"] = data["deliveredTo"]
    else:
        out["delivered_to"] = ""
    return out
