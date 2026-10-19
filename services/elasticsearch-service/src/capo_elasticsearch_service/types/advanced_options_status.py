"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AdvancedOptionsStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.advanced_options
    import capo_elasticsearch_service.types.option_status


class AdvancedOptionsStatus(TypedDict, closed=True):
    options: "capo_elasticsearch_service.types.advanced_options.AdvancedOptions"
    """<p> Specifies the status of advanced options for the specified Elasticsearch domain.</p>"""
    status: "capo_elasticsearch_service.types.option_status.OptionStatus"
    """<p> Specifies the status of <code>OptionStatus</code> for advanced options for the specified Elasticsearch domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedOptionsStatus) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.advanced_options

    out["Options"] = capo_elasticsearch_service.types.advanced_options.serialize_json(
        value["options"]
    )
    import capo_elasticsearch_service.types.option_status

    out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> AdvancedOptionsStatus:
    out: AdvancedOptionsStatus = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        import capo_elasticsearch_service.types.advanced_options

        out["options"] = (
            capo_elasticsearch_service.types.advanced_options.deserialize_json(
                data["Options"]
            )
        )
    else:
        out["options"] = {}
    if data.get("Status") is not None:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("AdvancedOptionsStatus.status required")
    return out
