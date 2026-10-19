"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#EngineModeStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_engine_mode
    import capo_elasticsearch_service.types.option_status


class EngineModeStatus(TypedDict, closed=True):
    options: "capo_elasticsearch_service.types.domain_engine_mode.DomainEngineMode"
    """<p>The engine mode configured for the domain.</p>"""
    status: "capo_elasticsearch_service.types.option_status.OptionStatus"
    """<p>The current status of the engine mode for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EngineModeStatus) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.domain_engine_mode

    out["Options"] = capo_elasticsearch_service.types.domain_engine_mode.serialize_json(
        value["options"]
    )
    import capo_elasticsearch_service.types.option_status

    out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> EngineModeStatus:
    out: EngineModeStatus = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        import capo_elasticsearch_service.types.domain_engine_mode

        out["options"] = (
            capo_elasticsearch_service.types.domain_engine_mode.deserialize_json(
                data["Options"]
            )
        )
    else:
        import typing

        out["options"] = typing.cast(
            "capo_elasticsearch_service.types.domain_engine_mode.DomainEngineMode", ""
        )
    if data.get("Status") is not None:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("EngineModeStatus.status required")
    return out
