"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateServiceActionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.service_action_detail


class CreateServiceActionOutput(TypedDict, closed=True):
    service_action_detail: NotRequired[
        "capo_service_catalog.types.service_action_detail.ServiceActionDetail"
    ]
    """<p>An object containing information about the self-service action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateServiceActionOutput) -> dict:
    out: dict = {}
    if "service_action_detail" in value:
        import capo_service_catalog.types.service_action_detail

        out["ServiceActionDetail"] = (
            capo_service_catalog.types.service_action_detail.serialize_aws_json_1_1(
                value["service_action_detail"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateServiceActionOutput:
    out: CreateServiceActionOutput = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionDetail") is not None:
        import capo_service_catalog.types.service_action_detail

        out["service_action_detail"] = (
            capo_service_catalog.types.service_action_detail.deserialize_aws_json_1_1(
                data["ServiceActionDetail"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateServiceActionOutput) -> dict:
    out: dict = {}
    if "service_action_detail" in value:
        import capo_service_catalog.types.service_action_detail

        out["ServiceActionDetail"] = (
            capo_service_catalog.types.service_action_detail.serialize_cbor(
                value["service_action_detail"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> CreateServiceActionOutput:
    out: CreateServiceActionOutput = {}  # type: ignore[typeddict-item]
    if data.get("ServiceActionDetail") is not None:
        import capo_service_catalog.types.service_action_detail

        out["service_action_detail"] = (
            capo_service_catalog.types.service_action_detail.deserialize_cbor(
                data["ServiceActionDetail"]
            )
        )
    return out
