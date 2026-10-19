"""Generated from Smithy shape ``com.amazonaws.ses#CloudWatchDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.cloud_watch_dimension_configurations


class CloudWatchDestination(TypedDict, closed=True):
    dimension_configurations: "capo_ses.types.cloud_watch_dimension_configurations.CloudWatchDimensionConfigurations"
    """<p>A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CloudWatchDestination, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    import capo_ses.types.cloud_watch_dimension_configurations

    capo_ses.types.cloud_watch_dimension_configurations.serialize_query(
        value["dimension_configurations"], pairs, f"{key_prefix}DimensionConfigurations"
    )


def deserialize_query(el: Element) -> CloudWatchDestination:
    out: CloudWatchDestination = {}  # type: ignore[typeddict-item]
    child_dimension_configurations = el.find("DimensionConfigurations")
    if child_dimension_configurations is not None:
        import capo_ses.types.cloud_watch_dimension_configurations

        out["dimension_configurations"] = (
            capo_ses.types.cloud_watch_dimension_configurations.deserialize_query(
                child_dimension_configurations
            )
        )
    else:
        out["dimension_configurations"] = []
    return out
