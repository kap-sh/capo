"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalyzerConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError
from capo_accessanalyzer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_accessanalyzer.types.internal_access_configuration
    import capo_accessanalyzer.types.unused_access_configuration


class _AnalyzerConfiguration_unusedAccess(TypedDict, closed=True):
    unusedAccess: "capo_accessanalyzer.types.unused_access_configuration.UnusedAccessConfiguration"


class _AnalyzerConfiguration_internalAccess(TypedDict, closed=True):
    internalAccess: "capo_accessanalyzer.types.internal_access_configuration.InternalAccessConfiguration"


AnalyzerConfiguration: TypeAlias = (
    _AnalyzerConfiguration_unusedAccess
    | _AnalyzerConfiguration_internalAccess
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzerConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AnalyzerConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "unusedAccess" in value:
        import capo_accessanalyzer.types.unused_access_configuration

        return {
            "unusedAccess": capo_accessanalyzer.types.unused_access_configuration.serialize_json(
                value["unusedAccess"]
            )
        }
    elif "internalAccess" in value:
        import capo_accessanalyzer.types.internal_access_configuration

        return {
            "internalAccess": capo_accessanalyzer.types.internal_access_configuration.serialize_json(
                value["internalAccess"]
            )
        }
    else:
        raise SerializationError("AnalyzerConfiguration: no variant present")


def deserialize_json(data: dict) -> AnalyzerConfiguration:
    if data.get("unusedAccess") is not None:
        import capo_accessanalyzer.types.unused_access_configuration

        return {
            "unusedAccess": capo_accessanalyzer.types.unused_access_configuration.deserialize_json(
                data["unusedAccess"]
            )
        }
    elif data.get("internalAccess") is not None:
        import capo_accessanalyzer.types.internal_access_configuration

        return {
            "internalAccess": capo_accessanalyzer.types.internal_access_configuration.deserialize_json(
                data["internalAccess"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AnalyzerConfiguration: no recognized variant key")
