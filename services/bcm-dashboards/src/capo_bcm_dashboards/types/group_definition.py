"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GroupDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.group_definition_type


class GroupDefinition(TypedDict, closed=True):
    key: "str"
    """<p>The key to use for grouping cost and usage data.</p>"""
    type: "capo_bcm_dashboards.types.group_definition_type.GroupDefinitionType"
    """<p>The type of grouping to apply.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GroupDefinition) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bcm_dashboards.types.group_definition_type

    out["type"] = (
        capo_bcm_dashboards.types.group_definition_type.serialize_aws_json_1_0(
            value.get("type", "DIMENSION")
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GroupDefinition:
    out: GroupDefinition = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("type") is not None:
        import capo_bcm_dashboards.types.group_definition_type

        out["type"] = (
            capo_bcm_dashboards.types.group_definition_type.deserialize_aws_json_1_0(
                data["type"]
            )
        )
    else:
        out["type"] = "DIMENSION"
    return out
