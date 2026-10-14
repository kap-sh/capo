"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#ResourceInUseException``."""

from typing import TYPE_CHECKING

import zapros
from typing_extensions import NotRequired, TypedDict

from capo_lex_model_building_service.errors import ServiceError

if TYPE_CHECKING:
    import capo_lex_model_building_service.types.reference_type
    import capo_lex_model_building_service.types.resource_reference


class ResourceInUseException_(TypedDict, closed=True):
    reference_type: NotRequired[
        "capo_lex_model_building_service.types.reference_type.ReferenceType"
    ]
    example_reference: NotRequired[
        "capo_lex_model_building_service.types.resource_reference.ResourceReference"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceInUseException_) -> dict:
    out: dict = {}
    if "reference_type" in value:
        import capo_lex_model_building_service.types.reference_type

        out["referenceType"] = (
            capo_lex_model_building_service.types.reference_type.serialize_json(
                value["reference_type"]
            )
        )
    if "example_reference" in value:
        import capo_lex_model_building_service.types.resource_reference

        out["exampleReference"] = (
            capo_lex_model_building_service.types.resource_reference.serialize_json(
                value["example_reference"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResourceInUseException_:
    out: ResourceInUseException_ = {}  # type: ignore[typeddict-item]
    if data.get("referenceType") is not None:
        import capo_lex_model_building_service.types.reference_type

        out["reference_type"] = (
            capo_lex_model_building_service.types.reference_type.deserialize_json(
                data["referenceType"]
            )
        )
    if data.get("exampleReference") is not None:
        import capo_lex_model_building_service.types.resource_reference

        out["example_reference"] = (
            capo_lex_model_building_service.types.resource_reference.deserialize_json(
                data["exampleReference"]
            )
        )
    return out


class ResourceInUseException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.lexmodelbuildingservice#ResourceInUseException``."""

    code: str | None = "ResourceInUseException"

    def __init__(
        self,
        data: ResourceInUseException_,
        message: str | None = None,
        *,
        response: zapros.Response,
    ):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="ResourceInUseException",
            message=message,
            response=response,
        )
        self.data = data

    @classmethod
    def from_json(
        cls, data: dict, message: str | None = None, *, response: zapros.Response
    ) -> "ResourceInUseException":
        return cls(deserialize_json(data), message, response=response)
