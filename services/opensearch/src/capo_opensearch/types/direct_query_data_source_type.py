"""Generated from Smithy shape ``com.amazonaws.opensearch#DirectQueryDataSourceType``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_opensearch.errors import DeserializationError, SerializationError
from capo_opensearch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_opensearch.types.cloud_watch_direct_query_data_source
    import capo_opensearch.types.prometheus_direct_query_data_source
    import capo_opensearch.types.security_lake_direct_query_data_source


class _DirectQueryDataSourceType_CloudWatchLog(TypedDict, closed=True):
    CloudWatchLog: "capo_opensearch.types.cloud_watch_direct_query_data_source.CloudWatchDirectQueryDataSource"


class _DirectQueryDataSourceType_SecurityLake(TypedDict, closed=True):
    SecurityLake: "capo_opensearch.types.security_lake_direct_query_data_source.SecurityLakeDirectQueryDataSource"


class _DirectQueryDataSourceType_Prometheus(TypedDict, closed=True):
    Prometheus: "capo_opensearch.types.prometheus_direct_query_data_source.PrometheusDirectQueryDataSource"


DirectQueryDataSourceType: TypeAlias = (
    _DirectQueryDataSourceType_CloudWatchLog
    | _DirectQueryDataSourceType_SecurityLake
    | _DirectQueryDataSourceType_Prometheus
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: DirectQueryDataSourceType) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"DirectQueryDataSourceType: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "CloudWatchLog" in value:
        import capo_opensearch.types.cloud_watch_direct_query_data_source

        return {
            "CloudWatchLog": capo_opensearch.types.cloud_watch_direct_query_data_source.serialize_json(
                value["CloudWatchLog"]
            )
        }
    elif "SecurityLake" in value:
        import capo_opensearch.types.security_lake_direct_query_data_source

        return {
            "SecurityLake": capo_opensearch.types.security_lake_direct_query_data_source.serialize_json(
                value["SecurityLake"]
            )
        }
    elif "Prometheus" in value:
        import capo_opensearch.types.prometheus_direct_query_data_source

        return {
            "Prometheus": capo_opensearch.types.prometheus_direct_query_data_source.serialize_json(
                value["Prometheus"]
            )
        }
    else:
        raise SerializationError("DirectQueryDataSourceType: no variant present")


def deserialize_json(data: dict) -> DirectQueryDataSourceType:
    if data.get("CloudWatchLog") is not None:
        import capo_opensearch.types.cloud_watch_direct_query_data_source

        return {
            "CloudWatchLog": capo_opensearch.types.cloud_watch_direct_query_data_source.deserialize_json(
                data["CloudWatchLog"]
            )
        }
    elif data.get("SecurityLake") is not None:
        import capo_opensearch.types.security_lake_direct_query_data_source

        return {
            "SecurityLake": capo_opensearch.types.security_lake_direct_query_data_source.deserialize_json(
                data["SecurityLake"]
            )
        }
    elif data.get("Prometheus") is not None:
        import capo_opensearch.types.prometheus_direct_query_data_source

        return {
            "Prometheus": capo_opensearch.types.prometheus_direct_query_data_source.deserialize_json(
                data["Prometheus"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "DirectQueryDataSourceType: no recognized variant key"
        )
