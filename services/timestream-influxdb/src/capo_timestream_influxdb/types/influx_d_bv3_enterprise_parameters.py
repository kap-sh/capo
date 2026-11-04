"""Generated from Smithy shape ``com.amazonaws.timestreaminfluxdb#InfluxDBv3EnterpriseParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_timestream_influxdb.types.data_fusion_runtime_type
    import capo_timestream_influxdb.types.duration
    import capo_timestream_influxdb.types.log_formats
    import capo_timestream_influxdb.types.percent_or_absolute_long
    import capo_timestream_influxdb.types.plugin_repository_secret_arn


class InfluxDBv3EnterpriseParameters(TypedDict, closed=True):
    query_file_limit: NotRequired["int"]
    """<p>Limits the number of Parquet files a query can access. If a query attempts to read more than this limit, InfluxDB 3 returns an error.</p> <p>Default: 432</p>"""
    query_log_size: NotRequired["int"]
    """<p>Defines the size of the query log. Up to this many queries remain in the log before older queries are evicted to make room for new ones.</p> <p>Default: 1000</p>"""
    log_filter: NotRequired["str"]
    """<p>Sets the filter directive for logs.</p>"""
    log_format: NotRequired["capo_timestream_influxdb.types.log_formats.LogFormats"]
    """<p>Defines the message format for logs.</p> <p>Default: full</p>"""
    data_fusion_num_threads: NotRequired["int"]
    """<p>Sets the maximum number of DataFusion runtime threads to use.</p>"""
    data_fusion_runtime_type: NotRequired[
        "capo_timestream_influxdb.types.data_fusion_runtime_type.DataFusionRuntimeType"
    ]
    """<p>Specifies the DataFusion tokio runtime type.</p> <p>Default: multi-thread</p>"""
    data_fusion_runtime_disable_lifo_slot: NotRequired["bool"]
    """<p>Disables the LIFO slot of the DataFusion runtime.</p>"""
    data_fusion_runtime_event_interval: NotRequired["int"]
    """<p>Sets the number of scheduler ticks after which the scheduler of the DataFusion tokio runtime polls for external events–for example: timers, I/O.</p>"""
    data_fusion_runtime_global_queue_interval: NotRequired["int"]
    """<p>Sets the number of scheduler ticks after which the scheduler of the DataFusion runtime polls the global task queue.</p>"""
    data_fusion_runtime_max_blocking_threads: NotRequired["int"]
    """<p>Specifies the limit for additional threads spawned by the DataFusion runtime.</p>"""
    data_fusion_runtime_max_io_events_per_tick: NotRequired["int"]
    """<p>Configures the maximum number of events processed per tick by the tokio DataFusion runtime.</p>"""
    data_fusion_runtime_thread_keep_alive: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Sets a custom timeout for a thread in the blocking pool of the tokio DataFusion runtime.</p>"""
    data_fusion_runtime_thread_priority: NotRequired["int"]
    """<p>Sets the thread priority for tokio DataFusion runtime workers.</p> <p>Default: 10</p>"""
    data_fusion_max_parquet_fanout: NotRequired["int"]
    """<p>When multiple parquet files are required in a sorted way (deduplication for example), specifies the maximum fanout.</p> <p>Default: 1000</p>"""
    data_fusion_use_cached_parquet_loader: NotRequired["bool"]
    """<p>Uses a cached parquet loader when reading parquet files from the object store.</p>"""
    data_fusion_config: NotRequired["str"]
    """<p>Provides custom configuration to DataFusion as a comma-separated list of key:value pairs.</p>"""
    max_http_request_size: NotRequired["int"]
    """<p>Specifies the maximum size of HTTP requests.</p> <p>Default: 10485760</p>"""
    force_snapshot_mem_threshold: NotRequired[
        "capo_timestream_influxdb.types.percent_or_absolute_long.PercentOrAbsoluteLong"
    ]
    """<p>Specifies the threshold for the internal memory buffer. Supports either a percentage (portion of available memory) or absolute value in MB–for example: 70% or 100</p> <p>Default: 70%</p>"""
    wal_snapshot_size: NotRequired["int"]
    """<p>Defines the number of WAL files to attempt to remove in a snapshot. This, multiplied by the interval, determines how often snapshots are taken.</p> <p>Default: 600</p>"""
    wal_max_write_buffer_size: NotRequired["int"]
    """<p>Specifies the maximum number of write requests that can be buffered before a flush must be executed and succeed.</p> <p>Default: 100000</p>"""
    snapshotted_wal_files_to_keep: NotRequired["int"]
    """<p>Specifies the number of snapshotted WAL files to retain in the object store. Flushing the WAL files does not clear the WAL files immediately; they are deleted when the number of snapshotted WAL files exceeds this number.</p> <p>Default: 300</p>"""
    preemptive_cache_age: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the interval to prefetch into the Parquet cache during compaction.</p> <p>Default: 3d</p>"""
    parquet_mem_cache_prune_percentage: NotRequired["float"]
    """<p>Specifies the percentage of entries to prune during a prune operation on the in-memory Parquet cache.</p> <p>Default: 0.1</p>"""
    parquet_mem_cache_prune_interval: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Sets the interval to check if the in-memory Parquet cache needs to be pruned.</p> <p>Default: 1s</p>"""
    disable_parquet_mem_cache: NotRequired["bool"]
    """<p>Disables the in-memory Parquet cache. By default, the cache is enabled.</p>"""
    parquet_mem_cache_query_path_duration: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the time window for caching recent Parquet files in memory.</p> <p>Default: 5h</p>"""
    last_cache_eviction_interval: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the interval to evict expired entries from the Last-N-Value cache, expressed as a human-readable duration–for example: 20s, 1m, 1h.</p> <p>Default: 10s</p>"""
    distinct_cache_eviction_interval: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the interval to evict expired entries from the distinct value cache, expressed as a human-readable duration–for example: 20s, 1m, 1h.</p> <p>Default: 10s</p>"""
    gen1_duration: NotRequired["capo_timestream_influxdb.types.duration.Duration"]
    """<p>Specifies the duration that Parquet files are arranged into. Data timestamps land each row into a file of this duration. Supported durations are 1m, 5m, and 10m. These files are known as “generation 1” files, which the compactor can merge into larger generations.</p> <p>Default: 10m</p>"""
    exec_mem_pool_bytes: NotRequired[
        "capo_timestream_influxdb.types.percent_or_absolute_long.PercentOrAbsoluteLong"
    ]
    """<p>Specifies the size of memory pool used during query execution. Can be given as absolute value in bytes or as a percentage of the total available memory–for example: 8000000000 or 10%.</p> <p>Default: 20%</p>"""
    parquet_mem_cache_size: NotRequired[
        "capo_timestream_influxdb.types.percent_or_absolute_long.PercentOrAbsoluteLong"
    ]
    """<p>Specifies the size of the in-memory Parquet cache in megabytes or percentage of total available memory.</p> <p>Default: 20%</p>"""
    wal_replay_fail_on_error: NotRequired["bool"]
    """<p>Determines whether WAL replay should fail when encountering errors.</p> <p>Default: false</p>"""
    wal_replay_concurrency_limit: NotRequired["int"]
    """<p>Concurrency limit during WAL replay. Setting this number too high can lead to OOM. The default is dynamically determined.</p> <p>Default: max(num_cpus, 10)</p>"""
    table_index_cache_max_entries: NotRequired["int"]
    """<p>Specifies the maximum number of entries in the table index cache.</p> <p>Default: 1000</p>"""
    table_index_cache_concurrency_limit: NotRequired["int"]
    """<p>Limits the concurrency level for table index cache operations.</p> <p>Default: 8</p>"""
    gen1_lookback_duration: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies how far back to look when creating generation 1 Parquet files.</p> <p>Default: 24h</p>"""
    retention_check_interval: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>The interval at which retention policies are checked and enforced. Enter as a human-readable time–for example: 30m or 1h.</p> <p>Default: 30m</p>"""
    delete_grace_period: NotRequired["capo_timestream_influxdb.types.duration.Duration"]
    """<p>Specifies the grace period before permanently deleting data.</p> <p>Default: 24h</p>"""
    hard_delete_default_duration: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Sets the default duration for hard deletion of data.</p> <p>Default: 90d</p>"""
    plugin_repository_url: NotRequired["str"]
    """<p>Specifies the URL of the repository that InfluxDB downloads plugins from.</p>"""
    plugin_repository_secret_arn: NotRequired[
        "capo_timestream_influxdb.types.plugin_repository_secret_arn.PluginRepositorySecretArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Secrets Manager secret that holds your repository access token.</p>"""
    ingest_query_instances: "int"
    """<p>Specifies number of instances in the DbCluster which can both ingest and query.</p>"""
    query_only_instances: "int"
    """<p>Specifies number of instances in the DbCluster which can only query.</p>"""
    dedicated_compactor: "bool"
    """<p>Specifies if the compactor instance should be a standalone instance or not.</p>"""
    compaction_row_limit: NotRequired["int"]
    """<p>Specifies the soft limit for the number of rows per file that the compactor writes. The compactor may write more rows than this limit.</p> <p>Default: 1000000</p>"""
    compaction_max_num_files_per_plan: NotRequired["int"]
    """<p>Sets the maximum number of files included in any compaction plan.</p> <p>Default: 500</p>"""
    compaction_gen2_duration: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the duration of the first level of compaction (gen2). Later levels of compaction are multiples of this duration. This value should be equal to or greater than the gen1 duration.</p> <p>Default: 20m</p>"""
    compaction_multipliers: NotRequired["str"]
    """<p>Specifies a comma-separated list of multiples defining the duration of each level of compaction. The number of elements in the list determines the number of compaction levels. The first element specifies the duration of the first level (gen3); subsequent levels are multiples of the previous level.</p> <p>Default: 3,4,6,5</p>"""
    compaction_cleanup_wait: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the amount of time that the compactor waits after finishing a compaction run to delete files marked as needing deletion during that compaction run.</p> <p>Default: 10m</p>"""
    compaction_check_interval: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies how often the compactor checks for new compaction work to perform.</p> <p>Default: 10s</p>"""
    last_value_cache_disable_from_history: NotRequired["bool"]
    """<p>Disables populating the last-N-value cache from historical data. If disabled, the cache is still populated with data from the write-ahead log (WAL).</p>"""
    distinct_value_cache_disable_from_history: NotRequired["bool"]
    """<p>Disables populating the distinct value cache from historical data. If disabled, the cache is still populated with data from the write-ahead log (WAL).</p>"""
    replication_interval: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Specifies the interval at which data replication occurs between cluster nodes.</p> <p>Default: 250ms</p>"""
    catalog_sync_interval: NotRequired[
        "capo_timestream_influxdb.types.duration.Duration"
    ]
    """<p>Defines how often the catalog synchronizes across cluster nodes.</p> <p>Default: 10s</p>"""
    upgrade_pacha_tree: NotRequired["bool"]
    """<p>Specifies whether to migrate the cluster from the Parquet storage engine to PachaTree. This action cannot be reversed. To create a new cluster on Parquet, set this to false.</p>"""
    wal_buffer_size: NotRequired["int"]
    """<p>The maximum size, in bytes, of the in-memory WAL buffer before a flush is triggered regardless of the flush interval. Increase this value if WAL files are flushed before the interval elapses.</p>"""
    snapshot_size: NotRequired[
        "capo_timestream_influxdb.types.percent_or_absolute_long.PercentOrAbsoluteLong"
    ]
    """<p>The maximum size of the active snapshot bucket before it is rotated for snapshotting.</p>"""
    snapshot_duration: NotRequired["capo_timestream_influxdb.types.duration.Duration"]
    """<p>The time-based trigger that controls how often the ingester creates snapshots. This value is also used on query nodes as the bucket rotation interval for the replica buffer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InfluxDBv3EnterpriseParameters) -> dict:
    out: dict = {}
    if "query_file_limit" in value:
        out["queryFileLimit"] = value["query_file_limit"]
    if "query_log_size" in value:
        out["queryLogSize"] = value["query_log_size"]
    if "log_filter" in value:
        out["logFilter"] = value["log_filter"]
    if "log_format" in value:
        import capo_timestream_influxdb.types.log_formats

        out["logFormat"] = (
            capo_timestream_influxdb.types.log_formats.serialize_aws_json_1_0(
                value["log_format"]
            )
        )
    if "data_fusion_num_threads" in value:
        out["dataFusionNumThreads"] = value["data_fusion_num_threads"]
    if "data_fusion_runtime_type" in value:
        import capo_timestream_influxdb.types.data_fusion_runtime_type

        out["dataFusionRuntimeType"] = (
            capo_timestream_influxdb.types.data_fusion_runtime_type.serialize_aws_json_1_0(
                value["data_fusion_runtime_type"]
            )
        )
    if "data_fusion_runtime_disable_lifo_slot" in value:
        out["dataFusionRuntimeDisableLifoSlot"] = value[
            "data_fusion_runtime_disable_lifo_slot"
        ]
    if "data_fusion_runtime_event_interval" in value:
        out["dataFusionRuntimeEventInterval"] = value[
            "data_fusion_runtime_event_interval"
        ]
    if "data_fusion_runtime_global_queue_interval" in value:
        out["dataFusionRuntimeGlobalQueueInterval"] = value[
            "data_fusion_runtime_global_queue_interval"
        ]
    if "data_fusion_runtime_max_blocking_threads" in value:
        out["dataFusionRuntimeMaxBlockingThreads"] = value[
            "data_fusion_runtime_max_blocking_threads"
        ]
    if "data_fusion_runtime_max_io_events_per_tick" in value:
        out["dataFusionRuntimeMaxIoEventsPerTick"] = value[
            "data_fusion_runtime_max_io_events_per_tick"
        ]
    if "data_fusion_runtime_thread_keep_alive" in value:
        import capo_timestream_influxdb.types.duration

        out["dataFusionRuntimeThreadKeepAlive"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["data_fusion_runtime_thread_keep_alive"]
            )
        )
    if "data_fusion_runtime_thread_priority" in value:
        out["dataFusionRuntimeThreadPriority"] = value[
            "data_fusion_runtime_thread_priority"
        ]
    if "data_fusion_max_parquet_fanout" in value:
        out["dataFusionMaxParquetFanout"] = value["data_fusion_max_parquet_fanout"]
    if "data_fusion_use_cached_parquet_loader" in value:
        out["dataFusionUseCachedParquetLoader"] = value[
            "data_fusion_use_cached_parquet_loader"
        ]
    if "data_fusion_config" in value:
        out["dataFusionConfig"] = value["data_fusion_config"]
    if "max_http_request_size" in value:
        out["maxHttpRequestSize"] = value["max_http_request_size"]
    if "force_snapshot_mem_threshold" in value:
        import capo_timestream_influxdb.types.percent_or_absolute_long

        out["forceSnapshotMemThreshold"] = (
            capo_timestream_influxdb.types.percent_or_absolute_long.serialize_aws_json_1_0(
                value["force_snapshot_mem_threshold"]
            )
        )
    if "wal_snapshot_size" in value:
        out["walSnapshotSize"] = value["wal_snapshot_size"]
    if "wal_max_write_buffer_size" in value:
        out["walMaxWriteBufferSize"] = value["wal_max_write_buffer_size"]
    if "snapshotted_wal_files_to_keep" in value:
        out["snapshottedWalFilesToKeep"] = value["snapshotted_wal_files_to_keep"]
    if "preemptive_cache_age" in value:
        import capo_timestream_influxdb.types.duration

        out["preemptiveCacheAge"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["preemptive_cache_age"]
            )
        )
    if "parquet_mem_cache_prune_percentage" in value:
        out["parquetMemCachePrunePercentage"] = (
            "NaN"
            if value["parquet_mem_cache_prune_percentage"]
            != value["parquet_mem_cache_prune_percentage"]
            else "Infinity"
            if value["parquet_mem_cache_prune_percentage"] == float("inf")
            else "-Infinity"
            if value["parquet_mem_cache_prune_percentage"] == float("-inf")
            else value["parquet_mem_cache_prune_percentage"]
        )
    if "parquet_mem_cache_prune_interval" in value:
        import capo_timestream_influxdb.types.duration

        out["parquetMemCachePruneInterval"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["parquet_mem_cache_prune_interval"]
            )
        )
    if "disable_parquet_mem_cache" in value:
        out["disableParquetMemCache"] = value["disable_parquet_mem_cache"]
    if "parquet_mem_cache_query_path_duration" in value:
        import capo_timestream_influxdb.types.duration

        out["parquetMemCacheQueryPathDuration"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["parquet_mem_cache_query_path_duration"]
            )
        )
    if "last_cache_eviction_interval" in value:
        import capo_timestream_influxdb.types.duration

        out["lastCacheEvictionInterval"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["last_cache_eviction_interval"]
            )
        )
    if "distinct_cache_eviction_interval" in value:
        import capo_timestream_influxdb.types.duration

        out["distinctCacheEvictionInterval"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["distinct_cache_eviction_interval"]
            )
        )
    if "gen1_duration" in value:
        import capo_timestream_influxdb.types.duration

        out["gen1Duration"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["gen1_duration"]
            )
        )
    if "exec_mem_pool_bytes" in value:
        import capo_timestream_influxdb.types.percent_or_absolute_long

        out["execMemPoolBytes"] = (
            capo_timestream_influxdb.types.percent_or_absolute_long.serialize_aws_json_1_0(
                value["exec_mem_pool_bytes"]
            )
        )
    if "parquet_mem_cache_size" in value:
        import capo_timestream_influxdb.types.percent_or_absolute_long

        out["parquetMemCacheSize"] = (
            capo_timestream_influxdb.types.percent_or_absolute_long.serialize_aws_json_1_0(
                value["parquet_mem_cache_size"]
            )
        )
    if "wal_replay_fail_on_error" in value:
        out["walReplayFailOnError"] = value["wal_replay_fail_on_error"]
    if "wal_replay_concurrency_limit" in value:
        out["walReplayConcurrencyLimit"] = value["wal_replay_concurrency_limit"]
    if "table_index_cache_max_entries" in value:
        out["tableIndexCacheMaxEntries"] = value["table_index_cache_max_entries"]
    if "table_index_cache_concurrency_limit" in value:
        out["tableIndexCacheConcurrencyLimit"] = value[
            "table_index_cache_concurrency_limit"
        ]
    if "gen1_lookback_duration" in value:
        import capo_timestream_influxdb.types.duration

        out["gen1LookbackDuration"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["gen1_lookback_duration"]
            )
        )
    if "retention_check_interval" in value:
        import capo_timestream_influxdb.types.duration

        out["retentionCheckInterval"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["retention_check_interval"]
            )
        )
    if "delete_grace_period" in value:
        import capo_timestream_influxdb.types.duration

        out["deleteGracePeriod"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["delete_grace_period"]
            )
        )
    if "hard_delete_default_duration" in value:
        import capo_timestream_influxdb.types.duration

        out["hardDeleteDefaultDuration"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["hard_delete_default_duration"]
            )
        )
    if "plugin_repository_url" in value:
        out["pluginRepositoryUrl"] = value["plugin_repository_url"]
    if "plugin_repository_secret_arn" in value:
        out["pluginRepositorySecretArn"] = value["plugin_repository_secret_arn"]
    out["ingestQueryInstances"] = value["ingest_query_instances"]
    out["queryOnlyInstances"] = value["query_only_instances"]
    out["dedicatedCompactor"] = value["dedicated_compactor"]
    if "compaction_row_limit" in value:
        out["compactionRowLimit"] = value["compaction_row_limit"]
    if "compaction_max_num_files_per_plan" in value:
        out["compactionMaxNumFilesPerPlan"] = value["compaction_max_num_files_per_plan"]
    if "compaction_gen2_duration" in value:
        import capo_timestream_influxdb.types.duration

        out["compactionGen2Duration"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["compaction_gen2_duration"]
            )
        )
    if "compaction_multipliers" in value:
        out["compactionMultipliers"] = value["compaction_multipliers"]
    if "compaction_cleanup_wait" in value:
        import capo_timestream_influxdb.types.duration

        out["compactionCleanupWait"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["compaction_cleanup_wait"]
            )
        )
    if "compaction_check_interval" in value:
        import capo_timestream_influxdb.types.duration

        out["compactionCheckInterval"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["compaction_check_interval"]
            )
        )
    if "last_value_cache_disable_from_history" in value:
        out["lastValueCacheDisableFromHistory"] = value[
            "last_value_cache_disable_from_history"
        ]
    if "distinct_value_cache_disable_from_history" in value:
        out["distinctValueCacheDisableFromHistory"] = value[
            "distinct_value_cache_disable_from_history"
        ]
    if "replication_interval" in value:
        import capo_timestream_influxdb.types.duration

        out["replicationInterval"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["replication_interval"]
            )
        )
    if "catalog_sync_interval" in value:
        import capo_timestream_influxdb.types.duration

        out["catalogSyncInterval"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["catalog_sync_interval"]
            )
        )
    if "upgrade_pacha_tree" in value:
        out["upgradePachaTree"] = value["upgrade_pacha_tree"]
    if "wal_buffer_size" in value:
        out["walBufferSize"] = value["wal_buffer_size"]
    if "snapshot_size" in value:
        import capo_timestream_influxdb.types.percent_or_absolute_long

        out["snapshotSize"] = (
            capo_timestream_influxdb.types.percent_or_absolute_long.serialize_aws_json_1_0(
                value["snapshot_size"]
            )
        )
    if "snapshot_duration" in value:
        import capo_timestream_influxdb.types.duration

        out["snapshotDuration"] = (
            capo_timestream_influxdb.types.duration.serialize_aws_json_1_0(
                value["snapshot_duration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> InfluxDBv3EnterpriseParameters:
    out: InfluxDBv3EnterpriseParameters = {}  # type: ignore[typeddict-item]
    if data.get("queryFileLimit") is not None:
        out["query_file_limit"] = data["queryFileLimit"]
    if data.get("queryLogSize") is not None:
        out["query_log_size"] = data["queryLogSize"]
    if data.get("logFilter") is not None:
        out["log_filter"] = data["logFilter"]
    if data.get("logFormat") is not None:
        import capo_timestream_influxdb.types.log_formats

        out["log_format"] = (
            capo_timestream_influxdb.types.log_formats.deserialize_aws_json_1_0(
                data["logFormat"]
            )
        )
    if data.get("dataFusionNumThreads") is not None:
        out["data_fusion_num_threads"] = data["dataFusionNumThreads"]
    if data.get("dataFusionRuntimeType") is not None:
        import capo_timestream_influxdb.types.data_fusion_runtime_type

        out["data_fusion_runtime_type"] = (
            capo_timestream_influxdb.types.data_fusion_runtime_type.deserialize_aws_json_1_0(
                data["dataFusionRuntimeType"]
            )
        )
    if data.get("dataFusionRuntimeDisableLifoSlot") is not None:
        out["data_fusion_runtime_disable_lifo_slot"] = data[
            "dataFusionRuntimeDisableLifoSlot"
        ]
    if data.get("dataFusionRuntimeEventInterval") is not None:
        out["data_fusion_runtime_event_interval"] = data[
            "dataFusionRuntimeEventInterval"
        ]
    if data.get("dataFusionRuntimeGlobalQueueInterval") is not None:
        out["data_fusion_runtime_global_queue_interval"] = data[
            "dataFusionRuntimeGlobalQueueInterval"
        ]
    if data.get("dataFusionRuntimeMaxBlockingThreads") is not None:
        out["data_fusion_runtime_max_blocking_threads"] = data[
            "dataFusionRuntimeMaxBlockingThreads"
        ]
    if data.get("dataFusionRuntimeMaxIoEventsPerTick") is not None:
        out["data_fusion_runtime_max_io_events_per_tick"] = data[
            "dataFusionRuntimeMaxIoEventsPerTick"
        ]
    if data.get("dataFusionRuntimeThreadKeepAlive") is not None:
        import capo_timestream_influxdb.types.duration

        out["data_fusion_runtime_thread_keep_alive"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["dataFusionRuntimeThreadKeepAlive"]
            )
        )
    if data.get("dataFusionRuntimeThreadPriority") is not None:
        out["data_fusion_runtime_thread_priority"] = data[
            "dataFusionRuntimeThreadPriority"
        ]
    if data.get("dataFusionMaxParquetFanout") is not None:
        out["data_fusion_max_parquet_fanout"] = data["dataFusionMaxParquetFanout"]
    if data.get("dataFusionUseCachedParquetLoader") is not None:
        out["data_fusion_use_cached_parquet_loader"] = data[
            "dataFusionUseCachedParquetLoader"
        ]
    if data.get("dataFusionConfig") is not None:
        out["data_fusion_config"] = data["dataFusionConfig"]
    if data.get("maxHttpRequestSize") is not None:
        out["max_http_request_size"] = data["maxHttpRequestSize"]
    if data.get("forceSnapshotMemThreshold") is not None:
        import capo_timestream_influxdb.types.percent_or_absolute_long

        out["force_snapshot_mem_threshold"] = (
            capo_timestream_influxdb.types.percent_or_absolute_long.deserialize_aws_json_1_0(
                data["forceSnapshotMemThreshold"]
            )
        )
    if data.get("walSnapshotSize") is not None:
        out["wal_snapshot_size"] = data["walSnapshotSize"]
    if data.get("walMaxWriteBufferSize") is not None:
        out["wal_max_write_buffer_size"] = data["walMaxWriteBufferSize"]
    if data.get("snapshottedWalFilesToKeep") is not None:
        out["snapshotted_wal_files_to_keep"] = data["snapshottedWalFilesToKeep"]
    if data.get("preemptiveCacheAge") is not None:
        import capo_timestream_influxdb.types.duration

        out["preemptive_cache_age"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["preemptiveCacheAge"]
            )
        )
    if data.get("parquetMemCachePrunePercentage") is not None:
        out["parquet_mem_cache_prune_percentage"] = float(
            data["parquetMemCachePrunePercentage"]
        )
    if data.get("parquetMemCachePruneInterval") is not None:
        import capo_timestream_influxdb.types.duration

        out["parquet_mem_cache_prune_interval"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["parquetMemCachePruneInterval"]
            )
        )
    if data.get("disableParquetMemCache") is not None:
        out["disable_parquet_mem_cache"] = data["disableParquetMemCache"]
    if data.get("parquetMemCacheQueryPathDuration") is not None:
        import capo_timestream_influxdb.types.duration

        out["parquet_mem_cache_query_path_duration"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["parquetMemCacheQueryPathDuration"]
            )
        )
    if data.get("lastCacheEvictionInterval") is not None:
        import capo_timestream_influxdb.types.duration

        out["last_cache_eviction_interval"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["lastCacheEvictionInterval"]
            )
        )
    if data.get("distinctCacheEvictionInterval") is not None:
        import capo_timestream_influxdb.types.duration

        out["distinct_cache_eviction_interval"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["distinctCacheEvictionInterval"]
            )
        )
    if data.get("gen1Duration") is not None:
        import capo_timestream_influxdb.types.duration

        out["gen1_duration"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["gen1Duration"]
            )
        )
    if data.get("execMemPoolBytes") is not None:
        import capo_timestream_influxdb.types.percent_or_absolute_long

        out["exec_mem_pool_bytes"] = (
            capo_timestream_influxdb.types.percent_or_absolute_long.deserialize_aws_json_1_0(
                data["execMemPoolBytes"]
            )
        )
    if data.get("parquetMemCacheSize") is not None:
        import capo_timestream_influxdb.types.percent_or_absolute_long

        out["parquet_mem_cache_size"] = (
            capo_timestream_influxdb.types.percent_or_absolute_long.deserialize_aws_json_1_0(
                data["parquetMemCacheSize"]
            )
        )
    if data.get("walReplayFailOnError") is not None:
        out["wal_replay_fail_on_error"] = data["walReplayFailOnError"]
    if data.get("walReplayConcurrencyLimit") is not None:
        out["wal_replay_concurrency_limit"] = data["walReplayConcurrencyLimit"]
    if data.get("tableIndexCacheMaxEntries") is not None:
        out["table_index_cache_max_entries"] = data["tableIndexCacheMaxEntries"]
    if data.get("tableIndexCacheConcurrencyLimit") is not None:
        out["table_index_cache_concurrency_limit"] = data[
            "tableIndexCacheConcurrencyLimit"
        ]
    if data.get("gen1LookbackDuration") is not None:
        import capo_timestream_influxdb.types.duration

        out["gen1_lookback_duration"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["gen1LookbackDuration"]
            )
        )
    if data.get("retentionCheckInterval") is not None:
        import capo_timestream_influxdb.types.duration

        out["retention_check_interval"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["retentionCheckInterval"]
            )
        )
    if data.get("deleteGracePeriod") is not None:
        import capo_timestream_influxdb.types.duration

        out["delete_grace_period"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["deleteGracePeriod"]
            )
        )
    if data.get("hardDeleteDefaultDuration") is not None:
        import capo_timestream_influxdb.types.duration

        out["hard_delete_default_duration"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["hardDeleteDefaultDuration"]
            )
        )
    if data.get("pluginRepositoryUrl") is not None:
        out["plugin_repository_url"] = data["pluginRepositoryUrl"]
    if data.get("pluginRepositorySecretArn") is not None:
        out["plugin_repository_secret_arn"] = data["pluginRepositorySecretArn"]
    if data.get("ingestQueryInstances") is not None:
        out["ingest_query_instances"] = data["ingestQueryInstances"]
    else:
        out["ingest_query_instances"] = 0
    if data.get("queryOnlyInstances") is not None:
        out["query_only_instances"] = data["queryOnlyInstances"]
    else:
        out["query_only_instances"] = 0
    if data.get("dedicatedCompactor") is not None:
        out["dedicated_compactor"] = data["dedicatedCompactor"]
    else:
        out["dedicated_compactor"] = False
    if data.get("compactionRowLimit") is not None:
        out["compaction_row_limit"] = data["compactionRowLimit"]
    if data.get("compactionMaxNumFilesPerPlan") is not None:
        out["compaction_max_num_files_per_plan"] = data["compactionMaxNumFilesPerPlan"]
    if data.get("compactionGen2Duration") is not None:
        import capo_timestream_influxdb.types.duration

        out["compaction_gen2_duration"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["compactionGen2Duration"]
            )
        )
    if data.get("compactionMultipliers") is not None:
        out["compaction_multipliers"] = data["compactionMultipliers"]
    if data.get("compactionCleanupWait") is not None:
        import capo_timestream_influxdb.types.duration

        out["compaction_cleanup_wait"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["compactionCleanupWait"]
            )
        )
    if data.get("compactionCheckInterval") is not None:
        import capo_timestream_influxdb.types.duration

        out["compaction_check_interval"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["compactionCheckInterval"]
            )
        )
    if data.get("lastValueCacheDisableFromHistory") is not None:
        out["last_value_cache_disable_from_history"] = data[
            "lastValueCacheDisableFromHistory"
        ]
    if data.get("distinctValueCacheDisableFromHistory") is not None:
        out["distinct_value_cache_disable_from_history"] = data[
            "distinctValueCacheDisableFromHistory"
        ]
    if data.get("replicationInterval") is not None:
        import capo_timestream_influxdb.types.duration

        out["replication_interval"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["replicationInterval"]
            )
        )
    if data.get("catalogSyncInterval") is not None:
        import capo_timestream_influxdb.types.duration

        out["catalog_sync_interval"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["catalogSyncInterval"]
            )
        )
    if data.get("upgradePachaTree") is not None:
        out["upgrade_pacha_tree"] = data["upgradePachaTree"]
    if data.get("walBufferSize") is not None:
        out["wal_buffer_size"] = data["walBufferSize"]
    if data.get("snapshotSize") is not None:
        import capo_timestream_influxdb.types.percent_or_absolute_long

        out["snapshot_size"] = (
            capo_timestream_influxdb.types.percent_or_absolute_long.deserialize_aws_json_1_0(
                data["snapshotSize"]
            )
        )
    if data.get("snapshotDuration") is not None:
        import capo_timestream_influxdb.types.duration

        out["snapshot_duration"] = (
            capo_timestream_influxdb.types.duration.deserialize_aws_json_1_0(
                data["snapshotDuration"]
            )
        )
    return out
