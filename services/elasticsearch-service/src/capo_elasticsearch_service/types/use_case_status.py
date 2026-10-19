"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#UseCaseStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.domain_use_case
    import capo_elasticsearch_service.types.option_status


class UseCaseStatus(TypedDict, closed=True):
    options: "capo_elasticsearch_service.types.domain_use_case.DomainUseCase"
    """<p>The use case configured for the domain.</p>"""
    status: "capo_elasticsearch_service.types.option_status.OptionStatus"
    """<p>The current status of the use case for the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UseCaseStatus) -> dict:
    out: dict = {}
    import capo_elasticsearch_service.types.domain_use_case

    out["Options"] = capo_elasticsearch_service.types.domain_use_case.serialize_json(
        value["options"]
    )
    import capo_elasticsearch_service.types.option_status

    out["Status"] = capo_elasticsearch_service.types.option_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UseCaseStatus:
    out: UseCaseStatus = {}  # type: ignore[typeddict-item]
    if data.get("Options") is not None:
        import capo_elasticsearch_service.types.domain_use_case

        out["options"] = (
            capo_elasticsearch_service.types.domain_use_case.deserialize_json(
                data["Options"]
            )
        )
    else:
        import typing

        out["options"] = typing.cast(
            "capo_elasticsearch_service.types.domain_use_case.DomainUseCase", ""
        )
    if data.get("Status") is not None:
        import capo_elasticsearch_service.types.option_status

        out["status"] = capo_elasticsearch_service.types.option_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("UseCaseStatus.status required")
    return out
