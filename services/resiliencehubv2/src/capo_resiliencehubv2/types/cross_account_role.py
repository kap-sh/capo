"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CrossAccountRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.iam_role_arn


class CrossAccountRole(TypedDict, closed=True):
    cross_account_role_arn: "capo_resiliencehubv2.types.iam_role_arn.IamRoleArn"
    external_id: NotRequired["str"]
    """<p>The external ID used for assuming the cross-account role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CrossAccountRole) -> dict:
    out: dict = {}
    out["crossAccountRoleArn"] = value["cross_account_role_arn"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    return out


def deserialize_json(data: dict) -> CrossAccountRole:
    out: CrossAccountRole = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRoleArn") is not None:
        out["cross_account_role_arn"] = data["crossAccountRoleArn"]
    else:
        out["cross_account_role_arn"] = ""
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    return out
