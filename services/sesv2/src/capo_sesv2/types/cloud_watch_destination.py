"""Generated from Smithy shape ``com.amazonaws.sesv2#CloudWatchDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sesv2.types.cloud_watch_dimension_configurations


class CloudWatchDestination(TypedDict, closed=True):
    dimension_configurations: "capo_sesv2.types.cloud_watch_dimension_configurations.CloudWatchDimensionConfigurations"
    """<p>An array of objects that define the dimensions to use when you send email events to Amazon CloudWatch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchDestination) -> dict:
    out: dict = {}
    import capo_sesv2.types.cloud_watch_dimension_configurations

    out["DimensionConfigurations"] = (
        capo_sesv2.types.cloud_watch_dimension_configurations.serialize_json(
            value["dimension_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> CloudWatchDestination:
    out: CloudWatchDestination = {}  # type: ignore[typeddict-item]
    if data.get("DimensionConfigurations") is not None:
        import capo_sesv2.types.cloud_watch_dimension_configurations

        out["dimension_configurations"] = (
            capo_sesv2.types.cloud_watch_dimension_configurations.deserialize_json(
                data["DimensionConfigurations"]
            )
        )
    else:
        out["dimension_configurations"] = []
    return out
