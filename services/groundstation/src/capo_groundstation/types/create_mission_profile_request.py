"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateMissionProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.config_arn
    import capo_groundstation.types.dataflow_edge_list
    import capo_groundstation.types.duration_in_seconds
    import capo_groundstation.types.kms_key
    import capo_groundstation.types.positive_duration_in_seconds
    import capo_groundstation.types.role_arn
    import capo_groundstation.types.safe_name
    import capo_groundstation.types.tags_map


class CreateMissionProfileRequest(TypedDict, closed=True):
    name: "capo_groundstation.types.safe_name.SafeName"
    """<p>Name of a mission profile.</p>"""
    contact_pre_pass_duration_seconds: NotRequired[
        "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>Amount of time prior to contact start you'd like to receive a Ground Station Contact State Change event indicating an upcoming pass.</p>"""
    contact_post_pass_duration_seconds: NotRequired[
        "capo_groundstation.types.duration_in_seconds.DurationInSeconds"
    ]
    """<p>Amount of time after a contact ends that you'd like to receive a Ground Station Contact State Change event indicating the pass has finished.</p>"""
    minimum_viable_contact_duration_seconds: "capo_groundstation.types.positive_duration_in_seconds.PositiveDurationInSeconds"
    """<p>Smallest amount of time in seconds that you'd like to see for an available contact. AWS Ground Station will not present you with contacts shorter than this duration.</p>"""
    dataflow_edges: "capo_groundstation.types.dataflow_edge_list.DataflowEdgeList"
    """<p>A list of lists of ARNs. Each list of ARNs is an edge, with a <i>from</i> <code> Config</code> and a <i>to</i> <code>Config</code>.</p>"""
    tracking_config_arn: "capo_groundstation.types.config_arn.ConfigArn"
    """<p>ARN of a tracking <code>Config</code>.</p>"""
    telemetry_sink_config_arn: NotRequired[
        "capo_groundstation.types.config_arn.ConfigArn"
    ]
    """<p>ARN of a telemetry sink <code>Config</code>.</p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags assigned to a mission profile.</p>"""
    streams_kms_key: NotRequired["capo_groundstation.types.kms_key.KmsKey"]
    """<p>KMS key to use for encrypting streams.</p>"""
    streams_kms_role: NotRequired["capo_groundstation.types.role_arn.RoleArn"]
    """<p>Role to use for encrypting streams with KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMissionProfileRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "contact_pre_pass_duration_seconds" in value:
        out["contactPrePassDurationSeconds"] = value[
            "contact_pre_pass_duration_seconds"
        ]
    if "contact_post_pass_duration_seconds" in value:
        out["contactPostPassDurationSeconds"] = value[
            "contact_post_pass_duration_seconds"
        ]
    out["minimumViableContactDurationSeconds"] = value[
        "minimum_viable_contact_duration_seconds"
    ]
    import capo_groundstation.types.dataflow_edge_list

    out["dataflowEdges"] = capo_groundstation.types.dataflow_edge_list.serialize_json(
        value["dataflow_edges"]
    )
    out["trackingConfigArn"] = value["tracking_config_arn"]
    if "telemetry_sink_config_arn" in value:
        out["telemetrySinkConfigArn"] = value["telemetry_sink_config_arn"]
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    if "streams_kms_key" in value:
        import capo_groundstation.types.kms_key

        out["streamsKmsKey"] = capo_groundstation.types.kms_key.serialize_json(
            value["streams_kms_key"]
        )
    if "streams_kms_role" in value:
        out["streamsKmsRole"] = value["streams_kms_role"]
    return out


def deserialize_json(data: dict) -> CreateMissionProfileRequest:
    out: CreateMissionProfileRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("contactPrePassDurationSeconds") is not None:
        out["contact_pre_pass_duration_seconds"] = data["contactPrePassDurationSeconds"]
    if data.get("contactPostPassDurationSeconds") is not None:
        out["contact_post_pass_duration_seconds"] = data[
            "contactPostPassDurationSeconds"
        ]
    if data.get("minimumViableContactDurationSeconds") is not None:
        out["minimum_viable_contact_duration_seconds"] = data[
            "minimumViableContactDurationSeconds"
        ]
    else:
        out["minimum_viable_contact_duration_seconds"] = 0
    if data.get("dataflowEdges") is not None:
        import capo_groundstation.types.dataflow_edge_list

        out["dataflow_edges"] = (
            capo_groundstation.types.dataflow_edge_list.deserialize_json(
                data["dataflowEdges"]
            )
        )
    else:
        out["dataflow_edges"] = []
    if data.get("trackingConfigArn") is not None:
        out["tracking_config_arn"] = data["trackingConfigArn"]
    else:
        out["tracking_config_arn"] = ""
    if data.get("telemetrySinkConfigArn") is not None:
        out["telemetry_sink_config_arn"] = data["telemetrySinkConfigArn"]
    if data.get("tags") is not None:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    if data.get("streamsKmsKey") is not None:
        import capo_groundstation.types.kms_key

        out["streams_kms_key"] = capo_groundstation.types.kms_key.deserialize_json(
            data["streamsKmsKey"]
        )
    if data.get("streamsKmsRole") is not None:
        out["streams_kms_role"] = data["streamsKmsRole"]
    return out
