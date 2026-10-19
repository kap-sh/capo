"""Generated from Smithy shape ``com.amazonaws.qbusiness#IdcAuthConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.idc_application_arn
    import capo_qbusiness.types.role_arn


class IdcAuthConfiguration(TypedDict, closed=True):
    idc_application_arn: "capo_qbusiness.types.idc_application_arn.IdcApplicationArn"
    """<p>The Amazon Resource Name (ARN) of the IAM Identity Center Application used to configure authentication.</p>"""
    role_arn: "capo_qbusiness.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role with permissions to perform actions on Amazon Web Services services on your behalf.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IdcAuthConfiguration) -> dict:
    out: dict = {}
    out["idcApplicationArn"] = value["idc_application_arn"]
    out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> IdcAuthConfiguration:
    out: IdcAuthConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("idcApplicationArn") is not None:
        out["idc_application_arn"] = data["idcApplicationArn"]
    else:
        out["idc_application_arn"] = ""
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        out["role_arn"] = ""
    return out
