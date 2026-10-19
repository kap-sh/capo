"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#WidgetConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.display_config
    import capo_bcm_dashboards.types.query_parameters


class WidgetConfig(TypedDict, closed=True):
    query_parameters: "capo_bcm_dashboards.types.query_parameters.QueryParameters"
    """<p>The parameters that define what data the widget should retrieve and how it should be filtered or grouped.</p>"""
    display_config: "capo_bcm_dashboards.types.display_config.DisplayConfig"
    """<p>The configuration that determines how the retrieved data should be visualized in the widget.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WidgetConfig) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.query_parameters

    out["queryParameters"] = (
        capo_bcm_dashboards.types.query_parameters.serialize_aws_json_1_0(
            value["query_parameters"]
        )
    )
    import capo_bcm_dashboards.types.display_config

    out["displayConfig"] = (
        capo_bcm_dashboards.types.display_config.serialize_aws_json_1_0(
            value["display_config"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> WidgetConfig:
    out: WidgetConfig = {}  # type: ignore[typeddict-item]
    if data.get("queryParameters") is not None:
        import capo_bcm_dashboards.types.query_parameters

        out["query_parameters"] = (
            capo_bcm_dashboards.types.query_parameters.deserialize_aws_json_1_0(
                data["queryParameters"]
            )
        )
    else:
        import capo_bcm_dashboards.types._unknown

        out["query_parameters"] = capo_bcm_dashboards.types._unknown.UnknownUnionMember(
            ""
        )
    if data.get("displayConfig") is not None:
        import capo_bcm_dashboards.types.display_config

        out["display_config"] = (
            capo_bcm_dashboards.types.display_config.deserialize_aws_json_1_0(
                data["displayConfig"]
            )
        )
    else:
        import capo_bcm_dashboards.types._unknown

        out["display_config"] = capo_bcm_dashboards.types._unknown.UnknownUnionMember(
            ""
        )
    return out
