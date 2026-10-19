"""Generated from Smithy shape ``com.amazonaws.wellarchitected#AggregationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.account_id
    import capo_wellarchitected.types.regions
    import capo_wellarchitected.types.role_arn


class AggregationConfiguration(TypedDict, closed=True):
    account_id: "capo_wellarchitected.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID to analyze.</p>"""
    regions: "capo_wellarchitected.types.regions.Regions"
    """<p>A list of Amazon Web Services Regions to include in the analysis.</p>"""
    access_role_arn: "capo_wellarchitected.types.role_arn.RoleArn"
    """<p>The ARN of an IAM role to assume for resource analysis in this account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationConfiguration) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    import capo_wellarchitected.types.regions

    out["regions"] = capo_wellarchitected.types.regions.serialize_json(value["regions"])
    out["accessRoleArn"] = value["access_role_arn"]
    return out


def deserialize_json(data: dict) -> AggregationConfiguration:
    out: AggregationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("regions") is not None:
        import capo_wellarchitected.types.regions

        out["regions"] = capo_wellarchitected.types.regions.deserialize_json(
            data["regions"]
        )
    else:
        out["regions"] = []
    if data.get("accessRoleArn") is not None:
        out["access_role_arn"] = data["accessRoleArn"]
    else:
        out["access_role_arn"] = ""
    return out
