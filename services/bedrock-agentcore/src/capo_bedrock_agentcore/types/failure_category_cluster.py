"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FailureCategoryCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.failure_sub_category_cluster_list


class FailureCategoryCluster(TypedDict, closed=True):
    cluster_id: "int"
    """<p>The unique identifier of the failure category cluster.</p>"""
    name: "str"
    """<p>The name of the failure category.</p>"""
    description: "str"
    """<p>A description of the failure category pattern.</p>"""
    affected_session_count: "int"
    """<p>The number of sessions affected by this failure category.</p>"""
    sub_categories: "capo_bedrock_agentcore.types.failure_sub_category_cluster_list.FailureSubCategoryClusterList"
    """<p>The list of failure subcategories within this category.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FailureCategoryCluster) -> dict:
    out: dict = {}
    out["clusterId"] = value["cluster_id"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["affectedSessionCount"] = value["affected_session_count"]
    import capo_bedrock_agentcore.types.failure_sub_category_cluster_list

    out["subCategories"] = (
        capo_bedrock_agentcore.types.failure_sub_category_cluster_list.serialize_json(
            value["sub_categories"]
        )
    )
    return out


def deserialize_json(data: dict) -> FailureCategoryCluster:
    out: FailureCategoryCluster = {}  # type: ignore[typeddict-item]
    if data.get("clusterId") is not None:
        out["cluster_id"] = data["clusterId"]
    else:
        out["cluster_id"] = 0
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    if data.get("affectedSessionCount") is not None:
        out["affected_session_count"] = data["affectedSessionCount"]
    else:
        out["affected_session_count"] = 0
    if data.get("subCategories") is not None:
        import capo_bedrock_agentcore.types.failure_sub_category_cluster_list

        out["sub_categories"] = (
            capo_bedrock_agentcore.types.failure_sub_category_cluster_list.deserialize_json(
                data["subCategories"]
            )
        )
    else:
        out["sub_categories"] = []
    return out
