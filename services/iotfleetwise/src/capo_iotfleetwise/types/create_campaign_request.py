"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateCampaignRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.campaign_name
    import capo_iotfleetwise.types.collection_scheme
    import capo_iotfleetwise.types.compression
    import capo_iotfleetwise.types.data_destination_configs
    import capo_iotfleetwise.types.data_extra_dimension_node_path_list
    import capo_iotfleetwise.types.data_partitions
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.diagnostics_mode
    import capo_iotfleetwise.types.priority
    import capo_iotfleetwise.types.signal_fetch_information_list
    import capo_iotfleetwise.types.signal_information_list
    import capo_iotfleetwise.types.spooling_mode
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.timestamp
    import capo_iotfleetwise.types.uint32


class CreateCampaignRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.campaign_name.campaignName"
    """<p> The name of the campaign to create. </p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>An optional description of the campaign to help identify its purpose.</p>"""
    signal_catalog_arn: "capo_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of the signal catalog to associate with the campaign. </p>"""
    target_arn: "capo_iotfleetwise.types.arn.arn"
    """<p> The ARN of the vehicle or fleet to deploy a campaign to. </p>"""
    start_time: NotRequired["capo_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time, in milliseconds, to deliver a campaign after it was approved. If it's not specified, <code>0</code> is used.</p> <p>Default: <code>0</code> </p>"""
    expiry_time: NotRequired["capo_iotfleetwise.types.timestamp.timestamp"]
    """<p>The time the campaign expires, in seconds since epoch (January 1, 1970 at midnight UTC time). Vehicle data isn't collected after the campaign expires. </p> <p>Default: 253402214400 (December 31, 9999, 00:00:00 UTC)</p>"""
    post_trigger_collection_duration: NotRequired[
        "capo_iotfleetwise.types.uint32.uint32"
    ]
    """<p>How long (in milliseconds) to collect raw data after a triggering event initiates the collection. If it's not specified, <code>0</code> is used.</p> <p>Default: <code>0</code> </p>"""
    diagnostics_mode: NotRequired[
        "capo_iotfleetwise.types.diagnostics_mode.DiagnosticsMode"
    ]
    """<p>Option for a vehicle to send diagnostic trouble codes to Amazon Web Services IoT FleetWise. If you want to send diagnostic trouble codes, use <code>SEND_ACTIVE_DTCS</code>. If it's not specified, <code>OFF</code> is used.</p> <p>Default: <code>OFF</code> </p>"""
    spooling_mode: NotRequired["capo_iotfleetwise.types.spooling_mode.SpoolingMode"]
    """<p>Determines whether to store collected data after a vehicle lost a connection with the cloud. After a connection is re-established, the data is automatically forwarded to Amazon Web Services IoT FleetWise. If you want to store collected data when a vehicle loses connection with the cloud, use <code>TO_DISK</code>. If it's not specified, <code>OFF</code> is used.</p> <p>Default: <code>OFF</code> </p>"""
    compression: NotRequired["capo_iotfleetwise.types.compression.Compression"]
    """<p>Determines whether to compress signals before transmitting data to Amazon Web Services IoT FleetWise. If you don't want to compress the signals, use <code>OFF</code>. If it's not specified, <code>SNAPPY</code> is used. </p> <p>Default: <code>SNAPPY</code> </p>"""
    priority: NotRequired["capo_iotfleetwise.types.priority.priority"]
    """<p>A number indicating the priority of one campaign over another campaign for a certain vehicle or fleet. A campaign with the lowest value is deployed to vehicles before any other campaigns. If it's not specified, <code>0</code> is used. </p> <p>Default: <code>0</code> </p>"""
    signals_to_collect: NotRequired[
        "capo_iotfleetwise.types.signal_information_list.SignalInformationList"
    ]
    """<p>A list of information about signals to collect. </p> <note> <p>If you upload a signal as a condition in a data partition for a campaign, then those same signals must be included in <code>signalsToCollect</code>.</p> </note>"""
    collection_scheme: "capo_iotfleetwise.types.collection_scheme.CollectionScheme"
    """<p> The data collection scheme associated with the campaign. You can specify a scheme that collects data based on time or an event.</p>"""
    data_extra_dimensions: NotRequired[
        "capo_iotfleetwise.types.data_extra_dimension_node_path_list.DataExtraDimensionNodePathList"
    ]
    """<p>A list of vehicle attributes to associate with a campaign. </p> <p>Enrich the data with specified vehicle attributes. For example, add <code>make</code> and <code>model</code> to the campaign, and Amazon Web Services IoT FleetWise will associate the data with those attributes as dimensions in Amazon Timestream. You can then query the data against <code>make</code> and <code>model</code>.</p> <p>Default: An empty array</p>"""
    tags: NotRequired["capo_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the campaign.</p>"""
    data_destination_configs: NotRequired[
        "capo_iotfleetwise.types.data_destination_configs.DataDestinationConfigs"
    ]
    """<p>The destination where the campaign sends data. You can send data to an MQTT topic, or store it in Amazon S3 or Amazon Timestream.</p> <p>MQTT is the publish/subscribe messaging protocol used by Amazon Web Services IoT to communicate with your devices.</p> <p>Amazon S3 optimizes the cost of data storage and provides additional mechanisms to use vehicle data, such as data lakes, centralized data storage, data processing pipelines, and analytics. Amazon Web Services IoT FleetWise supports at-least-once file delivery to S3. Your vehicle data is stored on multiple Amazon Web Services IoT FleetWise servers for redundancy and high availability.</p> <p>You can use Amazon Timestream to access and analyze time series data, and Timestream to query vehicle data so that you can identify trends and patterns.</p>"""
    data_partitions: NotRequired[
        "capo_iotfleetwise.types.data_partitions.DataPartitions"
    ]
    """<p>The data partitions associated with the signals collected from the vehicle.</p>"""
    signals_to_fetch: NotRequired[
        "capo_iotfleetwise.types.signal_fetch_information_list.SignalFetchInformationList"
    ]
    """<p>A list of information about signals to fetch.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCampaignRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["signalCatalogArn"] = value["signal_catalog_arn"]
    out["targetArn"] = value["target_arn"]
    if "start_time" in value:
        import capo_iotfleetwise.types.timestamp

        out["startTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["start_time"]
        )
    if "expiry_time" in value:
        import capo_iotfleetwise.types.timestamp

        out["expiryTime"] = capo_iotfleetwise.types.timestamp.serialize_aws_json_1_0(
            value["expiry_time"]
        )
    if "post_trigger_collection_duration" in value:
        out["postTriggerCollectionDuration"] = value["post_trigger_collection_duration"]
    if "diagnostics_mode" in value:
        import capo_iotfleetwise.types.diagnostics_mode

        out["diagnosticsMode"] = (
            capo_iotfleetwise.types.diagnostics_mode.serialize_aws_json_1_0(
                value["diagnostics_mode"]
            )
        )
    if "spooling_mode" in value:
        import capo_iotfleetwise.types.spooling_mode

        out["spoolingMode"] = (
            capo_iotfleetwise.types.spooling_mode.serialize_aws_json_1_0(
                value["spooling_mode"]
            )
        )
    if "compression" in value:
        import capo_iotfleetwise.types.compression

        out["compression"] = capo_iotfleetwise.types.compression.serialize_aws_json_1_0(
            value["compression"]
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "signals_to_collect" in value:
        import capo_iotfleetwise.types.signal_information_list

        out["signalsToCollect"] = (
            capo_iotfleetwise.types.signal_information_list.serialize_aws_json_1_0(
                value["signals_to_collect"]
            )
        )
    import capo_iotfleetwise.types.collection_scheme

    out["collectionScheme"] = (
        capo_iotfleetwise.types.collection_scheme.serialize_aws_json_1_0(
            value["collection_scheme"]
        )
    )
    if "data_extra_dimensions" in value:
        import capo_iotfleetwise.types.data_extra_dimension_node_path_list

        out["dataExtraDimensions"] = (
            capo_iotfleetwise.types.data_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["data_extra_dimensions"]
            )
        )
    if "tags" in value:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "data_destination_configs" in value:
        import capo_iotfleetwise.types.data_destination_configs

        out["dataDestinationConfigs"] = (
            capo_iotfleetwise.types.data_destination_configs.serialize_aws_json_1_0(
                value["data_destination_configs"]
            )
        )
    if "data_partitions" in value:
        import capo_iotfleetwise.types.data_partitions

        out["dataPartitions"] = (
            capo_iotfleetwise.types.data_partitions.serialize_aws_json_1_0(
                value["data_partitions"]
            )
        )
    if "signals_to_fetch" in value:
        import capo_iotfleetwise.types.signal_fetch_information_list

        out["signalsToFetch"] = (
            capo_iotfleetwise.types.signal_fetch_information_list.serialize_aws_json_1_0(
                value["signals_to_fetch"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCampaignRequest:
    out: CreateCampaignRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCampaignRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("signalCatalogArn") is not None:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    else:
        raise DeserializationError("CreateCampaignRequest.signal_catalog_arn required")
    if data.get("targetArn") is not None:
        out["target_arn"] = data["targetArn"]
    else:
        raise DeserializationError("CreateCampaignRequest.target_arn required")
    if data.get("startTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["start_time"] = capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
            data["startTime"]
        )
    if data.get("expiryTime") is not None:
        import capo_iotfleetwise.types.timestamp

        out["expiry_time"] = capo_iotfleetwise.types.timestamp.deserialize_aws_json_1_0(
            data["expiryTime"]
        )
    if data.get("postTriggerCollectionDuration") is not None:
        out["post_trigger_collection_duration"] = data["postTriggerCollectionDuration"]
    if data.get("diagnosticsMode") is not None:
        import capo_iotfleetwise.types.diagnostics_mode

        out["diagnostics_mode"] = (
            capo_iotfleetwise.types.diagnostics_mode.deserialize_aws_json_1_0(
                data["diagnosticsMode"]
            )
        )
    if data.get("spoolingMode") is not None:
        import capo_iotfleetwise.types.spooling_mode

        out["spooling_mode"] = (
            capo_iotfleetwise.types.spooling_mode.deserialize_aws_json_1_0(
                data["spoolingMode"]
            )
        )
    if data.get("compression") is not None:
        import capo_iotfleetwise.types.compression

        out["compression"] = (
            capo_iotfleetwise.types.compression.deserialize_aws_json_1_0(
                data["compression"]
            )
        )
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("signalsToCollect") is not None:
        import capo_iotfleetwise.types.signal_information_list

        out["signals_to_collect"] = (
            capo_iotfleetwise.types.signal_information_list.deserialize_aws_json_1_0(
                data["signalsToCollect"]
            )
        )
    if data.get("collectionScheme") is not None:
        import capo_iotfleetwise.types.collection_scheme

        out["collection_scheme"] = (
            capo_iotfleetwise.types.collection_scheme.deserialize_aws_json_1_0(
                data["collectionScheme"]
            )
        )
    else:
        raise DeserializationError("CreateCampaignRequest.collection_scheme required")
    if data.get("dataExtraDimensions") is not None:
        import capo_iotfleetwise.types.data_extra_dimension_node_path_list

        out["data_extra_dimensions"] = (
            capo_iotfleetwise.types.data_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["dataExtraDimensions"]
            )
        )
    if data.get("tags") is not None:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("dataDestinationConfigs") is not None:
        import capo_iotfleetwise.types.data_destination_configs

        out["data_destination_configs"] = (
            capo_iotfleetwise.types.data_destination_configs.deserialize_aws_json_1_0(
                data["dataDestinationConfigs"]
            )
        )
    if data.get("dataPartitions") is not None:
        import capo_iotfleetwise.types.data_partitions

        out["data_partitions"] = (
            capo_iotfleetwise.types.data_partitions.deserialize_aws_json_1_0(
                data["dataPartitions"]
            )
        )
    if data.get("signalsToFetch") is not None:
        import capo_iotfleetwise.types.signal_fetch_information_list

        out["signals_to_fetch"] = (
            capo_iotfleetwise.types.signal_fetch_information_list.deserialize_aws_json_1_0(
                data["signalsToFetch"]
            )
        )
    return out


def redact_sensitive(value: CreateCampaignRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "signals_to_collect" in value:
        out["signals_to_collect"] = "*** Sensitive Data Redacted ***"
    if "collection_scheme" in value:
        import capo_iotfleetwise.types.collection_scheme

        out["collection_scheme"] = (
            capo_iotfleetwise.types.collection_scheme.redact_sensitive(
                value["collection_scheme"]
            )
        )
    if "data_extra_dimensions" in value:
        out["data_extra_dimensions"] = "*** Sensitive Data Redacted ***"
    if "data_partitions" in value:
        import capo_iotfleetwise.types.data_partitions

        out["data_partitions"] = (
            capo_iotfleetwise.types.data_partitions.redact_sensitive(
                value["data_partitions"]
            )
        )
    if "signals_to_fetch" in value:
        out["signals_to_fetch"] = "*** Sensitive Data Redacted ***"
    return out
