"""Generated from Smithy shape ``com.amazonaws.connect#MetricDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.available_filter_list
    import capo_connect.types.created_by_info
    import capo_connect.types.default_stat
    import capo_connect.types.metric_calculation
    import capo_connect.types.metric_category
    import capo_connect.types.metric_creation_method
    import capo_connect.types.metric_description
    import capo_connect.types.metric_grouping_list
    import capo_connect.types.metric_id
    import capo_connect.types.metric_name
    import capo_connect.types.metric_status
    import capo_connect.types.metric_type
    import capo_connect.types.metric_unit
    import capo_connect.types.primary_event_source
    import capo_connect.types.primary_event_source_effective_timestamp_type
    import capo_connect.types.refresh_rate
    import capo_connect.types.region_name
    import capo_connect.types.supported_stats_list
    import capo_connect.types.supports_custom_calculation
    import capo_connect.types.supports_preaggregate_calculation
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp
    import capo_connect.types.trend_indicator


class MetricDefinition(TypedDict, closed=True):
    arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the metric. May be qualified with <code>$SAVED</code> or <code>$LATEST</code>.</p>"""
    id: "capo_connect.types.metric_id.MetricId"
    """<p>The identifier of the metric.</p>"""
    name: "capo_connect.types.metric_name.MetricName"
    """<p>The name of the metric.</p>"""
    description: NotRequired["capo_connect.types.metric_description.MetricDescription"]
    """<p>The description of the metric.</p>"""
    metric_calculation: NotRequired[
        "capo_connect.types.metric_calculation.MetricCalculation"
    ]
    """<p>The calculation definition for the metric.</p>"""
    creation_method: NotRequired[
        "capo_connect.types.metric_creation_method.MetricCreationMethod"
    ]
    """<p>The method used to create the metric. Valid values: <code>SERVICE_LEVEL_BUILDER</code> (created with the guided service-level experience) | <code>METRIC_BUILDER</code> (created with the free-form metric builder).</p>"""
    status: NotRequired["capo_connect.types.metric_status.MetricStatus"]
    """<p>The publish status of the metric. Valid values: <code>PUBLISHED</code> | <code>SAVED</code>.</p>"""
    type: "capo_connect.types.metric_type.MetricType"
    """<p>The type of the metric. Valid values: <code>AWS_MANAGED</code> | <code>CUSTOMER_MANAGED</code>.</p>"""
    unit: "capo_connect.types.metric_unit.MetricUnit"
    """<p>The display unit for the metric's data.</p>"""
    positive_trend_indicator: NotRequired[
        "capo_connect.types.trend_indicator.TrendIndicator"
    ]
    """<p>How an increase in the metric value should be interpreted. Valid values: <code>POSITIVE</code>, <code>NEUTRAL</code>, <code>NEGATIVE</code>.</p>"""
    groupings: "capo_connect.types.metric_grouping_list.MetricGroupingList"
    """<p>The groupings available for this metric.</p>"""
    filters: "capo_connect.types.available_filter_list.AvailableFilterList"
    """<p>The filters applied to the metric.</p>"""
    effective_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The earliest time that can be queried for this metric.</p>"""
    refresh_rate: "capo_connect.types.refresh_rate.RefreshRate"
    """<p>The minimum interval, in seconds, between data refreshes for this metric.</p>"""
    category: "capo_connect.types.metric_category.MetricCategory"
    """<p>The category of the metric.</p>"""
    supported_stats: NotRequired[
        "capo_connect.types.supported_stats_list.SupportedStatsList"
    ]
    """<p>The stat aggregations available for this metric.</p>"""
    default_stat: NotRequired["capo_connect.types.default_stat.DefaultStat"]
    """<p>The default stat aggregation for the metric.</p>"""
    supports_preaggregate_calculation: "capo_connect.types.supports_preaggregate_calculation.SupportsPreaggregateCalculation"
    """<p>Specifies whether the metric can be used inside aggregating statistical functions (SUM, AVG, etc.) in custom metric calculations.</p>"""
    supports_custom_calculation: (
        "capo_connect.types.supports_custom_calculation.SupportsCustomCalculation"
    )
    """<p>Specifies whether the metric can be used as a component of custom metrics.</p>"""
    primary_event_source: NotRequired[
        "capo_connect.types.primary_event_source.PrimaryEventSource"
    ]
    """<p>The primary event source for the metric data.</p>"""
    primary_event_source_effective_timestamp_type: NotRequired[
        "capo_connect.types.primary_event_source_effective_timestamp_type.PrimaryEventSourceEffectiveTimestampType"
    ]
    """<p>The timestamp type that determines where the metric appears on a time series.</p>"""
    created_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp of when the metric was created.</p>"""
    created_user: NotRequired["capo_connect.types.created_by_info.CreatedByInfo"]
    """<p>The user that created the metric. The creator for metrics created through the CreateMetric API will be <code>Amazon Connect API</code>.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The region where the metric was last modified.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp of when the metric was last modified.</p>"""
    last_modified_user: NotRequired["capo_connect.types.created_by_info.CreatedByInfo"]
    """<p>The user that last modified the metric. For modifications made through the API, this will be <code>Amazon Connect API</code>.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricDefinition) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "metric_calculation" in value:
        import capo_connect.types.metric_calculation

        out["MetricCalculation"] = capo_connect.types.metric_calculation.serialize_json(
            value["metric_calculation"]
        )
    if "creation_method" in value:
        import capo_connect.types.metric_creation_method

        out["CreationMethod"] = (
            capo_connect.types.metric_creation_method.serialize_json(
                value["creation_method"]
            )
        )
    if "status" in value:
        import capo_connect.types.metric_status

        out["Status"] = capo_connect.types.metric_status.serialize_json(value["status"])
    import capo_connect.types.metric_type

    out["Type"] = capo_connect.types.metric_type.serialize_json(value["type"])
    import capo_connect.types.metric_unit

    out["Unit"] = capo_connect.types.metric_unit.serialize_json(value["unit"])
    if "positive_trend_indicator" in value:
        import capo_connect.types.trend_indicator

        out["PositiveTrendIndicator"] = (
            capo_connect.types.trend_indicator.serialize_json(
                value["positive_trend_indicator"]
            )
        )
    import capo_connect.types.metric_grouping_list

    out["Groupings"] = capo_connect.types.metric_grouping_list.serialize_json(
        value["groupings"]
    )
    import capo_connect.types.available_filter_list

    out["Filters"] = capo_connect.types.available_filter_list.serialize_json(
        value["filters"]
    )
    if "effective_time" in value:
        import capo_connect.types.timestamp

        out["EffectiveTime"] = capo_connect.types.timestamp.serialize_json(
            value["effective_time"]
        )
    out["RefreshRate"] = value.get("refresh_rate", 0)
    out["Category"] = value["category"]
    if "supported_stats" in value:
        import capo_connect.types.supported_stats_list

        out["SupportedStats"] = capo_connect.types.supported_stats_list.serialize_json(
            value["supported_stats"]
        )
    if "default_stat" in value:
        out["DefaultStat"] = value["default_stat"]
    out["SupportsPreaggregateCalculation"] = value.get(
        "supports_preaggregate_calculation", False
    )
    out["SupportsCustomCalculation"] = value.get("supports_custom_calculation", False)
    if "primary_event_source" in value:
        out["PrimaryEventSource"] = value["primary_event_source"]
    if "primary_event_source_effective_timestamp_type" in value:
        out["PrimaryEventSourceEffectiveTimestampType"] = value[
            "primary_event_source_effective_timestamp_type"
        ]
    if "created_time" in value:
        import capo_connect.types.timestamp

        out["CreatedTime"] = capo_connect.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "created_user" in value:
        import capo_connect.types.created_by_info

        out["CreatedUser"] = capo_connect.types.created_by_info.serialize_json(
            value["created_user"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_user" in value:
        import capo_connect.types.created_by_info

        out["LastModifiedUser"] = capo_connect.types.created_by_info.serialize_json(
            value["last_modified_user"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> MetricDefinition:
    out: MetricDefinition = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("MetricDefinition.arn required")
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("MetricDefinition.id required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("MetricDefinition.name required")
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("MetricCalculation") is not None:
        import capo_connect.types.metric_calculation

        out["metric_calculation"] = (
            capo_connect.types.metric_calculation.deserialize_json(
                data["MetricCalculation"]
            )
        )
    if data.get("CreationMethod") is not None:
        import capo_connect.types.metric_creation_method

        out["creation_method"] = (
            capo_connect.types.metric_creation_method.deserialize_json(
                data["CreationMethod"]
            )
        )
    if data.get("Status") is not None:
        import capo_connect.types.metric_status

        out["status"] = capo_connect.types.metric_status.deserialize_json(
            data["Status"]
        )
    if data.get("Type") is not None:
        import capo_connect.types.metric_type

        out["type"] = capo_connect.types.metric_type.deserialize_json(data["Type"])
    else:
        raise DeserializationError("MetricDefinition.type required")
    if data.get("Unit") is not None:
        import capo_connect.types.metric_unit

        out["unit"] = capo_connect.types.metric_unit.deserialize_json(data["Unit"])
    else:
        raise DeserializationError("MetricDefinition.unit required")
    if data.get("PositiveTrendIndicator") is not None:
        import capo_connect.types.trend_indicator

        out["positive_trend_indicator"] = (
            capo_connect.types.trend_indicator.deserialize_json(
                data["PositiveTrendIndicator"]
            )
        )
    if data.get("Groupings") is not None:
        import capo_connect.types.metric_grouping_list

        out["groupings"] = capo_connect.types.metric_grouping_list.deserialize_json(
            data["Groupings"]
        )
    else:
        raise DeserializationError("MetricDefinition.groupings required")
    if data.get("Filters") is not None:
        import capo_connect.types.available_filter_list

        out["filters"] = capo_connect.types.available_filter_list.deserialize_json(
            data["Filters"]
        )
    else:
        raise DeserializationError("MetricDefinition.filters required")
    if data.get("EffectiveTime") is not None:
        import capo_connect.types.timestamp

        out["effective_time"] = capo_connect.types.timestamp.deserialize_json(
            data["EffectiveTime"]
        )
    if data.get("RefreshRate") is not None:
        out["refresh_rate"] = data["RefreshRate"]
    else:
        out["refresh_rate"] = 0
    if data.get("Category") is not None:
        out["category"] = data["Category"]
    else:
        raise DeserializationError("MetricDefinition.category required")
    if data.get("SupportedStats") is not None:
        import capo_connect.types.supported_stats_list

        out["supported_stats"] = (
            capo_connect.types.supported_stats_list.deserialize_json(
                data["SupportedStats"]
            )
        )
    if data.get("DefaultStat") is not None:
        out["default_stat"] = data["DefaultStat"]
    if data.get("SupportsPreaggregateCalculation") is not None:
        out["supports_preaggregate_calculation"] = data[
            "SupportsPreaggregateCalculation"
        ]
    else:
        out["supports_preaggregate_calculation"] = False
    if data.get("SupportsCustomCalculation") is not None:
        out["supports_custom_calculation"] = data["SupportsCustomCalculation"]
    else:
        out["supports_custom_calculation"] = False
    if data.get("PrimaryEventSource") is not None:
        out["primary_event_source"] = data["PrimaryEventSource"]
    if data.get("PrimaryEventSourceEffectiveTimestampType") is not None:
        out["primary_event_source_effective_timestamp_type"] = data[
            "PrimaryEventSourceEffectiveTimestampType"
        ]
    if data.get("CreatedTime") is not None:
        import capo_connect.types.timestamp

        out["created_time"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if data.get("CreatedUser") is not None:
        import capo_connect.types.created_by_info

        out["created_user"] = capo_connect.types.created_by_info.deserialize_json(
            data["CreatedUser"]
        )
    if data.get("LastModifiedRegion") is not None:
        out["last_modified_region"] = data["LastModifiedRegion"]
    if data.get("LastModifiedTime") is not None:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if data.get("LastModifiedUser") is not None:
        import capo_connect.types.created_by_info

        out["last_modified_user"] = capo_connect.types.created_by_info.deserialize_json(
            data["LastModifiedUser"]
        )
    if data.get("Tags") is not None:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
