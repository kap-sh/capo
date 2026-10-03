"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#InfluxDBv2Parameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.duration
    import capo_timestream_influxdb.types.log_level
    import capo_timestream_influxdb.types.tracing_type


class InfluxDBv2Parameters(TypedDict, closed=True):
    flux_log_enabled: NotRequired["bool"]
    """<p>Include option to show detailed logs for Flux queries.</p> <p>Default: false</p>"""
    log_level: NotRequired["capo_timestream_influxdb.types.log_level.LogLevel"]
    """<p>Log output level. InfluxDB outputs log entries with severity levels greater than or equal to the level specified.</p> <p>Default: info</p>"""
    no_tasks: NotRequired["bool"]
    """<p>Disable the task scheduler. If problematic tasks prevent InfluxDB from starting, use this option to start InfluxDB without scheduling or executing tasks.</p> <p>Default: false</p>"""
    query_concurrency: NotRequired["int"]
    """<p>Number of queries allowed to execute concurrently. Setting to 0 allows an unlimited number of concurrent queries.</p> <p>Default: 0</p>"""
    query_queue_size: NotRequired["int"]
    """<p>Maximum number of queries allowed in execution queue. When queue limit is reached, new queries are rejected. Setting to 0 allows an unlimited number of queries in the queue.</p> <p>Default: 0</p>"""
    tracing_type: NotRequired["capo_timestream_influxdb.types.tracing_type.TracingType"]
    """<p>Enable tracing in InfluxDB and specifies the tracing type. Tracing is disabled by default.</p>"""
    metrics_disabled: NotRequired["bool"]
    """<p>Disable the HTTP /metrics endpoint which exposes <a href="https://docs.influxdata.com/influxdb/v2/reference/internals/metrics/">internal InfluxDB metrics</a>.</p> <p>Default: false</p>"""
    http_idle_timeout: NotRequired["capo_timestream_influxdb.types.duration.Duration"]
    """<p>Maximum duration the server should keep established connections alive while waiting for new requests. Set to 0 for no timeout.</p> <p>Default: 3 minutes</p>"""
    http_read_header_timeout: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Maximum duration the server should try to read HTTP headers for new requests. Set to 0 for no timeout.</p> <p>Default: 10 seconds</p>"""
    http_read_timeout: NotRequired["capo_timestream_influxdb.types.duration.Duration"]
    """<p>Maximum duration the server should try to read the entirety of new requests. Set to 0 for no timeout.</p> <p>Default: 0</p>"""
    http_write_timeout: NotRequired["capo_timestream_influxdb.types.duration.Duration"]
    """<p>Maximum duration the server should spend processing and responding to write requests. Set to 0 for no timeout.</p> <p>Default: 0</p>"""
    influxql_max_select_buckets: NotRequired["int"]
    """<p>Maximum number of group by time buckets a SELECT statement can create. 0 allows an unlimited number of buckets.</p> <p>Default: 0</p>"""
    influxql_max_select_point: NotRequired["int"]
    """<p>Maximum number of points a SELECT statement can process. 0 allows an unlimited number of points. InfluxDB checks the point count every second (so queries exceeding the maximum aren’t immediately aborted).</p> <p>Default: 0</p>"""
    influxql_max_select_series: NotRequired["int"]
    """<p>Maximum number of series a SELECT statement can return. 0 allows an unlimited number of series.</p> <p>Default: 0</p>"""
    pprof_disabled: NotRequired["bool"]
    """<p>Disable the /debug/pprof HTTP endpoint. This endpoint provides runtime profiling data and can be helpful when debugging.</p> <p>Default: true</p>"""
    query_initial_memory_bytes: NotRequired["int"]
    """<p>Initial bytes of memory allocated for a query.</p> <p>Default: 0</p>"""
    query_max_memory_bytes: NotRequired["int"]
    """<p>Maximum total bytes of memory allowed for all running queries. When this limit is reached, new queries are rejected. Setting to 0 allows unlimited memory usage.</p> <p>Default: 0</p>"""
    query_memory_bytes: NotRequired["int"]
    """<p>Maximum bytes of memory allowed for a single query. Must be greater or equal to queryInitialMemoryBytes.</p> <p>Default: 0</p>"""
    session_length: NotRequired["int"]
    """<p>Specifies the Time to Live (TTL) in minutes for newly created user sessions.</p> <p>Default: 60</p>"""
    session_renew_disabled: NotRequired["bool"]
    """<p>Disables automatically extending a user’s session TTL on each request. By default, every request sets the session’s expiration time to five minutes from now. When disabled, sessions expire after the specified <a href="https://docs.influxdata.com/influxdb/v2/reference/config-options/#session-length">session length</a> and the user is redirected to the login page, even if recently active.</p> <p>Default: false</p>"""
    storage_cache_max_memory_size: NotRequired["int"]
    """<p>Maximum size (in bytes) a shard’s cache can reach before it starts rejecting writes. Must be greater than storageCacheSnapShotMemorySize and lower than instance’s total memory capacity. We recommend setting it to below 15% of the total memory capacity.</p> <p>Default: 1073741824</p>"""
    storage_cache_snapshot_memory_size: NotRequired["int"]
    """<p>Size (in bytes) at which the storage engine will snapshot the cache and write it to a TSM file to make more memory available. Must not be greater than storageCacheMaxMemorySize.</p> <p>Default: 26214400</p>"""
    storage_cache_snapshot_write_cold_duration: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Duration at which the storage engine will snapshot the cache and write it to a new TSM file if the shard hasn’t received writes or deletes.</p> <p>Default: 10 minutes</p>"""
    storage_compact_full_write_cold_duration: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Duration at which the storage engine will compact all TSM files in a shard if it hasn't received writes or deletes.</p> <p>Default: 4 hours</p>"""
    storage_compact_throughput_burst: NotRequired["int"]
    """<p>Rate limit (in bytes per second) that TSM compactions can write to disk.</p> <p>Default: 50331648</p>"""
    storage_max_concurrent_compactions: NotRequired["int"]
    """<p>Maximum number of full and level compactions that can run concurrently. A value of 0 results in 50% of runtime.GOMAXPROCS(0) used at runtime. Any number greater than zero limits compactions to that value. This setting does not apply to cache snapshotting.</p> <p>Default: 0</p>"""
    storage_max_index_log_file_size: NotRequired["int"]
    """<p>Size (in bytes) at which an index write-ahead log (WAL) file will compact into an index file. Lower sizes will cause log files to be compacted more quickly and result in lower heap usage at the expense of write throughput.</p> <p>Default: 1048576</p>"""
    storage_no_validate_field_size: NotRequired["bool"]
    """<p>Skip field size validation on incoming write requests.</p> <p>Default: false</p>"""
    storage_retention_check_interval: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Interval of retention policy enforcement checks. Must be greater than 0.</p> <p>Default: 30 minutes</p>"""
    storage_series_file_max_concurrent_snapshot_compactions: NotRequired["int"]
    """<p>Maximum number of snapshot compactions that can run concurrently across all series partitions in a database.</p> <p>Default: 0</p>"""
    storage_series_id_set_cache_size: NotRequired["int"]
    """<p>Size of the internal cache used in the TSI index to store previously calculated series results. Cached results are returned quickly rather than needing to be recalculated when a subsequent query with the same tag key/value predicate is executed. Setting this value to 0 will disable the cache and may decrease query performance.</p> <p>Default: 100</p>"""
    storage_wal_max_concurrent_writes: NotRequired["int"]
    """<p>Maximum number writes to the WAL directory to attempt at the same time. Setting this value to 0 results in number of processing units available x2.</p> <p>Default: 0</p>"""
    storage_wal_max_write_delay: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Maximum amount of time a write request to the WAL directory will wait when the <a href="https://docs.influxdata.com/influxdb/v2/reference/config-options/#storage-wal-max-concurrent-writes">maximum number of concurrent active writes to the WAL directory has been met</a>. Set to 0 to disable the timeout.</p> <p>Default: 10 minutes</p>"""
    ui_disabled: NotRequired["bool"]
    """<p>Disable the InfluxDB user interface (UI). The UI is enabled by default.</p> <p>Default: false</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InfluxDBv2Parameters) -> dict:
    out: dict = {}
    if "flux_log_enabled" in value:
        out["fluxLogEnabled"] = value["flux_log_enabled"]
    if "log_level" in value:
        import capo_timestream_influxdb.types.log_level

        out["logLevel"] = (
            capo_timestream_influxdb.types.log_level.serialize_aws_json_1_0(
                value["log_level"]
            )
        )
    if "no_tasks" in value:
        out["noTasks"] = value["no_tasks"]
    if "query_concurrency" in value:
        out["queryConcurrency"] = value["query_concurrency"]
    if "query_queue_size" in value:
        out["queryQueueSize"] = value["query_queue_size"]
    if "tracing_type" in value:
        import capo_timestream_influxdb.types.tracing_type

        out["tracingType"] = (
            capo_timestream_influxdb.types.tracing_type.serialize_aws_json_1_0(
                value["tracing_type"]
            )
        )
    if "metrics_disabled" in value:
        out["metricsDisabled"] = value["metrics_disabled"]
    if "http_idle_timeout" in value:
        import capo_timestream_influxdb.types.duration

        out["httpIdleTimeout"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["http_idle_timeout"]
            )
        )
    if "http_read_header_timeout" in value:
        import capo_timestream_influxdb.types.duration

        out["httpReadHeaderTimeout"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["http_read_header_timeout"]
            )
        )
    if "http_read_timeout" in value:
        import capo_timestream_influxdb.types.duration

        out["httpReadTimeout"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["http_read_timeout"]
            )
        )
    if "http_write_timeout" in value:
        import capo_timestream_influxdb.types.duration

        out["httpWriteTimeout"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["http_write_timeout"]
            )
        )
    if "influxql_max_select_buckets" in value:
        out["influxqlMaxSelectBuckets"] = value["influxql_max_select_buckets"]
    if "influxql_max_select_point" in value:
        out["influxqlMaxSelectPoint"] = value["influxql_max_select_point"]
    if "influxql_max_select_series" in value:
        out["influxqlMaxSelectSeries"] = value["influxql_max_select_series"]
    if "pprof_disabled" in value:
        out["pprofDisabled"] = value["pprof_disabled"]
    if "query_initial_memory_bytes" in value:
        out["queryInitialMemoryBytes"] = value["query_initial_memory_bytes"]
    if "query_max_memory_bytes" in value:
        out["queryMaxMemoryBytes"] = value["query_max_memory_bytes"]
    if "query_memory_bytes" in value:
        out["queryMemoryBytes"] = value["query_memory_bytes"]
    if "session_length" in value:
        out["sessionLength"] = value["session_length"]
    if "session_renew_disabled" in value:
        out["sessionRenewDisabled"] = value["session_renew_disabled"]
    if "storage_cache_max_memory_size" in value:
        out["storageCacheMaxMemorySize"] = value["storage_cache_max_memory_size"]
    if "storage_cache_snapshot_memory_size" in value:
        out["storageCacheSnapshotMemorySize"] = value[
            "storage_cache_snapshot_memory_size"
        ]
    if "storage_cache_snapshot_write_cold_duration" in value:
        import capo_timestream_influxdb.types.duration

        out["storageCacheSnapshotWriteColdDuration"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["storage_cache_snapshot_write_cold_duration"]
            )
        )
    if "storage_compact_full_write_cold_duration" in value:
        import capo_timestream_influxdb.types.duration

        out["storageCompactFullWriteColdDuration"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["storage_compact_full_write_cold_duration"]
            )
        )
    if "storage_compact_throughput_burst" in value:
        out["storageCompactThroughputBurst"] = value["storage_compact_throughput_burst"]
    if "storage_max_concurrent_compactions" in value:
        out["storageMaxConcurrentCompactions"] = value[
            "storage_max_concurrent_compactions"
        ]
    if "storage_max_index_log_file_size" in value:
        out["storageMaxIndexLogFileSize"] = value["storage_max_index_log_file_size"]
    if "storage_no_validate_field_size" in value:
        out["storageNoValidateFieldSize"] = value["storage_no_validate_field_size"]
    if "storage_retention_check_interval" in value:
        import capo_timestream_influxdb.types.duration

        out["storageRetentionCheckInterval"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["storage_retention_check_interval"]
            )
        )
    if "storage_series_file_max_concurrent_snapshot_compactions" in value:
        out["storageSeriesFileMaxConcurrentSnapshotCompactions"] = value[
            "storage_series_file_max_concurrent_snapshot_compactions"
        ]
    if "storage_series_id_set_cache_size" in value:
        out["storageSeriesIdSetCacheSize"] = value["storage_series_id_set_cache_size"]
    if "storage_wal_max_concurrent_writes" in value:
        out["storageWalMaxConcurrentWrites"] = value[
            "storage_wal_max_concurrent_writes"
        ]
    if "storage_wal_max_write_delay" in value:
        import capo_timestream_influxdb.types.duration

        out["storageWalMaxWriteDelay"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["storage_wal_max_write_delay"]
            )
        )
    if "ui_disabled" in value:
        out["uiDisabled"] = value["ui_disabled"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InfluxDBv2Parameters:
    out: InfluxDBv2Parameters = {}  # type: ignore[typeddict-item]
    if data.get("fluxLogEnabled") is not None:
        out["flux_log_enabled"] = data["fluxLogEnabled"]
    if data.get("logLevel") is not None:
        import capo_timestream_influxdb.types.log_level

        out["log_level"] = (
            capo_timestream_influxdb.types.log_level.deserialize_aws_json_1_0(
                data["logLevel"]
            )
        )
    if data.get("noTasks") is not None:
        out["no_tasks"] = data["noTasks"]
    if data.get("queryConcurrency") is not None:
        out["query_concurrency"] = data["queryConcurrency"]
    if data.get("queryQueueSize") is not None:
        out["query_queue_size"] = data["queryQueueSize"]
    if data.get("tracingType") is not None:
        import capo_timestream_influxdb.types.tracing_type

        out["tracing_type"] = (
            capo_timestream_influxdb.types.tracing_type.deserialize_aws_json_1_0(
                data["tracingType"]
            )
        )
    if data.get("metricsDisabled") is not None:
        out["metrics_disabled"] = data["metricsDisabled"]
    if data.get("httpIdleTimeout") is not None:
        import capo_timestream_influxdb.types.duration

        out["http_idle_timeout"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["httpIdleTimeout"]
            )
        )
    if data.get("httpReadHeaderTimeout") is not None:
        import capo_timestream_influxdb.types.duration

        out["http_read_header_timeout"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["httpReadHeaderTimeout"]
            )
        )
    if data.get("httpReadTimeout") is not None:
        import capo_timestream_influxdb.types.duration

        out["http_read_timeout"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["httpReadTimeout"]
            )
        )
    if data.get("httpWriteTimeout") is not None:
        import capo_timestream_influxdb.types.duration

        out["http_write_timeout"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["httpWriteTimeout"]
            )
        )
    if data.get("influxqlMaxSelectBuckets") is not None:
        out["influxql_max_select_buckets"] = data["influxqlMaxSelectBuckets"]
    if data.get("influxqlMaxSelectPoint") is not None:
        out["influxql_max_select_point"] = data["influxqlMaxSelectPoint"]
    if data.get("influxqlMaxSelectSeries") is not None:
        out["influxql_max_select_series"] = data["influxqlMaxSelectSeries"]
    if data.get("pprofDisabled") is not None:
        out["pprof_disabled"] = data["pprofDisabled"]
    if data.get("queryInitialMemoryBytes") is not None:
        out["query_initial_memory_bytes"] = data["queryInitialMemoryBytes"]
    if data.get("queryMaxMemoryBytes") is not None:
        out["query_max_memory_bytes"] = data["queryMaxMemoryBytes"]
    if data.get("queryMemoryBytes") is not None:
        out["query_memory_bytes"] = data["queryMemoryBytes"]
    if data.get("sessionLength") is not None:
        out["session_length"] = data["sessionLength"]
    if data.get("sessionRenewDisabled") is not None:
        out["session_renew_disabled"] = data["sessionRenewDisabled"]
    if data.get("storageCacheMaxMemorySize") is not None:
        out["storage_cache_max_memory_size"] = data["storageCacheMaxMemorySize"]
    if data.get("storageCacheSnapshotMemorySize") is not None:
        out["storage_cache_snapshot_memory_size"] = data[
            "storageCacheSnapshotMemorySize"
        ]
    if data.get("storageCacheSnapshotWriteColdDuration") is not None:
        import capo_timestream_influxdb.types.duration

        out["storage_cache_snapshot_write_cold_duration"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["storageCacheSnapshotWriteColdDuration"]
            )
        )
    if data.get("storageCompactFullWriteColdDuration") is not None:
        import capo_timestream_influxdb.types.duration

        out["storage_compact_full_write_cold_duration"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["storageCompactFullWriteColdDuration"]
            )
        )
    if data.get("storageCompactThroughputBurst") is not None:
        out["storage_compact_throughput_burst"] = data["storageCompactThroughputBurst"]
    if data.get("storageMaxConcurrentCompactions") is not None:
        out["storage_max_concurrent_compactions"] = data[
            "storageMaxConcurrentCompactions"
        ]
    if data.get("storageMaxIndexLogFileSize") is not None:
        out["storage_max_index_log_file_size"] = data["storageMaxIndexLogFileSize"]
    if data.get("storageNoValidateFieldSize") is not None:
        out["storage_no_validate_field_size"] = data["storageNoValidateFieldSize"]
    if data.get("storageRetentionCheckInterval") is not None:
        import capo_timestream_influxdb.types.duration

        out["storage_retention_check_interval"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["storageRetentionCheckInterval"]
            )
        )
    if data.get("storageSeriesFileMaxConcurrentSnapshotCompactions") is not None:
        out["storage_series_file_max_concurrent_snapshot_compactions"] = data[
            "storageSeriesFileMaxConcurrentSnapshotCompactions"
        ]
    if data.get("storageSeriesIdSetCacheSize") is not None:
        out["storage_series_id_set_cache_size"] = data["storageSeriesIdSetCacheSize"]
    if data.get("storageWalMaxConcurrentWrites") is not None:
        out["storage_wal_max_concurrent_writes"] = data["storageWalMaxConcurrentWrites"]
    if data.get("storageWalMaxWriteDelay") is not None:
        import capo_timestream_influxdb.types.duration

        out["storage_wal_max_write_delay"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["storageWalMaxWriteDelay"]
            )
        )
    if data.get("uiDisabled") is not None:
        out["ui_disabled"] = data["uiDisabled"]
    return out
