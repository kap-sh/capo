"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SourceConnectionParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.code_star_parameters


class SourceConnectionParameters(TypedDict, closed=True):
    code_star: NotRequired[
        "capo_service_catalog.types.code_star_parameters.CodeStarParameters"
    ]
    """<p>Provides <code>ConnectionType</code> details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceConnectionParameters) -> dict:
    out: dict = {}
    if "code_star" in value:
        import capo_service_catalog.types.code_star_parameters

        out["CodeStar"] = (
            capo_service_catalog.types.code_star_parameters.serialize_aws_json_1_1(
                value["code_star"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceConnectionParameters:
    out: SourceConnectionParameters = {}  # type: ignore[typeddict-item]
    if data.get("CodeStar") is not None:
        import capo_service_catalog.types.code_star_parameters

        out["code_star"] = (
            capo_service_catalog.types.code_star_parameters.deserialize_aws_json_1_1(
                data["CodeStar"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SourceConnectionParameters) -> dict:
    out: dict = {}
    if "code_star" in value:
        import capo_service_catalog.types.code_star_parameters

        out["CodeStar"] = (
            capo_service_catalog.types.code_star_parameters.serialize_cbor(
                value["code_star"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> SourceConnectionParameters:
    out: SourceConnectionParameters = {}  # type: ignore[typeddict-item]
    if data.get("CodeStar") is not None:
        import capo_service_catalog.types.code_star_parameters

        out["code_star"] = (
            capo_service_catalog.types.code_star_parameters.deserialize_cbor(
                data["CodeStar"]
            )
        )
    return out
