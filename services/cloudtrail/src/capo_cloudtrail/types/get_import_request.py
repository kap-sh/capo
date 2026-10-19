"""Generated from Smithy shape ``com.amazonaws.cloudtrail#GetImportRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.uuid


class GetImportRequest(TypedDict, closed=True):
    import_id: "capo_cloudtrail.types.uuid.UUID"
    """<p> The ID for the import. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetImportRequest) -> dict:
    out: dict = {}
    out["ImportId"] = value["import_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetImportRequest:
    out: GetImportRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImportId") is not None:
        out["import_id"] = data["ImportId"]
    else:
        out["import_id"] = ""
    return out
