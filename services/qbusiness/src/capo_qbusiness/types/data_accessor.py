"""Generated from Smithy shape ``com.amazonaws.qbusiness#DataAccessor``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.data_accessor_arn
    import capo_qbusiness.types.data_accessor_authentication_detail
    import capo_qbusiness.types.data_accessor_id
    import capo_qbusiness.types.data_accessor_name
    import capo_qbusiness.types.idc_application_arn
    import capo_qbusiness.types.principal_role_arn
    import capo_qbusiness.types.timestamp


class DataAccessor(TypedDict, closed=True):
    display_name: NotRequired[
        "capo_qbusiness.types.data_accessor_name.DataAccessorName"
    ]
    """<p>The friendly name of the data accessor.</p>"""
    data_accessor_id: NotRequired[
        "capo_qbusiness.types.data_accessor_id.DataAccessorId"
    ]
    """<p>The unique identifier of the data accessor.</p>"""
    data_accessor_arn: NotRequired[
        "capo_qbusiness.types.data_accessor_arn.DataAccessorArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the data accessor.</p>"""
    idc_application_arn: NotRequired[
        "capo_qbusiness.types.idc_application_arn.IdcApplicationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the associated IAM Identity Center application.</p>"""
    principal: NotRequired["capo_qbusiness.types.principal_role_arn.PrincipalRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role for the ISV associated with this data accessor.</p>"""
    authentication_detail: NotRequired[
        "capo_qbusiness.types.data_accessor_authentication_detail.DataAccessorAuthenticationDetail"
    ]
    """<p>The authentication configuration details for the data accessor. This specifies how the ISV authenticates when accessing data through this data accessor.</p>"""
    created_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp when the data accessor was created.</p>"""
    updated_at: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp when the data accessor was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataAccessor) -> dict:
    out: dict = {}
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "data_accessor_id" in value:
        out["dataAccessorId"] = value["data_accessor_id"]
    if "data_accessor_arn" in value:
        out["dataAccessorArn"] = value["data_accessor_arn"]
    if "idc_application_arn" in value:
        out["idcApplicationArn"] = value["idc_application_arn"]
    if "principal" in value:
        out["principal"] = value["principal"]
    if "authentication_detail" in value:
        import capo_qbusiness.types.data_accessor_authentication_detail

        out["authenticationDetail"] = (
            capo_qbusiness.types.data_accessor_authentication_detail.serialize_json(
                value["authentication_detail"]
            )
        )
    if "created_at" in value:
        import capo_qbusiness.types.timestamp

        out["createdAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_qbusiness.types.timestamp

        out["updatedAt"] = capo_qbusiness.types.timestamp.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> DataAccessor:
    out: DataAccessor = {}  # type: ignore[typeddict-item]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("dataAccessorId") is not None:
        out["data_accessor_id"] = data["dataAccessorId"]
    if data.get("dataAccessorArn") is not None:
        out["data_accessor_arn"] = data["dataAccessorArn"]
    if data.get("idcApplicationArn") is not None:
        out["idc_application_arn"] = data["idcApplicationArn"]
    if data.get("principal") is not None:
        out["principal"] = data["principal"]
    if data.get("authenticationDetail") is not None:
        import capo_qbusiness.types.data_accessor_authentication_detail

        out["authentication_detail"] = (
            capo_qbusiness.types.data_accessor_authentication_detail.deserialize_json(
                data["authenticationDetail"]
            )
        )
    if data.get("createdAt") is not None:
        import capo_qbusiness.types.timestamp

        out["created_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_qbusiness.types.timestamp

        out["updated_at"] = capo_qbusiness.types.timestamp.deserialize_json(
            data["updatedAt"]
        )
    return out


def redact_sensitive(value: DataAccessor) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "display_name" in value:
        out["display_name"] = "*** Sensitive Data Redacted ***"
    return out
