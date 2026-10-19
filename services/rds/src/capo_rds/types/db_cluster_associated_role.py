"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterAssociatedRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.iam_role_arn
    import capo_rds.types.string


class DBClusterAssociatedRole(TypedDict, closed=True):
    role_arn: "capo_rds.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role to associate with the DB cluster.</p>"""
    feature_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the feature associated with the IAM role. For information about supported feature names, see <a>DBEngineVersion</a>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterAssociatedRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    pairs.append((f"{key_prefix}RoleArn", str(value["role_arn"])))
    if "feature_name" in value:
        pairs.append((f"{key_prefix}FeatureName", str(value["feature_name"])))


def deserialize_query(el: Element) -> DBClusterAssociatedRole:
    out: DBClusterAssociatedRole = {}  # type: ignore[typeddict-item]
    child_role_arn = el.find("RoleArn")
    if child_role_arn is not None:
        out["role_arn"] = str(child_role_arn.text or "")
    else:
        out["role_arn"] = ""
    child_feature_name = el.find("FeatureName")
    if child_feature_name is not None:
        out["feature_name"] = str(child_feature_name.text or "")
    return out
