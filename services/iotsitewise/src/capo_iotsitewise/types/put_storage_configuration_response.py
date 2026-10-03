"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PutStorageConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.configuration_status
    import capo_iotsitewise.types.disallow_ingest_null_na_n
    import capo_iotsitewise.types.disassociated_data_storage_state
    import capo_iotsitewise.types.multi_layer_storage
    import capo_iotsitewise.types.retention_period
    import capo_iotsitewise.types.storage_type
    import capo_iotsitewise.types.warm_tier_retention_period
    import capo_iotsitewise.types.warm_tier_state


class PutStorageConfigurationResponse(TypedDict, closed=True):
    storage_type: "capo_iotsitewise.types.storage_type.StorageType"
    """<p>The storage tier that you specified for your data. The <code>storageType</code> parameter can be one of the following values:</p> <ul> <li> <p> <code>SITEWISE_DEFAULT_STORAGE</code> – IoT SiteWise saves your data into the hot tier. The hot tier is a service-managed database.</p> </li> <li> <p> <code>MULTI_LAYER_STORAGE</code> – IoT SiteWise saves your data in both the cold tier and the hot tier. The cold tier is a customer-managed Amazon S3 bucket.</p> </li> </ul>"""
    multi_layer_storage: NotRequired[
        "capo_iotsitewise.types.multi_layer_storage.MultiLayerStorage"
    ]
    """<p>Contains information about the storage destination.</p>"""
    disassociated_data_storage: NotRequired[
        "capo_iotsitewise.types.disassociated_data_storage_state.DisassociatedDataStorageState"
    ]
    """<p>Contains the storage configuration for time series (data streams) that aren't associated with asset properties. The <code>disassociatedDataStorage</code> can be one of the following values:</p> <ul> <li> <p> <code>ENABLED</code> – IoT SiteWise accepts time series that aren't associated with asset properties.</p> <important> <p>After the <code>disassociatedDataStorage</code> is enabled, you can't disable it.</p> </important> </li> <li> <p> <code>DISABLED</code> – IoT SiteWise doesn't accept time series (data streams) that aren't associated with asset properties.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-streams.html">Data streams</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    retention_period: NotRequired[
        "capo_iotsitewise.types.retention_period.RetentionPeriod"
    ]
    configuration_status: (
        "capo_iotsitewise.types.configuration_status.ConfigurationStatus"
    )
    warm_tier: NotRequired["capo_iotsitewise.types.warm_tier_state.WarmTierState"]
    """<p>A service managed storage tier optimized for analytical queries. It stores periodically uploaded, buffered and historical data ingested with the CreaeBulkImportJob API.</p>"""
    warm_tier_retention_period: NotRequired[
        "capo_iotsitewise.types.warm_tier_retention_period.WarmTierRetentionPeriod"
    ]
    """<p>Set this period to specify how long your data is stored in the warm tier before it is deleted. You can set this only if cold tier is enabled.</p>"""
    disallow_ingest_null_na_n: NotRequired[
        "capo_iotsitewise.types.disallow_ingest_null_na_n.DisallowIngestNullNaN"
    ]
    """<p>Describes the configuration for ingesting NULL and NaN data. By default the feature is allowed. The feature is disallowed if the value is <code>true</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutStorageConfigurationResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.storage_type

    out["storageType"] = capo_iotsitewise.types.storage_type.serialize_json(
        value["storage_type"]
    )
    if "multi_layer_storage" in value:
        import capo_iotsitewise.types.multi_layer_storage

        out["multiLayerStorage"] = (
            capo_iotsitewise.types.multi_layer_storage.serialize_json(
                value["multi_layer_storage"]
            )
        )
    if "disassociated_data_storage" in value:
        import capo_iotsitewise.types.disassociated_data_storage_state

        out["disassociatedDataStorage"] = (
            capo_iotsitewise.types.disassociated_data_storage_state.serialize_json(
                value["disassociated_data_storage"]
            )
        )
    if "retention_period" in value:
        import capo_iotsitewise.types.retention_period

        out["retentionPeriod"] = capo_iotsitewise.types.retention_period.serialize_json(
            value["retention_period"]
        )
    import capo_iotsitewise.types.configuration_status

    out["configurationStatus"] = (
        capo_iotsitewise.types.configuration_status.serialize_json(
            value["configuration_status"]
        )
    )
    if "warm_tier" in value:
        import capo_iotsitewise.types.warm_tier_state

        out["warmTier"] = capo_iotsitewise.types.warm_tier_state.serialize_json(
            value["warm_tier"]
        )
    if "warm_tier_retention_period" in value:
        import capo_iotsitewise.types.warm_tier_retention_period

        out["warmTierRetentionPeriod"] = (
            capo_iotsitewise.types.warm_tier_retention_period.serialize_json(
                value["warm_tier_retention_period"]
            )
        )
    if "disallow_ingest_null_na_n" in value:
        out["disallowIngestNullNaN"] = value["disallow_ingest_null_na_n"]
    return out


def deserialize_json(data: dict) -> PutStorageConfigurationResponse:
    out: PutStorageConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("storageType") is not None:
        import capo_iotsitewise.types.storage_type

        out["storage_type"] = capo_iotsitewise.types.storage_type.deserialize_json(
            data["storageType"]
        )
    else:
        raise DeserializationError(
            "PutStorageConfigurationResponse.storage_type required"
        )
    if data.get("multiLayerStorage") is not None:
        import capo_iotsitewise.types.multi_layer_storage

        out["multi_layer_storage"] = (
            capo_iotsitewise.types.multi_layer_storage.deserialize_json(
                data["multiLayerStorage"]
            )
        )
    if data.get("disassociatedDataStorage") is not None:
        import capo_iotsitewise.types.disassociated_data_storage_state

        out["disassociated_data_storage"] = (
            capo_iotsitewise.types.disassociated_data_storage_state.deserialize_json(
                data["disassociatedDataStorage"]
            )
        )
    if data.get("retentionPeriod") is not None:
        import capo_iotsitewise.types.retention_period

        out["retention_period"] = (
            capo_iotsitewise.types.retention_period.deserialize_json(
                data["retentionPeriod"]
            )
        )
    if data.get("configurationStatus") is not None:
        import capo_iotsitewise.types.configuration_status

        out["configuration_status"] = (
            capo_iotsitewise.types.configuration_status.deserialize_json(
                data["configurationStatus"]
            )
        )
    else:
        raise DeserializationError(
            "PutStorageConfigurationResponse.configuration_status required"
        )
    if data.get("warmTier") is not None:
        import capo_iotsitewise.types.warm_tier_state

        out["warm_tier"] = capo_iotsitewise.types.warm_tier_state.deserialize_json(
            data["warmTier"]
        )
    if data.get("warmTierRetentionPeriod") is not None:
        import capo_iotsitewise.types.warm_tier_retention_period

        out["warm_tier_retention_period"] = (
            capo_iotsitewise.types.warm_tier_retention_period.deserialize_json(
                data["warmTierRetentionPeriod"]
            )
        )
    if data.get("disallowIngestNullNaN") is not None:
        out["disallow_ingest_null_na_n"] = data["disallowIngestNullNaN"]
    return out
