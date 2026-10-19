"""Generated from Smithy shape ``com.amazonaws.mpa#IamIdentityCenter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mpa.types.idc_instance_arn
    import capo_mpa.types.string


class IamIdentityCenter(TypedDict, closed=True):
    instance_arn: "capo_mpa.types.idc_instance_arn.IdcInstanceArn"
    """<p>Amazon Resource Name (ARN) for the IAM Identity Center instance.</p>"""
    region: "capo_mpa.types.string.String"
    """<p>Amazon Web Services Region where the IAM Identity Center instance is located.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IamIdentityCenter) -> dict:
    out: dict = {}
    out["InstanceArn"] = value["instance_arn"]
    out["Region"] = value["region"]
    return out


def deserialize_json(data: dict) -> IamIdentityCenter:
    out: IamIdentityCenter = {}  # type: ignore[typeddict-item]
    if data.get("InstanceArn") is not None:
        out["instance_arn"] = data["InstanceArn"]
    else:
        out["instance_arn"] = ""
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    else:
        out["region"] = ""
    return out
