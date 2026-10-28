"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DisplayConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bcm_dashboards.errors import DeserializationError, SerializationError
from capo_bcm_dashboards.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.graph_display_config_map
    import capo_bcm_dashboards.types.table_display_config_struct


class DisplayConfigGraphMember(TypedDict, closed=True):
    graph: "capo_bcm_dashboards.types.graph_display_config_map.GraphDisplayConfigMap"


class DisplayConfigTableMember(TypedDict, closed=True):
    table: (
        "capo_bcm_dashboards.types.table_display_config_struct.TableDisplayConfigStruct"
    )


DisplayConfig: TypeAlias = (
    DisplayConfigGraphMember | DisplayConfigTableMember | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisplayConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DisplayConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "graph" in value:
        import capo_bcm_dashboards.types.graph_display_config_map

        return {
            "graph": capo_bcm_dashboards.types.graph_display_config_map.serialize_aws_json_1_0(
                value["graph"]
            )
        }
    elif "table" in value:
        import capo_bcm_dashboards.types.table_display_config_struct

        return {
            "table": capo_bcm_dashboards.types.table_display_config_struct.serialize_aws_json_1_0(
                value["table"]
            )
        }
    else:
        raise SerializationError("DisplayConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> DisplayConfig:
    if data.get("graph") is not None:
        import capo_bcm_dashboards.types.graph_display_config_map

        return {
            "graph": capo_bcm_dashboards.types.graph_display_config_map.deserialize_aws_json_1_0(
                data["graph"]
            )
        }
    elif data.get("table") is not None:
        import capo_bcm_dashboards.types.table_display_config_struct

        return {
            "table": capo_bcm_dashboards.types.table_display_config_struct.deserialize_aws_json_1_0(
                data["table"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("DisplayConfig: no recognized variant key")
