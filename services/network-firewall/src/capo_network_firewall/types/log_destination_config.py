"""Generated from Smithy shape ``com.amazonaws.networkfirewall#LogDestinationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.log_destination_map
    import capo_network_firewall.types.log_destination_type
    import capo_network_firewall.types.log_type


class LogDestinationConfig(TypedDict, closed=True):
    log_type: "capo_network_firewall.types.log_type.LogType"
    """<p>The type of log to record. You can record the following types of logs from your Network Firewall stateful engine.</p> <ul> <li> <p> <code>ALERT</code> - Logs for traffic that matches your stateful rules and that have an action that sends an alert. A stateful rule sends alerts for the rule actions DROP, ALERT, and REJECT. For more information, see <a>StatefulRule</a>.</p> </li> <li> <p> <code>FLOW</code> - Standard network traffic flow logs. The stateful rules engine records flow logs for all network traffic that it receives. Each flow log record captures the network flow for a specific standard stateless rule group.</p> </li> <li> <p> <code>TLS</code> - Logs for events that are related to TLS inspection. For more information, see <a href="https://docs.aws.amazon.com/network-firewall/latest/developerguide/tls-inspection-configurations.html">Inspecting SSL/TLS traffic with TLS inspection configurations</a> in the <i>Network Firewall Developer Guide</i>.</p> </li> </ul>"""
    log_destination_type: (
        "capo_network_firewall.types.log_destination_type.LogDestinationType"
    )
    """<p>The type of storage destination to send these logs to. You can send logs to an Amazon S3 bucket, a CloudWatch log group, or a Firehose delivery stream.</p>"""
    log_destination: "capo_network_firewall.types.log_destination_map.LogDestinationMap"
    """<p>The named location for the logs, provided in a key:value mapping that is specific to the chosen destination type. </p> <ul> <li> <p>For an Amazon S3 bucket, provide the name of the bucket, with key <code>bucketName</code>, and optionally provide a prefix, with key <code>prefix</code>. </p> <p>The following example specifies an Amazon S3 bucket named <code>DOC-EXAMPLE-BUCKET</code> and the prefix <code>alerts</code>: </p> <p> <code>"LogDestination": { "bucketName": "DOC-EXAMPLE-BUCKET", "prefix": "alerts" }</code> </p> </li> <li> <p>For a CloudWatch log group, provide the name of the CloudWatch log group, with key <code>logGroup</code>. The following example specifies a log group named <code>alert-log-group</code>: </p> <p> <code>"LogDestination": { "logGroup": "alert-log-group" }</code> </p> </li> <li> <p>For a Firehose delivery stream, provide the name of the delivery stream, with key <code>deliveryStream</code>. The following example specifies a delivery stream named <code>alert-delivery-stream</code>: </p> <p> <code>"LogDestination": { "deliveryStream": "alert-delivery-stream" }</code> </p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LogDestinationConfig) -> dict:
    out: dict = {}
    import capo_network_firewall.types.log_type

    out["LogType"] = capo_network_firewall.types.log_type.serialize_aws_json_1_0(
        value["log_type"]
    )
    import capo_network_firewall.types.log_destination_type

    out["LogDestinationType"] = (
        capo_network_firewall.types.log_destination_type.serialize_aws_json_1_0(
            value["log_destination_type"]
        )
    )
    import capo_network_firewall.types.log_destination_map

    out["LogDestination"] = (
        capo_network_firewall.types.log_destination_map.serialize_aws_json_1_0(
            value["log_destination"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LogDestinationConfig:
    out: LogDestinationConfig = {}  # type: ignore[typeddict-item]
    if data.get("LogType") is not None:
        import capo_network_firewall.types.log_type

        out["log_type"] = capo_network_firewall.types.log_type.deserialize_aws_json_1_0(
            data["LogType"]
        )
    else:
        raise DeserializationError("LogDestinationConfig.log_type required")
    if data.get("LogDestinationType") is not None:
        import capo_network_firewall.types.log_destination_type

        out["log_destination_type"] = (
            capo_network_firewall.types.log_destination_type.deserialize_aws_json_1_0(
                data["LogDestinationType"]
            )
        )
    else:
        raise DeserializationError("LogDestinationConfig.log_destination_type required")
    if data.get("LogDestination") is not None:
        import capo_network_firewall.types.log_destination_map

        out["log_destination"] = (
            capo_network_firewall.types.log_destination_map.deserialize_aws_json_1_0(
                data["LogDestination"]
            )
        )
    else:
        raise DeserializationError("LogDestinationConfig.log_destination required")
    return out
