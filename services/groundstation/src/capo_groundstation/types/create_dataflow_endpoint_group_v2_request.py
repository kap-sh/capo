"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateDataflowEndpointGroupV2Request``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.create_endpoint_details_list
    import capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds
    import capo_groundstation.types.tags_map


class CreateDataflowEndpointGroupV2Request(TypedDict, closed=True):
    endpoints: "capo_groundstation.types.create_endpoint_details_list.CreateEndpointDetailsList"
    """<p>Dataflow endpoint group's endpoint definitions</p>"""
    contact_pre_pass_duration_seconds: NotRequired[
        "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
    ]
    """<p> Amount of time, in seconds, before a contact starts that the Ground Station Dataflow Endpoint Group will be in a <code>PREPASS</code> state. A <a href="https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>PREPASS</code> state. </p>"""
    contact_post_pass_duration_seconds: NotRequired[
        "capo_groundstation.types.dataflow_endpoint_group_duration_in_seconds.DataflowEndpointGroupDurationInSeconds"
    ]
    """<p> Amount of time, in seconds, after a contact ends that the Ground Station Dataflow Endpoint Group will be in a <code>POSTPASS</code> state. A <a href="https://docs.aws.amazon.com/ground-station/latest/ug/monitoring.automating-events.html">Ground Station Dataflow Endpoint Group State Change event</a> will be emitted when the Dataflow Endpoint Group enters and exits the <code>POSTPASS</code> state. </p>"""
    tags: NotRequired["capo_groundstation.types.tags_map.TagsMap"]
    """<p>Tags of a V2 dataflow endpoint group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataflowEndpointGroupV2Request) -> dict:
    out: dict = {}
    import capo_groundstation.types.create_endpoint_details_list

    out["endpoints"] = (
        capo_groundstation.types.create_endpoint_details_list.serialize_json(
            value["endpoints"]
        )
    )
    if "contact_pre_pass_duration_seconds" in value:
        out["contactPrePassDurationSeconds"] = value[
            "contact_pre_pass_duration_seconds"
        ]
    if "contact_post_pass_duration_seconds" in value:
        out["contactPostPassDurationSeconds"] = value[
            "contact_post_pass_duration_seconds"
        ]
    if "tags" in value:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateDataflowEndpointGroupV2Request:
    out: CreateDataflowEndpointGroupV2Request = {}  # type: ignore[typeddict-item]
    if data.get("endpoints") is not None:
        import capo_groundstation.types.create_endpoint_details_list

        out["endpoints"] = (
            capo_groundstation.types.create_endpoint_details_list.deserialize_json(
                data["endpoints"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataflowEndpointGroupV2Request.endpoints required"
        )
    if data.get("contactPrePassDurationSeconds") is not None:
        out["contact_pre_pass_duration_seconds"] = data["contactPrePassDurationSeconds"]
    if data.get("contactPostPassDurationSeconds") is not None:
        out["contact_post_pass_duration_seconds"] = data[
            "contactPostPassDurationSeconds"
        ]
    if data.get("tags") is not None:
        import capo_groundstation.types.tags_map

        out["tags"] = capo_groundstation.types.tags_map.deserialize_json(data["tags"])
    return out
