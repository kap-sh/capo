"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateDataAccessorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessor_arn
    import capo_qbusiness.types.data_accessor_id
    import capo_qbusiness.types.idc_application_arn


class CreateDataAccessorResponse(TypedDict, closed=True):
    data_accessor_id: "capo_qbusiness.types.data_accessor_id.DataAccessorId"
    """<p>The unique identifier of the created data accessor.</p>"""
    idc_application_arn: "capo_qbusiness.types.idc_application_arn.IdcApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center application created for this data accessor.</p>"""
    data_accessor_arn: "capo_qbusiness.types.data_accessor_arn.DataAccessorArn"
    """<p>The Amazon Resource Name (ARN) of the created data accessor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAccessorResponse) -> dict:
    out: dict = {}
    out["dataAccessorId"] = value["data_accessor_id"]
    out["idcApplicationArn"] = value["idc_application_arn"]
    out["dataAccessorArn"] = value["data_accessor_arn"]
    return out


def deserialize_json(data: dict) -> CreateDataAccessorResponse:
    out: CreateDataAccessorResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataAccessorId") is not None:
        out["data_accessor_id"] = data["dataAccessorId"]
    else:
        out["data_accessor_id"] = ""
    if data.get("idcApplicationArn") is not None:
        out["idc_application_arn"] = data["idcApplicationArn"]
    else:
        out["idc_application_arn"] = ""
    if data.get("dataAccessorArn") is not None:
        out["data_accessor_arn"] = data["dataAccessorArn"]
    else:
        out["data_accessor_arn"] = ""
    return out
