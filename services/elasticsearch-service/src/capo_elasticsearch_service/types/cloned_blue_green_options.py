"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#ClonedBlueGreenOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.retention_options


class ClonedBlueGreenOptions(TypedDict, closed=True):
    retention_options: NotRequired[
        "capo_elasticsearch_service.types.retention_options.RetentionOptions"
    ]
    """<p>How long to keep the cluster that you cut over from after cutover completes. When you start the upgrade, only <code>RetentionInHours</code> is accepted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClonedBlueGreenOptions) -> dict:
    out: dict = {}
    if "retention_options" in value:
        import capo_elasticsearch_service.types.retention_options

        out["RetentionOptions"] = (
            capo_elasticsearch_service.types.retention_options.serialize_json(
                value["retention_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClonedBlueGreenOptions:
    out: ClonedBlueGreenOptions = {}  # type: ignore[typeddict-item]
    if data.get("RetentionOptions") is not None:
        import capo_elasticsearch_service.types.retention_options

        out["retention_options"] = (
            capo_elasticsearch_service.types.retention_options.deserialize_json(
                data["RetentionOptions"]
            )
        )
    return out
