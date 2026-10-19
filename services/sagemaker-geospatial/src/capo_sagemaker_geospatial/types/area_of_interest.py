"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#AreaOfInterest``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError, SerializationError
from capo_sagemaker_geospatial.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.area_of_interest_geometry


class _AreaOfInterest_AreaOfInterestGeometry(TypedDict, closed=True):
    AreaOfInterestGeometry: "capo_sagemaker_geospatial.types.area_of_interest_geometry.AreaOfInterestGeometry"


AreaOfInterest: TypeAlias = _AreaOfInterest_AreaOfInterestGeometry | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: AreaOfInterest) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"AreaOfInterest: cannot serialize unknown variant {value.name!r}"
        )
    elif "AreaOfInterestGeometry" in value:
        import capo_sagemaker_geospatial.types.area_of_interest_geometry

        return {
            "AreaOfInterestGeometry": capo_sagemaker_geospatial.types.area_of_interest_geometry.serialize_json(
                value["AreaOfInterestGeometry"]
            )
        }
    else:
        raise SerializationError("AreaOfInterest: no variant present")


def deserialize_json(data: dict) -> AreaOfInterest:
    if data.get("AreaOfInterestGeometry") is not None:
        import capo_sagemaker_geospatial.types.area_of_interest_geometry

        return {
            "AreaOfInterestGeometry": capo_sagemaker_geospatial.types.area_of_interest_geometry.deserialize_json(
                data["AreaOfInterestGeometry"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("AreaOfInterest: no recognized variant key")


def redact_sensitive(value: AreaOfInterest) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "AreaOfInterestGeometry" in value:
        import capo_sagemaker_geospatial.types.area_of_interest_geometry

        out["AreaOfInterestGeometry"] = (
            capo_sagemaker_geospatial.types.area_of_interest_geometry.redact_sensitive(
                value["AreaOfInterestGeometry"]
            )
        )
    return out
