"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GraphDisplayConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.visual_type


class GraphDisplayConfig(TypedDict, closed=True):
    visual_type: "capo_bcm_dashboards.types.visual_type.VisualType"
    """<p>The type of visualization to use for the data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GraphDisplayConfig) -> dict:
    out: dict = {}
    import capo_bcm_dashboards.types.visual_type

    out["visualType"] = capo_bcm_dashboards.types.visual_type.serialize_aws_json_1_0(
        value["visual_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GraphDisplayConfig:
    out: GraphDisplayConfig = {}  # type: ignore[typeddict-item]
    if data.get("visualType") is not None:
        import capo_bcm_dashboards.types.visual_type

        out["visual_type"] = (
            capo_bcm_dashboards.types.visual_type.deserialize_aws_json_1_0(
                data["visualType"]
            )
        )
    else:
        import typing

        out["visual_type"] = typing.cast(
            "capo_bcm_dashboards.types.visual_type.VisualType", ""
        )
    return out
