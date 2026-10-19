"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#IntegrationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError, SerializationError
from capo_cloudwatch_logs.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.open_search_integration_details


class _IntegrationDetails_openSearchIntegrationDetails(TypedDict, closed=True):
    openSearchIntegrationDetails: "capo_cloudwatch_logs.types.open_search_integration_details.OpenSearchIntegrationDetails"


IntegrationDetails: TypeAlias = (
    _IntegrationDetails_openSearchIntegrationDetails | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IntegrationDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"IntegrationDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "openSearchIntegrationDetails" in value:
        import capo_cloudwatch_logs.types.open_search_integration_details

        return {
            "openSearchIntegrationDetails": capo_cloudwatch_logs.types.open_search_integration_details.serialize_aws_json_1_1(
                value["openSearchIntegrationDetails"]
            )
        }
    else:
        raise SerializationError("IntegrationDetails: no variant present")


def deserialize_aws_json_1_1(data: dict) -> IntegrationDetails:
    if data.get("openSearchIntegrationDetails") is not None:
        import capo_cloudwatch_logs.types.open_search_integration_details

        return {
            "openSearchIntegrationDetails": capo_cloudwatch_logs.types.open_search_integration_details.deserialize_aws_json_1_1(
                data["openSearchIntegrationDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("IntegrationDetails: no recognized variant key")
