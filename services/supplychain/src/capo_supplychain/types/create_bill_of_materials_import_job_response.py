"""Generated from Smithy shape ``com.amazonaws.supplychain#CreateBillOfMaterialsImportJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.uuid


class CreateBillOfMaterialsImportJobResponse(TypedDict, closed=True):
    job_id: "capo_supplychain.types.uuid.UUID"
    """<p>The new BillOfMaterialsImportJob identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateBillOfMaterialsImportJobResponse) -> dict:
    out: dict = {}
    out["jobId"] = value["job_id"]
    return out


def deserialize_json(data: dict) -> CreateBillOfMaterialsImportJobResponse:
    out: CreateBillOfMaterialsImportJobResponse = {}  # type: ignore[typeddict-item]
    if data.get("jobId") is not None:
        out["job_id"] = data["jobId"]
    else:
        out["job_id"] = ""
    return out
