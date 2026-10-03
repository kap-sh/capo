"""Generated from Smithy shape ``com.amazonaws.batch#EcsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.container_insights


class EcsSettings(TypedDict, closed=True):
    container_insights: NotRequired[
        "capo_batch.types.container_insights.ContainerInsights"
    ]
    """<p>Specifies the CloudWatch Container Insights mode for the compute environment. Valid values are:</p> <dl> <dt>ENABLED</dt> <dd> <p>Turns on standard Container Insights, which collects CPU, memory, disk, and network utilization metrics for the compute environment.</p> </dd> <dt>ENHANCED</dt> <dd> <p>Turns on enhanced Container Insights, which collects the standard metrics along with additional per-task observability metrics.</p> </dd> <dt>DISABLED</dt> <dd> <p>Turns off Container Insights for the compute environment.</p> </dd> </dl> <p>If you don't specify a value, the default is <code>DISABLED</code>. For more information, see <a href="https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights.html">Container Insights</a> in the <i>Batch User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcsSettings) -> dict:
    out: dict = {}
    if "container_insights" in value:
        import capo_batch.types.container_insights

        out["containerInsights"] = capo_batch.types.container_insights.serialize_json(
            value["container_insights"]
        )
    return out


def deserialize_json(data: dict) -> EcsSettings:
    out: EcsSettings = {}  # type: ignore[typeddict-item]
    if data.get("containerInsights") is not None:
        import capo_batch.types.container_insights

        out["container_insights"] = (
            capo_batch.types.container_insights.deserialize_json(
                data["containerInsights"]
            )
        )
    return out
