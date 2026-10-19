"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#Widget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.description
    import capo_bcm_dashboards.types.widget_config_list
    import capo_bcm_dashboards.types.widget_height
    import capo_bcm_dashboards.types.widget_id
    import capo_bcm_dashboards.types.widget_title
    import capo_bcm_dashboards.types.widget_width


class Widget(TypedDict, closed=True):
    id: NotRequired["capo_bcm_dashboards.types.widget_id.WidgetId"]
    """<p>The unique identifier for the widget.</p>"""
    title: "capo_bcm_dashboards.types.widget_title.WidgetTitle"
    """<p>The title of the widget.</p>"""
    description: NotRequired["capo_bcm_dashboards.types.description.Description"]
    """<p>A description of the widget's purpose or the data it displays.</p>"""
    width: "capo_bcm_dashboards.types.widget_width.WidgetWidth"
    """<p>The width of the widget in column spans. The dashboard layout consists of a grid system.</p>"""
    height: "capo_bcm_dashboards.types.widget_height.WidgetHeight"
    """<p>The height of the widget in row spans. The dashboard layout consists of a grid system.</p>"""
    horizontal_offset: "int"
    """<p>Specifies the starting column position of the widget in the dashboard's grid layout. Used to control widget placement.</p>"""
    configs: "capo_bcm_dashboards.types.widget_config_list.WidgetConfigList"
    """<p>An array of configurations that define the data queries and display settings for the widget.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Widget) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    out["title"] = value["title"]
    if "description" in value:
        out["description"] = value["description"]
    out["width"] = value.get("width", 4)
    out["height"] = value.get("height", 7)
    out["horizontalOffset"] = value.get("horizontal_offset", 0)
    import capo_bcm_dashboards.types.widget_config_list

    out["configs"] = (
        capo_bcm_dashboards.types.widget_config_list.serialize_aws_json_1_0(
            value["configs"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Widget:
    out: Widget = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("width") is not None:
        out["width"] = data["width"]
    else:
        out["width"] = 4
    if data.get("height") is not None:
        out["height"] = data["height"]
    else:
        out["height"] = 7
    if data.get("horizontalOffset") is not None:
        out["horizontal_offset"] = data["horizontalOffset"]
    else:
        out["horizontal_offset"] = 0
    if data.get("configs") is not None:
        import capo_bcm_dashboards.types.widget_config_list

        out["configs"] = (
            capo_bcm_dashboards.types.widget_config_list.deserialize_aws_json_1_0(
                data["configs"]
            )
        )
    else:
        out["configs"] = []
    return out
